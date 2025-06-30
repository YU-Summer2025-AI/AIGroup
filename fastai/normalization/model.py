import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from fastai.tabular.all import *


engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/SYAS")



sql_query = text("SELECT * FROM matches_values")

with engine.connect() as conn:
    df = pd.read_sql(sql_query, conn)

print(df.head())

dep_var = 'match_status'
cont_names = ['male_age', 'male_height','female_age', 'female_height','height_diff', 'age_diff']
cat_names = [col for col in df.columns if col not in cont_names + [dep_var]]

print("Dep variable:", dep_var)
print("Continuous columns:", cont_names)
print("Categorical columns:", cat_names)


procs = [Categorify, Normalize]
dls = TabularDataLoaders.from_df(
    df,
    path='.',
    procs=procs,
    cat_names=cat_names,
    cont_names=cont_names,
    y_names=dep_var,
    valid_pct=0.2,
    seed=42
)
learn = tabular_learner(dls, metrics=accuracy)
learn.fit_one_cycle(0)

learn.export('model.pkl')


