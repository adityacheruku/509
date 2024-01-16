
/*Student Name: Vignesh kommuri
*/
USE VKommuri; 


DROP TABLE IF EXISTS VKommuri_orderline;
DROP TABLE IF EXISTS VKommuri_orders;
DROP TABLE IF EXISTS VKommuri_product;
DROP TABLE IF EXISTS VKommuri_customer;

CREATE TABLE VKommuri_customer (
    custnum INT PRIMARY KEY,
    custname VARCHAR(255),
    city VARCHAR(255),
    creditlimit INT
);


CREATE TABLE VKommuri_orders (
    ordernum INT PRIMARY KEY,
    orderdate DATE,
    filled INT,
    custnum INT,
    FOREIGN KEY (custnum) REFERENCES VKommuri_customer(custnum)
);

CREATE TABLE VKommuri_product (
    productnum INT PRIMARY KEY,
    descr VARCHAR(255),
    producttype VARCHAR(255),
    msrp DECIMAL(10, 2),
    onhand INT
);

CREATE TABLE VKommuri_orderline (
    ordernum INT,
    productnum INT,
    quantity INT,
    salesprice DECIMAL(10, 2),
    PRIMARY KEY (ordernum, productnum),
    FOREIGN KEY (ordernum) REFERENCES VKommuri_orders(ordernum),
    FOREIGN KEY (productnum) REFERENCES VKommuri_product(productnum)
);
