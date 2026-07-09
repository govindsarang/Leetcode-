# Write your MySQL query statement below
select Round(Count(Distinct a.player_id)/(Select count(distinct player_id) from Activity),2) as fraction  from Activity a 
join
(select player_id ,min(event_date) as first_login from Activity 
group by player_id)f
on a.player_id=f.player_id
WHERE a.event_date = DATE_ADD(f.first_login, INTERVAL 1 DAY);