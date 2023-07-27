-- Create the user if it does not exist, and set the password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Make sure the privileges are applied immediately
FLUSH PRIVILEGES;
