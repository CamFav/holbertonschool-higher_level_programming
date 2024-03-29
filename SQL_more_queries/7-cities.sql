-- Script that creates a database and a table with specific attributes.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id),
    name varchar(256) NOT NULL
);
