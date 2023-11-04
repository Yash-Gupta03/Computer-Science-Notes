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

### 37. What is the difference between delete, truncate and drop command ?

With delete command, we can set some filters with where clause for what records to delete, we can also restore the records back with rollback command<br>
With drop command, we drop the entire table from the database and all the data inside it.<br>
With truncate, we erase the entire table's data, it is faster than drop and delete and we can restore back it's data.



## HackerRank SQL Practice Questions

## SELECT QUERIES

### 1. Basic Select Query
```sql
select * from tablename where (condition1 and condition2);
```

### 2. Use of limit clause
```sql

SELECT DISTINCT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY), CITY LIMIT 1;
```

### 3. Use of left clause

```sql
SELECT CITY FROM STATION WHERE LEFT(CITY, 1) IN ('a','e','i','o','u');

SELECT DISTINCT CITY FROM STATION WHERE LEFT(CITY, 1) NOT IN ('A','E','I','O','U');
```

### 4. Use of case when then 
```sql
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
```

### 5. Use of concat

```sql
SELECT CONCAT(NAME,'(', LEFT(OCCUPATION, 1),')') FROM OCCUPATIONS ORDER BY NAME;

SELECT CONCAT('There are a total of ', COUNT(OCCUPATION), ' ', lower(OCCUPATION), 's.') FROM OCCUPATIONS GROUP BY OCCUPATION ORDER BY count(OCCUPATION),OCCUPATION;
```

### 6. Case when then
```
SELECT N,
    CASE
        WHEN P IS NULL THEN 'Root'
        WHEN (N IN (SELECT P FROM BST)) THEN 'Inner'
        ELSE 'Leaf'
    END
FROM BST ORDER BY N
```

## AGGREGATE FUNCTION - 
> COUNT(), SUM(), AVG(), 
### 1.  To round off a number 
```sql
SELECT ROUND(AVG(POPULATION)) FROM CITY  
```

### 2. Using Replace
```
SELECT CEIL(AVG(SALARY)-AVG(REPLACE(SALARY, 0, ''))) FROM EMPLOYEES;
```

### 3. using groupby and orderby
```sql
SELECT MAX(MONTHS*SALARY), COUNT(*) FROM EMPLOYEE WHERE MONTHS*SALARY= (SELECT MAX(SALARY*MONTHS) FROM EMPLOYEE);
-- OR
SELECT MONTHS*SALARY AS TOTAL, COUNT(*) FROM EMPLOYEE GROUP BY TOTAL ORDER BY TOTAL DESC LIMIT 1

SELECT ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2) FROM STATION;
```

### 4. QUERY LONG_W FOR LARGEST LAT_N THAT IS LESS THAN A NUMBER
```SQL
SELECT ROUND(LONG_W, 4) FROM STATION WHERE LAT_N < 137.2345 ORDER BY LAT_N DESC LIMIT 1;
```

### 5. Use of round, abs, min, max
```sql
SELECT ROUND(ABS(MIN(LAT_N)-MAX(LAT_N))+ABS(MIN(LONG_W)-MAX(LONG_W)), 4) FROM STATION
-- Manhatten Distance - abs(x1-y1)+abs(x2-y2)     // (x1, x2), (y1, y2)
```

### 6. use of sqrt, power, round, min, max
```sql
SELECT ROUND(SQRT(POWER((MAX(LAT_N)-MIN(LAT_N)), 2)+POWER((MAX(LONG_W)-MIN(LONG_W)) ,2)),4) FROM STATION;
```

<!-- 7. Median Question
    ```TOUGH``` -->


## JOINS

### 1. Basic Join 
```sql
SELECT CITY.NAME FROM CITY INNER JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE WHERE COUNTRY.CONTINENT = 'AFRICA'
```

### 2. Use of if and a different type of dependency
```sql
SELECT IF(STUDENTS.MARKS<70, NULL, STUDENTS.NAME), GRADES.GRADE, STUDENTS.MARKS FROM STUDENTS JOIN GRADES ON STUDENTS.MARKS BETWEEN GRADES.MIN_MARK AND GRADES.MAX_MARK ORDER BY GRADES.GRADE DESC, STUDENTS.NAME ASC
```

### 3. Connecting a lot of tables 
```sql
SELECT SUBMISSIONS.HACKER_ID, HACKERS.NAME
FROM SUBMISSIONS INNER JOIN HACKERS
ON HACKERS.HACKER_ID = SUBMISSIONS.HACKER_ID INNER JOIN CHALLENGES
ON SUBMISSIONS.CHALLENGE_ID = CHALLENGES.CHALLENGE_ID INNER JOIN DIFFICULTY
ON CHALLENGES.DIFFICULTY_LEVEL = DIFFICULTY.DIFFICULTY_LEVEL
WHERE SUBMISSIONS.SCORE = DIFFICULTY.SCORE
GROUP BY SUBMISSIONS.HACKER_ID, HACKERS.NAME
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC, HACKERS.HACKER_ID; 
```

### 4. Print star Pattern
```sql
SET @VAR = 21;
SELECT REPEAT('* ', @VAR := @VAR-1) FROM INFORMATION_SCHEMA.TABLES;
```




