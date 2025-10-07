SELECT institution, world_rank, score
FROM university_rankings
WHERE country = 'Japan' 
  AND year = 2013 
  AND world_rank <= 200
ORDER BY world_rank;