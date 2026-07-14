CREATE DATABASE billing_db;

USE billing_db;


-- DROP TABLE IF EXISTS customers;
CREATE TABLE IF NOT EXISTS customers (
    custome_id BIGINT AUTO_INCREMENT,
    account_no VARCHAR(50) NULL,
    lastname VARCHAR(50) NULL,
    firstname VARCHAR(50) NULL,
    middlename VARCHAR(50) NULL,
    `status` INT NOT NULL DEFAULT 1,
    plan VARCHAR(50) NULL,
    balance FLOAT NOT NULL DEFAULT 0,
    address VARCHAR(100) NULL,
    phone VARCHAR(13) NULL,
    email VARCHAR(50) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (custome_id),
    INDEX idx_custome_id (account_no)
) ENGINE=MYISAM;





-- SELECT * FROM customers	


/*
	INSERT INTO customers (account_no,lastname,firstname,middlename,plan,balance,address,phone,email)
	SELECT '100002','ISANAN','MAR','L','Test Plan',2000,'LEYTE','0922233311','onnixsd@gmail.com' UNION ALL
	SELECT '100003','ISO','NIXON','C','Test Plan 2',3000,'SAMAR','0922233322','onni2sd@gmail.com'
*/




 