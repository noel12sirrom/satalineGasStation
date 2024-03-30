CREATE TABLE chargecustomer (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    cutomer_name VARCHAR(100),
    number_of_representatives INT,
    preference VARCHAR(20)
  );
CREATE TABLE representatives (
    customer_id INT, 
    License_plate VARCHAR (20),
    FOREIGN KEY (customer_id) REFERENCES chargecustomer(customer_id)
    );


