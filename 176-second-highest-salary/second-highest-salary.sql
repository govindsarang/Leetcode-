# Write your MySQL query statement below
#Select max(e1.salary) as SecondHighestSalary
#rom Employee e1 inner join employee e2 
#on e1.salary<e2.salary
select ( Select
distinct salary  from Employee 
order by salary desc 
limit 1 offset 1 
) as SecondHighestSalary

