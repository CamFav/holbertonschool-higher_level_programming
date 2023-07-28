-- Creates a table with name that can't be null
CREATE TABLE IF NOT EXISTS force_name (
    id int,
    name varchar(256) NOT NULL
);
