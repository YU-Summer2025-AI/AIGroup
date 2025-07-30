from fastai.tabular.all import *
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from fastai.metrics import accuracy_multi
from functools import partial


engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/postgres")

sql_query = text("SELECT * FROM total_female")
with engine.connect() as conn:
    df = pd.read_sql(sql_query, conn) 
#model for traits
cont_names = [
    'height',
    'age', 
    'introvert', 
    'sensor', 
    'feeler', 
    'perceiver',
    'athletic_fit', 
    'lean_slender', 
    'large_broad_build', 
    'proportional', 
    'firm_toned',
    'average_medium_build',
    'a_few_extra_pounds',
]
trait_y_names = [
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
    'avg_muscular'
    ]

dls = TabularDataLoaders.from_df(
    df, # Feeding it the data
    path='.',
    y_names=trait_y_names, # What we want to predict
    cont_names=cont_names, # The inputs we're using
    procs=[Normalize]
)

learn = tabular_learner(
    dls,
    loss_func=BCEWithLogitsLossFlat(),  
    metrics=partial(accuracy_multi, thresh=0.5)
)
learn.fit_one_cycle(5)
learn.export('female_model_traits.pkl')
#model for religion
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
    'avg_yeshivish',
]
dls = TabularDataLoaders.from_df(
    df,
    path='.',
    y_names=religion_y_names,           
    cont_names=cont_names,
    procs=[Normalize]
)

learn = tabular_learner(
    dls,
    loss_func=BCEWithLogitsLossFlat(),  
    metrics=partial(accuracy_multi, thresh=0.5)
)  
learn.fit_one_cycle(5)
learn.export('female_model_religion.pkl')