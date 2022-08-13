-- Script that creates database and a user, and gives specific privileges to the user
-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create the user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grant SELECT privileges
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
