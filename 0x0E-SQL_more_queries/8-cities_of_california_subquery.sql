-- since no use of joins you canuse subquey to et state_id
SELECT cities.id, cities.name FROM cities WHERE cities.state_id=(SELECT states.id FROM states WHERE states.name="California") ORDER BY cities.id ASC;
