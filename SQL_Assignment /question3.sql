-- Code to inform the databse to use a databse 
USE Tech4Girls_DB;

-- Create another table
CREATE TABLE IF NOT EXISTS Courses(
    id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100)

);

-- Create a table names courses
INSERT INTO Courses(course_name)
VALUES
    ('Backend'),
    ('Front-End'),
    ('Data Analysis'),
    ('Network Engineering'),
    ('System Administration'),
    ('Quality Assurance Manager');


-- Create a table to match users to coourses
CREATE TABLE IF NOT EXISTS User_Courses(
    user_id INT NOT NULL,
    course_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);

INSERT INTO User_Courses(user_id,course_id) --This ensures that each user id cannot be linked to same course more than once, avoiding redundancy
-- The user id, corresponds to the Users in question 1 and the course id corresponds to the courses that
-- have been inputed.
-- So (1,1), means Ama takes a Backend course.The same Ama also takes Network Engineering(1,4)
VALUES
    (1,1), (1,4), (2,2), (2,6), (3,5), (3,3), (2,5);

SELECT * FROM Users;
SELECT * FROM Posts
SELECT * FROM Courses;
SELECT * FROM User_Courses;    

    
    
    

