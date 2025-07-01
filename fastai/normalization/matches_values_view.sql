
--there was no need for the members


CREATE VIEW matches_values AS
SELECT 
CASE matches.overall_pr
    WHEN 'Male declined' THEN 0
    WHEN 'Female declined' THEN 0
    ELSE 1
END AS match_status,


    CAST(SUBSTRING(male.height FROM '\((\d+)\s*cm\)') AS INTEGER) - CAST(SUBSTRING(female.height FROM '\((\d+)\s*cm\)') AS INTEGER) AS height_diff,
    CAST(male.age AS INTEGER) - CAST(female.age AS INTEGER) AS age_diff,


    CAST(SUBSTRING(male.height FROM '\((\d+)\s*cm\)') AS INTEGER) AS male_height,
    CAST(male.age AS INTEGER) as male_age,
    male.body_type as male_body_type,
    male.religious_orientation as male_religious_orientation,
    male.family_religious_background as male_family_religious_background,
    male.kosher as male_kosher,
    male.secular_education as male_secular_education,
    male.jewish_education as male_jewish_education, 

    CAST(SUBSTRING(female.height FROM '\((\d+)\s*cm\)') AS INTEGER) AS female_height,
    CAST(female.age AS INTEGER) as female_age,
    female.body_type as female_body_type,
    female.religious_orientation as female_religious_orientation,
    female.family_religious_background as female_family_religious_background,
    female.kosher as female_kosher,
    female.secular_education as female_secular_education,
    female.jewish_education as female_jewish_education
from matches
left join members as male on matches.male_id = male.id
left join members as female on matches.female_id = female.id;
