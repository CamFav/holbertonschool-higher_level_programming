-- removes all records with a score <= 5 in the table second_table of the database
UPDATE second_table
REMOVE score WHERE score <= 5;
