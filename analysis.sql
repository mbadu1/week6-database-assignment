-- analysis.sql
-- Explore the database structure

-- Show all tables
.tables

-- Show schema of the rankings table
.schema

-- View sample data
SELECT * FROM university_rankings LIMIT 5;

-- Basic statistics
SELECT 
    year,
    COUNT(*) as total_universities,
    AVG(score) as avg_score,
    MAX(score) as max_score,
    MIN(score) as min_score
FROM university_rankings
GROUP BY year;

-- Top 10 universities by score in 2014
SELECT institution, country, world_rank, score
FROM university_rankings
WHERE year = 2014
ORDER BY score DESC
LIMIT 10;

-- Count universities by country in 2015
SELECT country, COUNT(*) as count
FROM university_rankings
WHERE year = 2015
GROUP BY country
ORDER BY count DESC
LIMIT 10;