-- the database name will be passed as an argument of the mysql command
-- Script that lists all cities contained in the database

  SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states
   WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
