import pandas as pd
import shap
import torch
from fastai.tabular.all import *
from sqlalchemy import create_engine, text
import joblib
engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/SYAS")
sql_query = text("SELECT * FROM total_males")
with engine.connect() as conn:
    df = pd.read_sql(sql_query, conn)

# TRAITS MODEL
learn_traits = load_learner('male_model_traits.pkl')
X_traits = df[learn_traits.dls.cont_names]

def predict_fn_traits(x):
    return learn_traits.get_preds(dl=learn_traits.dls.test_dl(pd.DataFrame(x, columns=X_traits.columns)))[0].numpy()

background_traits = shap.kmeans(X_traits, 20)
explainer_traits = shap.KernelExplainer(predict_fn_traits, background_traits)
X_small_traits = X_traits.reset_index(drop=True)
shap_values_traits = explainer_traits.shap_values(X_small_traits)

joblib.dump((shap_values_traits, X_small_traits), "shap_male_traits.pkl")

# RELIGION MODEL ANALYSIS
learn_religion = load_learner('male_model_religion.pkl')
X_religion = df[learn_religion.dls.cont_names]  

def predict_fn_religion(x):
    return learn_religion.get_preds(dl=learn_religion.dls.test_dl(pd.DataFrame(x, columns=X_religion.columns)))[0].numpy()

background_religion = shap.kmeans(X_religion, 20)
explainer_religion = shap.KernelExplainer(predict_fn_religion, background_religion)
X_small_religion = X_religion.reset_index(drop=True)
shap_values_religion = explainer_religion.shap_values(X_small_religion)

joblib.dump((shap_values_religion, X_small_religion), "shap_male_religion.pkl")
