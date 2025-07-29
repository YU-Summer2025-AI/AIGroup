import pandas as pd
import numpy as np


def process_data(df: pd.DataFrame) -> pd.DataFrame:
    df['female_times_divorce'] = df['female_times_divorced'].replace('>=1', 1)
    df['male_times_divorce'] = df['male_times_divorced'].replace('>=1', 1)

    df['female_number_live_with_you'] = df['female_number_live_with_you'].replace('', 0)
    df['female_number_live_with_you'] = df['female_number_live_with_you'].replace('N/A', 0)

    df['male_number_live_with_you'] = df['male_number_live_with_you'].replace('', 0)
    df['male_number_live_with_you'] = df['male_number_live_with_you'].replace('N/A', 0)

    df['female_age_of_youngest'] = df['female_age_of_youngest'].replace('', 0)
    df['male_age_of_youngest'] = df['female_age_of_youngest'].replace('', 0)

    df['female_how_many_children'] = df['female_how_many_children'].replace('', 0)
    df['male_how_many_children'] = df['male_how_many_children'].replace('', 0)

    df['female_number_of_siblings'] = df['female_number_of_siblings'].replace('', 0)
    df['male_number_of_siblings'] = df['male_number_of_siblings'].replace('', 0)

    return df

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

def process_match_rating(df: pd.DataFrame) -> pd.DataFrame:
    df['match_quality'] = df['match_quality'].str.split().str[0]
    get_match_rating(df)
    df['overall_rating'] = df['male_s_rating'] * df['female_s_rating'] * df['quality_rating']
    good_match_values = [2, 4, 8, 16]
    df['is_good_match'] = np.where(df['overall_rating'].isin(good_match_values), 1, 0)
    # df.drop(columns=['overall_rating', 'male_s','male_s_rating', 'female_s', 'female_s_rating', 'quality_rating', 'match_quality'], inplace=True)
    return df

def process_good_match_values(df: pd.DataFrame) -> pd.DataFrame:
    df['match_quality'] = df['match_quality'].str.split().str[0]
    get_match_rating(df)
    df['overall_rating'] = df['male_s_rating'] * df['female_s_rating'] * df['quality_rating']
    return df


# list of all cat and cont names
cat_names = ['id', 'male_id', 'female_id', 'ms', 'male_s', 'female_s', 'male_pr', 'female_pr', 'matchmaker_pr',
         'match_quality', 'decline_reason', 'overall_pr',
         'female_country', 'female_city', 'female_state', 'female_gender', 'female_religious_orientation',
         'female_ethnicity', 'female_baal_teshuva', 'female_cohen', 'female_female_convert',
         'female_parents_convert', 'female_mother_maternal_grandmother_jewish',
         'female_family_religious_background', 'female_describe_family_religious_background',
         'female_female_hc', 'female_kosher', 'female_female_dress', 'female_male_hc',
         'female_frequency_of_tefilah', 'female_male_shul_attendance', 'female_torah_study',
         'female_watching_tv', 'female_going_out_to_movies', 'female_watching_movies_at_home',
         'female_secular_education', 'female_emphasis_of_studies', 'female_jewish_education',
         'female_study_in_israel', 'female_profession', 'female_job_description', 'female_eye_color',
         'female_hair_color', 'female_body_type', 'female_mental_physical_disability',
         'female_my_marriage_status', 'female_want_additional_children', 'female_can_marry_cohen',
         'female_political_orientation', 'female_smoking_habits', 'female_how_active_are_you',
         'female_plan_to_aliya', 'female_willing_to_relocate', 'female_pet_person', 'female_pet_i_own',
         'female_additional_pet_i_own', 'female_native_language', 'female_languages_spoken',
         'female_desired_marital_status', 'female_minimum_education_level',
         'female_acceptable_for_match_to_have_children', 'female_acceptable_religious_orientation',
         'female_acceptable_smoking_habits', 'female_ok_dating_someone_with_disability',
         'female_acceptable_aliyah_responses', 'female_acceptable_kosher_observance',
         'female_ok_dating_baal_teshuva', 'female_family_relgious_background', 'female_desired_torah_study',
         'female_desired_female_hc', 'female_desired_female_dress', 'female_jewish_education_preference',
         'female_body_type_preference', 'female_preference_regarding_ethnicity',
         'female_preference_cultural_background', 'female_my_personality_traits',
         'female_my_personality_go_out_to', 'female_favorite_music', 'female_physical_activities_interests',
         'female_my_favorite_pastimes', 'female_looking_for_in_a_person',
         'female_short_description_of_yourself', 'female_community_work', 'female_introvert_extravert',
         'female_sensor_intuitive', 'female_thinker_feeler', 'female_judger_perceiver', 'female_approved',
         'female_dating_status', 'female_colleges_universities', 'female_parents_convert_before_birth',
         'female_elementary_school', 'female_location_i_grew_up', 'female_name_secondary_school',
         'female_name_study_one_year', 'female_parent_location', 'female_complete_incomplete', 'female_photo',
         'female_site', 'female_profile_last_modified_date', 'female_updated',
         'female_acceptable_places_to_live', 'female_height_category',
         'male_country', 'male_city', 'male_state', 'male_gender', 'male_religious_orientation',
         'male_ethnicity', 'male_baal_teshuva', 'male_cohen', 'male_female_convert', 'male_parents_convert',
         'male_mother_maternal_grandmother_jewish', 'male_family_religious_background',
         'male_describe_family_religious_background', 'male_female_hc', 'male_kosher', 'male_female_dress',
         'male_male_hc', 'male_frequency_of_tefilah', 'male_male_shul_attendance', 'male_torah_study',
         'male_watching_tv', 'male_going_out_to_movies', 'male_watching_movies_at_home',
         'male_secular_education', 'male_emphasis_of_studies', 'male_jewish_education', 'male_study_in_israel',
         'male_profession', 'male_job_description', 'male_eye_color', 'male_hair_color', 'male_body_type',
         'male_mental_physical_disability', 'male_my_marriage_status', 'male_want_additional_children',
         'male_can_marry_cohen', 'male_political_orientation', 'male_smoking_habits', 'male_how_active_are_you',
         'male_plan_to_aliya', 'male_willing_to_relocate', 'male_pet_person', 'male_pet_i_own',
         'male_additional_pet_i_own', 'male_native_language', 'male_languages_spoken',
         'male_desired_marital_status', 'male_minimum_education_level',
         'male_acceptable_for_match_to_have_children', 'male_acceptable_religious_orientation',
         'male_acceptable_smoking_habits', 'male_ok_dating_someone_with_disability',
         'male_acceptable_aliyah_responses', 'male_acceptable_kosher_observance', 'male_ok_dating_baal_teshuva',
         'male_family_relgious_background', 'male_desired_torah_study', 'male_desired_female_hc',
         'male_desired_female_dress', 'male_jewish_education_preference', 'male_body_type_preference',
         'male_preference_regarding_ethnicity', 'male_preference_cultural_background',
         'male_my_personality_traits', 'male_my_personality_go_out_to', 'male_favorite_music',
         'male_physical_activities_interests', 'male_my_favorite_pastimes', 'male_looking_for_in_a_person',
         'male_short_description_of_yourself', 'male_community_work', 'male_introvert_extravert',
         'male_sensor_intuitive', 'male_thinker_feeler', 'male_judger_perceiver', 'male_approved',
         'male_dating_status', 'male_colleges_universities', 'male_parents_convert_before_birth',
         'male_elementary_school', 'male_location_i_grew_up', 'male_name_secondary_school',
         'male_name_study_one_year', 'male_parent_location', 'male_complete_incomplete', 'male_photo',
         'male_site', 'male_profile_last_modified_date', 'male_updated', 'male_acceptable_places_to_live',
         'male_height_category', 'female_how_long_single', 'male_how_long_single']

cont_names = ['female_age', 'female_years_orthodox_baal_teshuva', 'female_how_many_children',
          'female_number_live_with_you', 'female_age_of_youngest',
          'female_number_of_siblings', 'female_age_min', 'female_age_max', 'female_height_inches',
          'female_max_height_inches', 'female_min_height_inches', 'female_num_matches',
          'female_acceptance_rate', 'male_age', 'male_years_orthodox_baal_teshuva', 'male_how_many_children',
          'male_number_live_with_you', 'male_age_of_youngest', 'male_number_of_siblings', 'male_age_min',
          'male_age_max', 'male_height_inches', 'male_min_height_inches', 'male_max_height_inches',
          'male_num_matches', 'male_acceptance_rate']

imp_cat_names = ['male_id', 'female_id', 'female_body_type', 'male_body_type', 'female_kosher', 'male_kosher',
                     'female_acceptable_kosher_observance', 'male_acceptable_kosher_observance',
                     'female_body_type_preference', 'male_body_type_preference', 'female_going_out_to_movies',
                     'male_going_out_to_movies', 'female_female_hc', 'male_male_hc', 'male_desired_female_hc', 'female_religious_orientation',
                     'male_religious_orientation', 'female_torah_study',
                     'female_watching_tv', 'female_going_out_to_movies', 'female_watching_movies_at_home',
                     'male_torah_study', 'male_watching_tv', 'male_going_out_to_movies', 'male_watching_movies_at_home',
                     'female_eye_color', 'female_hair_color', 'male_eye_color', 'male_hair_color',
                     'female_acceptable_religious_orientation', 'male_acceptable_religious_orientation',
                     'female_acceptable_aliyah_responses', 'male_acceptable_aliyah_responses']

imp_cont_names = ['female_age', 'female_how_many_children', 'female_number_live_with_you',
                      'female_number_of_siblings', 'female_age_min', 'female_age_max', 'female_height_inches',
                      'female_max_height_inches', 'female_min_height_inches', 'female_num_matches',
                      'female_acceptance_rate', 'male_age', 'male_how_many_children', 'male_number_live_with_you',
                      'male_number_of_siblings', 'male_age_min', 'male_age_max', 'male_height_inches',
                      'male_min_height_inches', 'male_max_height_inches', 'male_num_matches', 'male_acceptance_rate',
                  'female_female_rejection_count_null',
                  'female_female_rejection_count_dated',
                  'female_female_rejection_count_spoke_on_phone_&_not_going_out',
                  'female_female_rejection_count_spoke_on_phone',
                  'female_female_rejection_count_went_on_date(s)_&_not_going_out_again',
                  'female_female_rejection_count_never_got_in_touch',
                  # 'female_female_rejection_count_not_my_physical_look',
                  'female_female_rejection_count_other',
                  'female_female_rejection_count_we_already_dated',
                  'female_female_rejection_count_too_far/_distance',
                  'female_female_rejection_count_religious_level',
                  'female_female_rejection_count_not_my_personality_type',
                  'female_female_rejection_count_age',
                  # 'female_female_rejection_count_went_on_date(s)_&_not_going_out_again_from_matches',
                  'female_female_rejection_count_already_friends_with_this_person',
                  'female_female_rejection_count_went_on_first_date',
                  'female_female_rejection_count_busy_with_other_matches',
                  'female_female_rejection_count__went_on_date(s)_&_not_going_out_again',
                  'female_female_rejection_count_education_level',
                  'female_female_rejection_count_went_on_multiple_dates',
                  'female_female_rejection_count_too_religious',
                  'female_female_rejection_count_none',
                  'female_female_rejection_count_not_religious_enough',
                  'female_female_rejection_count_engaged',
                  'female_female_rejection_count_already_know_this_person',
                  'female_female_rejection_count_child_status',
                  'female_female_rejection_count_marital_status',
                  'female_female_rejection_count_dating_exclusively',
                  'female_female_rejection_count_know_already',
                  'female_female_rejection_count_distance',
                  'female_female_rejection_count_physical_look',
                  'female_female_rejection_count_education',
                  'female_female_rejection_count_personality',
                  'female_female_rejection_count_already_dated',
                  'female_female_rejection_count_interested_but_busy,_please_re-issue_in_3_weeks',
                  # 'female_female_rejection_count_interested_but_busy,_please_re-issue_in_3_weeks_from_matches',
                  'female_female_rejection_count_male_timed_out',
                  'female_female_rejection_count_cultural_or_ethnic_background',
                  # 'female_female_rejection_count_child_status_from_matches',
                  # 'female_female_rejection_count_marital_status_from_matches',
                  'female_female_rejection_count_speaking_virtually',
                  'female_female_rejection_count_ai_declined',
                  'female_female_rejection_count_ai_no_response',
                  'female_female_rejection_count_ai_suggestion',
                  'female_female_rejection_count_ai_accepted',
                  'female_female_rejection_count_ai_unsure',
                  'female_female_rejection_count_family_background',
                  'male_male_rejection_count_null',
                  'male_male_rejection_count_spoke_on_phone',
                  'male_male_rejection_count_dated',
                  'male_male_rejection_count_went_on_first_date',
                  'male_male_rejection_count_spoke_on_phone_&_not_going_out',
                  'male_male_rejection_count_never_got_in_touch',
                  'male_male_rejection_count_went_on_date(s)_&_not_going_out_again',
                  'male_male_rejection_count_religious_level',
                  # 'male_male_rejection_count_went_on_date(s)_&_not_going_out_again_from_matches',
                  'male_male_rejection_count_other',
                  'male_male_rejection_count_not_my_personality_type',
                  'male_male_rejection_count_we_already_dated',
                  # 'male_male_rejection_count_not_my_physical_look',
                  'male_male_rejection_count_too_far/_distance',
                  'male_male_rejection_count_age',
                  'male_male_rejection_count_already_friends_with_this_person',
                  'male_male_rejection_count_education_level',
                  'male_male_rejection_count_too_religious',
                  'male_male_rejection_count_not_religious_enough',
                  'male_male_rejection_count_none',
                  'male_male_rejection_count_went_on_multiple_dates',
                  'male_male_rejection_count_already_know_this_person',
                  'male_male_rejection_count_child_status',
                  'male_male_rejection_count_marital_status',
                  'male_male_rejection_count_female_timed_out',
                  'male_male_rejection_count_dating_exclusively',
                  'male_male_rejection_count_know_already',
                  'male_male_rejection_count_distance',
                  'male_male_rejection_count_physical_look',
                  'male_male_rejection_count_personality',
                  'male_male_rejection_count_education',
                  'male_male_rejection_count_already_dated',
                  'male_male_rejection_count_interested_but_busy,_please_re-issue_in_3_weeks',
                  'male_male_rejection_count_engaged',
                  'male_male_rejection_count_cultural_or_ethnic_background',
                  # 'male_male_rejection_count_child_status_from_matches',
                  # 'male_male_rejection_count_marital_status_from_matches',
                  # 'male_male_rejection_count_interested_but_busy,_please_re-issue_in_3_weeks_from_matches',
                  'male_male_rejection_count_family_background',
                  'male_male_rejection_count_speaking_virtually',
                  'male_male_rejection_count_ai_declined',
                  'male_male_rejection_count_ai_accepted',
                  'male_male_rejection_count_ai_no_response',
                  'male_male_rejection_count_ai_suggestion',
                  'male_male_rejection_count_ai_unsure',
                  'male_male_rejection_count_busy_with_other_matches',
                 'female_female_reason_rejecting_count_null',
                 'female_female_reason_rejecting_count_too_religious',
                 'female_female_reason_rejecting_count_spoke_on_phone',
                 'female_female_reason_rejecting_count_not_my_personality_type',
                 'female_female_reason_rejecting_count_other',
                 'female_female_reason_rejecting_count_not_religious_enough',
                 'female_female_reason_rejecting_count_age',
                 'female_female_reason_rejecting_count_physical_look',
                 'female_female_reason_rejecting_count_already_friends_with_this_person',
                 'female_female_reason_rejecting_count_never_got_in_touch',
                 'female_female_reason_rejecting_count_we_already_dated',
                 'female_female_reason_rejecting_count_went_on_date(s)_&_not_going_out_again',
                 'female_female_reason_rejecting_count_spoke_on_phone_&_not_going_out',
                 'female_female_reason_rejecting_count_too_far/_distance',
                 'female_female_reason_rejecting_count_went_on_first_date',
                 'female_female_reason_rejecting_count_education_level',
                 'female_female_reason_rejecting_count_none',
                 'female_female_reason_rejecting_count_went_on_multiple_dates',
                 'female_female_reason_rejecting_count_already_know_this_person',
                 'female_female_reason_rejecting_count_child_status',
                 'female_female_reason_rejecting_count_marital_status',
                 'female_female_reason_rejecting_count_female_timed_out',
                 'female_female_reason_rejecting_count_dating_exclusively',
                 'female_female_reason_rejecting_count_know_already',
                 'female_female_reason_rejecting_count_distance',
                 'female_female_reason_rejecting_count_personality',
                 'female_female_reason_rejecting_count_education',
                 'female_female_reason_rejecting_count_already_dated',
                 'female_female_reason_rejecting_count_interested_but_busy,_please_re-issue_in_3_weeks',
                 'female_female_reason_rejecting_count_engaged',
                 'female_female_reason_rejecting_count_cultural_or_ethnic_background',
                 # 'female_female_reason_rejecting_count_child_status_from_matches',
                 # 'female_female_reason_rejecting_count_marital_status_from_matches',
                 # 'female_female_reason_rejecting_count_interested_but_busy,_please_re-issue_in_3_weeks_from_matches',
                 'female_female_reason_rejecting_count_family_background',
                 'female_female_reason_rejecting_count_speaking_virtually',
                 'female_female_reason_rejecting_count_ai_declined',
                 'female_female_reason_rejecting_count_ai_accepted',
                 'female_female_reason_rejecting_count_ai_no_response',
                 'female_female_reason_rejecting_count_ai_suggestion',
                 'female_female_reason_rejecting_count_ai_unsure',
                 'female_female_reason_rejecting_count_dated',
                 # 'female_female_reason_rejecting_count_went_on_date(s)_&_not_going_out_again_from_matches',
                 'female_female_reason_rejecting_count_religious_level',
                 'female_female_reason_rejecting_count_busy_with_other_matches',
                 'male_male_reason_rejecting_count_already_friends_with_this_person',
                 'male_male_reason_rejecting_count_null',
                 'male_male_reason_rejecting_count_spoke_on_phone',
                 'male_male_reason_rejecting_count_other',
                 'male_male_reason_rejecting_count_physical_look',
                 'male_male_reason_rejecting_count_too_far/_distance',
                 'male_male_reason_rejecting_count_not_my_personality_type',
                 'male_male_reason_rejecting_count_too_religious',
                 'male_male_reason_rejecting_count_we_already_dated',
                 'male_male_reason_rejecting_count_age',
                 'male_male_reason_rejecting_count_went_on_date(s)_&_not_going_out_again',
                 'male_male_reason_rejecting_count_not_religious_enough',
                 'male_male_reason_rejecting_count_education_level',
                 'male_male_reason_rejecting_count_none',
                 'male_male_reason_rejecting_count_never_got_in_touch',
                 'male_male_reason_rejecting_count_spoke_on_phone_&_not_going_out',
                 'male_male_reason_rejecting_count_went_on_first_date',
                 'male_male_reason_rejecting_count_went_on_multiple_dates',
                 'male_male_reason_rejecting_count_engaged',
                 'male_male_reason_rejecting_count_already_know_this_person',
                 'male_male_reason_rejecting_count_child_status',
                 'male_male_reason_rejecting_count_marital_status',
                 'male_male_reason_rejecting_count_dating_exclusively',
                 'male_male_reason_rejecting_count_know_already',
                 'male_male_reason_rejecting_count_distance',
                 'male_male_reason_rejecting_count_education',
                 'male_male_reason_rejecting_count_personality',
                 'male_male_reason_rejecting_count_already_dated',
                 'male_male_reason_rejecting_count_interested_but_busy,_please_re-issue_in_3_weeks',
                 # 'male_male_reason_rejecting_count_interested_but_busy,_please_re-issue_in_3_weeks_from_matches',
                 'male_male_reason_rejecting_count_male_timed_out',
                 'male_male_reason_rejecting_count_cultural_or_ethnic_background',
                 # 'male_male_reason_rejecting_count_child_status_from_matches',
                 # 'male_male_reason_rejecting_count_marital_status_from_matches',
                 'male_male_reason_rejecting_count_speaking_virtually',
                 'male_male_reason_rejecting_count_ai_declined',
                 'male_male_reason_rejecting_count_ai_no_response',
                 'male_male_reason_rejecting_count_ai_suggestion',
                 'male_male_reason_rejecting_count_ai_accepted',
                 'male_male_reason_rejecting_count_ai_unsure',
                 'male_male_reason_rejecting_count_family_background',
                 'male_male_reason_rejecting_count_religious_level',
                 'male_male_reason_rejecting_count_dated',
                 # 'male_male_reason_rejecting_count_went_on_date(s)_&_not_going_out_again_from_matches',
                 'male_male_reason_rejecting_count_busy_with_other_matches',
                 'male_male_reason_rejecting_count__went_on_date(s)_&_not_going_out_again',
                 'male_rejects_female_product_physical_look',
                 'female_rejects_male_product_physical_look',
                 'female_rejects_male_product_null',
                 'female_rejects_male_product_other',
                 'male_rejects_female_product_other',
                 'male_rejects_female_product_null',
                 'male_rejects_female_product_personality',
                 'male_rejects_female_product_know_already',
                 'male_rejects_female_product_too_religious',
                 'male_rejects_female_product_age'
                  ]

multi_val_imp_cat_names = ['female_acceptable_kosher_observance', 'male_acceptable_kosher_observance',
                        'female_body_type_preference', 'male_body_type_preference',
                        'female_acceptable_religious_orientation', 'male_acceptable_religious_orientation',
                        'female_acceptable_aliyah_responses', 'male_acceptable_aliyah_responses', 'male_desired_female_hc']

def drop_columns(df: pd.DataFrame, extra_col=[]) -> pd.DataFrame:
    detect = ['is_good_match']
    # female_looks_rejected_count = ['female_female_looks_rejected_count'] if 'female_female_looks_rejected_count' in df.columns else []
    # print(female_looks_rejected_count)
    all_columns_to_keep = imp_cat_names + imp_cont_names + detect + extra_col
    df = df[all_columns_to_keep]
    return df

def one_hot_encode(df: pd.DataFrame) -> pd.DataFrame:
    for column_title in multi_val_imp_cat_names:
        prefix = column_title
        stacked_categories = df[column_title].str.split(';', expand=True).stack().str.strip()
        one_hot_encoded_prefixed = pd.get_dummies(stacked_categories, prefix=prefix).groupby(level=0).sum()
        df = pd.concat([df, one_hot_encoded_prefixed], axis=1)

    df.drop(columns=multi_val_imp_cat_names, inplace=True)
    return df


def integer_encode_and_pad(df: pd.DataFrame) -> (pd.DataFrame, dict):
    """
    Converts multi-value categorical strings to padded integer sequences using pure Python.

    Returns:
        - The updated DataFrame with integer-encoded columns.
        - A dictionary of vocabulary mappings for each column.
    """
    vocab_mappings = {}

    for col in multi_val_imp_cat_names:
        # 1. Find all unique categories and create a vocabulary
        all_categories = df[col].str.split(';', expand=True).stack().str.strip().unique()
        vocab = {category: i + 1 for i, category in enumerate(all_categories)}  # 0 is for padding
        vocab_mappings[col] = vocab

        # 2. Transform the strings in each row to a list of integers
        def to_integer_list(row_str):
            if pd.isna(row_str):
                return []
            categories = [s.strip() for s in row_str.split(';')]
            return [vocab.get(cat) for cat in categories if cat in vocab]

        integer_lists = df[col].apply(to_integer_list).tolist()

        # 3. Pad the lists to a uniform length using a list comprehension
        max_length = max(len(lst) for lst in integer_lists)
        padded_lists = [lst + [0] * (max_length - len(lst)) for lst in integer_lists]

        # 4. Replace the original column with the padded sequences
        df[col] = padded_lists

    return df, vocab_mappings

def fill_nulls(df: pd.DataFrame) -> pd.DataFrame:
    # Identify columns that do not contain lists
    scalar_cols = [
        col for col in df.columns
        if df[col].first_valid_index() is None or not isinstance(df[col].loc[df[col].first_valid_index()], list)
    ]

    # Iterate through the scalar columns and fill them one by one
    for col in scalar_cols:
        # Calculate the mode for the individual column
        mode_val = df[col].mode()

        # Only fill if a mode actually exists
        if not mode_val.empty:
            df[col] = df[col].fillna(mode_val.iloc[0])

    return df

def get_cat_names():
    return  ['male_id',
             'female_id',
             # 'female_body_type', # didn't help
             # 'male_body_type', # didn't help
             # 'female_kosher', # didn't help
             # 'male_kosher', # didn't help
             # 'female_going_out_to_movies', # didn't help
             # 'male_going_out_to_movies', # didn't help
             # 'female_female_hc',
             # 'male_male_hc',
             # 'female_religious_orientation', # Feature 'female_religious_orientation': MAE change = 0.000377
             # 'male_religious_orientation',  # Feature 'male_religious_orientation': MAE change = 0.000151
             # 'female_torah_study',
             # 'female_watching_tv',
             # 'female_going_out_to_movies', # didn't help
             # 'female_watching_movies_at_home', # didn't help
             # 'male_torah_study',
             # 'male_watching_tv',
             # 'male_going_out_to_movies',
             # 'male_watching_movies_at_home',
             # 'female_eye_color',
             # 'female_hair_color',
             # 'male_eye_color',
             # 'male_hair_color',
             # 'female_age',
             # 'female_how_many_children',
             # 'female_number_live_with_you',
             # 'female_number_of_siblings',
             # 'female_age_min',
             # 'female_age_max',
             # 'female_height_inches',
             # 'female_max_height_inches',
             # 'female_min_height_inches',
             # 'female_num_matches',
             # 'female_acceptance_rate',
             # 'male_age',
             # 'male_how_many_children',
             # 'male_number_live_with_you',
             # 'male_number_of_siblings',
             # 'male_age_min',
             # 'male_age_max',
             # 'male_height_inches',
             # 'male_min_height_inches',
             # 'male_max_height_inches',
             # 'male_num_matches',
             # 'male_acceptance_rate',
             # 'is_good_match',
            ]
def get_cont_names():
    return [
            'male_rejects_female_product_physical_look',
            'female_rejects_male_product_physical_look',
            'female_rejects_male_product_null',
            'female_rejects_male_product_other',
            'male_rejects_female_product_other',
            'male_rejects_female_product_null',
            'male_rejects_female_product_personality',
            'male_rejects_female_product_know_already',
            'male_rejects_female_product_too_religious',
            'male_rejects_female_product_age',
            #'female_age', # female_age: 0.000855
            # 'female_how_many_children',
            # 'female_number_live_with_you',
            # 'female_number_of_siblings',
            # 'female_age_min', #throws errors
            # 'female_age_max', #throws errors
            # 'female_height_inches', # near zero MAE change
            # 'female_max_height_inches', #throws errors
            # 'female_min_height_inches', #throws errors
            # 'female_num_matches',
            'female_acceptance_rate', # Feature 'female_acceptance_rate': MAE change = 0.010291 KEEP
            # 'male_age', # KEEP but later got lower so dropping
            # 'male_how_many_children',
            # 'male_number_live_with_you',
            # 'male_number_of_siblings',
            # 'male_age_min', #throws errors
            # 'male_age_max', #throws errors
            # 'male_height_inches', # KEEP
            # 'male_min_height_inches', #throws errors
            # 'male_max_height_inches', #throws errors
            # 'male_num_matches',
            # 'male_acceptance_rate', # Feature 'male_acceptance_rate': MAE change = 0.002119 KEEP but later got lower so dropping
            # 'female_body_type_preference_A Few Extra Pounds', # Feature 'female_body_type_preference_A Few Extra Pounds': MAE change = 0.001036 KEEP but later got lower so dropping
            # 'female_body_type_preference_Any',
            # 'female_body_type_preference_Athletic/Fit', # Feature 'female_body_type_preference_Athletic/Fit': MAE change = 0.001041 KEEP but later got lower so dropping
            # 'female_body_type_preference_Average/Medium Build', # near zero MAE change
            # 'female_body_type_preference_Firm & Toned', # near zero MAE change
            # 'female_body_type_preference_Large/Broad Build', # near zero MAE change
            # 'female_body_type_preference_Lean/Slender', # near zero MAE change
            # 'female_body_type_preference_Muscular', # near zero MAE change
            # 'female_body_type_preference_Petite', # near zero MAE change
            # 'female_body_type_preference_Proportional', # near zero MAE change
            # 'male_body_type_preference_A Few Extra Pounds',  # near zero MAE change
            # 'male_body_type_preference_Any', # near zero MAE change
            # 'male_body_type_preference_Athletic/Fit', # near zero MAE change
            # 'male_body_type_preference_Average/Medium Build', #Feature 'male_body_type_preference_Average/Medium Build': MAE change = 0.001256 but later got lower so dropping
            # 'male_body_type_preference_Firm & Toned', # near zero MAE change
            # 'male_body_type_preference_Large/Broad Build', # near zero MAE change
            # 'male_body_type_preference_Lean/Slender', # near zero MAE change
            # 'male_body_type_preference_Muscular', #Feature 'male_body_type_preference_Muscular': MAE change = 0.001084 but later got lower so dropping
            # 'male_body_type_preference_Petite', # near zero MAE change
            # 'male_body_type_preference_Proportional', # near zero MAE change
            # 'female_acceptable_religious_orientation_Any',
            # 'female_acceptable_religious_orientation_Chassidish', # these one's never come up
            # 'female_acceptable_religious_orientation_Conservadox',
            # 'female_acceptable_religious_orientation_Conservative',
            # 'female_acceptable_religious_orientation_Heimish',
            # 'female_acceptable_religious_orientation_Just Jewish',
            # 'female_acceptable_religious_orientation_Lubavitch',
            # 'female_acceptable_religious_orientation_Modern Orthodox (Machmir)',# near zero MAE change
            # 'female_acceptable_religious_orientation_Modern Orthodox (Middle of the road)',# near zero MAE change
            # 'female_acceptable_religious_orientation_Modern Orthodox (liberal)',# near zero MAE change
            # 'female_acceptable_religious_orientation_Modern Yeshivish',# near zero MAE change
            # 'female_acceptable_religious_orientation_Reform',
            # 'female_acceptable_religious_orientation_Spiritual but not religious',
            # 'female_acceptable_religious_orientation_Strictly Frum/Not Yeshivish',# near zero MAE change
            # 'female_acceptable_religious_orientation_Traditional',
            # 'female_acceptable_religious_orientation_Unaffiliated',
            # 'female_acceptable_religious_orientation_Yeshivish',
            # 'male_acceptable_religious_orientation_Any',
            # 'male_acceptable_religious_orientation_Balabatish',
            # 'male_acceptable_religious_orientation_Carlebachian',
            # 'male_acceptable_religious_orientation_Chassidish',
            # 'male_acceptable_religious_orientation_Conservadox',
            # 'male_acceptable_religious_orientation_Conservative',
            # 'male_acceptable_religious_orientation_Heimish',
            # 'male_acceptable_religious_orientation_Just Jewish',
            # 'male_acceptable_religious_orientation_Lubavitch',
            # 'male_acceptable_religious_orientation_Modern Orthodox (Machmir)',# near zero MAE change
            # 'male_acceptable_religious_orientation_Modern Orthodox (Middle of the road)',# near zero MAE change
            # 'male_acceptable_religious_orientation_Modern Orthodox (liberal)',# near zero MAE change
            # 'male_acceptable_religious_orientation_Modern Yeshivish',# near zero MAE change
            # 'male_acceptable_religious_orientation_Reconstructionist',
            # 'male_acceptable_religious_orientation_Reform',
            # 'male_acceptable_religious_orientation_Sephardi',
            # 'male_acceptable_religious_orientation_Spiritual but not religious',
            # 'male_acceptable_religious_orientation_Strictly Frum/Not Yeshivish',
            # 'male_acceptable_religious_orientation_Traditional',
            # 'male_acceptable_religious_orientation_Unaffiliated',
            # 'male_acceptable_religious_orientation_Yekkish',
            # 'male_acceptable_religious_orientation_Yeshivish',
            # 'female_acceptable_aliyah_responses_Already Live in Israel',# near zero MAE change
            # 'female_acceptable_aliyah_responses_Maybe',# near zero MAE change
            # 'female_acceptable_aliyah_responses_Maybe or Preferred but not required',# near zero MAE change
            # 'female_acceptable_aliyah_responses_No',# near zero MAE change
            # 'female_acceptable_aliyah_responses_Yes',# near zero MAE change
            # 'male_acceptable_aliyah_responses_Already Live in Israel',# near zero MAE change
            # 'male_acceptable_aliyah_responses_Maybe',# near zero MAE change
            # 'male_acceptable_aliyah_responses_No',# near zero MAE change
            # 'male_acceptable_aliyah_responses_Yes',# near zero MAE change
            # 'male_desired_female_hc_Any',# near zero MAE change
            # 'male_desired_female_hc_Fully',# near zero MAE change
            # 'male_desired_female_hc_Fully with Sheitel',# near zero MAE change
            # 'male_desired_female_hc_Not at all',# near zero MAE change
            # 'male_desired_female_hc_Not important',# near zero MAE change
            # 'male_desired_female_hc_Partially',# near zero MAE change
            # 'male_desired_female_hc_Possibly',# near zero MAE change
            # 'male_desired_female_hc_Up to her',# near zero MAE change
            # 'female_acceptable_kosher_observance_Almost Never/Not at all',#female_acceptable_kosher_observance_Almost Never/Not at all: 0.001710
            # 'female_acceptable_kosher_observance_Always',# near zero MAE change
            # 'female_acceptable_kosher_observance_At home', #female_acceptable_kosher_observance_At home: 0.001933
            # 'female_acceptable_kosher_observance_At home & I eat dairy at non-kosher restaurants',# near zero MAE change
            # 'female_acceptable_kosher_observance_To some degree',# near zero MAE change
            # 'male_acceptable_kosher_observance_Almost Never/Not at all', # near zero MAE change
            # 'male_acceptable_kosher_observance_Always',# near zero MAE change
            # 'male_acceptable_kosher_observance_At home',# near zero MAE change
            # 'male_acceptable_kosher_observance_At home & I eat dairy at non-kosher restaurants',# near zero MAE change
            # 'male_acceptable_kosher_observance_To some degree',# near zero MAE change
            # 'female_female_rejection_count_null', #keep
            # 'female_female_rejection_count_dated',
            # 'female_female_rejection_count_spoke_on_phone_&_not_going_out',
            # 'female_female_rejection_count_spoke_on_phone',
            # 'female_female_rejection_count_went_on_date(s)_&_not_going_out_again',
            # 'female_female_rejection_count_never_got_in_touch',
            # 'female_female_rejection_count_not_my_physical_look',
            # 'female_female_rejection_count_other', #keep
            # 'female_female_rejection_count_we_already_dated',
            # 'female_female_rejection_count_too_far/_distance',
            # 'female_female_rejection_count_religious_level',
            # 'female_female_rejection_count_not_my_personality_type',
            # 'female_female_rejection_count_age',
            # 'female_female_rejection_count_went_on_date(s)_&_not_going_out_again_from_matches',
            # 'female_female_rejection_count_already_friends_with_this_person',
            # 'female_female_rejection_count_went_on_first_date',
            # 'female_female_rejection_count_busy_with_other_matches',
            # 'female_female_rejection_count__went_on_date(s)_&_not_going_out_again',
            # 'female_female_rejection_count_education_level',
            # 'female_female_rejection_count_went_on_multiple_dates',
            # 'female_female_rejection_count_too_religious',
            # 'female_female_rejection_count_none', #keep
            # 'female_female_rejection_count_not_religious_enough',
            # 'female_female_rejection_count_engaged',
            # 'female_female_rejection_count_already_know_this_person',
            # 'female_female_rejection_count_child_status',
            # 'female_female_rejection_count_marital_status',
            # 'female_female_rejection_count_dating_exclusively',
            # 'female_female_rejection_count_know_already',
            # 'female_female_rejection_count_distance',
            # 'female_female_rejection_count_physical_look', #keep
            # 'female_female_rejection_count_education',
            # 'female_female_rejection_count_personality',
            # 'female_female_rejection_count_already_dated',
            # 'female_female_rejection_count_interested_but_busy,_please_re-issue_in_3_weeks', #keep
            # 'female_female_rejection_count_interested_but_busy,_please_re-issue_in_3_weeks_from_matches',
            # 'female_female_rejection_count_male_timed_out',
            # 'female_female_rejection_count_cultural_or_ethnic_background',
            # 'female_female_rejection_count_child_status_from_matches',
            # 'female_female_rejection_count_marital_status_from_matches',
            # 'female_female_rejection_count_speaking_virtually',
            # 'female_female_rejection_count_ai_declined', #keep
            # 'female_female_rejection_count_ai_no_response',
            # 'female_female_rejection_count_ai_suggestion',
            # 'female_female_rejection_count_ai_accepted',
            # 'female_female_rejection_count_ai_unsure',
            # 'female_female_rejection_count_family_background',
            #  'male_male_rejection_count_null', #keep
            #  'male_male_rejection_count_spoke_on_phone', #keep
            #  'male_male_rejection_count_dated',
            #  'male_male_rejection_count_went_on_first_date', #keep
            #  'male_male_rejection_count_spoke_on_phone_&_not_going_out', #keep
            #  'male_male_rejection_count_never_got_in_touch',
            #  'male_male_rejection_count_went_on_date(s)_&_not_going_out_again',
            #  'male_male_rejection_count_religious_level',
            #  'male_male_rejection_count_went_on_date(s)_&_not_going_out_again_from_matches',
            #  'male_male_rejection_count_other', #keep
            #  'male_male_rejection_count_not_my_personality_type',
            #  'male_male_rejection_count_we_already_dated',
            #  'male_male_rejection_count_not_my_physical_look',
            #  'male_male_rejection_count_too_far/_distance',
            #  'male_male_rejection_count_age',
  #            'male_male_rejection_count_already_friends_with_this_person',
  #            'male_male_rejection_count_education_level',
  #            'male_male_rejection_count_too_religious',#keep
  #            'male_male_rejection_count_not_religious_enough', #keep
  #            'male_male_rejection_count_none',
  #            'male_male_rejection_count_went_on_multiple_dates',
  #            'male_male_rejection_count_already_know_this_person',
  #            'male_male_rejection_count_child_status',#keep
  #            'male_male_rejection_count_marital_status',#keep
  #            'male_male_rejection_count_female_timed_out',
  #            'male_male_rejection_count_dating_exclusively',
  #            'male_male_rejection_count_know_already', #keep
  #            'male_male_rejection_count_distance',#keep
  #            'male_male_rejection_count_physical_look',#keep
  #            'male_male_rejection_count_personality',#keep
  #            'male_male_rejection_count_education',
  #            'male_male_rejection_count_already_dated',#keep
  #            'male_male_rejection_count_interested_but_busy,_please_re-issue_in_3_weeks',
  #            'male_male_rejection_count_engaged',
  #            'male_male_rejection_count_cultural_or_ethnic_background',
  #            'male_male_rejection_count_child_status_from_matches',
  #            'male_male_rejection_count_marital_status_from_matches',#keep
  #            'male_male_rejection_count_interested_but_busy,_please_re-issue_in_3_weeks_from_matches',
  #            'male_male_rejection_count_family_background',
  #            'male_male_rejection_count_speaking_virtually',
  #            'male_male_rejection_count_ai_declined',
  #            'male_male_rejection_count_ai_accepted',
  #            'male_male_rejection_count_ai_no_response',
  #            'male_male_rejection_count_ai_suggestion',
  #            'male_male_rejection_count_ai_unsure',
  #            'male_male_rejection_count_busy_with_other_matches'
        'female_female_rejection_count_null',
        'female_female_rejection_count_spoke_on_phone_&_not_going_out',
        'female_female_rejection_count_spoke_on_phone',
        'female_female_rejection_count_went_on_date(s)_&_not_going_out_again',
        'female_female_rejection_count_never_got_in_touch',
        'female_female_rejection_count_other',
        'female_female_rejection_count_we_already_dated',
        'female_female_rejection_count_too_far/_distance',
        'female_female_rejection_count_not_my_personality_type',
        'female_female_rejection_count_age',
        'female_female_rejection_count_went_on_first_date',
        'female_female_rejection_count_went_on_multiple_dates',
        'female_female_rejection_count_too_religious',
        'female_female_rejection_count_none',
        'female_female_rejection_count_not_religious_enough',
        'female_female_rejection_count_already_know_this_person',
        'female_female_rejection_count_know_already',
        'female_female_rejection_count_distance',
        'female_female_rejection_count_physical_look',
        'female_female_rejection_count_education',
        'female_female_rejection_count_personality',
        'female_female_rejection_count_already_dated',
        'female_female_rejection_count_interested_but_busy,_please_re-issue_in_3_weeks',
        'female_female_rejection_count_cultural_or_ethnic_background',
        'female_female_rejection_count_ai_declined',
        'female_female_rejection_count_ai_no_response',
        'female_female_rejection_count_ai_accepted',
        'female_female_rejection_count_ai_unsure',
        'male_male_rejection_count_null',
        'male_male_rejection_count_spoke_on_phone',
        'male_male_rejection_count_went_on_first_date',
        'male_male_rejection_count_spoke_on_phone_&_not_going_out',
        'male_male_rejection_count_never_got_in_touch',
        'male_male_rejection_count_went_on_date(s)_&_not_going_out_again',
        'male_male_rejection_count_other',
        'male_male_rejection_count_not_my_personality_type',
        'male_male_rejection_count_age',
        'male_male_rejection_count_too_religious',
        'male_male_rejection_count_not_religious_enough',
        'male_male_rejection_count_none',
        'male_male_rejection_count_went_on_multiple_dates',
        'male_male_rejection_count_know_already',
        'male_male_rejection_count_distance',
        'male_male_rejection_count_physical_look',
        'male_male_rejection_count_personality',
        'male_male_rejection_count_education',
        'male_male_rejection_count_already_dated',
        'male_male_rejection_count_cultural_or_ethnic_background',
        'male_male_rejection_count_ai_declined',
        'male_male_rejection_count_ai_accepted',
        'male_male_rejection_count_ai_no_response',
        'male_male_rejection_count_ai_unsure',
        'female_female_reason_rejecting_count_null',
        'female_female_reason_rejecting_count_too_religious',
        'female_female_reason_rejecting_count_spoke_on_phone',
        'female_female_reason_rejecting_count_not_my_personality_type',
        'female_female_reason_rejecting_count_other',
        'female_female_reason_rejecting_count_not_religious_enough',
        'female_female_reason_rejecting_count_age',
        'female_female_reason_rejecting_count_physical_look',
        'female_female_reason_rejecting_count_never_got_in_touch',
        'female_female_reason_rejecting_count_went_on_date(s)_&_not_going_out_again',
        'female_female_reason_rejecting_count_spoke_on_phone_&_not_going_out',
        'female_female_reason_rejecting_count_too_far/_distance',
        'female_female_reason_rejecting_count_went_on_first_date',
        'female_female_reason_rejecting_count_education_level',
        'female_female_reason_rejecting_count_none',
        'female_female_reason_rejecting_count_went_on_multiple_dates',
        'female_female_reason_rejecting_count_already_know_this_person',
        'female_female_reason_rejecting_count_child_status',
        'female_female_reason_rejecting_count_marital_status',
        'female_female_reason_rejecting_count_know_already',
        'female_female_reason_rejecting_count_distance',
        'female_female_reason_rejecting_count_personality',
        'female_female_reason_rejecting_count_education',
        'female_female_reason_rejecting_count_already_dated',
        'female_female_reason_rejecting_count_interested_but_busy,_please_re-issue_in_3_weeks',
        'female_female_reason_rejecting_count_cultural_or_ethnic_background',
        'female_female_reason_rejecting_count_ai_declined',
        'female_female_reason_rejecting_count_ai_accepted',
        'female_female_reason_rejecting_count_ai_no_response',
        'female_female_reason_rejecting_count_ai_unsure',
        'male_male_reason_rejecting_count_null',
        'male_male_reason_rejecting_count_spoke_on_phone',
        'male_male_reason_rejecting_count_other',
        'male_male_reason_rejecting_count_physical_look',
        'male_male_reason_rejecting_count_too_far/_distance',
        'male_male_reason_rejecting_count_not_my_personality_type',
        'male_male_reason_rejecting_count_too_religious',
        'male_male_reason_rejecting_count_age',
        'male_male_reason_rejecting_count_went_on_date(s)_&_not_going_out_again',
        'male_male_reason_rejecting_count_not_religious_enough',
        'male_male_reason_rejecting_count_none',
        'male_male_reason_rejecting_count_never_got_in_touch',
        'male_male_reason_rejecting_count_spoke_on_phone_&_not_going_out',
        'male_male_reason_rejecting_count_went_on_first_date',
        'male_male_reason_rejecting_count_went_on_multiple_dates',
        'male_male_reason_rejecting_count_already_know_this_person',
        'male_male_reason_rejecting_count_marital_status',
        'male_male_reason_rejecting_count_know_already',
        'male_male_reason_rejecting_count_distance',
        'male_male_reason_rejecting_count_education',
        'male_male_reason_rejecting_count_personality',
        'male_male_reason_rejecting_count_already_dated',
        'male_male_reason_rejecting_count_interested_but_busy,_please_re-issue_in_3_weeks',
        'male_male_reason_rejecting_count_cultural_or_ethnic_background',
        'male_male_reason_rejecting_count_ai_declined',
        'male_male_reason_rejecting_count_ai_no_response',
        'male_male_reason_rejecting_count_ai_accepted',
        'male_male_reason_rejecting_count_ai_unsure',
        'male_rejects_female_product_physical_look',
        'female_rejects_male_product_physical_look',
        'female_rejects_male_product_null',
        'female_rejects_male_product_other',
        'male_rejects_female_product_other',
        'male_rejects_female_product_null',
        'male_rejects_female_product_personality',
        'male_rejects_female_product_know_already',
        'male_rejects_female_product_too_religious',
        'male_rejects_female_product_age'

            ]


def get_forest_cat_names():
    return [
        'female_body_type', # didn't help
        'male_body_type', # didn't help
        'female_kosher', # didn't help
        'male_kosher', # didn't help
        # 'female_going_out_to_movies', # didn't help
        # 'male_going_out_to_movies', # didn't help
        'female_female_hc',
        'male_male_hc',
        'female_religious_orientation', # Feature 'female_religious_orientation': MAE change = 0.000377
        'male_religious_orientation',  # Feature 'male_religious_orientation': MAE change = 0.000151
        'female_torah_study',
        'female_watching_tv',
        # 'female_going_out_to_movies', # didn't help
        # 'female_watching_movies_at_home', # didn't help
        'male_torah_study',
        'male_watching_tv',
        # 'male_going_out_to_movies', #caused to break
        # 'male_watching_movies_at_home', #caused to break
        'female_eye_color',
        'female_hair_color',
        'male_eye_color',
        'male_hair_color',
        'female_body_type_preference_A Few Extra Pounds', # Feature 'female_body_type_preference_A Few Extra Pounds': MAE change = 0.001036 KEEP but later got lower so dropping
        'female_body_type_preference_Any',
        'female_body_type_preference_Athletic/Fit', # Feature 'female_body_type_preference_Athletic/Fit': MAE change = 0.001041 KEEP but later got lower so dropping
        'female_body_type_preference_Average/Medium Build', # near zero MAE change
        'female_body_type_preference_Firm & Toned', # near zero MAE change
        'female_body_type_preference_Large/Broad Build', # near zero MAE change
        'female_body_type_preference_Lean/Slender', # near zero MAE change
        'female_body_type_preference_Muscular', # near zero MAE change
        'female_body_type_preference_Petite', # near zero MAE change
        'female_body_type_preference_Proportional', # near zero MAE change
        'male_body_type_preference_A Few Extra Pounds',  # near zero MAE change
        'male_body_type_preference_Any', # near zero MAE change
        'male_body_type_preference_Athletic/Fit', # near zero MAE change
        'male_body_type_preference_Average/Medium Build', #Feature 'male_body_type_preference_Average/Medium Build': MAE change = 0.001256 but later got lower so dropping
        'male_body_type_preference_Firm & Toned', # near zero MAE change
        'male_body_type_preference_Large/Broad Build', # near zero MAE change
        'male_body_type_preference_Lean/Slender', # near zero MAE change
        'male_body_type_preference_Muscular', #Feature 'male_body_type_preference_Muscular': MAE change = 0.001084 but later got lower so dropping
        'male_body_type_preference_Petite', # near zero MAE change
        'male_body_type_preference_Proportional', # near zero MAE change
        'female_acceptable_religious_orientation_Any',
        'female_acceptable_religious_orientation_Chassidish', # these one's never come up
        'female_acceptable_religious_orientation_Conservadox',
        'female_acceptable_religious_orientation_Conservative',
        'female_acceptable_religious_orientation_Heimish',
        'female_acceptable_religious_orientation_Just Jewish',
        'female_acceptable_religious_orientation_Lubavitch',
        'female_acceptable_religious_orientation_Modern Orthodox (Machmir)',# near zero MAE change
        'female_acceptable_religious_orientation_Modern Orthodox (Middle of the road)',# near zero MAE change
        'female_acceptable_religious_orientation_Modern Orthodox (liberal)',# near zero MAE change
        'female_acceptable_religious_orientation_Modern Yeshivish',# near zero MAE change
        'female_acceptable_religious_orientation_Reform',
        'female_acceptable_religious_orientation_Spiritual but not religious',
        'female_acceptable_religious_orientation_Strictly Frum/Not Yeshivish',# near zero MAE change
        'female_acceptable_religious_orientation_Traditional',
        'female_acceptable_religious_orientation_Unaffiliated',
        'female_acceptable_religious_orientation_Yeshivish',
        'male_acceptable_religious_orientation_Any',
        'male_acceptable_religious_orientation_Balabatish',
        'male_acceptable_religious_orientation_Carlebachian',
        'male_acceptable_religious_orientation_Chassidish',
        'male_acceptable_religious_orientation_Conservadox',
        'male_acceptable_religious_orientation_Conservative',
        'male_acceptable_religious_orientation_Heimish',
        'male_acceptable_religious_orientation_Just Jewish',
        'male_acceptable_religious_orientation_Lubavitch',
        'male_acceptable_religious_orientation_Modern Orthodox (Machmir)',# near zero MAE change
        'male_acceptable_religious_orientation_Modern Orthodox (Middle of the road)',# near zero MAE change
        'male_acceptable_religious_orientation_Modern Orthodox (liberal)',# near zero MAE change
        'male_acceptable_religious_orientation_Modern Yeshivish',# near zero MAE change
        'male_acceptable_religious_orientation_Reconstructionist',
        'male_acceptable_religious_orientation_Reform',
        'male_acceptable_religious_orientation_Sephardi',
        'male_acceptable_religious_orientation_Spiritual but not religious',
        'male_acceptable_religious_orientation_Strictly Frum/Not Yeshivish',
        'male_acceptable_religious_orientation_Traditional',
        'male_acceptable_religious_orientation_Unaffiliated',
        'male_acceptable_religious_orientation_Yekkish',
        'male_acceptable_religious_orientation_Yeshivish',
        'female_acceptable_aliyah_responses_Already Live in Israel',# near zero MAE change
        'female_acceptable_aliyah_responses_Maybe',# near zero MAE change
        'female_acceptable_aliyah_responses_Maybe or Preferred but not required',# near zero MAE change
        'female_acceptable_aliyah_responses_No',# near zero MAE change
        'female_acceptable_aliyah_responses_Yes',# near zero MAE change
        'male_acceptable_aliyah_responses_Already Live in Israel',# near zero MAE change
        'male_acceptable_aliyah_responses_Maybe',# near zero MAE change
        'male_acceptable_aliyah_responses_No',# near zero MAE change
        'male_acceptable_aliyah_responses_Yes',# near zero MAE change
        'male_desired_female_hc_Any',# near zero MAE change
        'male_desired_female_hc_Fully',# near zero MAE change
        'male_desired_female_hc_Fully with Sheitel',# near zero MAE change
        'male_desired_female_hc_Not at all',# near zero MAE change
        'male_desired_female_hc_Not important',# near zero MAE change
        'male_desired_female_hc_Partially',# near zero MAE change
        'male_desired_female_hc_Possibly',# near zero MAE change
        'male_desired_female_hc_Up to her',# near zero MAE change
        'female_acceptable_kosher_observance_Almost Never/Not at all',#female_acceptable_kosher_observance_Almost Never/Not at all: 0.001710
        'female_acceptable_kosher_observance_Always',# near zero MAE change
        'female_acceptable_kosher_observance_At home', #female_acceptable_kosher_observance_At home: 0.001933
        'female_acceptable_kosher_observance_At home & I eat dairy at non-kosher restaurants',# near zero MAE change
        'female_acceptable_kosher_observance_To some degree',# near zero MAE change
        'male_acceptable_kosher_observance_Almost Never/Not at all', # near zero MAE change
        'male_acceptable_kosher_observance_Always',# near zero MAE change
        'male_acceptable_kosher_observance_At home',# near zero MAE change
        'male_acceptable_kosher_observance_At home & I eat dairy at non-kosher restaurants',# near zero MAE change
        'male_acceptable_kosher_observance_To some degree',# near zero MAE change
    ]

def get_forest_cont_names():
    return [
       'female_age', # female_age: 0.000855
        'female_how_many_children',
        'female_number_live_with_you',
        # 'female_number_of_siblings',
        # 'female_age_min', #throws errors
        # 'female_age_max', #throws errors
        'female_height_inches', # near zero MAE change
        # 'female_max_height_inches', #throws errors
        # 'female_min_height_inches', #throws errors
        'female_num_matches',
        'female_acceptance_rate',  # Feature 'female_acceptance_rate': MAE change = 0.010291 KEEP
        'male_age', # KEEP but later got lower so dropping
        'male_how_many_children',
        'male_number_live_with_you',
        # 'male_number_of_siblings',
        # 'male_age_min', #throws errors
        # 'male_age_max', #throws errors
        'male_height_inches',  # KEEP
        # 'male_min_height_inches', #throws errors
        # 'male_max_height_inches', #throws errors
        'male_num_matches',
        'male_acceptance_rate', # Feature 'male_acceptance_rate': MAE change = 0.002119 KEEP but later got lower so dropping
        'female_female_rejection_count_null',
        'female_female_rejection_count_dated',
        'female_female_rejection_count_spoke_on_phone_&_not_going_out',
        'female_female_rejection_count_spoke_on_phone',
        'female_female_rejection_count_went_on_date(s)_&_not_going_out_again',
        'female_female_rejection_count_never_got_in_touch',
        # 'female_female_rejection_count_not_my_physical_look',
        'female_female_rejection_count_other',
        'female_female_rejection_count_we_already_dated',
        'female_female_rejection_count_too_far/_distance',
        'female_female_rejection_count_religious_level',
        'female_female_rejection_count_not_my_personality_type',
        'female_female_rejection_count_age',
        # 'female_female_rejection_count_went_on_date(s)_&_not_going_out_again_from_matches',
        'female_female_rejection_count_already_friends_with_this_person',
        'female_female_rejection_count_went_on_first_date',
        'female_female_rejection_count_busy_with_other_matches',
        'female_female_rejection_count__went_on_date(s)_&_not_going_out_again',
        'female_female_rejection_count_education_level',
        'female_female_rejection_count_went_on_multiple_dates',
        'female_female_rejection_count_too_religious',
        'female_female_rejection_count_none',
        'female_female_rejection_count_not_religious_enough',
        'female_female_rejection_count_engaged',
        'female_female_rejection_count_already_know_this_person',
        'female_female_rejection_count_child_status',
        'female_female_rejection_count_marital_status',
        'female_female_rejection_count_dating_exclusively',
        'female_female_rejection_count_know_already',
        'female_female_rejection_count_distance',
        'female_female_rejection_count_physical_look',
        'female_female_rejection_count_education',
        'female_female_rejection_count_personality',
        'female_female_rejection_count_already_dated',
        'female_female_rejection_count_interested_but_busy,_please_re-issue_in_3_weeks',
        # 'female_female_rejection_count_interested_but_busy,_please_re-issue_in_3_weeks_from_matches',
        'female_female_rejection_count_male_timed_out',
        'female_female_rejection_count_cultural_or_ethnic_background',
        # 'female_female_rejection_count_child_status_from_matches',
        # 'female_female_rejection_count_marital_status_from_matches',
        'female_female_rejection_count_speaking_virtually',
        'female_female_rejection_count_ai_declined',
        'female_female_rejection_count_ai_no_response',
        'female_female_rejection_count_ai_suggestion',
        'female_female_rejection_count_ai_accepted',
        'female_female_rejection_count_ai_unsure',
        'female_female_rejection_count_family_background',
         'male_male_rejection_count_null',
         'male_male_rejection_count_spoke_on_phone',
         'male_male_rejection_count_dated',
         'male_male_rejection_count_went_on_first_date',
         'male_male_rejection_count_spoke_on_phone_&_not_going_out',
         'male_male_rejection_count_never_got_in_touch',
         'male_male_rejection_count_went_on_date(s)_&_not_going_out_again',
         'male_male_rejection_count_religious_level',
         # 'male_male_rejection_count_went_on_date(s)_&_not_going_out_again_from_matches',
         'male_male_rejection_count_other',
         'male_male_rejection_count_not_my_personality_type',
         'male_male_rejection_count_we_already_dated',
         # 'male_male_rejection_count_not_my_physical_look',
         'male_male_rejection_count_too_far/_distance',
         'male_male_rejection_count_age',
         'male_male_rejection_count_already_friends_with_this_person',
         'male_male_rejection_count_education_level',
         'male_male_rejection_count_too_religious',
         'male_male_rejection_count_not_religious_enough',
         'male_male_rejection_count_none',
         'male_male_rejection_count_went_on_multiple_dates',
         'male_male_rejection_count_already_know_this_person',
         'male_male_rejection_count_child_status',
         'male_male_rejection_count_marital_status',
         'male_male_rejection_count_female_timed_out',
         'male_male_rejection_count_dating_exclusively',
         'male_male_rejection_count_know_already',
         'male_male_rejection_count_distance',
         'male_male_rejection_count_physical_look',
         'male_male_rejection_count_personality',
         'male_male_rejection_count_education',
         'male_male_rejection_count_already_dated',
         'male_male_rejection_count_interested_but_busy,_please_re-issue_in_3_weeks',
         'male_male_rejection_count_engaged',
         'male_male_rejection_count_cultural_or_ethnic_background',
         # 'male_male_rejection_count_child_status_from_matches',
         # 'male_male_rejection_count_marital_status_from_matches',
         # 'male_male_rejection_count_interested_but_busy,_please_re-issue_in_3_weeks_from_matches',
         'male_male_rejection_count_family_background',
         'male_male_rejection_count_speaking_virtually',
         'male_male_rejection_count_ai_declined',
         'male_male_rejection_count_ai_accepted',
         'male_male_rejection_count_ai_no_response',
         'male_male_rejection_count_ai_suggestion',
         'male_male_rejection_count_ai_unsure',
         'male_male_rejection_count_busy_with_other_matches',
         # 'collab_pred',
        'female_female_reason_rejecting_count_null',
        'female_female_reason_rejecting_count_too_religious',
        'female_female_reason_rejecting_count_spoke_on_phone',
        'female_female_reason_rejecting_count_not_my_personality_type',
        'female_female_reason_rejecting_count_other',
        'female_female_reason_rejecting_count_not_religious_enough',
        'female_female_reason_rejecting_count_age',
        'female_female_reason_rejecting_count_physical_look',
        'female_female_reason_rejecting_count_already_friends_with_this_person',
        'female_female_reason_rejecting_count_never_got_in_touch',
        'female_female_reason_rejecting_count_we_already_dated',
        'female_female_reason_rejecting_count_went_on_date(s)_&_not_going_out_again',
        'female_female_reason_rejecting_count_spoke_on_phone_&_not_going_out',
        'female_female_reason_rejecting_count_too_far/_distance',
        'female_female_reason_rejecting_count_went_on_first_date',
        'female_female_reason_rejecting_count_education_level',
        'female_female_reason_rejecting_count_none',
        'female_female_reason_rejecting_count_went_on_multiple_dates',
        'female_female_reason_rejecting_count_already_know_this_person',
        'female_female_reason_rejecting_count_child_status',
        'female_female_reason_rejecting_count_marital_status',
        'female_female_reason_rejecting_count_female_timed_out',
        'female_female_reason_rejecting_count_dating_exclusively',
        'female_female_reason_rejecting_count_know_already',
        'female_female_reason_rejecting_count_distance',
        'female_female_reason_rejecting_count_personality',
        'female_female_reason_rejecting_count_education',
        'female_female_reason_rejecting_count_already_dated',
        'female_female_reason_rejecting_count_interested_but_busy,_please_re-issue_in_3_weeks',
        'female_female_reason_rejecting_count_engaged',
        'female_female_reason_rejecting_count_cultural_or_ethnic_background',
        # 'female_female_reason_rejecting_count_child_status_from_matches',
        # 'female_female_reason_rejecting_count_marital_status_from_matches',
        # 'female_female_reason_rejecting_count_interested_but_busy,_please_re-issue_in_3_weeks_from_matches',
        'female_female_reason_rejecting_count_family_background',
        'female_female_reason_rejecting_count_speaking_virtually',
        'female_female_reason_rejecting_count_ai_declined',
        'female_female_reason_rejecting_count_ai_accepted',
        'female_female_reason_rejecting_count_ai_no_response',
        'female_female_reason_rejecting_count_ai_suggestion',
        'female_female_reason_rejecting_count_ai_unsure',
        'female_female_reason_rejecting_count_dated',
        # 'female_female_reason_rejecting_count_went_on_date(s)_&_not_going_out_again_from_matches',
        'female_female_reason_rejecting_count_religious_level',
        'female_female_reason_rejecting_count_busy_with_other_matches',
        'male_male_reason_rejecting_count_already_friends_with_this_person',
        'male_male_reason_rejecting_count_null',
        'male_male_reason_rejecting_count_spoke_on_phone',
        'male_male_reason_rejecting_count_other',
        'male_male_reason_rejecting_count_physical_look',
        'male_male_reason_rejecting_count_too_far/_distance',
        'male_male_reason_rejecting_count_not_my_personality_type',
        'male_male_reason_rejecting_count_too_religious',
        'male_male_reason_rejecting_count_we_already_dated',
        'male_male_reason_rejecting_count_age',
        'male_male_reason_rejecting_count_went_on_date(s)_&_not_going_out_again',
        'male_male_reason_rejecting_count_not_religious_enough',
        'male_male_reason_rejecting_count_education_level',
        'male_male_reason_rejecting_count_none',
        'male_male_reason_rejecting_count_never_got_in_touch',
        'male_male_reason_rejecting_count_spoke_on_phone_&_not_going_out',
        'male_male_reason_rejecting_count_went_on_first_date',
        'male_male_reason_rejecting_count_went_on_multiple_dates',
        'male_male_reason_rejecting_count_engaged',
        'male_male_reason_rejecting_count_already_know_this_person',
        'male_male_reason_rejecting_count_child_status',
        'male_male_reason_rejecting_count_marital_status',
        'male_male_reason_rejecting_count_dating_exclusively',
        'male_male_reason_rejecting_count_know_already',
        'male_male_reason_rejecting_count_distance',
        'male_male_reason_rejecting_count_education',
        'male_male_reason_rejecting_count_personality',
        'male_male_reason_rejecting_count_already_dated',
        'male_male_reason_rejecting_count_interested_but_busy,_please_re-issue_in_3_weeks',
        # 'male_male_reason_rejecting_count_interested_but_busy,_please_re-issue_in_3_weeks_from_matches',
        'male_male_reason_rejecting_count_male_timed_out',
        'male_male_reason_rejecting_count_cultural_or_ethnic_background',
        # 'male_male_reason_rejecting_count_child_status_from_matches',
        # 'male_male_reason_rejecting_count_marital_status_from_matches',
        'male_male_reason_rejecting_count_speaking_virtually',
        'male_male_reason_rejecting_count_ai_declined',
        'male_male_reason_rejecting_count_ai_no_response',
        'male_male_reason_rejecting_count_ai_suggestion',
        'male_male_reason_rejecting_count_ai_accepted',
        'male_male_reason_rejecting_count_ai_unsure',
        'male_male_reason_rejecting_count_family_background',
        'male_male_reason_rejecting_count_religious_level',
        'male_male_reason_rejecting_count_dated',
        # 'male_male_reason_rejecting_count_went_on_date(s)_&_not_going_out_again_from_matches',
        'male_male_reason_rejecting_count_busy_with_other_matches',
        'male_male_reason_rejecting_count__went_on_date(s)_&_not_going_out_again',
        'male_rejects_female_product_physical_look',
        'female_rejects_male_product_physical_look',
        'female_rejects_male_product_null',
        'female_rejects_male_product_other',
        'male_rejects_female_product_other',
        'male_rejects_female_product_null',
        'male_rejects_female_product_personality',
        'male_rejects_female_product_know_already',
        'male_rejects_female_product_too_religious',
        'male_rejects_female_product_age'
    ]
def get_gbr_cat_names():
    return [
        'female_body_type',
        'male_body_type',
        'female_female_hc',
        'male_male_hc',
        'female_religious_orientation',
        'male_religious_orientation',
        'female_torah_study',
        'female_watching_tv',
        'male_torah_study',
        'male_watching_tv',
        'female_eye_color',
        'female_hair_color',
        'male_eye_color',
        'male_hair_color',
        'female_body_type_preference_A Few Extra Pounds',
        'female_body_type_preference_Any',
        'female_body_type_preference_Athletic/Fit',
        'female_body_type_preference_Average/Medium Build',
        'female_body_type_preference_Large/Broad Build',
        'female_body_type_preference_Lean/Slender',
        'female_body_type_preference_Muscular',
        'female_body_type_preference_Proportional',
        'male_body_type_preference_Athletic/Fit',
        'male_body_type_preference_Average/Medium Build',
        'male_body_type_preference_Firm & Toned',
        'male_body_type_preference_Lean/Slender',
        'male_body_type_preference_Muscular',
        'male_body_type_preference_Petite',
        'male_body_type_preference_Proportional',
        'female_acceptable_religious_orientation_Conservadox',
        'female_acceptable_religious_orientation_Heimish',
        'female_acceptable_religious_orientation_Lubavitch',
        'female_acceptable_religious_orientation_Modern Orthodox (Machmir)',
        'female_acceptable_religious_orientation_Modern Orthodox (Middle of the road)',
        'female_acceptable_religious_orientation_Modern Orthodox (liberal)',
        'female_acceptable_religious_orientation_Modern Yeshivish',
        'female_acceptable_religious_orientation_Strictly Frum/Not Yeshivish',
        'female_acceptable_religious_orientation_Yeshivish',
        'male_acceptable_religious_orientation_Heimish',
        'male_acceptable_religious_orientation_Lubavitch',
        'male_acceptable_religious_orientation_Modern Orthodox (Machmir)',
        'male_acceptable_religious_orientation_Modern Orthodox (Middle of the road)',
        'male_acceptable_religious_orientation_Modern Orthodox (liberal)',
        'male_acceptable_religious_orientation_Modern Yeshivish',
        'male_acceptable_religious_orientation_Strictly Frum/Not Yeshivish',
        'male_acceptable_religious_orientation_Yeshivish',
        'female_acceptable_aliyah_responses_Already Live in Israel',
        'female_acceptable_aliyah_responses_Maybe',
        'female_acceptable_aliyah_responses_No',
        'female_acceptable_aliyah_responses_Yes',
        'male_acceptable_aliyah_responses_Already Live in Israel',
        'male_acceptable_aliyah_responses_Maybe',
        'male_acceptable_aliyah_responses_No',
        'male_acceptable_aliyah_responses_Yes',
        'male_desired_female_hc_Any',
        'male_desired_female_hc_Fully',
        'male_desired_female_hc_Partially',
        'male_desired_female_hc_Up to her',
        'female_acceptable_kosher_observance_At home',
        'female_acceptable_kosher_observance_At home & I eat dairy at non-kosher restaurants',
        'male_acceptable_kosher_observance_At home',
        'male_acceptable_kosher_observance_At home & I eat dairy at non-kosher restaurants'
    ]

def get_gbr_cont_names():
    return [
         'female_age',
         'female_number_of_siblings',
         'female_age_min',
         'female_age_max',
         'female_height_inches',
         'female_max_height_inches',
         'female_min_height_inches',
         'female_num_matches',
         'female_acceptance_rate',
         'male_age',
         'male_number_of_siblings',
         'male_age_min',
         'male_age_max',
         'male_height_inches',
         'male_min_height_inches',
         'male_max_height_inches',
         'male_num_matches',
         'male_acceptance_rate',
         'female_female_rejection_count_null',
         'female_female_rejection_count_spoke_on_phone_&_not_going_out',
         'female_female_rejection_count_spoke_on_phone',
         'female_female_rejection_count_went_on_date(s)_&_not_going_out_again',
         'female_female_rejection_count_never_got_in_touch',
         'female_female_rejection_count_other',
         'female_female_rejection_count_we_already_dated',
         'female_female_rejection_count_too_far/_distance',
         'female_female_rejection_count_not_my_personality_type',
         'female_female_rejection_count_age',
         'female_female_rejection_count_went_on_first_date',
         'female_female_rejection_count_went_on_multiple_dates',
         'female_female_rejection_count_too_religious',
         'female_female_rejection_count_none',
         'female_female_rejection_count_not_religious_enough',
         'female_female_rejection_count_already_know_this_person',
         'female_female_rejection_count_know_already',
         'female_female_rejection_count_distance',
         'female_female_rejection_count_physical_look',
         'female_female_rejection_count_education',
         'female_female_rejection_count_personality',
         'female_female_rejection_count_already_dated',
         'female_female_rejection_count_interested_but_busy,_please_re-issue_in_3_weeks',
         'female_female_rejection_count_cultural_or_ethnic_background',
         'female_female_rejection_count_ai_declined',
         'female_female_rejection_count_ai_no_response',
         'female_female_rejection_count_ai_accepted',
         'female_female_rejection_count_ai_unsure',
         'male_male_rejection_count_null',
         'male_male_rejection_count_spoke_on_phone',
         'male_male_rejection_count_went_on_first_date',
         'male_male_rejection_count_spoke_on_phone_&_not_going_out',
         'male_male_rejection_count_never_got_in_touch',
         'male_male_rejection_count_went_on_date(s)_&_not_going_out_again',
         'male_male_rejection_count_other',
         'male_male_rejection_count_not_my_personality_type',
         'male_male_rejection_count_age',
         'male_male_rejection_count_too_religious',
         'male_male_rejection_count_not_religious_enough',
         'male_male_rejection_count_none',
         'male_male_rejection_count_went_on_multiple_dates',
         'male_male_rejection_count_know_already',
         'male_male_rejection_count_distance',
         'male_male_rejection_count_physical_look',
         'male_male_rejection_count_personality',
         'male_male_rejection_count_education',
         'male_male_rejection_count_already_dated',
         'male_male_rejection_count_cultural_or_ethnic_background',
         'male_male_rejection_count_ai_declined',
         'male_male_rejection_count_ai_accepted',
         'male_male_rejection_count_ai_no_response',
         'male_male_rejection_count_ai_unsure',
         'female_female_reason_rejecting_count_null',
         'female_female_reason_rejecting_count_too_religious',
         'female_female_reason_rejecting_count_spoke_on_phone',
         'female_female_reason_rejecting_count_not_my_personality_type',
         'female_female_reason_rejecting_count_other',
         'female_female_reason_rejecting_count_not_religious_enough',
         'female_female_reason_rejecting_count_age',
         'female_female_reason_rejecting_count_physical_look',
         'female_female_reason_rejecting_count_never_got_in_touch',
         'female_female_reason_rejecting_count_went_on_date(s)_&_not_going_out_again',
         'female_female_reason_rejecting_count_spoke_on_phone_&_not_going_out',
         'female_female_reason_rejecting_count_too_far/_distance',
         'female_female_reason_rejecting_count_went_on_first_date',
         'female_female_reason_rejecting_count_education_level',
         'female_female_reason_rejecting_count_none',
         'female_female_reason_rejecting_count_went_on_multiple_dates',
         'female_female_reason_rejecting_count_already_know_this_person',
         'female_female_reason_rejecting_count_child_status',
         'female_female_reason_rejecting_count_marital_status',
         'female_female_reason_rejecting_count_know_already',
         'female_female_reason_rejecting_count_distance',
         'female_female_reason_rejecting_count_personality',
         'female_female_reason_rejecting_count_education',
         'female_female_reason_rejecting_count_already_dated',
         'female_female_reason_rejecting_count_interested_but_busy,_please_re-issue_in_3_weeks',
         'female_female_reason_rejecting_count_cultural_or_ethnic_background',
         'female_female_reason_rejecting_count_ai_declined',
         'female_female_reason_rejecting_count_ai_accepted',
         'female_female_reason_rejecting_count_ai_no_response',
         'female_female_reason_rejecting_count_ai_unsure',
         'male_male_reason_rejecting_count_null',
         'male_male_reason_rejecting_count_spoke_on_phone',
         'male_male_reason_rejecting_count_other',
         'male_male_reason_rejecting_count_physical_look',
         'male_male_reason_rejecting_count_too_far/_distance',
         'male_male_reason_rejecting_count_not_my_personality_type',
         'male_male_reason_rejecting_count_too_religious',
         'male_male_reason_rejecting_count_age',
         'male_male_reason_rejecting_count_went_on_date(s)_&_not_going_out_again',
         'male_male_reason_rejecting_count_not_religious_enough',
         'male_male_reason_rejecting_count_none',
         'male_male_reason_rejecting_count_never_got_in_touch',
         'male_male_reason_rejecting_count_spoke_on_phone_&_not_going_out',
         'male_male_reason_rejecting_count_went_on_first_date',
         'male_male_reason_rejecting_count_went_on_multiple_dates',
         'male_male_reason_rejecting_count_already_know_this_person',
         'male_male_reason_rejecting_count_marital_status',
         'male_male_reason_rejecting_count_know_already',
         'male_male_reason_rejecting_count_distance',
         'male_male_reason_rejecting_count_education',
         'male_male_reason_rejecting_count_personality',
         'male_male_reason_rejecting_count_already_dated',
         'male_male_reason_rejecting_count_interested_but_busy,_please_re-issue_in_3_weeks',
         'male_male_reason_rejecting_count_cultural_or_ethnic_background',
         'male_male_reason_rejecting_count_ai_declined',
         'male_male_reason_rejecting_count_ai_no_response',
         'male_male_reason_rejecting_count_ai_accepted',
         'male_male_reason_rejecting_count_ai_unsure',
         'male_rejects_female_product_physical_look',
         'female_rejects_male_product_physical_look',
         'female_rejects_male_product_null',
         'female_rejects_male_product_other',
         'male_rejects_female_product_other',
         'male_rejects_female_product_null',
         'male_rejects_female_product_personality',
         'male_rejects_female_product_know_already',
         'male_rejects_female_product_too_religious',
         'male_rejects_female_product_age'
    ]