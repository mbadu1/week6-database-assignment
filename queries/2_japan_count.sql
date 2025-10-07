SELECT COUNT(*) as japan_top_200_count
FROM rankings
WHERE country = 'Japan' 
  AND year = 2013 
  AND world_rank <= 200;