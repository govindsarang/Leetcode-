# Write your MySQL query statement below
select e.name as Employee from Employee e
inner join Employee d 
on e.managerId=d.id
where e.salary>d.salary
