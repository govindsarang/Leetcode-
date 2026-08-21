# Write your MySQL query statement below
select employee_id,
case 
when employee_id % 2=0 then 0
when name like "M%" Then 0
Else salary 
End as bonus
from Employees
order by employee_id