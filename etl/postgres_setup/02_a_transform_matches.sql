DELETE FROM matches
WHERE id IN
    (SELECT matches.id
     FROM matches
     LEFT JOIN members AS m ON matches.male_id = m.id LEFT JOIN members AS f ON matches.female_id = f.id
     WHERE (
        m.short_description_of_yourself ~* '\mtest\M'
        AND m.looking_for_in_a_person~* '\mtest\M'
        AND m.looking_for_in_a_person NOT LIKE '%litmus test%'
        AND m.looking_for_in_a_person NOT LIKE '%biggest test%')
        OR
        (f.short_description_of_yourself ~* '\mtest\M'
        AND f.looking_for_in_a_person~* '\mtest\M'
        AND f.looking_for_in_a_person NOT LIKE '%litmus test%'
        AND f.looking_for_in_a_person NOT LIKE '%biggest test%')
        OR
        (m.short_description_of_yourself ILIKE '%testing%' AND m."looking_for_in_a_person" ILIKE '%testing%')
        OR
        (f.short_description_of_yourself ILIKE '%testing%' AND f."looking_for_in_a_person" ILIKE '%testing%')
        OR m.city ~* '\mtest\M'
        OR m.name_secondary_school  ILIKE '%test%'
        OR f.city ~* '\mtest\M'
        OR f.name_Secondary_School  ILIKE '%test%'
    );