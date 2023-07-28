-- Lists all cities contained in the database.
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
on states.id = cities.state_id;
