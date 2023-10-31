# MySQL Questions - 

### 1. How do you create a new database in MySQL?

create database dbname;


### 2. How do you create a new table in MySQL?

create table tablename (columnname datatype, .....);


### 3. How do you insert values into a table?

insert into tablename (column1, column2) values (val1, val2, val3);


### 4. How do you retrieve all the columns from a table?

select * from tablename

### 5. How can you retrieve specific columns from a table?

select column1, column2 from tablename

### 6. What is the use of the WHERE clause?

It is to set a filter while retrieving data based on a certain condition.

### 7. How would you fetch data from a table where the age is greater than 25?

select * from tablename where age > 25; 

### 8. What are the different types of SQL JOINs?

Inner Join, left Join, Right Join, Full Join.

### 9. Write a SQL query to join two tables: students and courses, assuming each student is enrolled in a course and they share a common column course_id.

select * from students inner join courses on student.courseId = courses.courseId

### 10. What is the difference between the HAVING clause and the WHERE clause?

select is used before aggregating the records and having sets condition on aggregated data.

### 11. How would you list the number of students enrolled in each course, but only display courses with more than 5 students?

select courseName, count(studentsName) as noOfStudents from students groupBy(CourseName) having noOfStudents > 5;

### 12. What is the LIKE operator used for?

It is used for pattern matching.

### 13. Write a SQL query to find all students whose names start with 'A'.

select * from students where name like 'A%';

### 14. How would you update a record in a table?

update tablename set column1 = '', column2 = '';

### 15. How can you delete records from a table?

delete from tablename where condition


### 16. How do you drop a table?

drop table tablename


### 17. What is the purpose of the ALTER table command?

Used to modify the table, add, delete columns.

### 18. How would you add a new column email to the students table?

alter table tablename add column email varchar(25);

### 19. Write a query to find the total number of distinct courses from the enrollments table.

select count(distinct courseName) from enrollment.

### 20. What does the EXISTS operator do?

It tests for the existence of record in the subquery.

### 21. Write a SQL query to find students who have enrolled in a course.

select student_Id from students where exists (select 1 from enrollments where student.studentId = enrollment.studentId)

### 22. How can you concatenate columns in MySQL?

using concat() function

### 23. Write a query to get the full name of a student, given first_name and last_name columns.

select concat(firstName, ' ', lastName) as fullName from student;

### 24. How do you find the total number of rows in a table?

select count(*) from tablename;

### 25. How can you fetch the first 5 records from a table?

select * from tablename limit 5;

### 26. What is the difference between CHAR and VARCHAR data types?

char is fixed-length, varchar is variable length.

### 27. How can you change the data type of a column?

alter table tablename modify columnName newDataType

### 28. Write a SQL query to find the 3rd highest salary from a salaries table.

select distinct salary from tablename orderBy salary desc limit 1 offset 2;

### 29. How do you create a primary key in a table?

alter table tablename add primary key (column_name);

### 30. What is foreign key ?

It is a field in one table which is the primary key in another table, to maintain referential integrity.

### 31. How to declare foreign key ?

alter table tablename add foreign key (columnName) references tablename(primarykey)



### 32. What is an entity ?

Entity represents a real world object.

Weak entity means that does not have its own primary key.

Tangible entities means which exists physically like cars and books.

Non-tangible that does not exist physically like social media accounts.


### 33. What is an Attribute ?

Properties or characteristics of an entity are attributes.

Types - 

Key Attribute - That can uniquely identify a tuple.(id)

Composite Attribute - That is composed of many other attributes.(address)

Multivalued Attribute - That can have multiple values.(phone number)

Derived Attribute - Attribute that can be derived from other attributes.(age)


### 34. Association in DBMS ?

It describes relationship between two objects.

### 35. Aggregate functions in DBMS ?

count, sum, min, max, avg

### 36. What is uuid ?

It is a universal unique identifier.



## HackerRank SQL Practice Questions

### Basic Select
```sql
select * from tablename where (condition1 and condition2);

Remember to use only single equal instead of double equal to compare.
/*
Query -
Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.*/

SELECT DISTINCT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY), CITY LIMIT 1;

SELECT DISTINCT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY) DESC, CITY LIMIT 1;


/*
Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
*/
SELECT CITY FROM STATION WHERE LEFT(CITY, 1) IN ('a','e','i','o','u');

-- Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

SELECT DISTINCT CITY FROM STATION WHERE LEFT(CITY, 1) NOT IN ('A','E','I','O','U');


-- Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:

-- Equilateral: It's a triangle with  sides of equal length.
-- Isosceles: It's a triangle with  sides of equal length.
-- Scalene: It's a triangle with  sides of differing lengths.
-- Not A Triangle: The given values of A, B, and C don't form a triangle.


SELECT 
    CASE
        WHEN A+B>C AND A+C>B AND B+C>A THEN
            CASE
                WHEN A=B AND B=C THEN 'Equilateral'
                WHEN A=B OR B=C OR A=C THEN 'Isosceles'
                ELSE 'Scalene'
            END
        ELSE 'Not A Triangle'
    END
FROM TRIANGLES
