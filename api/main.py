import numpy as np
np.set_printoptions(linewidth=130)
from fastapi import FastAPI
from process_data import get_data
from process_data import process_matches

app_state = {}

app = FastAPI()

df_members = get_data.get_dataframe_from_postgres('members')
df_matches = get_data.get_dataframe_from_postgres('matches')
df_matches = process_matches.process_overall_rating(df_matches)

# these go after the initialization of df_matches and df_members to avoid having circular importation
import recommendations
import get_user_info

@app.get("/get_gender")
def get_gender(id: int):
    return get_user_info.get_gender(df_members, id)

@app.get("/get_user_summary")
def get_user_summary(id: int):
    return get_user_info.get_user_summary(df_members, id)


@app.get("/get_recommendations")
def get_user_recommendations(id: int, number_of_recommendations: int):
    if get_gender(id) == 'Male':
        if df_matches.loc[df_matches['male_id'] == id].empty:
            return f'User {id} has no former matches that we can use to generate new matches'
        else:
            return recommendations.get_male_recommendations(id, number_of_recommendations)


    elif get_gender(id) == 'Female':
        if df_matches.loc[df_matches['female_id'] == id].empty:
            return f'User {id} has no former matches that we can use to generate new matches'
        else:
            return recommendations.get_female_recommendations(id, number_of_recommendations)

    else:
        return f'Member {id} not in system'

