CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE temp_member_embeddings (
    id INT PRIMARY KEY,
    family_religious_background_embedding TEXT
);

CREATE TABLE matches
(
    id INT PRIMARY KEY,
    male_id INT,
    female_id INT,
    ms TEXT,
    male_s TEXT,
    female_s TEXT,
    male_pr TEXT,
    female_pr TEXT,
    matchmaker_pr TEXT,
    match_quality TEXT,
    decline_reason TEXT
);

CREATE TABLE members (
    id INT PRIMARY KEY,
    country VARCHAR,
    city VARCHAR,
    state VARCHAR,
    gender VARCHAR,
    age VARCHAR,
    religious_orientation VARCHAR,
    ethnicity VARCHAR,
    cultural_background VARCHAR,
    baal_teshuva VARCHAR,
    years_orthodox_baal_teshuva VARCHAR,
    cohen VARCHAR,
    female_convert VARCHAR,
    parents_convert VARCHAR,
    mother_maternal_grandmother_jewish VARCHAR,
    family_religious_background VARCHAR,
    describe_family_religious_background VARCHAR,
    female_hc VARCHAR,
    kosher VARCHAR,
    female_dress VARCHAR,
    male_hc VARCHAR,
    frequency_of_tefilah VARCHAR,
    male_shul_attendance VARCHAR,
    torah_study VARCHAR,
    watching_tv VARCHAR,
    going_out_to_movies VARCHAR,
    watching_movies_at_home VARCHAR,
    want_to_meet_someone_who_cover_hair VARCHAR,
    want_to_meet_someone_who_wears_only_skirts VARCHAR,
    secular_education VARCHAR,
    emphasis_of_studies VARCHAR,
    jewish_education VARCHAR,
    study_in_israel VARCHAR,
    profession VARCHAR,
    job_description VARCHAR,
    eye_color VARCHAR,
    hair_color VARCHAR,
    height VARCHAR,
    body_type VARCHAR,
    mental_physical_disability VARCHAR,
    my_marriage_status VARCHAR,
    how_long_married VARCHAR,
    how_long_single VARCHAR,
    times_divorced VARCHAR,
    have_jewish_divorce VARCHAR,
    have_civil_divorce VARCHAR,
    have_children VARCHAR,
    how_many_children VARCHAR,
    number_live_with_you VARCHAR,
    age_of_youngest VARCHAR,
    want_additional_children VARCHAR,
    can_marry_cohen VARCHAR,
    number_of_siblings VARCHAR,
    political_orientation VARCHAR,
    smoking_habits VARCHAR,
    how_active_are_you VARCHAR,
    plan_to_aliya VARCHAR,
    willing_to_relocate VARCHAR,
    pet_person VARCHAR,
    pet_i_own VARCHAR,
    additional_pet_i_own VARCHAR,
    native_language VARCHAR,
    languages_spoken VARCHAR,
    age_min VARCHAR,
    age_max VARCHAR,
    height_min VARCHAR,
    height_max VARCHAR,
    desired_marital_status VARCHAR,
    minimum_education_level VARCHAR,
    acceptable_for_match_to_have_children VARCHAR,
    acceptable_religious_orientation VARCHAR,
    acceptable_smoking_habits VARCHAR,
    ok_dating_someone_with_disability VARCHAR,
    acceptable_aliyah_responses VARCHAR,
    acceptable_kosher_observance VARCHAR,
    ok_dating_baal_teshuva VARCHAR,
    acceptable_places_to_live_countries VARCHAR,
    acceptable_places_states VARCHAR,
    family_relgious_background VARCHAR,
    desired_torah_study VARCHAR,
    desired_female_hc VARCHAR,
    desired_female_dress VARCHAR,
    jewish_education_preference VARCHAR,
    body_type_preference VARCHAR,
    preference_regarding_ethnicity VARCHAR,
    preference_cultural_background VARCHAR,
    my_personality_traits VARCHAR,
    my_personality_go_out_to VARCHAR,
    favorite_music VARCHAR,
    physical_activities_interests VARCHAR,
    my_favorite_pastimes VARCHAR,
    looking_for_in_a_person VARCHAR,
    short_description_of_yourself VARCHAR,
    looking_for_in_spouse VARCHAR,
    community_work VARCHAR,
    introvert_extravert VARCHAR,
    sensor_intuitive VARCHAR,
    thinker_feeler VARCHAR,
    judger_perceiver VARCHAR,
    approved VARCHAR,
    dating_status VARCHAR,
    colleges_universities VARCHAR,
    community_work_2 VARCHAR,
    parents_convert_before_birth VARCHAR,
    elementary_school VARCHAR,
    location_i_grew_up VARCHAR,
    name_secondary_school VARCHAR,
    name_seminaries VARCHAR,
    name_study_one_year VARCHAR,
    parent_shul VARCHAR,
    parent_location VARCHAR,
    parents_marital_status VARCHAR,
    complete_incomplete VARCHAR,
    photo VARCHAR,
    site VARCHAR,
    profile_last_modified_date TIMESTAMP WITHOUT TIME ZONE,
    updated VARCHAR
);

COPY matches
    (
    id,
    male_id,
    female_id,
    ms,
    male_s,
    female_s,
    male_pr,
    female_pr,
    matchmaker_pr,
    match_quality,
    decline_reason
    )
FROM '/docker-entrypoint-initdb.d/raw_data/MatchesData_YU_CS_Deptv3.csv'
DELIMITER ','
CSV HEADER;

COPY members
    (
    id,
    country,
    city,
    state,
    gender,
    age,
    religious_orientation,
    ethnicity,
    cultural_background,
    baal_teshuva,
    years_orthodox_baal_teshuva,
    cohen,
    female_convert,
    parents_convert,
    mother_maternal_grandmother_jewish,
    family_religious_background,
    describe_family_religious_background,
    female_hc,
    kosher,
    female_dress,
    male_hc,
    frequency_of_tefilah,
    male_shul_attendance,
    torah_study,
    watching_tv,
    going_out_to_movies,
    watching_movies_at_home,
    want_to_meet_someone_who_cover_hair,
    want_to_meet_someone_who_wears_only_skirts,
    secular_education,
    emphasis_of_studies,
    jewish_education,
    study_in_israel,
    profession,
    job_description,
    eye_color,
    hair_color,
    height,
    body_type,
    mental_physical_disability,
    my_marriage_status,
    how_long_married,
    how_long_single,
    times_divorced,
    have_jewish_divorce,
    have_civil_divorce,
    have_children,
    how_many_children,
    number_live_with_you,
    age_of_youngest,
    want_additional_children,
    can_marry_cohen,
    number_of_siblings,
    political_orientation,
    smoking_habits,
    how_active_are_you,
    plan_to_aliya,
    willing_to_relocate,
    pet_person,
    pet_i_own,
    additional_pet_i_own,
    native_language,
    languages_spoken,
    age_min,
    age_max,
    height_min,
    height_max,
    desired_marital_status,
    minimum_education_level,
    acceptable_for_match_to_have_children,
    acceptable_religious_orientation,
    acceptable_smoking_habits,
    ok_dating_someone_with_disability,
    acceptable_aliyah_responses,
    acceptable_kosher_observance,
    ok_dating_baal_teshuva,
    acceptable_places_to_live_countries,
    acceptable_places_states,
    family_relgious_background,
    desired_torah_study,
    desired_female_hc,
    desired_female_dress,
    jewish_education_preference,
    body_type_preference,
    preference_regarding_ethnicity,
    preference_cultural_background,
    my_personality_traits,
    my_personality_go_out_to,
    favorite_music,
    physical_activities_interests,
    my_favorite_pastimes,
    looking_for_in_a_person,
    short_description_of_yourself,
    looking_for_in_spouse,
    community_work,
    introvert_extravert,
    sensor_intuitive,
    thinker_feeler,
    judger_perceiver,
    approved,
    dating_status,
    colleges_universities,
    community_work_2,
    parents_convert_before_birth,
    elementary_school,
    location_i_grew_up,
    name_secondary_school,
    name_seminaries,
    name_study_one_year,
    parent_shul,
    parent_location,
    parents_marital_status,
    complete_incomplete,
    photo,
    site,
    profile_last_modified_date,
    updated
)
FROM '/docker-entrypoint-initdb.d/raw_data/YUAIMemberData17June2025.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ',',
    NULL 'NULL'
);

-- the following gets rid of duplicate matches (match of man and woman that appears twice)
DELETE FROM matches
WHERE id NOT IN (
    SELECT MIN(id)
    FROM matches
    GROUP BY male_id, female_id
);

ALTER TABLE matches
ADD CONSTRAINT no_duplicate_matches UNIQUE (male_id, female_id);

-- nulls out any male or female id in matches that doesn't correspond to an id in members (about 2 unique ids)
UPDATE matches
SET male_id = NULL
WHERE male_id NOT IN (SELECT id FROM members);

UPDATE matches
SET female_id = NULL
WHERE female_id NOT IN (SELECT id FROM members);

ALTER TABLE matches
ADD CONSTRAINT male_member
FOREIGN KEY (male_id)
REFERENCES members (id);

ALTER TABLE matches
ADD CONSTRAINT female_member
FOREIGN KEY (female_id)
REFERENCES members(id);

COPY temp_member_embeddings
    (
    id,
    family_religious_background_embedding
    )
FROM '/docker-entrypoint-initdb.d/raw_data/embeddings.csv'
DELIMITER ','
CSV HEADER;