import pandas as pd
import pandas as pd
import shap
from fastai.tabular.all import *
from sqlalchemy import create_engine, text
import joblib


learn = load_learner('male_model.pkl')

engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/postgres")
sql_query = text("SELECT * FROM total_males")
with engine.connect() as conn:
    df = pd.read_sql(sql_query, conn)

X = df[learn.dls.cont_names]

import torch
from shap import DeepExplainer

def predict_fn(x):
    return learn.get_preds(dl=learn.dls.test_dl(pd.DataFrame(x, columns=X.columns)))[0].numpy()

#background = X.sample(200, random_state=1)
background = shap.kmeans(X, 20)
explainer = shap.KernelExplainer(predict_fn, background)

X_small = X.reset_index(drop=True)
shap_values = explainer.shap_values(X_small)

import joblib
joblib.dump((shap_values, X_small), "shap_male.pkl")