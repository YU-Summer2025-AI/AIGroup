import pandas as pd
import numpy as np

def get_match_rating(df: pd.DataFrame) -> pd.DataFrame:
    status_mapping = {
        None: 1,
        'Declined': 1,
        'New match': 1,
        'Approved': 4
    }
    quality_mapping = {
        None: 1,
        'NULL': 1,
        'Not': 1,
        'On': 2
    }

    df['male_s_rating'] = df['male_s'].map(status_mapping)
    df['female_s_rating'] = df['female_s'].map(status_mapping)
    df['quality_rating'] = df['match_quality'].map(quality_mapping)

    return df

def process_overall_rating(df: pd.DataFrame) -> pd.DataFrame:
    df['match_quality'] = df['match_quality'].str.split().str[0]
    df = get_match_rating(df)
    df['overall_rating'] = df['male_s_rating'] * df['female_s_rating'] * df['quality_rating']
    good_match_values = [2, 4, 8, 16]
    df['is_good_match'] = np.where(df['overall_rating'].isin(good_match_values), 1, 0)
    return df