-- https://www.hackerrank.com/challenges/what-type-of-triangle
SELECT
CASE
    WHEN (((A+B)<=C) OR ((B+C)<=A) OR ((C+A)<=B)) THEN 'Not A Triangle'
    WHEN ((A=B) AND (B=C)) THEN 'Equilateral'
    WHEN ((A=B) OR (B=C) OR (C=A)) THEN 'Isosceles'
    ELSE 'Scalene'
END
AS TRIANGLE_TYPE
FROM TRIANGLES;
-- https://www.hackerrank.com/challenges/the-pads
SELECT CONCAT(NAME, '(', LEFT(OCCUPATION,1), ')')
AS FULL_DESC
FROM OCCUPATIONS
ORDER BY FULL_DESC;
SELECT CONCAT('There are total ', COUNT(OCCUPATION), ' ', LOWER(OCCUPATION), 's.')
FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY COUNT(OCCUPATION), OCCUPATION;
-- https://www.hackerrank.com/challenges/occupations
SET @D=0, @P=0, @S=0, @A=0;
SELECT MIN(DOCTOR), MIN(PROFESSOR), MIN(SINGER), MIN(ACTOR) 
FROM (
    SELECT 
        CASE 
            WHEN OCCUPATION = 'Doctor' 
                THEN (@D:=@D+1) 
            WHEN OCCUPATION = 'Professor' 
                THEN (@P:=@P+1) 
            WHEN OCCUPATION = 'Singer' 
                THEN (@S:=@S+1) 
            WHEN OCCUPATION = 'Actor' 
                THEN (@A:=@A+1) END AS ID, 
        CASE 
            WHEN OCCUPATION = 'Doctor' 
            THEN NAME END AS DOCTOR, 
        CASE 
            WHEN OCCUPATION = 'Professor' 
            THEN NAME END AS PROFESSOR, 
        CASE 
            WHEN OCCUPATION = 'Singer' 
            THEN NAME END AS SINGER, 
        CASE 
            WHEN OCCUPATION = 'Actor' 
            THEN NAME END AS ACTOR 
    FROM OCCUPATIONS 
    ORDER BY NAME
) TEMP 
GROUP BY ID;
-- https://www.hackerrank.com/challenges/binary-search-tree-1
SELECT N, 
    CASE 
        WHEN P IS NULL 
            THEN 'Root' 
        WHEN  N IN (
            SELECT DISTINCT P FROM BST
            ) THEN 'Inner' 
        ELSE 'Leaf' END 
FROM BST ORDER BY N;
-- or 
SELECT N, 
    CASE 
        WHEN P IS NULL 
            THEN 'Root' 
        WHEN M IS NULL 
            THEN 'Leaf' 
        ELSE 'Inner' END 
FROM (
    SELECT DISTINCT B1.*, B2.P AS M 
    FROM BST B1 
    LEFT JOIN BST B2 ON B1.N = B2.P) TEMP 
ORDER BY N;
-- https://www.hackerrank.com/challenges/the-company
SELECT COMPANY_CODE, 
    FOUNDER, 
    COUNT(DISTINCT LEAD_MANAGER_CODE), 
    COUNT(DISTINCT SENIOR_MANAGER_CODE), 
    COUNT(DISTINCT MANAGER_CODE), 
    COUNT(DISTINCT EMPLOYEE_CODE) 
FROM (
    SELECT C.COMPANY_CODE, 
        C.FOUNDER, 
        LM.LEAD_MANAGER_CODE, 
        SM.SENIOR_MANAGER_CODE, 
        M.MANAGER_CODE, 
        E.EMPLOYEE_CODE 
    FROM COMPANY C 
    JOIN LEAD_MANAGER LM 
        ON LM.COMPANY_CODE = C.COMPANY_CODE 
    JOIN SENIOR_MANAGER SM 
        ON SM.COMPANY_CODE = C.COMPANY_CODE 
    JOIN MANAGER M 
        ON M.COMPANY_CODE = C.COMPANY_CODE 
    JOIN EMPLOYEE E 
        ON E.COMPANY_CODE = C.COMPANY_CODE
    ) TEMP 
GROUP BY COMPANY_CODE;
