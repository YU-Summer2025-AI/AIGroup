import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from main import df_matches
from main import df_members

# initializing matrices
male_female_matrix = df_matches.pivot_table(index='male_id', columns='female_id', values='overall_rating')
male_female_matrix.fillna(0, inplace=True)

female_male_matrix = df_matches.pivot_table(index='female_id', columns='male_id', values='overall_rating')
female_male_matrix.fillna(0, inplace=True)


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

def get_male_recommendations(id: int, num_recs: int) -> pd.DataFrame:
    similarity = cosine_similarity(male_female_matrix)
    # the while true loop is to make sure that we have enough recommendations after getting rid of the old ones
    # that we don't fall short of the requested number
    while True:
        multiplier = 2
        recommendations = generate_recommendations(id, similarity, male_female_matrix, num_recs*multiplier)

        previous_matches = df_matches[df_matches['male_id'] == id]
        new_recs = recommendations[~recommendations['female_id'] \
                    .isin(previous_matches['female_id'])] # removes previous matches that were recommended
        if new_recs.shape[0] >= num_recs:
            return (new_recs
                    .head(num_recs)
                    .to_dict(orient="records"))
        else:
            multiplier *= 2

def get_female_recommendations(id: int, num_recs: int) -> pd.DataFrame:
    similarity = cosine_similarity(female_male_matrix)
    recommendations = generate_recommendations(id, similarity, female_male_matrix, num_recs * 2)

    previous_matches = df_matches[df_matches['female_id'] == id]
    new_recs = recommendations[~recommendations['male_id'] \
        .isin(previous_matches['male_id'])]  # removes previous matches that were recommended
    return (new_recs
            .head(num_recs)
            .to_dict(orient="records"))
