from fastai.tabular.all import *
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text
learn = load_learner('female_model.pkl')
engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/SYAS")

sql_query = text("SELECT * FROM member_values")
with engine.connect() as conn:
    df = pd.read_sql(sql_query, conn) 

row = df.iloc[0] 
result = learn.predict(row)
print(result)