
-- Inform sql to work with Tech4Girls_DB
USE Tech4Girls_DB;

-- Create another table
CREATE TABLE IF NOT EXISTS Posts(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    title VARCHAR(225) NOT NULL,
    context TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL

);
-- See all created tables
SHOW TABLES;

-- Input data into the created table
INSERT INTO Posts(user_id,title,context)
VALUES
     (1,'Class rep','Commmunicate information and organise class'),
     (1,'Backend Engineer','Create connection between database,front-end and backend'),
     (2,'Linux System Administrator','Manage,maintain and troubleshooting'),
     (2,'Python Data Analyst','Analyse data with python'),
     (2,'Python DevOps Engineer', 'Use python for development and operations'),
     (3,'Database Administrator','Database management and security'),
     (3,'Product Manager','Planning, Budgeting, Risk Management, Team Coordination');

-- See what specifically is in the table
SELECT * FROM Posts;     

