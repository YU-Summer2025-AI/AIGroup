DROP VIEW IF EXISTS matches_values;

CREATE VIEW matches_values AS
SELECT 
CASE matches.overall_pr
    WHEN 'Male declined' THEN 0
    WHEN 'Female declined' THEN 0
    ELSE 1
END AS match_status,

    male.height - female.height as height_diff,
    male.age - female.age as age_diff,

    male.height AS male_height,
    male.age AS male_age,
    male.gender AS male_gender,
    male.A_Few_Extra_Pounds AS male_A_Few_Extra_Pounds,
    male.Athletic_Fit AS male_Athletic_Fit,
    male.Average_Medium_Build AS male_Average_Medium_Build,
    male.Firm_Toned AS male_Firm_Toned,
    male.Large_Broad_Build AS male_Large_Broad_Build,
    male.Lean_Slender AS male_Lean_Slender,
    male.Muscular AS male_Muscular,
    male.Proportional AS male_Proportional,
    male.Heimish AS male_Heimish,
    male.Traditional AS male_Traditional,
    male.M_O_Middle_of_the_road AS male_M_O_Middle_of_the_road,
    male.Strictly_Frum_Not_Yeshivish AS male_Strictly_Frum_Not_Yeshivish,
    male.M_O_Machmir AS male_M_O_Machmir,
    male.Conservadox AS male_Conservadox,
    male.Chassidish AS male_Chassidish,
    male.Conservative AS male_Conservative,
    male.M_Yeshivish AS male_M_Yeshivish,
    male.Spiritual_but_not_religious AS male_Spiritual_but_not_religious,
    male.M_O_liberal AS male_M_O_liberal,
    male.Lubavitch AS male_Lubavitch,
    male.Just_Jewish AS male_Just_Jewish,
    male.Reform AS male_Reform,
    male.Yeshivish AS male_Yeshivish,
    male.Introvert AS male_Introvert,
    male.Sensor AS male_Sensor,
    male.Feeler AS male_Feeler,
    male.Perceiver AS male_Perceiver,

    female.height AS female_height,
    female.age AS female_age,
    female.gender AS female_gender,
    female.A_Few_Extra_Pounds AS female_A_Few_Extra_Pounds,
    female.Athletic_Fit AS female_Athletic_Fit,
    female.Average_Medium_Build AS female_Average_Medium_Build,
    female.Firm_Toned AS female_Firm_Toned,
    female.Large_Broad_Build AS female_Large_Broad_Build,
    female.Lean_Slender AS female_Lean_Slender,
    female.Muscular AS female_Muscular,
    female.Proportional AS female_Proportional,
    female.Heimish AS female_Heimish,
    female.Traditional AS female_Traditional,
    female.M_O_Middle_of_the_road AS female_M_O_Middle_of_the_road,
    female.Strictly_Frum_Not_Yeshivish AS female_Strictly_Frum_Not_Yeshivish,
    female.M_O_Machmir AS female_M_O_Machmir,
    female.Conservadox AS female_Conservadox,
    female.Chassidish AS female_Chassidish,
    female.Conservative AS female_Conservative,
    female.M_Yeshivish AS female_M_Yeshivish,
    female.Spiritual_but_not_religious AS female_Spiritual_but_not_religious,
    female.M_O_liberal AS female_M_O_liberal,
    female.Lubavitch AS female_Lubavitch,
    female.Just_Jewish AS female_Just_Jewish,
    female.Reform AS female_Reform,
    female.Yeshivish AS female_Yeshivish,
    female.Introvert AS female_Introvert,
    female.Sensor AS female_Sensor,
    female.Feeler AS female_Feeler,
    female.Perceiver AS female_Perceiver
from matches
left join member_values as male on matches.male_id = male.id
left join member_values as female on matches.female_id = female.id;

