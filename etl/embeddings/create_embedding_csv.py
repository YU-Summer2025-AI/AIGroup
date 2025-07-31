from sqlalchemy import create_engine
import pandas as pd
from get_embedding import compute_embedding
from sqlalchemy import text

engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/SYAS")

sql_query = f"""
SELECT id, short_description_of_yourself AS short_description_of_yourself_embedding
FROM members
WHERE id IN (
    SELECT male_id FROM matches
    UNION
    SELECT female_id FROM matches
);
"""


def embed(text_list):
    batch_size = 8
    embedding_vectors = []
    for i in range(0, len(text_list), batch_size):
        batch_vectors = compute_embedding(text_list[i : (i + batch_size)])
        embedding_vectors.extend(batch_vectors)
        print(f"Computed batch {len(embedding_vectors)}/{len(text_list)}")
    embedding_strings = [f'[{",".join(map(str, v))}]' for v in embedding_vectors]
    return embedding_strings


with engine.connect() as conn:
    df = pd.read_sql(sql_query, conn)

# Get rid of rows with missing values
df.dropna(axis=0, inplace=True)

columns_to_save = ["id"]

for column in df.columns:
    if column == "id" or df[column].dtype != "object":
        continue
    print(f"Getting embeddings for {column}")
    df[f"{column}_embeddings"] = embed(df[column].to_list())
    columns_to_save.append(f"{column}_embeddings")


df.to_csv(
    "description_embeddings.csv", index=False, na_rep="NULL", columns=columns_to_save
)
