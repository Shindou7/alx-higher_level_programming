-- Script that lists all the cities of California registered in the database
-- the database name will be passed as an argument of the mysql command
-- Query to list all the cities from California
-- Query to get the id of California

SELECT id, name
FROM cities
WHERE state_id = (
      SELECT id
      FROM states
      WHERE name = "California");
