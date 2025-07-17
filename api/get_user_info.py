import pandas as pd

def get_gender(df: pd.DataFrame, id: int) -> str:
    gender = df.loc[df['id'] == id, 'gender']
    if gender.empty:
        return 'Member# not in system'
    else: return gender.iloc[0]

def get_user_summary(df: pd.DataFrame, id: int):
    imp_data = ['gender', 'age', 'country', 'state', 'city', 'height', 'body_type', 'religious_orientation', 'kosher']
    user = df.loc[df['id'] == id]
    if user.empty:
        return f'Member {id} not in system'
    else: return user[imp_data].T
