-- list content of 2 tables usin join
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON states.id=cities.state_id ORDER BY cities.id ASC;
