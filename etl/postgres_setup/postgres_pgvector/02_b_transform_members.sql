

ALTER TABLE members
DROP COLUMN Cultural_Background,
DROP COLUMN how_long_married,
DROP COLUMN have_jewish_divorce,
DROP COLUMN have_civil_divorce,
DROP COLUMN have_children,
DROP COLUMN looking_for_in_spouse,
DROP COLUMN community_work_2,
DROP COLUMN name_seminaries,
DROP COLUMN parents_marital_status,
DROP COLUMN parent_shul,
DROP COLUMN want_to_meet_someone_who_cover_hair,
DROP COLUMN want_to_meet_someone_who_wears_only_skirts;

DELETE FROM members
WHERE short_description_of_yourself ~* '\mtest\M'
AND looking_for_in_a_person~* '\mtest\M'
AND looking_for_in_a_person NOT LIKE '%litmus test%'
AND looking_for_in_a_person NOT LIKE '%biggest test%'
OR short_description_of_yourself ILIKE '%testing%'
AND looking_for_in_a_person ILIKE '%testing%'
OR City ~* '\mtest\M'
OR Name_Secondary_School  ILIKE '%test%';

UPDATE members
SET times_divorced =
    CASE
        WHEN  My_marriage_status = 'Single (Never Married)' THEN '0'
        ELSE '>=1'
    END
WHERE times_divorced IS NULL OR TRIM(times_divorced) = '';

UPDATE members
SET female_convert = 'NA'
WHERE gender IN ('Male');

UPDATE members
SET desired_female_hc =
    CASE
        WHEN (desired_female_hc IS NULL OR TRIM(desired_female_hc) = '') THEN female_hc
        ELSE desired_female_hc
    END
WHERE gender in ('Male');

UPDATE members
SET female_hc = 'NA'
WHERE gender in ('Male');

UPDATE members
SET female_hc =
    CASE
        WHEN (female_hc IS NULL OR TRIM(female_hc) = '') THEN desired_female_hc
        ELSE female_hc
    END
WHERE gender in ('Female');

UPDATE members
SET desired_female_hc = 'NA'
WHERE gender in ('Female');

UPDATE members
SET female_dress = 'NA'
WHERE gender IN ('Male');

UPDATE members
SET male_hc = 'NA'
WHERE gender IN ('Female');

UPDATE members
SET male_shul_attendance = 'NA'
WHERE gender IN ('Female');

UPDATE members
SET female_dress =
    CASE
        WHEN (female_dress IS NULL OR TRIM(female_dress) = '') THEN desired_female_dress
        ELSE female_dress
    END
WHERE gender in ('Female');

UPDATE members
SET desired_female_dress = 'NA'
WHERE gender in ('Female');

UPDATE members
SET can_marry_cohen =
    CASE
        WHEN gender IN ('Male') THEN 'NA'
        WHEN can_marry_cohen = 'No' THEN 'No'
        WHEN female_convert IN ('Yes') THEN 'No'
        WHEN times_divorced IN ('1', '>=1', '2','3','4','5') THEN 'No' --note: the gender when already filters out men
        ELSE 'Yes'
    END;

UPDATE members
SET desired_torah_study = 'NA'
WHERE gender IN ('Male') AND (desired_torah_study IS NULL or desired_torah_study = '');

UPDATE members
SET preference_cultural_background = 'Any'
WHERE preference_cultural_background IS NULL OR TRIM(preference_cultural_background) = '';

UPDATE members
SET looking_for_in_a_person = 'open to anything/not picky'
WHERE looking_for_in_a_person IS NULL OR TRIM(looking_for_in_a_person) = '';

UPDATE members
SET Introvert_Extravert = ''
WHERE Introvert_Extravert IS NULL;

UPDATE members
SET Sensor_Intuitive = ''
WHERE Sensor_Intuitive IS NULL;

UPDATE members
SET Thinker_Feeler = ''
WHERE Thinker_Feeler IS NULL;

UPDATE members
SET Judger_Perceiver = ''
WHERE Judger_Perceiver IS NULL;

UPDATE members
SET parents_convert_before_birth = 'No'
WHERE parents_convert_before_birth IS NULL OR TRIM(parents_convert_before_birth) = '';
ALTER TABLE members ADD COLUMN acceptable_places_to_live VARCHAR;

UPDATE members
SET  acceptable_places_to_live = acceptable_places_to_live_countries || ' ' || acceptable_places_states;

ALTER TABLE members
DROP COLUMN acceptable_places_to_live_Countries,
DROP COLUMN acceptable_places_states;

ALTER TABLE members ADD COLUMN description_embedding vector(1024);

UPDATE members
SET description_embedding = temp.description_embedding::vector
FROM temp_member_embeddings temp
WHERE members.id = temp.id;