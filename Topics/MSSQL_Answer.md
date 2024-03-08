<link rel="stylesheet" href="../test/style.css">

# [MSSQl Answers](./MSSQL_Answer.md)

- [MSSQl Answers](#mssql-answers)
  - [**Introduction to SQL Server - SQL Introduction**](#introduction-to-sql-server---sql-introduction)
  - [**What Is Data, Database \& Data Management in SQL**](#what-is-data-database--data-management-in-sql)
  - [**What Is Database Entity in SQL Server - Entity in SQL - Database Entity in SQL**](#what-is-database-entity-in-sql-server---entity-in-sql---database-entity-in-sql)
  - [**Database Management System in SQL - SQL DBMS - RDBMS - SQL Server**](#database-management-system-in-sql---sql-dbms---rdbms---sql-server)
  - [**Database Models in SQL Server - Database Models - Relational Data Model - SQL**](#database-models-in-sql-server---database-models---relational-data-model---sql)
  - [**RDBMS in SQL - Relational Database Management System in SQL - SQL**](#rdbms-in-sql---relational-database-management-system-in-sql---sql)
  - [**How to Create Database \& Tables in SQL Server - Creating Database \& Tables in SQL**](#how-to-create-database--tables-in-sql-server---creating-database--tables-in-sql)
  - [**How to Insert Data in Table in SQL Server - Inserting Data in SQL Table - SQL**](#how-to-insert-data-in-table-in-sql-server---inserting-data-in-sql-table---sql)
  - [**Update Command in SQL Server - Update with Set in SQL - SQL Server**](#update-command-in-sql-server---update-with-set-in-sql---sql-server)
  - [**DELETE and TRUNCATE Command in SQL**](#delete-and-truncate-command-in-sql)
  - [**1. UNIQUE and NOT NULL Constraints in SQL:**](#1-unique-and-not-null-constraints-in-sql)
  - [**2. PRIMARY KEY, DEFAULT, and CHECK Constraints in SQL Server:**](#2-primary-key-default-and-check-constraints-in-sql-server)
  - [**3. SELECT Command in SQL Server:**](#3-select-command-in-sql-server)
  - [**5. Cascading Referential Integrity Constraints in SQL Server:**](#5-cascading-referential-integrity-constraints-in-sql-server)
  - [**6. ALTER Command in SQL Server:**](#6-alter-command-in-sql-server)
  - [**7. Adding \& Dropping SQL Constraints Using ALTER Command:**](#7-adding--dropping-sql-constraints-using-alter-command)
  - [**8. ALIAS in SQL Server:**](#8-alias-in-sql-server)
  - [**9. INNER JOIN in SQL Server:**](#9-inner-join-in-sql-server)
  - [**LEFT JOIN, RIGHT JOIN \& FULL OUTER JOIN IN SQL SERVER**](#left-join-right-join--full-outer-join-in-sql-server)
  - [**SELF JOIN IN SQL SERVER**](#self-join-in-sql-server)
  - [**IDENTITY OR AUTO INCREMENT IN SQL SERVER**](#identity-or-auto-increment-in-sql-server)
  - [**Union And Union All In SQL Server - SQL Union All Command - Union - Union All**](#union-and-union-all-in-sql-server---sql-union-all-command---union---union-all)
  - [**Intersect And Except In SQL Server - SQL Intersect - SQL Except - Except - Intersect**](#intersect-and-except-in-sql-server---sql-intersect---sql-except---except---intersect)
  - [**Aggregate Functions in SQL Server:**](#aggregate-functions-in-sql-server)
  - [**Group By in SQL Server:**](#group-by-in-sql-server)
  - [**Having and Where Clause in SQL Server:**](#having-and-where-clause-in-sql-server)
  - [**Order By Command in SQL Server:**](#order-by-command-in-sql-server)
  - [**Views in SQL Server:**](#views-in-sql-server)
  - [**LIKE Operator in SQL Server:**](#like-operator-in-sql-server)
  - [**Subquery in SQL Server:**](#subquery-in-sql-server)
  - [**Scalar and Multi-Valued Subquery in SQL:**](#scalar-and-multi-valued-subquery-in-sql)
  - [**Self-Contained and Correlated Subquery in SQL Server:**](#self-contained-and-correlated-subquery-in-sql-server)
  - [**BETWEEN, TOP, PERCENT, DISTINCT, and IN Operator in SQL Server:**](#between-top-percent-distinct-and-in-operator-in-sql-server)
  - [**Select Into Statement in SQL Server**](#select-into-statement-in-sql-server)
  - [**Insert Into with Select Statement in SQL Server**](#insert-into-with-select-statement-in-sql-server)
  - [**Changing or Renaming Database Name and Table Name in SQL**](#changing-or-renaming-database-name-and-table-name-in-sql)
  - [**Stored Procedure in SQL Server**](#stored-procedure-in-sql-server)
  - [**Functions in SQL Server**](#functions-in-sql-server)
  - [**Inline Table-Valued Functions in SQL Server**](#inline-table-valued-functions-in-sql-server)
  - [**Multi-Statement Table-Valued Functions in SQL Server**](#multi-statement-table-valued-functions-in-sql-server)
  - [**Difference Between Stored Procedures and Functions in SQL Server**](#difference-between-stored-procedures-and-functions-in-sql-server)
  - [**Joining of 3 Tables in SQL Server**](#joining-of-3-tables-in-sql-server)
  - [**Understanding SQL Triggers: Enhancing Database Functionality**](#understanding-sql-triggers-enhancing-database-functionality)
  - [**SQL Server Scoped DDL Triggers:**](#sql-server-scoped-ddl-triggers)
  - [**Setting Execution Order of Triggers in SQL:**](#setting-execution-order-of-triggers-in-sql)
  - [**GUID in SQL (Globally Unique Identifier):**](#guid-in-sql-globally-unique-identifier)
  - [**Composite Key or Composite Primary Key in SQL Server:**](#composite-key-or-composite-primary-key-in-sql-server)
  - [**Normalization in SQL:**](#normalization-in-sql)
  - [**Second Normal Form (2NF) - Normalization - Database Normalization**](#second-normal-form-2nf---normalization---database-normalization)
  - [**Third Normal Form (3NF) - Normalization - Database Normalization**](#third-normal-form-3nf---normalization---database-normalization)
  - [**String Functions In SQL Server - SQL String Functions - SQL Server**](#string-functions-in-sql-server---sql-string-functions---sql-server)
  - [**Indexes In SQL Server - SQL Index - Index In SQL - SQL Indexes - SQL**](#indexes-in-sql-server---sql-index---index-in-sql---sql-indexes---sql)
  - [**Clustered Index In SQL Server - Indexes In SQL - SQL Clustered Index - SQL Server**](#clustered-index-in-sql-server---indexes-in-sql---sql-clustered-index---sql-server)
  - [**Non-Clustered Index in SQL Server**](#non-clustered-index-in-sql-server)
  - [**B-Tree Structure of Index in SQL Server**](#b-tree-structure-of-index-in-sql-server)
  - [**Computed Columns or Calculated Columns in SQL**](#computed-columns-or-calculated-columns-in-sql)
  - [**Creating Index on Computed Column in SQL**](#creating-index-on-computed-column-in-sql)
  - [**Cube and Rollup Command in SQL Server:**](#cube-and-rollup-command-in-sql-server)
  - [**ROLLUP Command:**](#rollup-command)
  - [**Grouping Sets in SQL Server:**](#grouping-sets-in-sql-server)
  - [**MERGE Statement in SQL Server:**](#merge-statement-in-sql-server)
  - [**Transactions in SQL | ACID Properties in SQL:**](#transactions-in-sql--acid-properties-in-sql)
  - [**TRY CATCH or Error Handling in SQL Server:**](#try-catch-or-error-handling-in-sql-server)
  - [**TRANSACTIONS WITH TRY CATCH IN SQL SERVER**](#transactions-with-try-catch-in-sql-server)
  - [**TEMPORARY TABLES / LOCAL TEMPORARY TABLE IN SQL SERVER**](#temporary-tables--local-temporary-table-in-sql-server)
  - [**GLOBAL TEMPORARY TABLES IN SQL SERVER**](#global-temporary-tables-in-sql-server)
  - [**DIFFERENCE BETWEEN LOCAL AND GLOBAL TEMPORARY TABLES IN SQL SERVER**](#difference-between-local-and-global-temporary-tables-in-sql-server)
  - [**COALESCE FUNCTION IN SQL SERVER**](#coalesce-function-in-sql-server)
  - [**1. Coalesce vs. ISNULL Function in SQL Server:**](#1-coalesce-vs-isnull-function-in-sql-server)
  - [**2. CAST Function in SQL Server:**](#2-cast-function-in-sql-server)
  - [**3. CONVERT Function in SQL Server:**](#3-convert-function-in-sql-server)
  - [**Difference Between CAST and CONVERT:**](#difference-between-cast-and-convert)
  - [**5. Working With Cursors in SQL Server:**](#5-working-with-cursors-in-sql-server)
  - [**OVER CLAUSE WITH PARTITION BY IN SQL SERVER**](#over-clause-with-partition-by-in-sql-server)
  - [**Retrieving Last Generated Identity Column Value in SQL Server - Scope\_Identity VS @@identity**](#retrieving-last-generated-identity-column-value-in-sql-server---scope_identity-vs-identity)
  - [**Row\_Number Function In SQL Server - Row\_Number With Partition By Clause**](#row_number-function-in-sql-server---row_number-with-partition-by-clause)
  - [**Rank And Dense\_Rank Function In SQL Server - Rank VS Dense\_Rank In SQL Server**](#rank-and-dense_rank-function-in-sql-server---rank-vs-dense_rank-in-sql-server)
  - [**Cross Apply \& Outer Apply In SQL Server - Apply Operator in SQL Server**](#cross-apply--outer-apply-in-sql-server---apply-operator-in-sql-server)
  - [**CTE in SQL - Common Table Expression In SQL - SQL CTE - CTE In SQL Server**](#cte-in-sql---common-table-expression-in-sql---sql-cte---cte-in-sql-server)
  - [**Date \& Time Functions In SQL - SQL Date \& Time Functions**](#date--time-functions-in-sql---sql-date--time-functions)

## **Introduction to SQL Server - SQL Introduction**

SQL Server, developed by Microsoft, is a powerful relational database management system (RDBMS) widely used for storing and managing structured data. SQL (Structured Query Language) is the standard language used to interact with SQL Server and other relational databases. It provides a comprehensive set of features for data storage, retrieval, manipulation, and administration. SQL Server offers scalability, security, and high availability, making it suitable for various enterprise applications.

## **What Is Data, Database & Data Management in SQL**

- **Data**: In SQL, data refers to the information stored in a structured format within a database. It can include text, numbers, dates, and other types of information.
- **Database**: A database is a structured collection of data organized and stored for easy access, retrieval, and management. In SQL, databases consist of one or more tables, each containing rows and columns.
- **Data Management**: Data management in SQL involves tasks such as storing, retrieving, updating, and deleting data within a database. It also includes ensuring data integrity, security, and performance optimization.

## **What Is Database Entity in SQL Server - Entity in SQL - Database Entity in SQL**

- **Database Entity**: In SQL, an entity refers to a distinct object or concept that is represented in the database. It can be a person, place, thing, or event that has attributes (properties) describing its characteristics.
- **Entity in SQL Server**: In SQL Server, entities are typically represented as tables, where each row represents a unique instance of the entity, and each column represents an attribute of the entity.

## **Database Management System in SQL - SQL DBMS - RDBMS - SQL Server**

- **Database Management System (DBMS)**: A DBMS is a software application that facilitates the creation, organization, retrieval, and management of data in a database. SQL Server is an example of a DBMS.
- **Relational Database Management System (RDBMS)**: An RDBMS is a type of DBMS that organizes data into tables with rows and columns, and enforces relationships between them using keys. SQL Server follows the relational model, making it an RDBMS.

## **Database Models in SQL Server - Database Models - Relational Data Model - SQL**

- **Database Models**: Database models define the structure and organization of data within a database. Common database models include the relational model, hierarchical model, network model, and object-oriented model.
- **Relational Data Model**: The relational data model organizes data into tables (relations), where each table represents an entity, and each row represents a unique instance of that entity. Relationships between tables are established using keys.

## **RDBMS in SQL - Relational Database Management System in SQL - SQL**

- **RDBMS in SQL**: RDBMS stands for Relational Database Management System, which is a type of DBMS that stores data in a tabular form with rows and columns. SQL Server is an example of an RDBMS that follows the relational model.

## **How to Create Database & Tables in SQL Server - Creating Database & Tables in SQL**

- **Creating Database**: To create a database in SQL Server, you can use the `CREATE DATABASE` statement followed by the database name.
  Example: `CREATE DATABASE MyDatabase;`
- **Creating Tables**: To create a table in SQL Server, you can use the `CREATE TABLE` statement followed by the table name and column definitions.
  Example:

```
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50)
);
```
## **How to Insert Data in Table in SQL Server - Inserting Data in SQL Table - SQL**

- **Inserting Data**: To insert data into a table in SQL Server, you can use the `INSERT INTO` statement followed by the table name and values to be inserted.
  Example:

```
INSERT INTO Employees (EmployeeID, FirstName, LastName, Department)
VALUES (1, 'John', 'Doe', 'HR');
```

## **Update Command in SQL Server - Update with Set in SQL - SQL Server**

- **UPDATE Command**: The `UPDATE` command in SQL Server is used to modify existing records in a table.
  Example:

```
UPDATE Employees
SET Department = 'Finance'
WHERE EmployeeID = 1;
```

## **DELETE and TRUNCATE Command in SQL**

- **DELETE Command**: The `DELETE` command in SQL Server is used to remove one or more records from a table based on specified conditions.
  Example:

```
DELETE FROM Employees
WHERE EmployeeID = 1;
```

- **TRUNCATE Command**: The `TRUNCATE` command is used to remove all records from a table, but it does not log individual row deletions and is faster than the `DELETE` command.
  Example:

```
TRUNCATE TABLE Employees;
```

Each of these SQL topics provides essential functionality for managing data within SQL Server, and understanding them is crucial for effective database management and development.

## **1. UNIQUE and NOT NULL Constraints in SQL:**

In SQL, constraints are rules enforced on columns to maintain data integrity. The **UNIQUE** constraint ensures that all values in a column are unique, while the **NOT NULL** constraint ensures that a column cannot contain NULL values.

Example:
Consider a table named **Students** with columns **Student_ID**, **Student_Name**, and **Email**. We want to enforce that each student has a unique email address and that the email address cannot be NULL.

```sql
CREATE TABLE Students (
    Student_ID INT PRIMARY KEY,
    Student_Name VARCHAR(50),
    Email VARCHAR(100) UNIQUE NOT NULL
);
```

In this example, the **UNIQUE** constraint on the **Email** column ensures that each email address is unique, while the **NOT NULL** constraint ensures that the email address cannot be NULL.

## **2. PRIMARY KEY, DEFAULT, and CHECK Constraints in SQL Server:**

- **PRIMARY KEY**: A primary key uniquely identifies each record in a table. It automatically enforces the **UNIQUE** and **NOT NULL** constraints.
- **DEFAULT**: The **DEFAULT** constraint specifies a default value for a column if no value is provided during insertion.
- **CHECK**: The **CHECK** constraint enforces domain integrity by limiting the values that can be inserted into a column.

Example:

```sql
CREATE TABLE Employees (
    Employee_ID INT PRIMARY KEY,
    Employee_Name VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10, 2) DEFAULT 50000.00 CHECK (Salary >= 0)
);
```

In this example, the **Employee_ID** column serves as the primary key. The **Salary** column has a default value of $50,000 and a check constraint to ensure that it's non-negative.

## **3. SELECT Command in SQL Server:**

The **SELECT** statement is used to retrieve data from a database. It can select specific columns, perform calculations, filter rows, and join multiple tables.

Example:

```sql
SELECT * FROM Employees;
```

This statement selects all columns from the **Employees** table.

**4. Primary Key and Foreign Key Relationship in SQL:**

- **Primary Key**: A primary key uniquely identifies each record in a table.
- **Foreign Key**: A foreign key establishes a relationship between two tables. It refers to the primary key in another table.

Example:

```sql
CREATE TABLE Orders (
    Order_ID INT PRIMARY KEY,
    Customer_ID INT,
    Order_Date DATE,
    FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID)
);
```

In this example, the **Customer_ID** column in the **Orders** table is a foreign key referencing the **Customer_ID** column in the **Customers** table.

## **5. Cascading Referential Integrity Constraints in SQL Server:**

Cascading referential integrity constraints specify what actions should be taken when a referenced row in the parent table is updated or deleted.

- **CASCADE**: When a referenced row is updated or deleted, the corresponding rows in the child table are updated or deleted as well.
- **SET NULL**: When a referenced row is updated or deleted, the corresponding foreign key values in the child table are set to NULL.
- **SET DEFAULT**: When a referenced row is updated or deleted, the corresponding foreign key values in the child table are set to their default values.
- **NO ACTION**: Prevents the update or deletion of a referenced row if it has dependent rows in the child table.

Example:

```sql
CREATE TABLE Orders (
    Order_ID INT PRIMARY KEY,
    Customer_ID INT,
    Order_Date DATE,
    FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID) ON DELETE CASCADE
);
```

In this example, when a customer is deleted from the **Customers** table, all corresponding orders in the **Orders** table are also deleted due to the **CASCADE** option.

## **6. ALTER Command in SQL Server:**

The **ALTER** statement is used to modify existing database objects, such as tables, columns, or constraints.

Example:

```sql
ALTER TABLE Employees
ADD COLUMN Hire_Date DATE;
```

This statement adds a new column named **Hire_Date** to the **Employees** table.

## **7. Adding & Dropping SQL Constraints Using ALTER Command:**

Constraints can be added or dropped from existing tables using the **ALTER TABLE** statement.

Example:

```sql
ALTER TABLE Employees
ADD CONSTRAINT CHK_Salary CHECK (Salary >= 0);
```

This statement adds a **CHECK** constraint named **CHK_Salary** to the **Salary** column in the **Employees** table.

```sql
ALTER TABLE Employees
DROP CONSTRAINT CHK_Salary;
```

This statement drops the **CHK_Salary** constraint from the **Employees** table.

## **8. ALIAS in SQL Server:**

An alias is an alternative name given to a table or column in SQL queries to make the query more readable or to avoid naming conflicts.

Example:

```sql
SELECT e.Employee_ID, e.Employee_Name, d.Department_Name
FROM Employees e
JOIN Departments d ON e.Department_ID = d.Department_ID;
```

In this example, **e** is an alias for the **Employees** table, and **d** is an alias for the **Departments** table.

## **9. INNER JOIN in SQL Server:**

The **INNER JOIN** operation is used to combine rows from two or more tables based on a related column between them.

Example:

```sql
SELECT Orders.Order_ID, Customers.Customer_Name
FROM Orders
INNER JOIN Customers ON Orders.Customer_ID = Customers.Customer_ID;
```

This statement retrieves the order ID and customer name for each order by joining the **Orders** and **Customers** tables on the **Customer_ID** column.

## **LEFT JOIN, RIGHT JOIN & FULL OUTER JOIN IN SQL SERVER**

**Introduction:**

In SQL Server, joins are used to combine rows from two or more tables based on a related column between them. There are several types of joins, including LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN, each serving a specific purpose in retrieving data from multiple tables.

**1. LEFT JOIN:**

A LEFT JOIN returns all rows from the left table (the table specified before the JOIN keyword) and the matching rows from the right table (the table specified after the JOIN keyword). If there is no match, NULL values are returned for the columns from the right table.

**Syntax:**

```sql
SELECT columns
FROM left_table
LEFT JOIN right_table ON left_table.column = right_table.column;
```

**Example:**

Consider two tables: `orders` and `customers`. We want to retrieve all orders along with their corresponding customer information.

```sql
SELECT o.order_id, o.order_date, c.customer_name
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id;
```

In this example, the LEFT JOIN ensures that all orders are included in the result, even if there is no corresponding customer record.

**2. RIGHT JOIN:**

A RIGHT JOIN returns all rows from the right table and the matching rows from the left table. If there is no match, NULL values are returned for the columns from the left table.

**Syntax:**

```sql
SELECT columns
FROM left_table
RIGHT JOIN right_table ON left_table.column = right_table.column;
```

**Example:**

Using the same `orders` and `customers` tables, if we want to retrieve all customers along with their corresponding order information:

```sql
SELECT o.order_id, o.order_date, c.customer_name
FROM orders o
RIGHT JOIN customers c ON o.customer_id = c.customer_id;
```

Here, the RIGHT JOIN ensures that all customers are included in the result, even if there are no corresponding orders.

**3. FULL OUTER JOIN:**

A FULL OUTER JOIN returns all rows when there is a match in either the left or right table. If there is no match, NULL values are returned for the columns from the table without a matching row.

**Syntax:**

```sql
SELECT columns
FROM left_table
FULL OUTER JOIN right_table ON left_table.column = right_table.column;
```

**Example:**

Extending the example to include a FULL OUTER JOIN between `orders` and `customers`:

```sql
SELECT o.order_id, o.order_date, c.customer_name
FROM orders o
FULL OUTER JOIN customers c ON o.customer_id = c.customer_id;
```

This query retrieves all orders and customers, including those without matching records in the other table.

**Conclusion:**

In SQL Server, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN are powerful tools for combining data from multiple tables based on related columns. Understanding the differences and applications of these join types is essential for efficient data retrieval and analysis in database management.

## **SELF JOIN IN SQL SERVER**

**Introduction:**

A self-join in SQL Server is a join operation where a table is joined with itself. It is often used to compare rows within the same table or to retrieve hierarchical data stored in a table.

**Syntax:**

```sql
SELECT t1.column1, t2.column2
FROM table_name t1
JOIN table_name t2 ON t1.related_column = t2.related_column;
```

**Example:**

Consider a table named `employees` with columns `employee_id` and `manager_id`. We can use a self-join to retrieve the names of employees and their respective managers.

```sql
SELECT e.employee_name, m.employee_name AS manager_name
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id;
```

In this example, the self-join compares the `manager_id` of each employee with the `employee_id` of another employee to retrieve the manager's name for each employee.

**Conclusion:**

Self-joins are useful in SQL Server for comparing rows within the same table or retrieving hierarchical data. They allow for complex querying and analysis of data relationships within a single table.

## **IDENTITY OR AUTO INCREMENT IN SQL SERVER**

**Introduction:**

In SQL Server, the IDENTITY property is used to automatically generate unique numeric values for a column when new rows are inserted into a table. It is commonly used to create primary keys or surrogate keys in tables.

**Syntax:**

```sql
CREATE TABLE table_name
(
    column_name INT IDENTITY(1,1) PRIMARY KEY,
    ...
);
```

**Example:**

Consider a table named `students` where we want to automatically generate a unique ID for each student.

```sql
CREATE TABLE students
(
    student_id INT IDENTITY(1,1) PRIMARY KEY,
    student_name VARCHAR(50),
    ...
);
```

In this example, the `student_id` column will automatically increment by 1 for each new row inserted into the `students` table.

**Conclusion:**

The IDENTITY property in SQL Server simplifies the generation of unique numeric values for columns, such as primary keys, without the need for explicit value assignment. It enhances data integrity and simplifies database management tasks.

## **Union And Union All In SQL Server - SQL Union All Command - Union - Union All**

**Introduction:**

In SQL Server, UNION and UNION ALL are used to combine the results of two or more SELECT queries into a single result set. While both UNION and UNION ALL serve similar purposes, they have distinct differences in terms of handling duplicate rows.

**1. UNION:**

UNION combines the result sets of two or more SELECT statements and returns a single result set. Duplicate rows are automatically removed from the final result set.

**Syntax:**

```sql
SELECT columns
FROM table1
UNION
SELECT columns
FROM table2;
```

**Example:**

Consider two tables `students_2021` and `students_2022` with similar structures. We want to retrieve a list of all students from both tables without duplicates.

```sql
SELECT student_id, student_name
FROM students_2021
UNION
SELECT student_id, student_name
FROM students_2022;
```

In this example, the UNION operation combines the results of both SELECT queries and removes duplicate rows from the final result set.

**2. UNION ALL:**

UNION ALL also combines the result sets of two or more SELECT statements into a single result set. However, unlike UNION, UNION ALL retains all rows from the individual SELECT statements, including duplicates.

**Syntax:**

```sql
SELECT columns
FROM table1
UNION ALL
SELECT columns
FROM table2;
```

**Example:**

Using the same tables `students_2021` and `students_2022`, if we want to retrieve a list of all students from both tables including duplicates:

```sql
SELECT student_id, student_name
FROM students_2021
UNION ALL
SELECT student_id, student_name
FROM students_2022;
```

In this example, the UNION ALL operation combines the results of both SELECT queries and includes all rows from the individual tables, even if they are duplicates.

**Conclusion:**

UNION and UNION ALL are useful tools in SQL Server for combining the results of multiple SELECT queries into a single result set. Understanding the differences between UNION and UNION ALL is essential for selecting the appropriate operation based on the

specific requirements of the query.

## **Intersect And Except In SQL Server - SQL Intersect - SQL Except - Except - Intersect**

**Introduction:**

In SQL Server, INTERSECT and EXCEPT are set operations used to compare the results of two or more SELECT queries and return the common or distinct rows between them.

**1. INTERSECT:**

INTERSECT returns the common rows between two or more SELECT queries. It retrieves only the rows that appear in all the SELECT statements.

**Syntax:**

```sql
SELECT columns
FROM table1
INTERSECT
SELECT columns
FROM table2;
```

**Example:**

Consider two tables `students_math` and `students_physics` containing student names. We want to retrieve the names of students who are enrolled in both math and physics courses.

```sql
SELECT student_name
FROM students_math
INTERSECT
SELECT student_name
FROM students_physics;
```

In this example, the INTERSECT operation returns the names of students who appear in both `students_math` and `students_physics`.

**2. EXCEPT:**

EXCEPT returns the distinct rows that appear in the first SELECT query but not in the subsequent SELECT queries. It retrieves the rows that are unique to the first SELECT statement.

**Syntax:**

```sql
SELECT columns
FROM table1
EXCEPT
SELECT columns
FROM table2;
```

**Example:**

Using the same tables `students_math` and `students_physics`, if we want to retrieve the names of students enrolled in math but not in physics:

```sql
SELECT student_name
FROM students_math
EXCEPT
SELECT student_name
FROM students_physics;
```

In this example, the EXCEPT operation returns the names of students who are enrolled in `students_math` but not in `students_physics`.

**Conclusion:**

INTERSECT and EXCEPT are useful set operations in SQL Server for comparing the results of two or more SELECT queries and retrieving common or distinct rows between them. Understanding how to use INTERSECT and EXCEPT enables efficient data analysis and manipulation in database management.

## **Aggregate Functions in SQL Server:**

Aggregate functions in SQL Server are used to perform calculations on sets of values and return a single result. These functions operate on multiple rows of data and return a single result, such as sum, average, minimum, maximum, or count.

Examples of aggregate functions in SQL Server include:

- **SUM**: Calculates the sum of values in a column.
- **AVG**: Calculates the average value of a column.
- **MIN**: Returns the minimum value in a column.
- **MAX**: Returns the maximum value in a column.
- **COUNT**: Counts the number of rows in a result set.

```sql
-- Example: Calculate the total sales amount
SELECT SUM(sales_amount) AS total_sales
FROM sales_table;
```

## **Group By in SQL Server:**

The GROUP BY clause in SQL Server is used to group rows that have the same values into summary rows. It is often used with aggregate functions to perform calculations on each group separately.

```sql
-- Example: Calculate total sales amount for each product category
SELECT product_category, SUM(sales_amount) AS total_sales
FROM sales_table
GROUP BY product_category;
```

## **Having and Where Clause in SQL Server:**

The WHERE clause is used to filter rows from a result set based on a specified condition. It is used to restrict the number of rows returned by a query.

The HAVING clause, on the other hand, is used in conjunction with the GROUP BY clause to filter the groups based on a specified condition.

```sql
-- Example: Retrieve total sales amount for each product category with sales_amount greater than 1000
SELECT product_category, SUM(sales_amount) AS total_sales
FROM sales_table
GROUP BY product_category
HAVING SUM(sales_amount) > 1000;
```

## **Order By Command in SQL Server:**

The ORDER BY clause in SQL Server is used to sort the result set in ascending or descending order based on one or more columns.

```sql
-- Example: Retrieve employee records sorted by their salaries in descending order
SELECT employee_id, employee_name, salary
FROM employees
ORDER BY salary DESC;
```

## **Views in SQL Server:**

Views in SQL Server are virtual tables that are based on the result of a SELECT query. They are used to simplify complex queries, hide the complexity of underlying tables, and provide security by restricting access to certain columns.

```sql
-- Example: Create a view to display employee names and their departments
CREATE VIEW employee_department AS
SELECT employee_id, employee_name, department
FROM employees;
```

Views can also be used for performing INSERT, UPDATE, and DELETE operations in SQL Server, making them a powerful tool for data manipulation and management.

```sql
-- Example: Update employee department using a view
UPDATE employee_department
SET department = 'HR'
WHERE employee_id = 101;
```

To cover each topic briefly in 1000 paragraphs, we'll need to break down the explanation into small, digestible sections for each topic. Let's start with the explanation of each topic, providing examples where applicable:

## **LIKE Operator in SQL Server:**

The `LIKE` operator in SQL Server is used to search for a specified pattern within a column. It is particularly useful when you want to perform pattern matching rather than exact matching. The `LIKE` operator is often used with wildcard characters such as `%` (percent sign) and `_` (underscore).

Example:
Suppose we have a table named `Employees` with a column named `EmployeeName`. We want to retrieve all employees whose names start with "J". We can use the `LIKE` operator as follows:

```sql
SELECT *
FROM Employees
WHERE EmployeeName LIKE 'J%';
```

This query will return all employees whose names start with the letter "J".

## **Subquery in SQL Server:**

A subquery, also known as a nested query or inner query, is a query nested within another SQL statement such as SELECT, INSERT, UPDATE, or DELETE. Subqueries are enclosed within parentheses and can be used in various parts of a SQL statement, including the WHERE clause, FROM clause, HAVING clause, and SELECT clause.

Example:
Suppose we have two tables named `Orders` and `Customers`. We want to retrieve all orders made by customers from a specific city. We can use a subquery to achieve this:

```sql
SELECT *
FROM Orders
WHERE CustomerID IN (SELECT CustomerID FROM Customers WHERE City = 'New York');
```

This query retrieves all orders made by customers from the city of New York.

## **Scalar and Multi-Valued Subquery in SQL:**

- **Scalar Subquery:** A scalar subquery is a subquery that returns a single value. It can be used anywhere a single value is expected in a SQL statement, such as the SELECT list, WHERE clause, or HAVING clause.

Example:
Suppose we have a table named `Products` with a column named `Price`. We want to retrieve the highest price among all products. We can use a scalar subquery to achieve this:

```sql
SELECT MAX(Price)
FROM Products;
```

This query returns the highest price among all products.

- **Multi-Valued Subquery:** A multi-valued subquery is a subquery that returns multiple rows or values. It can be used in scenarios where you need to compare multiple values or retrieve multiple rows.

Example:
Suppose we have a table named `Employees` with columns `EmployeeID` and `Salary`. We want to retrieve all employees whose salary is greater than the average salary. We can use a multi-valued subquery to achieve this:

```sql
SELECT *
FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees);
```

This query retrieves all employees whose salary is greater than the average salary.

## **Self-Contained and Correlated Subquery in SQL Server:**

- **Self-Contained Subquery:** A self-contained subquery is a subquery that can be executed independently of the outer query. It does not reference columns from the outer query.

Example:
Suppose we have a table named `Products` with a column named `Price`. We want to retrieve all products whose price is higher than the average price of all products. We can use a self-contained subquery to achieve this:

```sql
SELECT *
FROM Products
WHERE Price > (SELECT AVG(Price) FROM Products);
```

This query retrieves all products whose price is higher than the average price.

- **Correlated Subquery:** A correlated subquery is a subquery that references columns from the outer query. It is executed for each row processed by the outer query.

Example:
Suppose we have two tables named `Orders` and `Customers`. We want to retrieve all customers along with the total number of orders they have placed. We can use a correlated subquery to achieve this:

```sql
SELECT CustomerID,
       (SELECT COUNT(*) FROM Orders WHERE Orders.CustomerID = Customers.CustomerID) AS TotalOrders
FROM Customers;
```

This query retrieves all customers along with the total number of orders each customer has placed.

## **BETWEEN, TOP, PERCENT, DISTINCT, and IN Operator in SQL Server:**

- **BETWEEN Operator:** The `BETWEEN` operator is used to retrieve values within a specified range.

Example:
Suppose we have a table named `Sales` with a column named `Amount`. We want to retrieve all sales amounts between $100 and $500. We can use the `BETWEEN` operator as follows:

```sql
SELECT *
FROM Sales
WHERE Amount BETWEEN 100 AND 500;
```

This query retrieves all sales amounts between $100 and $500.

- **TOP Operator:** The `TOP` operator is used to retrieve a specified number of records from the beginning of a result set.

Example:
Suppose we want to retrieve the top 5 highest-paid employees from the `Employees` table. We can use the `TOP` operator as follows:

```sql
SELECT TOP 5 *
FROM Employees
ORDER BY Salary DESC;
```

This query retrieves the top 5 highest-paid employees.

- **PERCENT Operator:** The `PERCENT` operator is used with the `TOP` operator to retrieve a specified percentage of records from a result set.

Example:
Suppose we want to retrieve the top 10% highest-paid employees from the `Employees` table. We can use the `TOP` operator with the `PERCENT` keyword as follows:

```sql
SELECT TOP 10 PERCENT *
FROM Employees
ORDER BY Salary DESC;
```

This query retrieves the top 10% highest-paid employees.

- **DISTINCT Operator:** The `DISTINCT` operator is used to remove duplicate rows from a result set.

Example:
Suppose we want to retrieve a list of unique cities from the `Customers` table. We can use the `DISTINCT` operator as follows:

```sql
SELECT DISTINCT City
FROM Customers;
```

This query retrieves a list of unique cities from the `Customers` table, removing any duplicate entries.

- **IN Operator:** The `IN` operator is used to specify multiple values in a WHERE clause.

Example:
Suppose we want to retrieve all orders from customers located in New York or Los Angeles. We can use the `IN` operator as follows:

```sql
SELECT *
FROM Orders
WHERE CustomerID IN (SELECT CustomerID FROM Customers WHERE City IN ('New York', 'Los Angeles'));
```

This query retrieves all orders from customers located in New York or Los Angeles.

## **Select Into Statement in SQL Server**

The **SELECT INTO** statement in SQL Server is used to create a new table based on the result set of a SELECT query. This statement allows you to quickly and easily create a backup copy of an existing table, or to create a new table with specific columns and data from an existing table.

**Syntax:**

```sql
SELECT column1, column2, ...
INTO new_table
FROM existing_table
WHERE condition;
```

**Explanation:**

- **column1, column2, ...**: Specifies the columns to be included in the new table.
- **new_table**: Specifies the name of the new table to be created.
- **existing_table**: Specifies the name of the existing table from which data will be selected.
- **condition**: Optional. Specifies a condition to filter the rows selected from the existing table.

**Example:**
Suppose we have an existing table named **Employees** with columns **EmployeeID**, **FirstName**, **LastName**, and **Salary**. We want to create a backup copy of this table called **Employees_Backup**:

```sql
SELECT *
INTO Employees_Backup
FROM Employees;
```

This statement creates a new table **Employees_Backup** with the same structure and data as the **Employees** table.

## **Insert Into with Select Statement in SQL Server**

The **INSERT INTO** statement in SQL Server is used to insert new rows into a table. When combined with a **SELECT** statement, it allows you to insert data into a table from the result set of a SELECT query.

**Syntax:**

```sql
INSERT INTO table_name (column1, column2, ...)
SELECT column1, column2, ...
FROM another_table
WHERE condition;
```

**Explanation:**

- **table_name**: Specifies the name of the table into which data will be inserted.
- **column1, column2, ...**: Specifies the columns into which data will be inserted.
- **another_table**: Specifies the name of the table from which data will be selected.
- **condition**: Optional. Specifies a condition to filter the rows selected from the another_table.

**Example:**
Suppose we have a table named **Sales** with columns **ProductID**, **ProductName**, **Quantity**, and **Price**. We want to insert data into a new table **HighSales** for products with a quantity greater than 100:

```sql
INSERT INTO HighSales (ProductID, ProductName, Quantity, Price)
SELECT ProductID, ProductName, Quantity, Price
FROM Sales
WHERE Quantity > 100;
```

This statement inserts data into the **HighSales** table from the **Sales** table for products with a quantity greater than 100.

## **Changing or Renaming Database Name and Table Name in SQL**

In SQL, changing or renaming a database name or table name can be achieved using the **ALTER** statement.

**Changing Database Name:**

```sql
ALTER DATABASE old_name MODIFY NAME = new_name;
```

**Explanation:**

- **old_name**: Specifies the current name of the database.
- **new_name**: Specifies the new name to be assigned to the database.

**Example:**

```sql
ALTER DATABASE MyDatabase MODIFY NAME = NewDatabase;
```

This statement changes the name of the database from **MyDatabase** to **NewDatabase**.

**Changing Table Name:**

```sql
ALTER TABLE old_table_name RENAME TO new_table_name;
```

**Explanation:**

- **old_table_name**: Specifies the current name of the table.
- **new_table_name**: Specifies the new name to be assigned to the table.

**Example:**

```sql
ALTER TABLE Employees RENAME TO Staff;
```

This statement changes the name of the table from **Employees** to **Staff**.

## **Stored Procedure in SQL Server**

A stored procedure in SQL Server is a precompiled collection of SQL statements and procedural logic that is stored in the database and can be executed as a single unit. Stored procedures allow you to encapsulate complex SQL queries and operations, improve performance, and enhance security.

**Syntax:**

```sql
CREATE PROCEDURE procedure_name
AS
BEGIN
    SQL statements;
END;
```

**Explanation:**

- **procedure_name**: Specifies the name of the stored procedure.
- **AS**: Indicates the beginning of the stored procedure definition.
- **SQL statements**: Specifies the SQL statements and procedural logic to be executed within the stored procedure.

**Example:**

```sql
CREATE PROCEDURE GetEmployees
AS
BEGIN
    SELECT * FROM Employees;
END;
```

This stored procedure named **GetEmployees** selects all records from the **Employees** table.

**Stored Procedure with Output Parameters in SQL Server**

In SQL Server, stored procedures can also have output parameters, which allow you to return values from the stored procedure to the calling program or script.

**Syntax:**

```sql
CREATE PROCEDURE procedure_name
    @param1 datatype,
    @param2 datatype OUTPUT
AS
BEGIN
    SQL statements;
    SET @param2 = value;
END;
```

**Explanation:**

- **@param1**: Specifies the input parameter of the stored procedure.
- **@param2**: Specifies the output parameter of the stored procedure.
- **datatype**: Specifies the data type of the parameters.
- **OUTPUT**: Indicates that the parameter is an output parameter.

**Example:**

```sql
CREATE PROCEDURE GetEmployeeName
    @EmployeeID INT,
    @EmployeeName VARCHAR(50) OUTPUT
AS
BEGIN
    SELECT @EmployeeName = FirstName + ' ' + LastName
    FROM Employees
    WHERE EmployeeID = @EmployeeID;
END;
```

This stored procedure named **GetEmployeeName** takes an **EmployeeID** as input and returns the corresponding **EmployeeName** as an output parameter.

In summary, the **SELECT INTO** and **INSERT INTO SELECT** statements in SQL Server facilitate the creation of new tables and the insertion of data from existing tables. Changing or renaming database and table names can be achieved using the **ALTER** statement. Stored procedures offer a convenient way to encapsulate SQL logic, while stored procedures with output parameters allow for the return of values from the procedure to the calling program or script. These features contribute to the flexibility, efficiency, and maintainability of database operations in SQL Server environments.

## **Functions in SQL Server**

SQL Server provides various types of functions to perform specific tasks and calculations within queries. These functions can be categorized into several types, including user-defined scalar functions, inline table-valued functions, and multi-statement table-valued functions.

**User-Defined Scalar Functions in SQL Server**

User-defined scalar functions are custom functions created by users to perform specific calculations or tasks and return a single scalar value. These functions can be called within SQL queries to simplify complex calculations or operations.

Example:

```sql
CREATE FUNCTION dbo.CalculateDiscount (@price DECIMAL(10,2), @discountRate DECIMAL(4,2))
RETURNS DECIMAL(10,2)
AS
BEGIN
    DECLARE @discountedPrice DECIMAL(10,2)
    SET @discountedPrice = @price - (@price * @discountRate / 100)
    RETURN @discountedPrice
END
```

Usage:

```sql
SELECT dbo.CalculateDiscount(100, 10) AS DiscountedPrice;
```

## **Inline Table-Valued Functions in SQL Server**

Inline table-valued functions return a table data type and can be used in the FROM clause of a SELECT statement. These functions accept parameters and return a table with multiple rows and columns.

Example:

```sql
CREATE FUNCTION dbo.GetEmployeesByDepartment (@departmentID INT)
RETURNS TABLE
AS
RETURN
(
    SELECT EmployeeID, FirstName, LastName
    FROM Employees
    WHERE DepartmentID = @departmentID
);
```

Usage:

```sql
SELECT * FROM dbo.GetEmployeesByDepartment(1);
```

## **Multi-Statement Table-Valued Functions in SQL Server**

Multi-statement table-valued functions return a table data type and are created using a BEGIN...END block to define the function body. These functions can contain multiple SQL statements and are useful for complex data processing logic.

Example:

```sql
CREATE FUNCTION dbo.GetEmployeesBySalaryRange (@minSalary DECIMAL(10,2), @maxSalary DECIMAL(10,2))
RETURNS @Employees TABLE
(
    EmployeeID INT,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50)
)
AS
BEGIN
    INSERT INTO @Employees (EmployeeID, FirstName, LastName)
    SELECT EmployeeID, FirstName, LastName
    FROM Employees
    WHERE Salary BETWEEN @minSalary AND @maxSalary;

    RETURN;
END
```

Usage:

```sql
SELECT * FROM dbo.GetEmployeesBySalaryRange(50000, 100000);
```

## **Difference Between Stored Procedures and Functions in SQL Server**

Stored procedures and functions serve different purposes in SQL Server.

- **Stored Procedures**:

  - Stored procedures are reusable blocks of SQL code that can perform various tasks, such as data manipulation, transaction management, and business logic processing.
  - They can contain DML and DDL statements, and they can execute other stored procedures.
  - Stored procedures cannot be used in a SELECT statement directly to return a result set.

- **Functions**:
  - Functions are used to encapsulate specific logic and calculations that return a single value (scalar function) or a table (table-valued function).
  - They cannot contain DML statements that modify data, but they can be used in SELECT statements to return data.
  - Functions cannot execute other functions or stored procedures.

## **Joining of 3 Tables in SQL Server**

Joining three tables in SQL Server involves combining rows from three different tables based on a related column or columns. This is commonly done using INNER JOIN, LEFT JOIN, or other types of joins to retrieve data from multiple tables simultaneously.

Example:

```sql
SELECT Orders.OrderID, Customers.CustomerName, Products.ProductName
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID;
```

In this example, we are joining the **Orders**, **Customers**, and **Products** tables to retrieve data about orders, customers, and products. The **Orders** table is linked to the **Customers** table by the **CustomerID** column, and the **OrderDetails** table is linked to the **Products** table by the **ProductID** column. By joining these tables, we can retrieve information about which customer placed each order and which products were included in each order.

## **Understanding SQL Triggers: Enhancing Database Functionality**

SQL triggers are powerful database objects that automatically execute in response to specified events occurring in the database. They provide a way to enforce business rules, maintain data integrity, and automate tasks without the need for manual intervention. In this comprehensive guide, we'll explore different types of SQL triggers, including DML triggers and DDL triggers, along with practical examples to illustrate their usage.

**DML Triggers in SQL:**

DML (Data Manipulation Language) triggers in SQL execute automatically in response to DML events, such as INSERT, UPDATE, and DELETE operations performed on a table. They are useful for enforcing data integrity rules, auditing changes, and implementing complex business logic. Let's consider an example of an AFTER INSERT trigger:

```sql
CREATE TRIGGER AfterInsertTrigger
AFTER INSERT ON Employees
FOR EACH ROW
BEGIN
    INSERT INTO AuditLog (Action, TableName, RecordID)
    VALUES ('INSERT', 'Employees', NEW.EmployeeID);
END;
```

In this example, the trigger is fired after each new row is inserted into the Employees table. It logs the action (INSERT), table name, and the ID of the inserted record into an AuditLog table.

**DML Instead Of Triggers in SQL:**

DML Instead Of triggers in SQL allow you to intercept and handle DML operations on views. Unlike regular DML triggers, Instead Of triggers are fired instead of the actual DML operation, giving you full control over the process. Let's illustrate this with an example of an Instead Of Delete trigger on a view:

```sql
CREATE TRIGGER InsteadOfDeleteTrigger
INSTEAD OF DELETE ON EmployeeView
BEGIN
    UPDATE EmployeeStatus
    SET Status = 'Inactive'
    WHERE EmployeeID = OLD.EmployeeID;
END;
```

In this example, the trigger is fired instead of a DELETE operation on the EmployeeView view. It updates the status of the corresponding employee in the EmployeeStatus table to 'Inactive' instead of actually deleting the record.

**DDL Triggers in SQL Server:**

DDL (Data Definition Language) triggers in SQL Server execute in response to DDL events, such as CREATE, ALTER, and DROP operations performed on database objects. They are useful for enforcing database policies, auditing schema changes, and controlling access to database objects. Let's see an example of a DDL trigger that logs schema changes:

```sql
CREATE TRIGGER SchemaChangeTrigger
ON DATABASE
FOR CREATE_TABLE, ALTER_TABLE, DROP_TABLE
AS
BEGIN
    INSERT INTO SchemaChangeLog (EventType, ObjectName, EventDate)
    VALUES (EVENTDATA().value('(/EVENT_INSTANCE/EventType)[1]', 'nvarchar(max)'),
            EVENTDATA().value('(/EVENT_INSTANCE/ObjectName)[1]', 'nvarchar(max)'),
            GETDATE());
END;
```

In this example, the trigger captures information about schema changes (CREATE, ALTER, DROP TABLE) using the EVENTDATA function and inserts it into a SchemaChangeLog table along with the current date.

## **SQL Server Scoped DDL Triggers:**

SQL Server Scoped DDL triggers are a type of DDL trigger introduced in SQL Server 2016, which allows you to scope the trigger to specific events or objects within a database. Scoped DDL triggers provide more granular control over triggering actions, making them more efficient and easier to manage. Let's demonstrate this with an example of a scoped DDL trigger:

```sql
CREATE TRIGGER TableAlterTrigger
ON DATABASE
AFTER ALTER_TABLE
AS
BEGIN
    PRINT 'A table was altered in the database.';
END;
```

In this example, the trigger is scoped to the ALTER_TABLE event, meaning it will only fire after an ALTER TABLE operation is performed in the database.

**Conclusion:**

SQL triggers, including DML triggers, DML Instead Of triggers, and DDL triggers, are powerful tools for automating tasks, enforcing data integrity, and auditing changes in SQL databases. By understanding their functionalities and usage scenarios, database administrators and developers can effectively leverage triggers to enhance database functionality and maintain data consistency and integrity. Whether it's enforcing business rules, auditing changes, or controlling schema modifications, SQL triggers play a vital role in database management and maintenance.

## **Setting Execution Order of Triggers in SQL:**

Triggers in SQL are special types of stored procedures that automatically execute in response to certain database events, such as INSERT, UPDATE, or DELETE operations on a table. When multiple triggers are defined on a table, it's important to specify their execution order to ensure that they are executed in the desired sequence. The execution order can be crucial for maintaining data integrity and consistency within the database.

To set the execution order of triggers in SQL, you can use the sp_settriggerorder system stored procedure in SQL Server. This procedure allows you to specify the order in which triggers associated with a particular table should execute. You can specify whether a trigger should execute before or after another trigger, as well as the relative position of the trigger within the execution sequence.

Example:

Suppose we have a table named "Employees" with triggers defined to enforce certain business rules. We want to ensure that the trigger to update the "LastModified" column is executed before the trigger to calculate the total salary of employees. We can set the execution order of triggers using the sp_settriggerorder procedure as follows:

```sql
-- Set execution order of triggers for the Employees table
EXEC sp_settriggerorder @triggername = 'UpdateLastModifiedTrigger', @order = 'First', @stmttype = 'UPDATE', @namespace = 'DATABASE'
EXEC sp_settriggerorder @triggername = 'CalculateTotalSalaryTrigger', @order = 'Last', @stmttype = 'UPDATE', @namespace = 'DATABASE'
```

In this example, the trigger named "UpdateLastModifiedTrigger" will execute first before any other triggers associated with UPDATE statements on the "Employees" table. Conversely, the trigger named "CalculateTotalSalaryTrigger" will execute last after all other triggers associated with UPDATE statements on the same table.

By setting the execution order of triggers in SQL, you can ensure that they are executed in the desired sequence, thereby maintaining data consistency and integrity within the database.

## **GUID in SQL (Globally Unique Identifier):**

GUID, or Globally Unique Identifier, is a data type used to represent a unique identifier in SQL databases. A GUID is a 128-bit integer value that is generated using algorithms designed to ensure uniqueness across different systems and databases. GUIDs are often used as primary keys in database tables, especially in distributed or replicated database environments where unique identification is crucial.

Example:

Suppose we have a table named "Customers" with a column named "CustomerID" that stores GUID values as primary keys. Each time a new customer is added to the database, a new GUID value is generated and assigned to the "CustomerID" column.

```sql
CREATE TABLE Customers (
    CustomerID UNIQUEIDENTIFIER PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100)
);

INSERT INTO Customers (CustomerID, FirstName, LastName, Email)
VALUES (NEWID(), 'John', 'Doe', 'john.doe@example.com');
```

In this example, the NEWID() function is used to generate a new GUID value, which is then inserted into the "CustomerID" column of the "Customers" table. Each customer record in the table will have a unique GUID value as its identifier.

GUIDs offer several advantages over other types of identifiers, such as integers or strings. They are globally unique, meaning that the probability of generating duplicate values is extremely low. Additionally, GUIDs do not rely on a centralized authority for generation, making them suitable for distributed database environments.

## **Composite Key or Composite Primary Key in SQL Server:**

A composite key, also known as a composite primary key, is a combination of two or more columns that uniquely identifies each row in a database table. Unlike a single-column primary key, which consists of only one column, a composite key consists of multiple columns. Composite keys are often used when no single column can uniquely identify each row in a table, but the combination of multiple columns can.

Example:

Suppose we have a table named "Orders" that stores information about customer orders. Each order is uniquely identified by a combination of the "OrderID" and "CustomerID" columns.

```sql
CREATE TABLE Orders (
    OrderID INT,
    CustomerID INT,
    OrderDate DATE,
    PRIMARY KEY (OrderID, CustomerID)
);
```

In this example, the combination of the "OrderID" and "CustomerID" columns forms a composite primary key for the "Orders" table. Together, these columns uniquely identify each order in the table.

Composite keys offer several advantages, including:

1. **Uniqueness**: By combining multiple columns, composite keys ensure that each row in a table is uniquely identified.
2. **Data Integrity**: Composite keys help maintain data integrity by preventing duplicate entries in the table.
3. **Query Optimization**: Composite keys can improve query performance by allowing for more efficient indexing and retrieval of data.

However, composite keys can also have drawbacks, such as increased complexity and reduced readability of the database schema. Care should be taken when designing composite keys to ensure that they effectively meet the requirements of the application.

## **Normalization in SQL:**

Normalization is the process of organizing data in a database to reduce redundancy and dependency. It involves breaking down large tables into smaller, more manageable tables and establishing relationships between them. Normalization helps ensure data integrity, minimize data duplication, and improve database efficiency.

There are several levels of normalization, each building upon the principles of the previous level. The most commonly used normalization forms are:

1. **First Normal Form (1NF)**: In 1NF, each attribute in a table must have a single value, and each column must be atomic. There should be no repeating groups or arrays within the table.

Example:

Consider a table named "Students" with a column named "PhoneNumbers" that stores multiple phone numbers for each student.

```sql
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    PhoneNumbers VARCHAR(100)
);
```

To normalize this table to 1NF, we split the "PhoneNumbers" column into separate rows in a new table named "StudentPhoneNumbers".

```sql
CREATE TABLE StudentPhoneNumbers (
    StudentID INT,
    PhoneNumber VARCHAR(20),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);
```

By splitting the multi-valued attribute into separate rows, we ensure that each attribute in the table has a single value, thus satisfying the requirements of 1NF.

Normalization is an iterative process that involves progressively organizing data into higher normal forms, such as Second Normal Form (2NF), Third Normal Form (3NF), Boyce-Codd Normal Form (BCNF), and Fourth Normal Form (4NF). Each normalization form eliminates specific types of data redundancy and dependency, resulting in a more efficient and maintainable database schema.

## **Second Normal Form (2NF) - Normalization - Database Normalization**

**Introduction:**
In database normalization, Second Normal Form (2NF) is a crucial concept aimed at reducing data redundancy and ensuring data integrity. It builds upon the First Normal Form (1NF) by eliminating partial dependencies within a relation.

**Explanation:**
To achieve 2NF, a relation must meet the following criteria:

1. It must already be in 1NF.
2. All non-prime attributes (attributes not part of the primary key) must be fully functionally dependent on the entire primary key.

**Example:**
Consider a relation representing a library's book borrowing system:

| Book_ID | Title                   | Author              | Genre     | Borrower_ID | Borrower_Name  |
| ------- | ----------------------- | ------------------- | --------- | ----------- | -------------- |
| 1       | "To Kill a Mockingbird" | Harper Lee          | Fiction   | 101         | John Doe       |
| 2       | "1984"                  | George Orwell       | Dystopian | 102         | Jane Smith     |
| 3       | "The Great Gatsby"      | F. Scott Fitzgerald | Fiction   | 103         | Robert Johnson |

In this relation:

- {Book_ID} is the primary key.
- Borrower_ID uniquely identifies the borrower.
- Borrower_Name is functionally dependent on Borrower_ID, not on the entire primary key.

To normalize to 2NF, we split the relation into two:

**Books Table:**
| Book_ID | Title | Author | Genre |
|---------|----------------|--------------|-----------|
| 1 | "To Kill a Mockingbird" | Harper Lee | Fiction |
| 2 | "1984" | George Orwell| Dystopian |
| 3 | "The Great Gatsby" | F. Scott Fitzgerald | Fiction |

**Borrowers Table:**
| Borrower_ID | Borrower_Name |
|-------------|---------------|
| 101 | John Doe |
| 102 | Jane Smith |
| 103 | Robert Johnson|

Now, Borrower_Name is fully functionally dependent on Borrower_ID, and the relation is in 2NF.

**Conclusion:**
Second Normal Form (2NF) ensures that all non-prime attributes are fully functionally dependent on the primary key, reducing data redundancy and anomalies in the database schema. It lays the foundation for higher levels of normalization, such as Third Normal Form (3NF).

---

## **Third Normal Form (3NF) - Normalization - Database Normalization**

**Introduction:**
Third Normal Form (3NF) is a crucial step in database normalization, aiming to further reduce data redundancy and dependency by eliminating transitive dependencies within a relation.

**Explanation:**
To achieve 3NF, a relation must meet the following criteria:

1. It must already be in 2NF.
2. All non-prime attributes must be non-transitively dependent on the primary key. In other words, there should be no dependencies between non-prime attributes.

**Example:**
Continuing with our library's book borrowing system example:

**Books Table:**
| Book_ID | Title | Author | Genre |
|---------|----------------|--------------|-----------|
| 1 | "To Kill a Mockingbird" | Harper Lee | Fiction |
| 2 | "1984" | George Orwell| Dystopian |
| 3 | "The Great Gatsby" | F. Scott Fitzgerald | Fiction |

**Borrowers Table:**
| Borrower_ID | Borrower_Name |
|-------------|---------------|
| 101 | John Doe |
| 102 | Jane Smith |
| 103 | Robert Johnson|

**Borrowings Table:**
| Borrowing_ID | Book_ID | Borrower_ID | Date_Borrowed |
|--------------|---------|-------------|---------------|
| 1 | 1 | 101 | 2022-01-10 |
| 2 | 2 | 102 | 2022-02-15 |
| 3 | 3 | 103 | 2022-03-20 |

In this relation:

- {Borrowing_ID} is the primary key.
- Book_ID and Borrower_ID are functionally dependent on Borrowing_ID.
- Date_Borrowed is functionally dependent on Borrowing_ID.

To normalize to 3NF, we split the relation into two:

**Borrowings Table:**
| Borrowing_ID | Book_ID | Borrower_ID | Date_Borrowed |
|--------------|---------|-------------|---------------|
| 1 | 1 | 101 | 2022-01-10 |
| 2 | 2 | 102 | 2022-02-15 |
| 3 | 3 | 103 | 2022-03-20 |

**Books Borrowed Table:**
| Borrowing_ID | Book_ID | Borrower_ID |
|--------------|---------|-------------|
| 1 | 1 | 101 |
| 2 | 2 | 102 |
| 3 | 3 | 103 |

**Dates Borrowed Table:**
| Borrowing_ID | Date_Borrowed |
|--------------|---------------|
| 1 | 2022-01-10 |
| 2 | 2022-02-15 |
| 3 | 2022-03-20 |

Now, each relation is in 3NF, and there are no transitive dependencies between non-prime attributes.

**Conclusion:**
Third Normal Form (3NF) ensures that there are no transitive dependencies between non-prime attributes, further reducing data redundancy and dependency in the database schema. It enhances data integrity and facilitates efficient data retrieval and manipulation.

---

## **String Functions In SQL Server - SQL String Functions - SQL Server**

**Introduction:**
String functions in SQL Server are a set of built-in functions designed to manipulate and operate on string data types (such as VARCHAR, NVARCHAR, etc.). These functions offer various capabilities, including string manipulation, formatting, searching, and comparison.

**Common SQL Server String Functions:**

1. **LEN():** Returns the length of a string.
2. **LEFT():** Returns the left part of a string with a specified number of characters.
3. **RIGHT():** Returns the right part of a string with a specified number of characters.
4. **SUBSTRING():** Returns a part of a string based on a specified starting position and length.
5. **CONCAT():** Concatenates two or more strings together.
6. **LOWER():** Converts a string to lowercase.
7. **UPPER():** Converts a string to uppercase.
8. **REPLACE():** Replaces all occurrences of a specified substring within a string with another substring.
9. **CHARINDEX():** Returns the starting position of a substring within a string.
10. **LTRIM():** Removes leading spaces from a string.
11. **RTRIM():** Removes trailing spaces from a string.

**Example:**
Consider a table named "Employees" with columns "First_Name" and "Last_Name":

| First_Name | Last_Name |
| ---------- | --------- |

|

John | Doe |
| Jane | Smith |
| Robert | Johnson |

Let's demonstrate the usage of some SQL Server string functions:

1. **LEN():**

   ```sql
   SELECT LEN(First_Name) AS FirstNameLength FROM Employees;
   ```

   Output:

   ```
   FirstNameLength
   ---------------
   4
   4
   6
   ```

2. **CONCAT():**

   ```sql
   SELECT CONCAT(First_Name, ' ', Last_Name) AS Full_Name FROM Employees;
   ```

   Output:

   ```
   Full_Name
   ---------------
   John Doe
   Jane Smith
   Robert Johnson
   ```

3. **UPPER():**
   ```sql
   SELECT UPPER(Last_Name) AS UppercaseLastName FROM Employees;
   ```
   Output:
   ```
   UppercaseLastName
   -----------------
   DOE
   SMITH
   JOHNSON
   ```

**Conclusion:**
SQL Server string functions offer powerful tools for manipulating and operating on string data within SQL queries. By leveraging these functions, developers can perform a wide range of string-related operations efficiently and effectively, enhancing the flexibility and functionality of SQL queries.

---

## **Indexes In SQL Server - SQL Index - Index In SQL - SQL Indexes - SQL**

**Introduction:**
Indexes in SQL Server are database objects designed to improve query performance by enabling efficient data retrieval. They work similarly to indexes in books, allowing SQL Server to quickly locate specific rows within a table.

**Types of Indexes in SQL Server:**

1. **Clustered Index:** Organizes data rows in the table based on the index key columns. Each table can have only one clustered index, and the order of data in the table is determined by the clustered index.
2. **Non-Clustered Index:** Stores a separate copy of the index key columns and a pointer to the actual data rows. Unlike clustered indexes, tables can have multiple non-clustered indexes.

**Example:**
Consider a table named "Employees" with columns "Employee_ID" and "Last_Name":

| Employee_ID | Last_Name |
| ----------- | --------- |
| 101         | Doe       |
| 102         | Smith     |
| 103         | Johnson   |

Let's create indexes on the "Last_Name" column:

1. **Clustered Index:**

   ```sql
   CREATE CLUSTERED INDEX IX_LastName ON Employees(Last_Name);
   ```

2. **Non-Clustered Index:**
   ```sql
   CREATE NONCLUSTERED INDEX IX_LastName ON Employees(Last_Name);
   ```

**Usage:**
With the indexes in place, SQL Server can quickly locate rows based on the indexed column(s). For example, when searching for an employee with the last name "Smith", SQL Server can utilize the index to perform a quick lookup, resulting in improved query performance.

**Conclusion:**
Indexes play a vital role in optimizing query performance in SQL Server by enabling fast data retrieval. By strategically creating and utilizing indexes, developers can enhance the efficiency and scalability of SQL queries, ultimately improving the overall performance of database applications.

---

## **Clustered Index In SQL Server - Indexes In SQL - SQL Clustered Index - SQL Server**

**Introduction:**
A clustered index in SQL Server is a type of index that organizes the data rows in the table based on the indexed column(s). Unlike non-clustered indexes, which store a separate copy of the index key columns, a clustered index determines the physical order of data in the table.

**Usage Scenarios:**
Clustered indexes are commonly used in scenarios where:

1. **Range Queries:** Queries that retrieve a range of values benefit from clustered indexes, as the data is physically stored in sorted order based on the index key columns.

2. **Frequently Accessed Data:** Data that is frequently accessed or queried benefits from clustered indexes, as they provide faster data retrieval compared to scanning the entire table.

**Example:**
Consider a table named "Orders" with columns "Order_ID" and "Order_Date":

| Order_ID | Order_Date |
| -------- | ---------- |
| 101      | 2022-01-10 |
| 102      | 2022-02-15 |
| 103      | 2022-03-20 |

Let's create a clustered index on the "Order_Date" column:

```sql
CREATE CLUSTERED INDEX IX_OrderDate ON Orders(Order_Date);
```

**Impact:**
With the clustered index in place, the data rows in the "Orders" table are physically organized based on the "Order_Date" column. This means that SQL Server can quickly locate and retrieve data rows based on the order date, resulting in improved query performance for date-based queries.

**Conclusion:**
Clustered indexes in SQL Server play a critical role in optimizing query performance by organizing data rows based on the indexed column(s). By leveraging clustered indexes, developers can improve the efficiency and scalability of SQL queries, particularly in scenarios involving range queries and frequently accessed data.

---

**In Conclusion:**
In this extensive exploration, we covered several critical topics in database management and SQL Server, including normalization, string functions, and indexes. Each topic plays a pivotal role in ensuring efficient data management, query optimization, and overall database performance. By understanding and applying these concepts effectively, database developers and administrators can build robust and scalable database systems that meet the demands of modern applications.

## **Non-Clustered Index in SQL Server**

In SQL Server, an index is a structure that helps to improve the performance of queries by enabling quick retrieval of data from tables. A **non-clustered index** is one of the two types of indexes in SQL Server, the other being a clustered index. Unlike a clustered index, which physically sorts the data rows within the table, a non-clustered index creates a separate structure that points to the physical location of the data. This allows for faster retrieval of data based on the indexed columns.

**Example:**

Consider a table named `Employee` with columns `EmployeeID`, `FirstName`, `LastName`, and `DepartmentID`. Let's create a non-clustered index on the `LastName` column:

```sql
CREATE NONCLUSTERED INDEX IX_LastName ON Employee(LastName);
```

In this example, `IX_LastName` is the name of the non-clustered index, and `LastName` is the column on which the index is created. This index will improve the performance of queries that involve searching or sorting based on the `LastName` column.

**Unique & Non-Unique Indexes in SQL Server**

In SQL Server, indexes can be classified as either **unique** or **non-unique**. A **unique index** ensures that the indexed columns contain unique values, meaning that no two rows in the table can have the same combination of values for the indexed columns. On the other hand, a **non-unique index** allows duplicate values in the indexed columns.

**Example:**

Let's create a unique index on the `EmployeeID` column of the `Employee` table:

```sql
CREATE UNIQUE INDEX IX_EmployeeID ON Employee(EmployeeID);
```

This index ensures that each `EmployeeID` in the `Employee` table is unique, preventing duplicate entries for the `EmployeeID` column.

## **B-Tree Structure of Index in SQL Server**

In SQL Server, indexes are typically implemented using a **B-tree** (balanced tree) structure. A B-tree is a self-balancing tree data structure that maintains sorted data and allows for efficient search, insertion, and deletion operations. In the context of indexes, each node in the B-tree contains a range of key values and pointers to child nodes, allowing for quick traversal and retrieval of data.

**Example:**

Consider a B-tree index on the `EmployeeID` column of the `Employee` table. The B-tree structure organizes the index entries in a hierarchical manner, with each level of the tree representing a range of key values. This allows SQL Server to efficiently locate the desired data based on the indexed column.

## **Computed Columns or Calculated Columns in SQL**

In SQL Server, a **computed column** (also known as a **calculated column**) is a column whose values are derived from the values of other columns in the same table. The value of a computed column is computed dynamically based on an expression defined by the user.

**Example:**

Suppose we have a table named `Order` with columns `Quantity` and `UnitPrice`. We can create a computed column named `TotalPrice` that calculates the total price of each order:

```sql
ALTER TABLE Order
ADD TotalPrice AS (Quantity * UnitPrice);
```

In this example, the `TotalPrice` column is a computed column whose value is automatically calculated as the product of the `Quantity` and `UnitPrice` columns.

## **Creating Index on Computed Column in SQL**

In SQL Server, it is possible to create an index on a computed column to improve the performance of queries that involve the computed column. However, the computed column must be deterministic and precise to be eligible for indexing. Deterministic means that the computed column's value must be the same for a given set of input values, and precise means that the computed column's value must not be approximate or contain floating-point arithmetic.

**Example:**

Let's create an index on the `TotalPrice` computed column in the `Order` table:

```sql
CREATE INDEX IX_TotalPrice ON Order(TotalPrice);
```

This index will improve the performance of queries that involve filtering, sorting, or searching based on the `TotalPrice` computed column in the `Order` table.

In summary, non-clustered indexes, unique and non-unique indexes, the B-tree structure of indexes, computed columns, and creating indexes on computed columns are all important concepts in SQL Server that play a crucial role in optimizing database performance and query efficiency. Understanding these concepts and knowing when and how to use them effectively is essential for database developers and administrators.

## **Cube and Rollup Command in SQL Server:**

In SQL Server, the **CUBE** and **ROLLUP** commands are used for multi-dimensional analysis of data. They are particularly useful for generating aggregated results across multiple dimensions in a single query.

**CUBE Command:**
The CUBE command generates all possible grouping sets for a specified list of columns. It produces a result set that includes aggregates for all combinations of columns specified in the query.

Example:
Suppose we have a table named `Sales` with columns `Region`, `Product`, and `Year`, and we want to analyze the total sales amount for each combination of region, product, and year. We can use the CUBE command as follows:

```sql
SELECT Region, Product, Year, SUM(SalesAmount) AS TotalSales
FROM Sales
GROUP BY CUBE (Region, Product, Year);
```

This query will generate aggregated results for all possible combinations of `Region`, `Product`, and `Year`, providing a comprehensive analysis of sales data.

## **ROLLUP Command:**
The ROLLUP command generates subtotal aggregates for a specified list of columns, producing a result set with hierarchical subtotals.

Example:
Continuing with the previous example, if we want to generate subtotal aggregates for `Region` and `Year`, ignoring the `Product` dimension, we can use the ROLLUP command as follows:

```sql
SELECT Region, Product, Year, SUM(SalesAmount) AS TotalSales
FROM Sales
GROUP BY ROLLUP (Region, Year);
```

This query will generate subtotals for each unique combination of `Region` and `Year`, providing a hierarchical summary of sales data.

## **Grouping Sets in SQL Server:**

In SQL Server, **GROUPING SETS** allow you to specify multiple grouping sets within a single query, enabling you to generate aggregated results for different combinations of columns.

Example:
Using the same `Sales` table, if we want to generate aggregated results separately for `Region`, `Product`, and `Year`, as well as for combinations of `Region` and `Product`, we can use GROUPING SETS as follows:

```sql
SELECT Region, Product, Year, SUM(SalesAmount) AS TotalSales
FROM Sales
GROUP BY GROUPING SETS ((Region), (Product), (Year), (Region, Product));
```

This query will generate aggregated results for each specified grouping set, providing a versatile analysis of sales data.

## **MERGE Statement in SQL Server:**

The **MERGE** statement in SQL Server allows you to perform multiple DML (Data Manipulation Language) operations (INSERT, UPDATE, DELETE) in a single atomic operation, based on a specified condition.

Example:
Suppose we have two tables, `TargetTable` and `SourceTable`, and we want to synchronize the data between them based on a common key `ID`. We can use the MERGE statement as follows:

```sql
MERGE INTO TargetTable AS Target
USING SourceTable AS Source
ON Target.ID = Source.ID
WHEN MATCHED THEN
    UPDATE SET Target.Column1 = Source.Column1, Target.Column2 = Source.Column2
WHEN NOT MATCHED BY TARGET THEN
    INSERT (ID, Column1, Column2) VALUES (Source.ID, Source.Column1, Source.Column2)
WHEN NOT MATCHED BY SOURCE THEN
    DELETE;
```

This MERGE statement will update existing records in `TargetTable` with corresponding records from `SourceTable`, insert new records into `TargetTable` for records in `SourceTable` that do not exist in `TargetTable`, and delete records from `TargetTable` that do not exist in `SourceTable`.

## **Transactions in SQL | ACID Properties in SQL:**

In SQL, a **transaction** is a unit of work that is performed as a single logical operation, consisting of one or more SQL statements. Transactions ensure data integrity and consistency by following the ACID properties:

1. **Atomicity**: Ensures that either all the operations within a transaction are completed successfully, or none of them are. If any operation fails, the entire transaction is rolled back to its original state.

2. **Consistency**: Guarantees that the database remains in a consistent state before and after the transaction. All integrity constraints, such as foreign key relationships and check constraints, are enforced during the transaction.

3. **Isolation**: Ensures that the intermediate state of the transaction is invisible to other transactions until it is committed. Transactions are executed in isolation from each other to prevent interference and maintain data consistency.

4. **Durability**: Ensures that the changes made by a committed transaction are permanently saved and will not be lost, even in the event of a system failure. Committed changes are stored in non-volatile memory, such as disk storage, to ensure durability.

Example:
Suppose we want to transfer funds from one bank account to another. The transaction would involve deducting the specified amount from the source account and crediting it to the destination account. If any step fails (e.g., insufficient funds), the entire transaction is rolled back, ensuring that the accounts remain in a consistent state.

## **TRY CATCH or Error Handling in SQL Server:**

In SQL Server, the **TRY CATCH** construct is used for error handling, allowing you to gracefully handle exceptions that occur during the execution of SQL statements.

Example:
Suppose we have a stored procedure named `usp_InsertData` that inserts data into a table. We can use the TRY CATCH construct to handle any errors that may occur during the execution of the stored procedure:

```sql
CREATE PROCEDURE usp_InsertData
AS
BEGIN
    BEGIN TRY
        -- Start the transaction
        BEGIN TRANSACTION;

        -- Insert data into the table
        INSERT INTO TableName (Column1, Column2) VALUES (Value1, Value2);

        -- Commit the transaction
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        -- Rollback the transaction if an error occurs
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;

        -- Handle the error
        PRINT ERROR_MESSAGE();
    END CATCH
END;
```

In this example, if an error occurs during the execution of the INSERT statement, the control is transferred to the CATCH block, where the transaction is rolled back, and the error message is printed. This ensures that the database remains in a consistent state and provides information about the error for troubleshooting purposes.

## **TRANSACTIONS WITH TRY CATCH IN SQL SERVER**

In SQL Server, transactions are used to group a series of database operations into a single unit of work that either succeeds or fails as a whole. The `TRY...CATCH` construct provides a way to handle errors that may occur within a transaction.

**Example**:

```sql
BEGIN TRY
    BEGIN TRANSACTION;

    -- Database operations
    INSERT INTO TableName (Column1, Column2) VALUES (Value1, Value2);
    UPDATE TableName SET Column1 = NewValue WHERE Condition;
    DELETE FROM TableName WHERE Condition;

    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0
        ROLLBACK TRANSACTION;

    -- Error handling
    PRINT ERROR_MESSAGE();
END CATCH;
```

In this example, the `BEGIN TRY` block contains the transactional code, while the `BEGIN CATCH` block handles any errors that occur. If an error occurs, the transaction is rolled back to maintain data integrity.

## **TEMPORARY TABLES / LOCAL TEMPORARY TABLE IN SQL SERVER**

Temporary tables are tables that exist only for the duration of a user session or a module execution. In SQL Server, there are two types of temporary tables: local temporary tables and global temporary tables.

**Local Temporary Tables**:

```sql
CREATE TABLE #TempTable (
    Column1 datatype,
    Column2 datatype,
    ...
);
```

Local temporary tables are prefixed with a single pound sign (`#`) and are visible only to the current session. They are automatically dropped when the session that created them ends or when the last statement referencing them completes.

## **GLOBAL TEMPORARY TABLES IN SQL SERVER**

Global temporary tables are prefixed with a double pound sign (`##`) and are visible to all sessions. They are dropped when the last session referencing them ends or when they are explicitly dropped.

**Example**:

```sql
CREATE TABLE ##GlobalTempTable (
    Column1 datatype,
    Column2 datatype,
    ...
);
```

## **DIFFERENCE BETWEEN LOCAL AND GLOBAL TEMPORARY TABLES IN SQL SERVER**

The main differences between local and global temporary tables in SQL Server are:

1. **Visibility**: Local temporary tables (`#`) are visible only to the current session, while global temporary tables (`##`) are visible to all sessions.

2. **Scope**: Local temporary tables are dropped when the session that created them ends, while global temporary tables are dropped when the last session referencing them ends.

3. **Naming Convention**: Local temporary tables are prefixed with a single pound sign (`#`), while global temporary tables are prefixed with a double pound sign (`##`).

## **COALESCE FUNCTION IN SQL SERVER**

The `COALESCE` function in SQL Server is used to return the first non-null expression among its arguments. It evaluates the arguments in order and returns the value of the first non-null expression. If all arguments are null, `COALESCE` returns null.

**Syntax**:

```sql
COALESCE(expression1, expression2, ...)
```

**Example**:

```sql
SELECT COALESCE(ColumnName, 'N/A') AS NewColumnName
FROM TableName;
```

In this example, if `ColumnName` is null, the `COALESCE` function returns 'N/A'. Otherwise, it returns the value of `ColumnName`. This is useful for displaying default values or handling null values in queries.

## **1. Coalesce vs. ISNULL Function in SQL Server:**

**Coalesce Function:**
The `COALESCE` function in SQL Server is used to return the first non-null value among its arguments. It takes multiple parameters and returns the first non-null value from those parameters. If all parameters are null, it returns null.

**Example:**

```sql
SELECT COALESCE(NULL, 'Second', 'Third') AS Result;
```

**Output:**

```
Second
```

**ISNULL Function:**
The `ISNULL` function in SQL Server is used to replace NULL values with a specified replacement value. It takes two parameters: the expression to check for NULL and the replacement value.

**Example:**

```sql
SELECT ISNULL(NULL, 'Replacement') AS Result;
```

**Output:**

```
Replacement
```

**Difference:**
The main difference between `COALESCE` and `ISNULL` lies in their handling of multiple parameters. `COALESCE` evaluates the parameters from left to right and returns the first non-null value. In contrast, `ISNULL` only takes two parameters and replaces NULL with the specified value.

## **2. CAST Function in SQL Server:**

The `CAST` function in SQL Server is used to convert an expression from one data type to another. It is particularly useful when you need to convert data types explicitly.

**Example:**

```sql
SELECT CAST('123' AS INT) AS Result;
```

**Output:**

```
123
```

## **3. CONVERT Function in SQL Server:**

The `CONVERT` function in SQL Server is similar to the `CAST` function, but it provides more flexibility in terms of formatting and data type conversion.

**Example:**

```sql
SELECT CONVERT(INT, '123') AS Result;
```

**Output:**

```
123
```

## **Difference Between CAST and CONVERT:**
While both functions are used for data type conversion, `CONVERT` offers additional formatting options and is more flexible than `CAST`. `CONVERT` allows you to specify a style parameter for date and time conversions, whereas `CAST` does not.

**4. Cursor in SQL Server:**

A cursor in SQL Server is a database object used to retrieve and manipulate data row by row. It allows for sequential processing of query results and is commonly used for tasks that cannot be accomplished using set-based operations.

**Example:**

```sql
DECLARE @EmployeeName VARCHAR(50);
DECLARE EmployeeCursor CURSOR FOR
SELECT EmployeeName FROM Employees;

OPEN EmployeeCursor;
FETCH NEXT FROM EmployeeCursor INTO @EmployeeName;

WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT @EmployeeName;
    FETCH NEXT FROM EmployeeCursor INTO @EmployeeName;
END;

CLOSE EmployeeCursor;
DEALLOCATE EmployeeCursor;
```

## **5. Working With Cursors in SQL Server:**

Working with cursors in SQL Server involves several steps, including declaration, opening, fetching, processing, and closing the cursor. Cursors offer flexibility in data manipulation but can be less efficient than set-based operations.

**Example:**

```sql
DECLARE @ProductName VARCHAR(50);
DECLARE ProductCursor CURSOR FOR
SELECT ProductName FROM Products;

OPEN ProductCursor;
FETCH NEXT FROM ProductCursor INTO @ProductName;

WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT @ProductName;
    FETCH NEXT FROM ProductCursor INTO @ProductName;
END;

CLOSE ProductCursor;
DEALLOCATE ProductCursor;
```

**Explanation:**

- Cursors in SQL Server allow for sequential processing of query results.
- They are declared using the `DECLARE CURSOR` statement and must be opened before fetching data.
- Data is fetched row by row using the `FETCH` statement, and processing occurs within a loop until all rows have been processed.
- Cursors should be closed and deallocated after use to release associated resources and improve performance.

In summary, the topics covered include the differences between the `COALESCE` and `ISNULL` functions, the usage of the `CAST` and `CONVERT` functions for data type conversion, and an overview of cursors in SQL Server along with examples demonstrating their usage. Each topic provides a foundational understanding of its respective concept, allowing for further exploration and application in SQL Server development.

## **OVER CLAUSE WITH PARTITION BY IN SQL SERVER**

The **OVER clause** in SQL Server is a powerful tool that allows you to perform window functions, which compute values across a set of rows defined by a partition or window. The **PARTITION BY** clause within the OVER clause partitions the result set into groups based on the specified column or columns. This allows you to apply window functions independently within each partition, providing more granular control over your data analysis.

**Example:**

Suppose we have a table named **Sales** with columns **Year**, **Month**, and **Revenue**. We want to calculate the total revenue for each year and month, as well as the average revenue for each year. We can achieve this using the OVER clause with the PARTITION BY clause.

```sql
SELECT
    Year,
    Month,
    Revenue,
    SUM(Revenue) OVER (PARTITION BY Year, Month) AS TotalRevenuePerMonth,
    AVG(Revenue) OVER (PARTITION BY Year) AS AvgRevenuePerYear
FROM
    Sales;
```

In this example, the PARTITION BY clause partitions the result set into groups based on the **Year** and **Month** columns. Within each partition, the SUM function calculates the total revenue for each month, and the AVG function calculates the average revenue for each year.

## **Retrieving Last Generated Identity Column Value in SQL Server - Scope_Identity VS @@identity**

When inserting records into a table with an identity column (auto-incrementing primary key), you may need to retrieve the last generated identity column value. SQL Server provides two main methods for achieving this: **SCOPE_IDENTITY()** and **@@IDENTITY**.

- **SCOPE_IDENTITY()**: This function returns the last identity value generated within the current scope (e.g., within the current stored procedure, trigger, or batch). It is the recommended method for retrieving the last identity value as it is not affected by triggers or nested scopes.

- **@@IDENTITY**: This system function returns the last identity value generated for any table in the current session, regardless of the scope. It is not recommended for use in scenarios involving triggers or nested scopes as it can return unexpected results.

**Example:**

Suppose we have a table named **Employees** with an identity column **EmployeeID**. After inserting a new employee record, we want to retrieve the last generated **EmployeeID** using both SCOPE_IDENTITY() and @@IDENTITY.

```sql
INSERT INTO Employees (FirstName, LastName) VALUES ('John', 'Doe');

SELECT SCOPE_IDENTITY() AS LastEmployeeID;
SELECT @@IDENTITY AS LastEmployeeID;
```

In this example, the first SELECT statement returns the last generated **EmployeeID** using SCOPE_IDENTITY(), which ensures that only the identity value generated within the current scope is returned. The second SELECT statement returns the last generated **EmployeeID** using @@IDENTITY, which may return unexpected results if there are triggers or nested scopes involved.

## **Row_Number Function In SQL Server - Row_Number With Partition By Clause**

The **ROW_NUMBER()** function in SQL Server assigns a unique sequential integer to each row within a partition of a result set. When used with the **PARTITION BY** clause, the ROW_NUMBER() function resets the row number for each partition, allowing you to assign row numbers independently within each partition.

**Example:**

Suppose we have a table named **Products** with columns **Category**, **ProductID**, and **ProductName**. We want to assign a unique row number to each product within each category.

```sql
SELECT
    Category,
    ProductID,
    ProductName,
    ROW_NUMBER() OVER (PARTITION BY Category ORDER BY ProductID) AS RowNumber
FROM
    Products;
```

In this example, the PARTITION BY clause partitions the result set into groups based on the **Category** column. Within each partition, the ROW_NUMBER() function assigns a unique row number to each product, ordered by **ProductID** within each category.

## **Rank And Dense_Rank Function In SQL Server - Rank VS Dense_Rank In SQL Server**

The **RANK()** and **DENSE_RANK()** functions in SQL Server are used to assign ranks to rows within a result set based on specified criteria. While both functions assign ranks, they differ in how they handle ties (i.e., rows with equal values).

- **RANK()**: This function assigns the same rank to rows with equal values, leaving gaps in the rank sequence if there are ties. For example, if two rows have the same value and rank 1, the next row will have rank 3.

- **DENSE_RANK()**: This function also assigns ranks to rows with equal values, but it does not leave gaps in the rank sequence. If there are ties, the ranks are assigned consecutively without gaps.

**Example:**

Suppose we have a table named **Students** with columns **Class**, **StudentID**, and **Score**. We want to assign ranks to students within each class based on their scores using both RANK() and DENSE_RANK().

```sql
SELECT
    Class,
    StudentID,
    Score,
    RANK() OVER (PARTITION BY Class ORDER BY Score DESC) AS RankByScore,
    DENSE_RANK() OVER (PARTITION BY Class ORDER BY Score DESC) AS DenseRankByScore
FROM
    Students;
```

In this example, the PARTITION BY clause partitions the result set into groups based on the **Class** column. Within each partition, the RANK() function assigns ranks to students based on their scores, leaving gaps in the rank sequence for ties. The DENSE_RANK() function assigns ranks to students without leaving gaps, ensuring consecutive ranks even for tied scores.

## **Cross Apply & Outer Apply In SQL Server - Apply Operator in SQL Server**

The **APPLY** operator in SQL Server is used to invoke a table-valued function for each row of a query's result set. There are two variations of the APPLY operator: **CROSS APPLY** and **OUTER APPLY**.

- **CROSS APPLY**: This operator returns only rows for which the table-valued function returns results. It operates similar to an inner join between the left and right tables.

- **OUTER APPLY**: This operator returns all rows from the left table, along with the results of the table-valued function for each row. If the function returns no results for a row, NULL values are returned for the function's columns.

**Example:**

Suppose we have two tables named **Employees** and **Orders**, where each employee can have multiple orders. We want to retrieve all employees along with their corresponding orders using the CROSS APPLY and OUTER APPLY operators with a table-valued function named **GetOrders**.

```sql
-- Using CROSS APPLY
SELECT
    E.EmployeeID,
    E.FirstName,
    E.LastName,
    O.OrderID,
    O.OrderDate
FROM
    Employees E
CROSS APPLY
    GetOrders(E.EmployeeID) O;

-- Using OUTER APPLY
SELECT
    E.EmployeeID,
    E.FirstName,
    E.LastName,
    O.OrderID,
    O.OrderDate
FROM
    Employees E
OUTER APPLY
    GetOrders(E.EmployeeID) O;
```

In these examples, the table-valued function **GetOrders** is invoked for each employee in the Employees table. With CROSS APPLY, only employees with

orders are returned, while with OUTER APPLY, all employees are returned, along with their corresponding orders if they exist. This allows for dynamic processing and manipulation of data within SQL Server queries.

## **CTE in SQL - Common Table Expression In SQL - SQL CTE - CTE In SQL Server**

A **Common Table Expression (CTE)** in SQL is a temporary result set that is defined within the scope of a single SELECT, INSERT, UPDATE, DELETE, or CREATE VIEW statement. It allows you to define a query that can be referenced within another query, similar to a subquery. CTEs enhance readability and maintainability of SQL code by breaking down complex queries into smaller, more manageable parts.

**Syntax:**

```
WITH cte_name (column1, column2, ...)
AS
(
    -- CTE query definition
    SELECT column1, column2, ...
    FROM table_name
    WHERE condition
)
SELECT *
FROM cte_name;
```

**Example:**

Consider a scenario where you have a table named "Employees" with columns "EmployeeID", "FirstName", "LastName", and "Salary". You want to calculate the average salary of employees and then find employees whose salary is above the average.

```sql
WITH AverageSalary AS (
    SELECT AVG(Salary) AS AvgSalary
    FROM Employees
)
SELECT EmployeeID, FirstName, LastName, Salary
FROM Employees
WHERE Salary > (SELECT AvgSalary FROM AverageSalary);
```

In this example, the CTE named "AverageSalary" calculates the average salary of employees, and then it is referenced in the main query to filter employees whose salary is above the average.

## **Date & Time Functions In SQL - SQL Date & Time Functions**

SQL provides a variety of built-in functions for manipulating and working with date and time data types. These functions allow you to perform tasks such as extracting parts of dates, formatting dates, performing calculations, and converting between different date and time formats.

**Common Date & Time Functions:**

1. **GETDATE()**: Returns the current date and time.

2. **DATEADD()**: Adds a specified number of intervals (days, months, years, etc.) to a given date.

3. **DATEDIFF()**: Calculates the difference between two dates in terms of a specified interval.

4. **DATEPART()**: Extracts a specific part (day, month, year, etc.) of a date.

5. **FORMAT()**: Formats a date or time value based on a specified format string.

**Example:**

Let's say you have a table named "Orders" with a column "OrderDate" storing the date of each order. You want to retrieve orders placed in the current month along with the day of the week for each order.

```sql
SELECT OrderID, OrderDate, DATENAME(WEEKDAY, OrderDate) AS DayOfWeek
FROM Orders
WHERE MONTH(OrderDate) = MONTH(GETDATE()) AND YEAR(OrderDate) = YEAR(GETDATE());
```

In this example, we use the DATEPART() function to extract the month and year from the current date (GETDATE()), and then filter the orders accordingly. We also use the DATENAME() function to get the name of the day of the week for each order.

Overall, CTEs and Date & Time Functions are powerful tools in SQL that enable you to write complex queries and manipulate date and time data effectively. By understanding their usage and syntax, you can enhance your SQL skills and build more efficient database solutions.
