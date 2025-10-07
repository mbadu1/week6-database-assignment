SELECT COUNT(*) as count_to_delete
FROM university_rankings
WHERE year = 2015 AND score < 45;

-- View the universities to be deleted
SELECT institution, country, score
FROM university_rankings
WHERE year = 2015 AND score < 45;

-- Delete universities with score < 45 in 2015
DELETE FROM university_rankings
WHERE year = 2015 AND score < 45;