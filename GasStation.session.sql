CREATE TABLE representatives (
    customer_id INT, 
    License_plate VARCHAR (20),
    FOREIGN KEY (customer_id) REFERENCES chargecustomer(customer_id) ON DELETE CASCADE
);

