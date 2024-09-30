-- Create a database 

CREATE DATABASE artistsdb;

-- Use this Database 

USE artistsdb;

-- Show this database 

SELECT * from artistsdb;

CREATE TABLE artists (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50),
	age INT,
	genre VARCHAR(10)
);

-- Insert some data 

INSERT INTO artists (name,age,genre) VALUES ('Chitresh',20,'Hiphop');


