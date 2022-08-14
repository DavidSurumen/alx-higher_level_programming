-- Creates database 'hbtn_0d_usa' and the table 'states' in that db
-- command to create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create table in the db
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY, `name` VARCHAR(256));
