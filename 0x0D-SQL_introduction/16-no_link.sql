-- Lists all records of the table 'second_table' except those without 'name' value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
