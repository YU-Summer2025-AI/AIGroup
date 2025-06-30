SELECT
    CASE 
        WHEN gender = 'Male' THEN 1
    ELSE 0
    END AS gender,
    CASE 
        WHEN body_type = 'A Few Extra Pounds' THEN 1
    ELSE 0
    END AS A_Few_Extra_Pounds,
    CASE 
        WHEN body_type = 'Athletic/Fit' THEN 1
    ELSE 0
    END AS Athletic_Fit,
    CASE 
        WHEN body_type = 'Average/Medium Build' THEN 1
    ELSE 0
    END AS Average_Medium_Build,
    CASE 
        WHEN body_type = 'Firm & Toned' THEN 1
    ELSE 0
    END AS Firm_Toned,
    CASE 
        WHEN body_type = 'Large/Broad Build' THEN 1
    ELSE 0
    END AS Large_Broad_Build,
    CASE 
        WHEN body_type = 'Lean/Slender' THEN 1
    ELSE 0
    END AS Lean_Slender,
    CASE 
        WHEN body_type = 'A Few Extra Pounds' THEN 1
    ELSE 0
    END AS A_Few_Extra_Pounds,
    CASE 
        WHEN body_type = 'Muscular' THEN 1
    ELSE 0
    END AS Muscular,
    CASE 
        WHEN body_type = 'Proportional' THEN 1
    ELSE 0
    END AS Proportional,


    CASE 
        WHEN religious_orientation = 'Heimish' THEN 1
        WHEN religious_orientation = 'Heimish ' THEN 1
    ELSE 0
    END AS Heimish,
    CASE 
        WHEN religious_orientation = 'Traditional' THEN 1
    ELSE 0
    END AS Traditional,
    CASE 
        WHEN religious_orientation = 'Modern Orthodox (Middle of the road)' THEN 1
    ELSE 0
    END AS M_O_Middle_of_the_road,
    CASE 
        WHEN religious_orientation = 'Strictly Frum/Not Yeshivish' THEN 1
    ELSE 0
    END AS Strictly_Frum_Not_Yeshivish,
    CASE 
        WHEN religious_orientation = 'Modern Orthodox (Machmir)' THEN 1
    ELSE 0
    END AS M_O_Machmir,
    CASE 
        WHEN religious_orientation = 'Conservadox' THEN 1
    ELSE 0
    END AS Conservadox,
    CASE 
        WHEN religious_orientation = 'Chassidish' THEN 1
    ELSE 0
    END AS Chassidish,
    CASE 
        WHEN religious_orientation = 'Conservative' THEN 1
    ELSE 0
    END AS Conservative,
    CASE 
        WHEN religious_orientation = 'Modern Yeshivish' THEN 1
    ELSE 0
    END AS M_Yeshivish,
    CASE 
        WHEN religious_orientation = 'Spiritual but not religious' THEN 1
    ELSE 0
    END AS Spiritual_but_not_religious,
    CASE 
        WHEN religious_orientation ='Modern Orthodox (liberal)' THEN 1
    ELSE 0
    END AS M_O_liberal,
    CASE 
        WHEN religious_orientation = 'Lubavitch' THEN 1
    ELSE 0
    END AS Lubavitch,
    CASE 
        WHEN religious_orientation = 'Just Jewish' THEN 1
    ELSE 0
    END AS Just_Jewish,
    CASE 
        WHEN religious_orientation = 'Reform' THEN 1
    ELSE 0
    END AS Reform,
    CASE 
        WHEN religious_orientation = 'Yeshivish' THEN 1
    ELSE 0
    END AS Yeshivish
FROM members
