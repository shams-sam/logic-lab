-- https://www.hackerrank.com/challenges/revising-the-select-query
SELECT * 
FROM CITY 
WHERE POPULATION > 10000 
AND COUNTRYCODE LIKE 'USA';
-- https://www.hackerrank.com/challenges/revising-the-select-query-2
SELECT NAME
FROM CITY
WHERE POPULATION > 120000
AND COUNTRYCODE LIKE 'USA';
-- https://www.hackerrank.com/challenges/select-all-sql
SELECT * 
FROM CITY;
-- https://www.hackerrank.com/challenges/select-by-id
SELECT * 
FROM CITY 
WHERE ID = 1661;
-- https://www.hackerrank.com/challenges/japanese-cities-attributes
SELECT * 
FROM CITY 
WHERE COUNTRYCODE LIKE 'JPN';
-- https://www.hackerrank.com/challenges/japanese-cities-name
SELECT NAME 
FROM CITY 
WHERE COUNTRYCODE LIKE 'JPN';
-- https://www.hackerrank.com/challenges/weather-observation-station-1
SELECT CITY, STATE 
FROM STATION;
-- https://www.hackerrank.com/challenges/weather-observation-station-3
SELECT DISTINCT CITY 
FROM STATION 
WHERE ID % 2 = 0;
-- https://www.hackerrank.com/challenges/weather-observation-station-4
SELECT COUNT(id) - COUNT(DISTINCT CITY) 
FROM STATION;
-- https://www.hackerrank.com/challenges/weather-observation-station-5
SELECT CITY, LENGTH FROM 
(   SELECT CITY, LENGTH(CITY) AS LENGTH 
    FROM STATION 
    ORDER BY LENGTH(CITY), CITY 
    LIMIT 1) MIN_TABLE
UNION
(   SELECT CITY, LENGTH(CITY) AS LENGTH 
    FROM STATION 
    ORDER BY LENGTH(CITY) DESC, CITY 
    LIMIT 1);
-- https://www.hackerrank.com/challenges/weather-observation-station-6
SELECT CITY 
FROM STATION 
WHERE CITY REGEXP '^[aeiou]';
-- https://www.hackerrank.com/challenges/weather-observation-station-7
SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY REGEXP '[aeiou]$';
-- https://www.hackerrank.com/challenges/weather-observation-station-8
SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY REGEXP '^[aeiou].*[aeiou]$';
-- https://www.hackerrank.com/challenges/weather-observation-station-9
SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY NOT REGEXP '^[aeiou]';
-- https://www.hackerrank.com/challenges/weather-observation-station-10
SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY NOT REGEXP '[aeiou]$';
-- https://www.hackerrank.com/challenges/weather-observation-station-11
SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY NOT REGEXP '^[aeiou]'
OR CITY NOT REGEXP '[aeiou]$';
-- https://www.hackerrank.com/challenges/weather-observation-station-12
SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY NOT REGEXP '^[aeiou]'
AND CITY NOT REGEXP '[aeiou]$';
-- https://www.hackerrank.com/challenges/more-than-75-marks
SELECT NAME 
FROM STUDENTS 
WHERE MARKS > 75
ORDER BY RIGHT(NAME, 3), ID;
-- https://www.hackerrank.com/challenges/name-of-employees
SELECT NAME 
FROM EMPLOYEE
ORDER BY NAME;
-- https://www.hackerrank.com/challenges/salary-of-employees
SELECT NAME 
FROM EMPLOYEE
WHERE SALARY > 2000
AND MONTHS < 10
ORDER BY EMPLOYEE_ID;
