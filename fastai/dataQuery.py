import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from fastai.tabular.all import *


engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/SYAS")


with open('query.sql', 'r') as file:
    sql_query = text(file.read())
with engine.connect() as conn:
    df = pd.read_sql(sql_query, conn)
    df['Male_Age'] = df['Male_Age'].astype(int)
    df['Female_Age'] = df['Female_Age'].astype(int)
print(df.head())


 
cat_names = ['Male_MemberData', 'Female_MemberData', 'Male_Frequency_of_Torah_study', 'Female_Dress', 'Male_Family_Background', 'Female_Family_Background', 'Male_Marriage_Status', 'Female_Marriage_Status', 'Male_Political_Orientation', 'Female_Political_Orientation', 'Male_Introvert_Extravert', 'Female_Introvert_Extravert', 'Male_Sensor_Intuitive', 'Female_Sensor_Intuitive', 'Male_Thinker_Feeler', 'Female_Thinker_Feeler', 'Male_Judger_Perceiver', 'Female_Judger_Perceiver', 'Male_Minimum_Education_level', 'Female_Minimum_Education_level', 'Male_Jewish_Education', 'Female_Jewish_Education']
cont_names = ['Male_Age', 'Female_Age']

dep_var = 'ms'


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
learn.fit_one_cycle(5)
