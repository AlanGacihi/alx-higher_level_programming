-- Count of scores.
SELECT score, count(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
