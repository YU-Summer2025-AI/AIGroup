from fastai.tabular.all import *
import pandas as pd
from sqlalchemy import create_engine, text

learn = load_learner('model.pkl')

engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/SYAS")
query = text("SELECT * FROM matches_values LIMIT 5")  

with engine.connect() as conn:
    df = pd.read_sql(query, conn)

row = df.iloc[3].copy()

original_prob = learn.predict(row)[2].item()
print(f"Original match probability: {original_prob:.2%}")

row['height_diff'] += 2

new_prob = learn.predict(row)[2].item()
print(f"With height +20cm: {new_prob:.2%}")

print(f"Change: {new_prob - original_prob:.2%}")