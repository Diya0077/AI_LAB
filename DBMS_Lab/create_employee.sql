CREATE TABLE employee(
employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    Designatuion VARCHAR(50),
    city VARCHAR(50),
    EXP INT,
    Salary INT
    );
   
INSERT INTO employee (employee_id , name , Designatuion , city, EXP, Salary)
VALUES
(1,'Akash Roy','Manager','Kolkata',20,100000),
(2,'Bikash Ghose','Team Lead','Mumbai',8,75000),
(3,'Riya Pal','Software Engineer','Kolkata',3,50000),
(4,'Mousumi Dey','Software Engineer','Delhi',3,50000),
(5,'Tapas Das','Sales Manager','Kolkata',6,65000),
(6,'Payel Das','Stock Mnager','Mumbai',6,55000),
(7,'Krish Bose','Developer','Mumbai',2,30000),
(8,'Kushal Roy','Developer','Bangalore',2,30000),
(9,'Shreya Das','Software Engineer','Pune',4,35000),
(10,'Pritha Pal','Developer','Hyderabad',3,45000),
(11,'Suvojit Mondal','Developer','Kolkata',2,30000);

SELECT*FROM employee;

