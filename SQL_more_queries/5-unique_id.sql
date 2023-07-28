-- Creates a table with a id that must be unique.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 PRIMARY KEY,
    name varchar(256)
);
