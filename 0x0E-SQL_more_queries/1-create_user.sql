-- Script that creates the MySQL server user 'user_0d_1'
-- command to create user if not exists already
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_psw';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
