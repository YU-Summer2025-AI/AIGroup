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

CREATE VIEW matches_physical_eval AS
SELECT
    -- Selecting match details from the 'matches' table
    m.id AS match_id,
    m.male_id AS m_id,
    m.female_id AS f_id,

    -- Selecting physical attributes for the male from the 'members' table
    male_info.age AS m_age,
    male_info.height AS m_height,
    male_info.Body_type AS m_bt,
    male_info.hair_color AS m_hair_c,
    male_info.eye_color AS m_eye_c,
    male_info.smoking_habits AS m_smoker,
    male_info.how_active_are_you AS m_fitness,
    male_info.mental_physical_disability AS m_mp_disability,

    -- Selecting physical attributes for the female from the 'members' table
    female_info.age AS f_age,
    female_info.height AS f_height,
    female_info.body_type AS f_bt,
    female_info.hair_color AS f_hair_c,
    female_info.eye_color AS f_eye_c,
    female_info.smoking_habits AS f_smoker,
    female_info.how_active_are_you AS f_fitness,
    female_info.mental_physical_disability AS f_mp_disability,

    -- Selecting match outcome details from the 'matches' table
    m.overall_pr,
    m.match_quality,
    m.decline_reason
FROM
    matches AS m
-- Join with the members table to get the male's information
JOIN
    members AS male_info ON m.male_id = male_info.id
-- Join with the members table again to get the female's information
JOIN
    members AS female_info ON m.female_id = female_info.id;