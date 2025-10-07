SELECT institution, year, score
FROM university_rankings
WHERE institution LIKE '%Oxford%' AND year = 2014;

-- Update Oxford's score by adding 1.2 points
UPDATE university_rankings
SET score = score + 1.2
WHERE institution LIKE '%Oxford%' AND year = 2014;