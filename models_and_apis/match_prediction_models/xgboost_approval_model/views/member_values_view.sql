DROP VIEW IF EXISTS matches_values;
DROP VIEW IF EXISTS member_values;

CREATE VIEW member_values AS
SELECT
    CAST(SUBSTRING(height FROM '\((\d+)\s*cm\)') AS INTEGER) AS height_cm,
    CAST(SUBSTRING(height_min FROM '\((\d+)\s*cm\)') AS INTEGER) AS height_min_cm,
    CAST(SUBSTRING(height_max FROM '\((\d+)\s*cm\)') AS INTEGER) AS height_max_cm,
    CAST(age AS INTEGER) AS age_int,
    body_type,
    description_embedding,
religious_orientation,
introvert_extravert,
sensor_intuitive,
thinker_feeler,
judger_perceiver,
ethnicity,
baal_teshuva,
kosher,
male_hc,
frequency_of_tefilah,
male_shul_attendance,
torah_study,
secular_education,
jewish_education,
study_in_israel,
eye_color,
hair_color,
CASE
  WHEN how_many_children IS NULL OR how_many_children = '' THEN 0
  ELSE CAST(how_many_children AS INTEGER)
END AS how_many_children,
CASE
  WHEN number_live_with_you IS NULL OR number_live_with_you = '' 
  OR number_live_with_you = 'N/A' THEN 0
  ELSE CAST(number_live_with_you AS INTEGER)
END AS number_live_with_you,
want_additional_children,
CASE
  WHEN number_of_siblings IS NULL OR number_of_siblings = '' THEN 0
  ELSE CAST(number_of_siblings AS INTEGER)
END AS number_of_siblings,
political_orientation,
smoking_habits,
how_active_are_you,
plan_to_aliya,
willing_to_relocate,
pet_person,
pet_i_own,
CAST(age_min AS INTEGER) AS age_min,
CAST(age_max AS INTEGER) AS age_max,
acceptable_for_match_to_have_children,
acceptable_smoking_habits,
minimum_education_level,
CASE
  WHEN age_of_youngest = '' OR age_of_youngest IS NULL THEN NULL
  ELSE CAST(age_of_youngest AS INTEGER)
END AS age_of_youngest,
CASE
  WHEN times_divorced IS NULL OR times_divorced = '' THEN 0
  WHEN times_divorced = '>=1' THEN 1
  ELSE CAST(times_divorced AS INTEGER)
END AS times_divorced,
profession,
female_hc,
female_dress,
how_long_single,  
desired_marital_status, 
my_marriage_status, 
acceptable_religious_orientation, 
acceptable_aliyah_responses, 
acceptable_kosher_observance, 
ok_dating_baal_teshuva, 
desired_torah_study, 
desired_female_hc, 
desired_female_dress, 
jewish_education_preference, 
body_type_preference, 
preference_regarding_ethnicity, 
my_personality_traits, 
my_personality_go_out_to, 
favorite_music, 
physical_activities_interests, 
my_favorite_pastimes,
id
FROM members;
