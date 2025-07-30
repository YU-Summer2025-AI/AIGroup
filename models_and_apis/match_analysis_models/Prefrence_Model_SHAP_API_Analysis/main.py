from fastapi import FastAPI
from fastapi.responses import FileResponse
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import shap
import pandas as pd
import joblib
import numpy as np
from sqlalchemy import create_engine, text
from pydantic import BaseModel
from fastai.tabular.all import load_learner





app = FastAPI()
shap_values_male_traits, X_male_traits = joblib.load("shap_male_traits.pkl")
shap_values_female_traits, X_female_traits = joblib.load("shap_female_traits.pkl")
shap_values_female_religion, X_female_religion = joblib.load("shap_female_religion.pkl")
shap_values_male_religion, X_male_religion = joblib.load("shap_male_religion.pkl")

religion_y_names = [
            'avg_heimish',
            'avg_traditional',
            'avg_middle_of_road',
            'avg_strickly_frum',
            'avg_machmir',
            'avg_conservadox',
            'avg_chassidish',
            'avg_conservative',
            'avg_m_yeshivish',
            'avg_spiritual_but_not_religious',
            'avg_m_o_liberal',
            'avg_lubavitch',
            'avg_just_jewish',
            'avg_reform',
            'avg_yeshivish',]
traits_y_names = [
            'avg_lean_slender',
            'avg_introvert', 
            'avg_sensor', 
            'avg_feeler', 
            'avg_athletic_fit',
            'avg_proportional', 
            'avg_firm_toned', 
            'avg_perceiver', 
            'avg_large_broad_build',
            'avg_medium_build',
            'avg_a_few_extra_pounds',
            'avg_muscular',
        ]

@app.get("/")
def read_root():
    return {"message": "SHAP API is running."}

@app.get("/shap/graph{gender}/{model}")
def global_shap_plot(gender: str, model: str):
    file_name = f"shap_{gender}_{model}.pkl"
    shap_values, X_small_full = joblib.load(file_name)
    mask = [not col.startswith("avg_") for col in X_small_full.columns]
    if model == "traits" :
        mask = [not col.startswith("avg_") for col in X_small_full.columns]

        X_small = X_small_full.loc[:, mask]
        cont_names = list(X_small.columns)

        shap_values = shap_values[:, mask, :]
        target_names = traits_y_names
        target_indices = [traits_y_names.index(name) for name in target_names]

        fig, axes = plt.subplots(3, 4, figsize=(24, 16))
        axes = axes.flatten()
        output_files = []
        for i, ax in enumerate(axes):
            plt.sca(ax)
            shap_values_target = shap_values[:, :, target_indices[i]]
            shap.summary_plot(
                shap_values_target,
                X_small,
                feature_names=cont_names,
                show=False,
                plot_type="dot",
                plot_size=(None),
            )
            plt.title(f"SHAP for {traits_y_names[i]}")
            plt.gca().tick_params(axis='y', labelsize=10)
            ax.set_title(f"SHAP for {target_names[i]}")
        plt.suptitle(f"SHAP Summary Plots for {gender.title()} - {model.title()} Model", fontsize=20)
        plt.tight_layout()
        output_path = f"shap_{gender}_{model}.png"
        plt.savefig(output_path)
        plt.close()

        return FileResponse(output_path)

    elif model == "religion":
       

        X_small = X_small_full.loc[:, mask]
        cont_names = list(X_small.columns)

        shap_values = shap_values[:, mask, :]
        target_names = religion_y_names
        target_indices = [religion_y_names.index(name) for name in target_names]

        fig, axes = plt.subplots(3, 5, figsize=(24, 16))
        axes = axes.flatten()
        output_files = []
        for i, ax in enumerate(axes):
            plt.sca(ax)
            shap_values_target = shap_values[:, :, target_indices[i]]
            shap.summary_plot(
                shap_values_target,
                X_small,
                feature_names=cont_names,
                show=False,
                plot_type="dot",
                plot_size=(None),
            )
            plt.title(f"SHAP for {religion_y_names[i]}")
            plt.gca().tick_params(axis='y', labelsize=10)
            ax.set_title(f"SHAP for {target_names[i]}")
        plt.suptitle(f"SHAP Summary Plots for {gender.title()} - {model.title()} Model", fontsize=20)
        plt.tight_layout()
        output_path = f"shap_{gender}_{model}.png"
        plt.savefig(output_path)
        plt.close()
        return FileResponse(output_path)

@app.get("/shap/individual_graph{gender}/{model}/{id}")
def global_shap_plot(gender: str, model: str, id: int):
    if(gender == "male"):
        engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/postgres")
        sql_query = text("SELECT * FROM total_males")
        with engine.connect() as conn:
            df = pd.read_sql(sql_query, conn)
        idx = df.index[df["male_id"] == id].tolist()[0]
        file_name = f"shap_{gender}_{model}.pkl"
        shap_values, X_small_full = joblib.load(file_name)
        y_names = []
        if(model == "traits"):
            y_names = traits_y_names
        elif model == "religion":
            y_names = religion_y_names
            
        fig, ax = plt.subplots(figsize=(10, 6))  # One figure and one subplot
        plt.sca(ax)
        plt.sca(ax)
        shap.summary_plot(
            shap_values[idx:idx+1],
            X_small_full.iloc[idx:idx+1],
            feature_names=X_small_full.columns.tolist(),
            plot_type="bar",
            show=False,
            class_names= y_names
        )
        ax.tick_params(axis='y', labelsize=6)
        traits_member_id = df.iloc[idx]["male_id"]
        ax.set_title(f"{model} Model: ID {id}", fontsize=12)
        ax.set_xlabel("mean(|SHAP value|)", fontsize=6)
        output_path = f"shap_{gender}_{model}_{id}.png"
        plt.savefig(output_path)
        plt.close()
        return FileResponse(output_path)
    elif gender == "female":
        engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/postgres")
        sql_query = text("SELECT * FROM total_female")
        with engine.connect() as conn:
            df = pd.read_sql(sql_query, conn)
        idx = df.index[df["id"] == id].tolist()[0]
        file_name = f"shap_{gender}_{model}.pkl"
        shap_values, X_small_full = joblib.load(file_name)
        y_names = []
        if(model == "traits"):
            y_names = traits_y_names
        elif model == "religion":
            y_names = religion_y_names
            
        fig, ax = plt.subplots(figsize=(10, 6))  # One figure and one subplot
        plt.sca(ax)
        plt.sca(ax)
        shap.summary_plot(
            shap_values[idx:idx+1],
            X_small_full.iloc[idx:idx+1],
            feature_names=X_small_full.columns.tolist(),
            plot_type="bar",
            show=False,
            class_names= y_names
        )
        ax.tick_params(axis='y', labelsize=6)
        traits_member_id = df.iloc[idx]["id"]
        ax.set_title(f"{model} Model: ID {id}", fontsize=12)
        ax.set_xlabel("mean(|SHAP value|)", fontsize=6)
        output_path = f"shap_{gender}_{model}_{id}.png"
        plt.savefig(output_path)
        plt.close()
        return FileResponse(output_path)
class ProfileTraits(BaseModel):
    age: float
    height: float
    introvert: int
    sensor: int
    feeler: int
    perceiver: int
    athletic_fit: int
    lean_slender: int
    large_broad_build: int
    proportional: int
    firm_toned: int
    average_medium_build: int
    a_few_extra_pounds: int

@app.post("/shap/create_new_graph/{gender}/{model}")
def create_graph(gender: str, model: str, traits: ProfileTraits):
    model_path = f"{gender}_model_{model}.pkl"
    model_obj = load_learner(model_path)
    shap_path = f"shap_{gender}_{model}.pkl"
    shap_values, X_small_full = joblib.load(shap_path)
    def predict_fn_traits(x):
        return model_obj.get_preds(dl=model_obj.dls.test_dl(pd.DataFrame(x, columns=X_small_full.columns)))[0].numpy()

    background = shap.kmeans(X_small_full, 20)
    explainer = shap.KernelExplainer(predict_fn_traits, background)
    
    input_df = pd.DataFrame([traits.dict()])
    input_df = input_df[X_small_full.columns]
    shap_values_input = explainer.shap_values(input_df)
    if(model == "traits"):
        y_names = traits_y_names
    elif model == "religion":
        y_names = religion_y_names

    
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.sca(ax)
    shap.summary_plot(
        shap_values_input,
        input_df,
        feature_names=input_df.columns.tolist(),
        plot_type="bar",
        show=False,
        class_names= y_names,
    )
    raw_scores = predict_fn_traits(input_df)
    scored_pairs = list(zip(y_names, raw_scores[0]))


    top_scored = sorted(scored_pairs, key=lambda x: x[1], reverse=True)[:4]
    top_scores_dict = {name: round(float(score), 2) for name, score in top_scored}
    print(top_scores_dict)
    title = "Top scores: " + ", ".join(f"{k}: {v:.2f}" for k, v in top_scores_dict.items())
    ax.set_title(title, fontsize=14)

    output_path = f"shap_{gender}_{model}_custom.png"
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
    return FileResponse(output_path)


    
