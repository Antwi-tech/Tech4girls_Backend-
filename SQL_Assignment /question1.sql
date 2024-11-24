
-- Command to create a database that does not exists
CREATE DATABASE IF NOT EXISTS Tech4Girls_DB;
-- This command displays the databases that have been created
SHOW DATABASES;
-- This command tells sql what particular daabase we want to use
USE Tech4Girls_DB;

-- Command to create a table that does not exists and specify their columns
CREATE TABLE IF NOT EXISTS Users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- Command to insert data into the specified  cloumns. Every row is known as a record
INSERT INTO Users(username,email)
VALUES
      ('ama','ama@example.com'),
      ('Abena','abena@example.com'),
      ('Adjoa','adjoa@example.com');

-- Command to see the table itself
SELECT * FROM Users;


