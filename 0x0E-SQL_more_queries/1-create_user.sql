-- Creates the MySQL server user_0d_1
-- With all privileges on the server
-- password set to user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES
ON *.*
TO 'user_0d_1'@'localhost';
