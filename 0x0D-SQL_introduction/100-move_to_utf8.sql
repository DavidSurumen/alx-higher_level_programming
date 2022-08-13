-- Script that converts 'hbtn_0c_0' db to UTF8, the table 'first_table', and the field 'name'

-- Convert field
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4;
-- Convert table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Convert database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
