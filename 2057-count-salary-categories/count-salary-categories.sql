# Write your MySQL query statement below
select "High Salary" as category, count(income) as accounts_count from Accounts
where income>50000
Union
select "Low Salary" as category, count(income) as accounts_count from Accounts
where income<20000
Union 
select "Average Salary" as category, count(income) as accounts_count from Accounts
where income>=20000
and income <=50000

 
