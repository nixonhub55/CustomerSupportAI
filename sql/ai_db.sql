CREATE DATABASE ai_db;


USE ai_db;



-- DROP TABLE IF EXISTS knowledge;
CREATE TABLE knowledge ( 
    knowledge_id INT AUTO_INCREMENT PRIMARY KEY, 
    category VARCHAR(50) NOT NULL, 
    title VARCHAR(150) NOT NULL, 
    keywords VARCHAR(255), 
    content LONGTEXT NOT NULL, 
    priority INT DEFAULT 1, 
    is_active TINYINT DEFAULT 1, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
 


 
	INSERT INTO knowledge
	(category,title,keywords,content) 
	VALUES 
	(
	'Billing', 
	'Payment Process', 
	'payment,pay,bill,gcash,maya', 
	'Customers may pay using GCash, Maya, Bank Transfer or Cash at the office. Payments are normally posted within 24 hours.'
	);
	
	
	INSERT INTO knowledge
	(category,title,keywords,content)

	VALUES

	(
	'Billing',

	'Reconnection Policy',

	'reconnect,reconnection,restore',

	'Accounts are reactivated after payment has been verified and posted.'
	);
	
		
	INSERT INTO knowledge
	(category,title,keywords,content)
	VALUES
	(
	'Billing',
	'Disconnection Policy',
	'disconnect,inactive,suspended',
	'Accounts with unpaid balances may become In-Active until payment is received.'
	);

 
