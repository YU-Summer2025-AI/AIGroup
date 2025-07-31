import json
import shap
import numpy as np
import xgboost as xgb
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text

model = xgb.XGBClassifier()
model.load_model("../xgboost_model/top_xgb_model_1.json")
column_names = model.get_booster().feature_names

engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/SYAS")

explainer = shap.TreeExplainer(model)


def parse_vector_fast(vec_str):
    if isinstance(vec_str, str):
        try:
            # Safely parse the string using the optimized json library
            return np.array(json.loads(vec_str))[:50]
        except json.JSONDecodeError:
            # Handle cases where the string is not valid JSON
            return None
    return None  # Handle other potential null/malformed data


def load_match(match_id):
    with engine.connect() as conn:
        sql_query = text(f"SELECT * FROM matches_values WHERE match_id = {match_id}")
        match = pd.read_sql(sql_query, conn)
        for col in match:
            if pd.isna(match[col].iloc[0]):
                match[col] = match[col].astype("Int64")
            if "embedding" in col:
                match[col] = match[col].apply(parse_vector_fast)
        return match


def load_match_by_id(male_id, female_id):
    params = {"male_id": male_id, "female_id": female_id}
    with open("../queries/new_match_by_id.sql", "r") as file:
        sql_query = file.read()

    with engine.connect() as conn:
        match = pd.read_sql(sql_query, conn, params=params)
        for col in match:
            if pd.isna(match[col].iloc[0]):
                match[col] = match[col].astype("Int64")
            if "embedding" in col:
                match[col] = match[col].apply(parse_vector_fast)
        return match


def encode_data(df):
    cols_to_add = []
    cols_to_remove = []
    for col in df.columns.copy():
        if df[col].dtype == "object" and "embedding" not in col:
            df[col] = df[col].str.replace(" ", "")
            df[col] = df[col].replace("", np.nan).astype(str)
            dummy_columns = (
                df[col].str.get_dummies(sep=";").astype(int).add_prefix(col + "_")
            )
            cols_to_remove.append(col)
            cols_to_add.append(dummy_columns)
        elif "embedding" in col:
            vec_len = 50
            nan_placeholder = [np.nan] * vec_len
            data_for_df = [
                v if v is not None else nan_placeholder for v in df[col].tolist()
            ]
            vector_df = pd.DataFrame(data_for_df, index=df.index, dtype=np.float32)
            vector_df.columns = [f"{col}_{i}" for i in range(vector_df.shape[1])]
            cols_to_remove.append(col)
            cols_to_add.append(vector_df)
    df = pd.concat([df.drop(cols_to_remove, axis=1)] + cols_to_add, axis=1)
    return df


def get_top_shap_values(encoded_match):
    shap_explanation = explainer(encoded_match)[0]
    abs_shap_values = np.abs(shap_explanation.values)
    top_indices = np.argsort(abs_shap_values)[-10:][::-1]
    top_features = {
        shap_explanation.feature_names[i]: (
            "Positive Impact" if shap_explanation.values[i] > 0 else "Negative Impact"
        )
        for i in top_indices
    }
    return top_features


def calculate_probs_for_match(match_id):
    match_data = load_match(match_id)
    encoded_match = encode_data(match_data).reindex(columns=column_names, fill_value=0)
    probs = model.predict_proba(encoded_match)[0]
    top_shap_values = get_top_shap_values(encoded_match)
    explained_probs = {
        "Probabilities": {"Declined": float(probs[0]), "Both Approve": float(probs[1])},
        "Top Columns": top_shap_values,
    }
    return explained_probs

def calculate_probs_for_ids(male_id, female_id):
    match_data = load_match_by_id(male_id, female_id)
    encoded_match = encode_data(match_data).reindex(columns=column_names, fill_value=0)
    probs = model.predict_proba(encoded_match)[0]
    top_shap_values = get_top_shap_values(encoded_match)
    explained_probs = {
        "Probabilities": {"Declined": float(probs[0]), "Both Approve": float(probs[1])},
        "Top Columns": top_shap_values,
    }
    return explained_probs


