-- Script that converts 'hbtn_0c_0' db to UTF8, the table 'first_table', and the field 'name'
-- Convert db to utf8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Convert table
ALTER TABLE first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Convert field
ALTER TABLE first_table MODIFY name TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
