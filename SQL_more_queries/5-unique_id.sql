-- Creates a table with a id that must be unique.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1 PRIMARY KEY,
    name varchar(256)
);
