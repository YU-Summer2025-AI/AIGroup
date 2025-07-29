import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import encryption

def get_male_female_matrix(df: pd.DataFrame) -> pd.DataFrame:
    male_female_matrix = df.pivot_table(index='male_id', columns='female_id', values='overall_rating')
    male_female_matrix.fillna(0, inplace=True)
    return male_female_matrix

def get_female_male_matrix(df: pd.DataFrame) -> pd.DataFrame:
    female_male_matrix = df.pivot_table(index='female_id', columns='male_id', values='overall_rating')
    female_male_matrix.fillna(0, inplace=True)
    return female_male_matrix

def find_similar_people(id, user_similarity, matrix, top_n=5):
    user_index = matrix.index.get_loc(id)
    similar_users = user_similarity[user_index]
    similar_users_indices = np.argsort(similar_users)[::-1][1:top_n+1]
    return matrix.index[similar_users_indices]

def generate_recommendations(id, user_similarity, matrix, top_n=5):
    similar_people = find_similar_people(id, user_similarity, matrix, top_n)

    similar_males_ratings = matrix.loc[similar_people]

    average_ratings = similar_males_ratings.mean()

    recommended_females = (average_ratings
                           .sort_values(ascending=False)
                           .head(top_n))
    return (recommended_females
            .reset_index()
            .rename(columns={'index': 'user_id', 0: 'score'}))

def get_male_recommendations(id: int, num_matches, num_recs: int, df_matches: pd.DataFrame) -> pd.DataFrame:
    male_female_matrix = get_male_female_matrix(df_matches)
    similarity = cosine_similarity(male_female_matrix)
    # the while true loop is to make sure that we have enough recommendations after getting rid of the old ones
    # that we don't fall short of the requested number
    while True:
        multiplier = 1
        recommendations = generate_recommendations(id, similarity, male_female_matrix, num_matches * multiplier)

        previous_matches = df_matches[df_matches['male_id'] == id]
        new_recs = recommendations[~recommendations['female_id'] \
                    .isin(previous_matches['female_id'])] # removes previous matches that were recommended
        if new_recs.shape[0] >= num_recs:
            ids = new_recs['female_id']
            encrypted_ids = encryption.encrypt(ids)
            return encrypted_ids.head(num_recs).to_list()
        else:
            multiplier *= 2

def get_female_recommendations(id: int, num_matches, num_recs: int, df_matches: pd.DataFrame) -> pd.DataFrame:
    female_male_matrix = get_female_male_matrix(df_matches)
    similarity = cosine_similarity(female_male_matrix)
    while True:
        multiplier = 1
        recommendations = generate_recommendations(id, similarity, female_male_matrix, num_matches * multiplier)

        previous_matches = df_matches[df_matches['female_id'] == id]
        new_recs = recommendations[~recommendations['male_id'] \
                    .isin(previous_matches['male_id'])] # removes previous matches that were recommended
        if new_recs.shape[0] >= num_recs:
            ids = new_recs['male_id']
            encrypted_ids = encryption.encrypt(ids)
            return encrypted_ids.head(num_recs).to_list()
        else:
            multiplier *= 2
