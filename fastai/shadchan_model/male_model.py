from fastai.tabular.all import *
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/SYAS")

sql_query = text("SELECT * FROM total_males")
with engine.connect() as conn:
    df = pd.read_sql(sql_query, conn) 

cont_names = [
    'height',
    'age', 
    'introvert', 
    'sensor', 
    'feeler', 
    'perceiver',
    'athletic_fit', 
    'lean_slender', 
    'yeshivish', 
    'just_jewish', 
]
y_names = [
    'avg_age',
    'avg_introvert', 
    'avg_sensor', 
    'avg_feeler', 
    'avg_athletic_fit',
    'avg_machmir', 
    'avg_just_jewish', 
    'avg_heimish', ]

dls = TabularDataLoaders.from_df(
    df,
    path='.',
    y_names=y_names,           
    cont_names=cont_names,
    procs=[Normalize]
)

learn = tabular_learner(dls, metrics=rmse)  
learn.fit_one_cycle(5)
learn.export('male_model.pkl')
