import pandas as pd
import os
from sqlalchemy import create_engine, text

DB_USER = os.getenv('PG_USER', 'admin')
DB_PASSWORD = os.getenv('PG_PASSWORD', 'admin')
DB_HOST = os.getenv('PG_HOST', 'localhost')
DB_PORT = os.getenv('PG_PORT', '5432')
DB_NAME = os.getenv('PG_DB_NAME', 'SYAS')
TABLE_NAME = 'your_table_name'

def get_dataframe_from_postgres(table_name: str) -> pd.DataFrame:
    db_connection_str = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = None
    df = pd.DataFrame()
    try:
        engine = create_engine(db_connection_str)
        sql_query = text(f"SELECT * FROM {table_name}")
        df = pd.read_sql(sql_query, engine)
    except ImportError:
        print("Error: psycopg2-binary is not installed. Please install it using 'pip install psycopg2-binary'")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if engine:
            engine.dispose()
    return df