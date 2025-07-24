from fastai.tabular.all import *
import pandas as pd
from sqlalchemy import create_engine, text

learn = load_learner('model.pkl')

engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/postgres")
query = text("SELECT * FROM matches_values LIMIT 1")  

with engine.connect() as conn:
    df = pd.read_sql(query, conn)

row = df.iloc[0]
print(learn.predict(row))