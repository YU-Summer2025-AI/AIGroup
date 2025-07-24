DROP VIEW IF EXISTS total_female,
                    female_pref,
                    female_approved_full,
                    female_approved_approved,
                    females
CASCADE;


CREATE VIEW females AS
SELECT DISTINCT female_id
FROM matches
WHERE ms = 'Closed';

CREATE VIEW male_approved AS
SELECT m.female_id, m.male_id
FROM matches m
JOIN females f ON m.female_id = f.female_id
WHERE m.ms = 'Closed'
ORDER BY m.female_id;

CREATE VIEW male_approved_full AS
SELECT ma.female_id, mv.* 
FROM member_values mv
JOIN male_approved ma ON mv.id = ma.male_id;
CREATE VIEW female_pref AS
SELECT
    female_id,
    ROUND(AVG(height), 3) AS avg_height,
    ROUND(AVG(age), 3) AS avg_age,
    ROUND(AVG(a_few_extra_pounds), 3) AS avg_a_few_extra_pounds,
    ROUND(AVG(athletic_fit), 3) AS avg_athletic_fit,
    ROUND(AVG(average_medium_build), 3) AS avg_medium_build,
    ROUND(AVG(firm_toned), 3) AS avg_firm_toned,
    ROUND(AVG(large_broad_build), 3) AS avg_large_broad_build,
    ROUND(AVG(lean_slender), 3) AS avg_lean_slender,
    ROUND(AVG(muscular), 3) AS avg_muscular,
    ROUND(AVG(proportional), 3) AS avg_proportional,
    ROUND(AVG(heimish), 3) AS avg_heimish,
    ROUND(AVG(traditional), 3) AS avg_traditional,
    ROUND(AVG(m_o_middle_of_the_road), 3) AS avg_middle_of_road,
    ROUND(AVG(strictly_frum_not_yeshivish), 3) AS avg_strickly_frum,
    ROUND(AVG(m_o_machmir), 3) AS avg_machmir,
    ROUND(AVG(conservadox), 3) AS avg_conservadox,
    ROUND(AVG(chassidish), 3) AS avg_chassidish,
    ROUND(AVG(conservative), 3) AS avg_conservative,
    ROUND(AVG(m_yeshivish), 3) AS avg_m_yeshivish,
    ROUND(AVG(spiritual_but_not_religious), 3) AS avg_spiritual_but_not_religious,
    ROUND(AVG(m_o_liberal), 3) AS avg_m_o_liberal,
    ROUND(AVG(lubavitch), 3) AS avg_lubavitch,
    ROUND(AVG(just_jewish), 3) AS avg_just_jewish,
    ROUND(AVG(reform), 3) AS avg_reform,
    ROUND(AVG(yeshivish), 3) AS avg_yeshivish,
    ROUND(AVG(introvert), 3) AS avg_introvert,
    ROUND(AVG(sensor), 3) AS avg_sensor,
    ROUND(AVG(feeler), 3) AS avg_feeler,
    ROUND(AVG(perceiver), 3) AS avg_perceiver,
    COUNT(*) AS match_count
FROM male_approved_full
GROUP BY female_id;

CREATE VIEW total_female AS
    SELECT *
    FROM female_pref
    JOIN member_values
    ON female_pref.female_id = member_values.id;
SELECT *
FROM total_female;