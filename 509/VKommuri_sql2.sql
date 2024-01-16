
/*Student Name: Vignesh kommuri
*/
USE VKommuri; 


INSERT INTO VKommuri_customer (custnum, custname, city, creditlimit)
VALUES
    (1, 'John Doe', 'New York', 1000),
    (2, 'Jane Smith', 'Los Angeles', 1500);

INSERT INTO VKommuri_orders (ordernum, orderdate, filled, custnum)
VALUES
    (1, '2023-09-10', 1, 2),
    (2, '2023-09-20', 1, 9);
    


INSERT INTO VKommuri_product (productnum, descr, producttype, msrp, onhand)
VALUES
    (1, 'Swiss army knife', 'Sports', 51.69, 22),
    (2, 'Electric heater', 'Hardware', 99.99, 10);


INSERT INTO VKommuri_orderline (ordernum, productnum, quantity, salesprice)
VALUES
    (1, 7, 2, 34.99),
    (2, 6, 1, 980.00);