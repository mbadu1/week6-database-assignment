SELECT institution, year, score
FROM university_rankings
WHERE institution LIKE '%Oxford%' AND year = 2014;