-- Query to create the table 'unique_id' in MySQL server
-- should not fail if exists

CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
