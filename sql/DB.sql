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




 
INSERT INTO customers (account_no,lastname,firstname,middlename,plan,balance,address,phone,email)
SELECT '100002','ISANAN','MAR','L','Test Plan',2000,'LEYTE','0922233311','onnixsd@gmail.com' UNION ALL
SELECT '100003','ISO','NIXON','C','Test Plan 2',3000,'SAMAR','0922233322','onni2sd@gmail.com';



CREATE TABLE plans (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,
    plan_name VARCHAR(100) NOT NULL,
    speed VARCHAR(50),
    monthly_fee DECIMAL(10,2) NOT NULL,
    description TEXT,
    STATUS TINYINT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=INNODB;


INSERT INTO plans
(plan_name, speed, monthly_fee, description)
VALUES
('Fiber 50', '50 Mbps', 999.00, 'Residential Fiber 50 Mbps'),
('Fiber 100', '100 Mbps', 1499.00, 'Residential Fiber 100 Mbps'),
('Fiber 300', '300 Mbps', 2499.00, 'Residential Fiber 300 Mbps');


CREATE TABLE payments (
    payment_id BIGINT AUTO_INCREMENT PRIMARY KEY, 
    account_no VARCHAR(50) NOT NULL, 
    amount DECIMAL(10,2) NOT NULL, 
    payment_date DATETIME NOT NULL, 
    payment_method VARCHAR(50), 
    reference_no VARCHAR(100), 
    remarks VARCHAR(255), 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    INDEX idx_account (account_no)
) ENGINE=INNODB;


-- DROP TABLE IF EXISTS payments;
CREATE TABLE payments (
    payment_id BIGINT AUTO_INCREMENT PRIMARY KEY, 
    account_no VARCHAR(50) NOT NULL, 
    amount DECIMAL(10,2) NOT NULL, 
    payment_date DATETIME NOT NULL, 
    payment_method VARCHAR(50), 
    reference_no VARCHAR(100), 
    remarks VARCHAR(255), 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    INDEX idx_account (account_no)
) ENGINE=INNODB;


/*
INSERT INTO payments
(account_no, amount, payment_date, payment_method, reference_no)
VALUES
('100001',500,'2026-05-10 09:30:00','GCash','GC123456'),
('100001',600,'2026-06-10 10:15:00','Cash','OFFICE001'),
('100001',700,'2026-07-10 08:45:00','Maya','MY987654');

*/


CREATE TABLE invoices ( 
    invoice_id BIGINT AUTO_INCREMENT PRIMARY KEY, 
    account_no VARCHAR(50) NOT NULL, 
    billing_month DATE NOT NULL, 
    due_date DATE NOT NULL, 
    amount DECIMAL(10,2) NOT NULL, 
    STATUS ENUM(
        'UNPAID',
        'PAID',
        'OVERDUE'
    ) DEFAULT 'UNPAID', 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    INDEX idx_account(account_no)
) ENGINE=INNODB;



INSERT INTO invoices
(account_no,billing_month,due_date,amount,STATUS)
VALUES
('100001','2026-07-01','2026-07-20',1000,'UNPAID'),
('100001','2026-06-01','2026-06-20',1000,'PAID'),
('100001','2026-05-01','2026-05-20',1000,'PAID');



CREATE TABLE tickets ( 
    ticket_id BIGINT AUTO_INCREMENT PRIMARY KEY, 
    account_no VARCHAR(50) NOT NULL, 
    SUBJECT VARCHAR(150), 
    description TEXT, 
    STATUS ENUM(
        'OPEN',
        'IN_PROGRESS',
        'RESOLVED',
        'CLOSED'
    ) DEFAULT 'OPEN', 
    priority ENUM(
        'LOW',
        'MEDIUM',
        'HIGH',
        'CRITICAL'
    ) DEFAULT 'MEDIUM', 
    opened_at DATETIME DEFAULT CURRENT_TIMESTAMP, 
    closed_at DATETIME NULL, 
    INDEX idx_account(account_no)
) ENGINE=INNODB;



INSERT INTO tickets
(account_no,SUBJECT,description,STATUS,priority)
VALUES
(
'100001',
'Slow Internet',
'Customer reports slow browsing.',
'OPEN',
'HIGH'
);



CREATE TABLE service_requests ( 
    request_id BIGINT AUTO_INCREMENT PRIMARY KEY, 
    account_no VARCHAR(50) NOT NULL, 
    request_type ENUM(
        'INSTALLATION',
        'RELOCATION',
        'RECONNECTION',
        'DISCONNECTION',
        'UPGRADE',
        'DOWNGRADE'
    ),

    STATUS ENUM(
        'PENDING',
        'APPROVED',
        'ONGOING',
        'COMPLETED',
        'CANCELLED'
    ) DEFAULT 'PENDING', 
    remarks TEXT, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    completed_at DATETIME NULL, 
    INDEX idx_account(account_no)
) ENGINE=INNODB;


ALTER TABLE customers ADD COLUMN plan_id INT NULL;
UPDATE customers SET plan_id = 2 WHERE account_no = '100001';

-- DROP TABLE IF EXISTS knowledge;
CREATE TABLE knowledge ( 
    knowledge_id BIGINT AUTO_INCREMENT PRIMARY KEY, 
    category VARCHAR(50) NOT NULL, 
    title VARCHAR(150) NOT NULL, 
    keywords VARCHAR(255), 
    content LONGTEXT NOT NULL, 
    STATUS TINYINT DEFAULT 1, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP, 
    INDEX idx_category(category),
    INDEX idx_status(STATUS)
) ENGINE=INNODB;



INSERT INTO knowledge
(category,title,keywords,content)
VALUES

(
'PAYMENT',
'Payment Methods',
'payment,gcash,maya,cash',
'Customers can pay using GCash, Maya, bank transfer, or cash at the office.'
),

(
'BILLING',
'Due Date',
'due,date,billing',
'Monthly due date is every 20th of the month.'
),

(
'RECONNECTION',
'Reconnection Policy',
'reconnect,reconnection',
'Reconnection is processed after full payment of all outstanding balances.'
),

(
'DISCONNECTION',
'Disconnection Policy',
'disconnect,cutoff',
'Accounts with unpaid balances may be disconnected according to company policy.'
);



	
DROP TABLE IF EXISTS v_cb_customers;
DROP VIEW IF EXISTS v_cb_customers;
DELIMITER $$ 
CREATE VIEW `v_cb_customers` AS  
	SELECT custome_id AS customer_id
	      ,account_no
	      ,lastname
	      ,firstname 
	      ,middlename
	      ,(CASE
		   WHEN `status`=1 THEN 'Active'
		   WHEN `status`=0 THEN 'In-Active'
	        END) AS `status`
	      ,plan
	      ,balance
	      ,address
	      ,phone
	      ,email
	      ,created_at
	      ,plan_id
	FROM customers;
        $$ 
DELIMITER ;
 		
		
 