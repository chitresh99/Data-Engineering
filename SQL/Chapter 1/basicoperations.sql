-- Create a database 

CREATE DATABASE artistsdb;

-- Use this Database 

USE artistsdb;

-- Show this database 

SELECT * from artists;

CREATE TABLE artists (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50),
	age INT,
	genre VARCHAR(10)
);

-- Insert some data 

INSERT INTO artists (name,age,genre) VALUES ('Chitresh',20,'Hiphop');

CREATE TABLE shows (
show_id INT AUTO_INCREMENT PRIMARY KEY,
show_name VARCHAR(100) NOT NULL
);


CREATE TABLE artist_shows(
	artist_id INT,
	show_id INT,
	PRIMARY KEY (artist_id,course_id),
	FOREIGN KEY (artist_id) REFERENCES artists(id),
	FOREIGN KEY (show_id) REFERNECES shows(show_id)
);


