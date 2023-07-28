-- Creates a table with a id that can't be null
CREATE TABLE IF NOT EXISTS force_name (
    id int DEFAULT 1,
    name varchar(256)
);
