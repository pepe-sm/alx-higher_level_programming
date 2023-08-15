-- Lists all score and names where name is not null orderdered  in descendin order.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
