import pandas as pd
from fastapi import FastAPI
from process_data import get_data, process_matches, xgboost_model_data_processing
from contextlib import asynccontextmanager
import recommendations, get_user_info, encryption, predictions
from fastai.tabular.all import *

app_state = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- Code here runs on startup ---
    print("INFO:     Application startup: Loading and processing data...")

    # Load the raw data
    df_members_raw = get_data.get_dataframe_from_postgres('members')
    df_matches_raw = get_data.get_dataframe_from_postgres('matches')

    # Process the matches dataframe
    df_matches_processed = process_matches.process_overall_rating(df_matches_raw)
    # Store the dataframes in our application state
    app_state["df_members"] = df_members_raw
    app_state["df_matches"] = df_matches_processed

    with open('xgboost_model.pkl', 'rb') as file:
        xgb_model = pickle.load(file)
        app_state["xgboost_model"] = xgb_model
    yield

    app_state.clear()

app = FastAPI(lifespan=lifespan)

@app.get("/get_user_summary")
def get_user_summary(encrypted_id: int):
    id = encryption.decrypt(encrypted_id)
    df_members = app_state.get("df_members")
    return get_user_info.get_user_summary(df_members, id)


@app.get("/get_recommendations")
def get_user_recommendations(encrypted_id: int, number_of_recommendations: int):
    id = encryption.decrypt(encrypted_id)
    df_members = app_state.get("df_members")
    df_matches = app_state.get("df_matches")

    num_matches = get_user_info.get_num_matches(df_members, id)
    gender = get_user_info.get_gender(df_members, id)
    if gender == 'Male':
        if df_matches.loc[df_matches['male_id'] == id].empty:
            return f'User {encrypted_id} has no former matches that we can use to generate new matches'
        else:
            return recommendations.get_male_recommendations(id, num_matches, number_of_recommendations, df_matches)

    elif gender == 'Female':
        if df_matches.loc[df_matches['female_id'] == id].empty:
            return f'User {encrypted_id} has no former matches that we can use to generate new matches'
        else:
            return recommendations.get_female_recommendations(id, num_matches, number_of_recommendations, df_matches)

    else:
        return f'Member {encrypted_id} not in system'

@app.get("/get_match_prediction")
def get_match_prediction(encrypted_male_id: int, encrypted_female_id: int):
    male_id = encryption.decrypt(encrypted_male_id)
    female_id = encryption.decrypt(encrypted_female_id)

    correct_genders = (get_user_info.get_gender(app_state['df_members'], male_id) == 'Male'
                       and get_user_info.get_gender(app_state['df_members'], female_id) == 'Female')

    if not correct_genders:
        return f'Try again: enter valid genders'
    else:
        return predictions.predict_match(app_state['df_matches'], app_state['df_members'], app_state['xgboost_model'], male_id, female_id)
