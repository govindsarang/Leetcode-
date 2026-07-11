# Write your MySQL query statement below
Select sell_date ,
count(distinct product) as num_sold,
Group_concat(
    distinct product 
    order by product 
) As products 
From Activities 
group by sell_date 
order by sell_date,product 
