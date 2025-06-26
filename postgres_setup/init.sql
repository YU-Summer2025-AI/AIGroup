CREATE TABLE Matches
(
    Match_ID INT PRIMARY KEY,
    Male_ID INT,
    Female_ID INT,
    Match_status_for_match TEXT,
    Match_status_male TEXT,
    Match_status_female TEXT,
    Progress_report_male TEXT,
    Progress_report_female TEXT,
    Progress_report_Matchmaker TEXT,
    How_far_off_was_the_match TEXT,
    Decline_reason TEXT
);

CREATE TABLE MemberData (
        "Member_ID" INT PRIMARY KEY ,
        "Country" VARCHAR, 
        "City" VARCHAR, 
        "State" VARCHAR, 
        "Gender" VARCHAR, 
        "Age" VARCHAR,
        "Religious_orientation" VARCHAR, 
        "Ethnicity" VARCHAR, 
        "Cultural_Background" VARCHAR, 
        baal_teshuva VARCHAR, 
        "years_Orthodox_baal_teshuva" VARCHAR, 
        "Cohen" VARCHAR, 
        convert_female VARCHAR, 
        parents_convert VARCHAR, 
        "mother_maternal_grandmother_Jewish" VARCHAR, 
        "Family_religious_background" VARCHAR, 
        "Describe_family_religious_background" VARCHAR, 
        "Head_covering_female" VARCHAR, 
        "Kosher" VARCHAR, 
        "Dress_female" VARCHAR, 
        "Head_covering_male" VARCHAR, 
        "Frequency_of_Tefilah" VARCHAR, 
        "Frequency_of_shul_attendance_male" VARCHAR, 
        "Frequency_of_Torah_study_male" VARCHAR, 
        "Watching_TV" VARCHAR, 
        "Going_out_to_Movies" VARCHAR, 
        "Watching_Movies_at_home" VARCHAR, 
        want_to_meet_someone_who_cover_hair VARCHAR, 
        want_to_meet_someone_who_wears_only_skirts VARCHAR, 
        "Secular_education" VARCHAR, 
        "Emphasis_of_studies" VARCHAR, 
        "Jewish_education" VARCHAR, 
        "study_in_Israel" VARCHAR, 
        "Profession" VARCHAR, 
        "Job_description" VARCHAR, 
        "Eye_color" VARCHAR, 
        "Hair_color" VARCHAR, 
        "Height" VARCHAR, 
        "Body_type" VARCHAR, 
        mental_physical_disability VARCHAR, 
        "My_marriage_status" VARCHAR, 
        how_long_married VARCHAR, 
        "How_long_single" VARCHAR, 
        times_divorced VARCHAR, 
        "have_Jewish_Divorce" VARCHAR, 
        have_civil_divorce VARCHAR, 
        have_children VARCHAR, 
        how_many_children VARCHAR, 
        number_live_with_you VARCHAR, 
        age_of_youngest VARCHAR, 
        want_additional_children VARCHAR, 
        "Can_marry_Cohen" VARCHAR, 
        "Number_of_siblings" VARCHAR, 
        "Political_orientation" VARCHAR, 
        "Smoking_habits" VARCHAR, 
        "How_active_are_you" VARCHAR, 
        "Plan_to_aliya" VARCHAR, 
        willing_to_relocate VARCHAR, 
        pet_person VARCHAR, 
        "Pet_i_own" VARCHAR, 
        "Additional_pet_i_own" VARCHAR, 
        native_language VARCHAR, 
        "Languages_spoken" VARCHAR, 
        "Age_range_From" VARCHAR, 
        "Age_range_To" VARCHAR, 
        "Height_range_From" VARCHAR, 
        "Height_range_To" VARCHAR, 
        "Desired_marital_status" VARCHAR, 
        "Minimum_Education_level" VARCHAR, 
        acceptable_for_match_to_have_children VARCHAR, 
        "Acceptable_religious_orientation" VARCHAR, 
        "Acceptable_smoking_habits" VARCHAR, 
        ok_dating_someone_with_disability VARCHAR, 
        "Acceptable_aliyah_responses" VARCHAR, 
        "Acceptable_kosher_observance" VARCHAR, 
        ok_dating_baal_teshuva VARCHAR, 
        "Acceptable_places_to_live_Countries" VARCHAR, 
        "Acceptable_places_States" VARCHAR, 
        family_relgious_background VARCHAR, 
        male_torah_study_female_sign_up VARCHAR, 
        want_covered_hair_male_sign_up VARCHAR, 
        want_only_wears_skirts VARCHAR, 
        "Jewish_education_preference" VARCHAR, 
        "Body_Type_preference" VARCHAR, 
        "Preference_regarding_Ethnicity" VARCHAR, 
        "Preference_cultural_background" VARCHAR, 
        "My_Personality_Traits" VARCHAR, 
        "My_Personality_go_out_to" VARCHAR, 
        "Favorite_Music" VARCHAR, 
        "Physical_Activities_interests" VARCHAR, 
        "My_Favorite_Pastimes" VARCHAR, 
        looking_for_in_a_person VARCHAR, 
        short_description_of_yourself VARCHAR, 
        looking_for_in_spouse VARCHAR, 
        community_work VARCHAR, 
        "Introvert_Extravert" VARCHAR, 
        "Sensor_Intuitive" VARCHAR, 
        "Thinker_Feeler" VARCHAR, 
        "Judger_Perceiver" VARCHAR, 
        "Approved" VARCHAR, 
        "Dating_Status" VARCHAR, 
        "Colleges_universities" VARCHAR, 
        community_work_2 VARCHAR, 
        parents_convert_before_birth VARCHAR, 
        "Elementary_school" VARCHAR, 
        "Location_I_grew_up" VARCHAR, 
        "Name_Secondary_School" VARCHAR, 
        "Name_seminaries" VARCHAR, 
        "Name_study_one_year" VARCHAR, 
        "Parent_shul" VARCHAR, 
        "Parent_location" VARCHAR, 
        "Parents_marital_status" VARCHAR, 
        "Complete_Incomplete" VARCHAR, 
        "Photo" VARCHAR, 
        "Site" VARCHAR, 
        "Profile_Last_modified_date" TIMESTAMP WITHOUT TIME ZONE, 
        "Updated" VARCHAR
);

COPY Matches
(Match_ID, Male_ID, Female_ID, Match_status_for_match, Match_status_male, Match_status_female, Progress_report_male, Progress_report_female, Progress_report_Matchmaker, How_far_off_was_the_match, Decline_reason)
FROM '/docker-entrypoint-initdb.d/raw_data/MatchesData_YU_CS_Deptv3.csv'
DELIMITER ','
CSV HEADER;

COPY MemberData
("Member_ID","Country","City","State","Gender","Age","Religious_orientation","Ethnicity","Cultural_Background",baal_teshuva,"years_Orthodox_baal_teshuva","Cohen",convert_female,parents_convert,"mother_maternal_grandmother_Jewish","Family_religious_background","Describe_family_religious_background","Head_covering_female","Kosher","Dress_female","Head_covering_male","Frequency_of_Tefilah","Frequency_of_shul_attendance_male","Frequency_of_Torah_study_male","Watching_TV","Going_out_to_Movies","Watching_Movies_at_home",want_to_meet_someone_who_cover_hair,want_to_meet_someone_who_wears_only_skirts,"Secular_education","Emphasis_of_studies","Jewish_education","study_in_Israel","Profession","Job_description","Eye_color","Hair_color","Height","Body_type",mental_physical_disability,"My_marriage_status",how_long_married,"How_long_single",times_divorced,"have_Jewish_Divorce",have_civil_divorce,have_children,how_many_children,number_live_with_you,age_of_youngest,want_additional_children,"Can_marry_Cohen","Number_of_siblings","Political_orientation","Smoking_habits","How_active_are_you","Plan_to_aliya",willing_to_relocate,pet_person,"Pet_i_own","Additional_pet_i_own",native_language,"Languages_spoken","Age_range_From","Age_range_To","Height_range_From","Height_range_To","Desired_marital_status","Minimum_Education_level",acceptable_for_match_to_have_children,"Acceptable_religious_orientation","Acceptable_smoking_habits",ok_dating_someone_with_disability,"Acceptable_aliyah_responses","Acceptable_kosher_observance",ok_dating_baal_teshuva,"Acceptable_places_to_live_Countries","Acceptable_places_States",family_relgious_background,male_torah_study_female_sign_up,want_covered_hair_male_sign_up,want_only_wears_skirts,"Jewish_education_preference","Body_Type_preference","Preference_regarding_Ethnicity","Preference_cultural_background","My_Personality_Traits","My_Personality_go_out_to","Favorite_Music","Physical_Activities_interests","My_Favorite_Pastimes",looking_for_in_a_person,short_description_of_yourself,looking_for_in_spouse,community_work,"Introvert_Extravert","Sensor_Intuitive","Thinker_Feeler","Judger_Perceiver","Approved","Dating_Status","Colleges_universities",community_work_2,parents_convert_before_birth,"Elementary_school","Location_I_grew_up","Name_Secondary_School","Name_seminaries","Name_study_one_year","Parent_shul","Parent_location","Parents_marital_status","Complete_Incomplete","Photo","Site","Profile_Last_modified_date","Updated")
FROM '/docker-entrypoint-initdb.d/raw_data/YUAIMemberData17June2025.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ',',
    NULL 'NULL'
);

ALTER TABLE matches
RENAME COLUMN Match_ID TO id;

ALTER TABLE matches
RENAME COLUMN Match_status_for_match TO ms;

ALTER TABLE matches
RENAME COLUMN Match_status_male TO male_s;

ALTER TABLE matches
RENAME COLUMN Match_status_female TO female_s;

ALTER TABLE matches
RENAME COLUMN Progress_report_male TO male_pr;

ALTER TABLE matches
RENAME COLUMN Progress_report_female TO female_pr;

ALTER TABLE matches
RENAME COLUMN Progress_report_Matchmaker TO matchmaker_pr;

ALTER TABLE matches
RENAME COLUMN How_far_off_was_the_match TO match_quality;


ALTER TABLE MemberData
RENAME TO members;

ALTER TABLE members
RENAME COLUMN "Member_ID" TO id;

ALTER TABLE members
RENAME COLUMN "Gender" TO gender;

ALTER TABLE members
RENAME COLUMN "Age" TO age;

ALTER TABLE members
RENAME COLUMN "Age_range_From" TO age_min;

ALTER TABLE members
RENAME COLUMN "Age_range_To" TO age_max;

ALTER TABLE members
RENAME COLUMN "Height" TO height;

ALTER TABLE members
RENAME COLUMN "Height_range_From" TO height_min;

ALTER TABLE members
RENAME COLUMN "Height_range_To" TO height_max;

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

ALTER TABLE matches
ADD COLUMN overall_pr VARCHAR(255);

UPDATE matches
SET overall_pr =
	CASE
		-- This is the GREATEST() function from your subquery.
		-- It finds the highest progress value among the four source columns.
		GREATEST(
			COALESCE( -- Use COALESCE to safely handle NULLs, defaulting them to 0
				CASE matchmaker_pr
					WHEN 'AI No Response' THEN 10
                    WHEN 'Never Got in Touch' THEN 40
                    WHEN 'AI Accepted' THEN 50
                    WHEN 'Spoke on phone' THEN 70
                    WHEN 'Speaking Virtually' THEN 80
                    WHEN 'Spoke on phone & not going out' THEN 90
                    WHEN 'Spoke on phone & Not going out' THEN 90
                    WHEN 'Spoke on phone & NOT going out' THEN 90
                    WHEN 'Went on First date' THEN 100
                    WHEN 'Went on multiple dates' THEN 110
                    WHEN 'Dating exclusively' THEN 120
                    WHEN 'Went on date(s) & not going out again' THEN 130
                    WHEN 'Engaged' THEN 140
                    ELSE 0
				END, 0),
			COALESCE(
				CASE male_pr
					WHEN 'AI No Response' THEN 10
                    WHEN 'Never Got in Touch' THEN 40
                    WHEN 'AI Accepted' THEN 50
                    WHEN 'Spoke on phone' THEN 70
                    WHEN 'Speaking Virtually' THEN 80
                    WHEN 'Spoke on phone & not going out' THEN 90
                    WHEN 'Spoke on phone & Not going out' THEN 90
                    WHEN 'Spoke on phone & NOT going out' THEN 90
                    WHEN 'Went on First date' THEN 100
                    WHEN 'Went on multiple dates' THEN 110
                    WHEN 'Dating exclusively' THEN 120
                    WHEN 'Went on date(s) & not going out again' THEN 130
                    WHEN 'Engaged' THEN 140
                    ELSE 0
				END, 0),
			COALESCE(
				CASE female_pr
					WHEN 'AI No Response' THEN 10
                    WHEN 'Never Got in Touch' THEN 40
                    WHEN 'AI Accepted' THEN 50
                    WHEN 'Spoke on phone' THEN 70
                    WHEN 'Speaking Virtually' THEN 80
                    WHEN 'Spoke on phone & not going out' THEN 90
                    WHEN 'Spoke on phone & Not going out' THEN 90
                    WHEN 'Spoke on phone & NOT going out' THEN 90
                    WHEN 'Went on First date' THEN 100
                    WHEN 'Went on multiple dates' THEN 110
                    WHEN 'Dating exclusively' THEN 120
                    WHEN 'Went on date(s) & not going out again' THEN 130
                    WHEN 'Engaged' THEN 140
                    ELSE 0
				END, 0),
			COALESCE(
				CASE ms
				    WHEN 'New match' THEN 20
				    WHEN 'Phone# sent' THEN 30
					WHEN 'Mutually approved' THEN 40
				    WHEN 'Male declined' THEN 150
				    WHEN 'Female declined' THEN 160
					ELSE 0
				END, 0),
		    COALESCE(
                CASE
                    WHEN male_s = 'Declined' AND female_s = 'Declined' THEN 170
                    WHEN male_s = 'Declined' THEN 150
                    WHEN female_s = 'Declined' THEN 160
                    WHEN male_s = 'Approved' AND female_s = 'Approved' THEN 40
                    WHEN male_s = 'New match' OR female_s = 'New match' THEN 20
                    ELSE 0
                END, 0)
		)
		-- This is the CASE statement from your outer query.
		-- It translates the max_progress number back into a human-readable string.
		WHEN 0 THEN NULL
        WHEN 10 THEN 'AI No Response'
        WHEN 20 THEN 'New match'
        WHEN 30 THEN 'Phone# sent'
        WHEN 40 THEN 'Never Got in Touch'
        WHEN 50 THEN 'AI Accepted'
        WHEN 60 THEN 'Mutually approved'
        WHEN 70 THEN 'Spoke on phone'
        WHEN 80 THEN 'Speaking Virtually'
        WHEN 90 THEN 'Spoke on phone & not going out'
        WHEN 100 THEN 'Went on First date'
        WHEN 110 THEN 'Went on multiple dates'
        WHEN 120 THEN 'Dating exclusively' 
        WHEN 130 THEN 'Went on date(s) & not going out again'
        WHEN 140 THEN 'Engaged'
        WHEN 150 THEN 'Male declined'
        WHEN 160 THEN 'Female declined'
	    WHEN 170 THEN 'Both declined'
        ELSE NULL
	END;

ALTER TABLE members
DROP COLUMN "Cultural_Background",
DROP COLUMN how_long_married,
DROP COLUMN "have_Jewish_Divorce",
DROP COLUMN have_civil_divorce,
DROP COLUMN have_children,
DROP COLUMN looking_for_in_spouse,
DROP COLUMN community_work_2,
DROP COLUMN "Name_seminaries",
DROP COLUMN "Parents_marital_status",
DROP COLUMN "Parent_shul";


UPDATE members
SET times_divorced = 
    CASE
        WHEN  "My_marriage_status" = 'Single (Never Married)' THEN '0'
        ELSE '>=1'
    END
WHERE times_divorced IS NULL OR TRIM(times_divorced) = '';


DELETE FROM matches
WHERE id IN    
    (SELECT matches.id FROM matches LEFT JOIN members AS m ON matches.male_id = m.id LEFT JOIN members AS f ON matches.female_id = f.id WHERE 
    (m."short_description_of_yourself" ~* '\mtest\M' AND 
    m."looking_for_in_a_person"~* '\mtest\M' AND 
    m."looking_for_in_a_person" NOT LIKE '%litmus test%' AND 
    m."looking_for_in_a_person" NOT LIKE '%biggest test%')
    OR
    (f."short_description_of_yourself" ~* '\mtest\M' AND 
    f."looking_for_in_a_person"~* '\mtest\M' AND 
    f."looking_for_in_a_person" NOT LIKE '%litmus test%' AND 
    f."looking_for_in_a_person" NOT LIKE '%biggest test%')
    OR
    (m."short_description_of_yourself"ILIKE '%testing%' AND m."looking_for_in_a_person" ILIKE '%testing%')
    OR
    (f."short_description_of_yourself"ILIKE '%testing%' AND f."looking_for_in_a_person" ILIKE '%testing%')
    OR m."City" ~* '\mtest\M' 
    OR m."Name_Secondary_School"  ILIKE '%test%'
    OR f."City" ~* '\mtest\M' 
    OR f."Name_Secondary_School"  ILIKE '%test%'
);
DELETE FROM members WHERE "short_description_of_yourself" ~* '\mtest\M' AND 
"looking_for_in_a_person"~* '\mtest\M' AND 
"looking_for_in_a_person" NOT LIKE '%litmus test%' AND 
"looking_for_in_a_person" NOT LIKE '%biggest test%' OR
"short_description_of_yourself"ILIKE '%testing%' AND
"looking_for_in_a_person" ILIKE '%testing%' OR
"City" ~* '\mtest\M' OR 
"Name_Secondary_School"  ILIKE '%test%';



=======
UPDATE members
SET "Preference_cultural_background" = 'Any'
WHERE "Preference_cultural_background" IS NULL OR TRIM("Preference_cultural_background") = '';

UPDATE members
SET looking_for_in_a_person = 'open to anything/not picky'
WHERE looking_for_in_a_person IS NULL OR TRIM(looking_for_in_a_person) = '';

UPDATE members
SET "Introvert_Extravert" = ''
WHERE "Introvert_Extravert" IS NULL;

UPDATE members
SET "Sensor_Intuitive" = ''
WHERE "Sensor_Intuitive" IS NULL;

UPDATE members
SET "Thinker_Feeler" = ''
WHERE "Thinker_Feeler" IS NULL;

UPDATE members
SET "Judger_Perceiver" = ''
WHERE "Judger_Perceiver" IS NULL;

UPDATE members
SET parents_convert_before_birth = 'No'
WHERE parents_convert_before_birth IS NULL OR TRIM(parents_convert_before_birth) = '';
ALTER TABLE members ADD COLUMN "Acceptable_places_to_live" VARCHAR;

UPDATE members
SET  "Acceptable_places_to_live" = "Acceptable_places_to_live_Countries" || ' ' || "Acceptable_places_States";

ALTER TABLE members
DROP COLUMN "Acceptable_places_to_live_Countries",
DROP COLUMN "Acceptable_places_States";
