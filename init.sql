CREATE TABLE students (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(250),
    first_name VARCHAR(250),
    last_name VARCHAR(250),
    classes JSON DEFAULT NULL,
    PRIMARY KEY (id)
);