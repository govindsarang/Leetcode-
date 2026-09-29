# Write your MySQL query statement below
with user_avg as (
    select user_id,Avg(tokens) as avg_tokens
    from prompts 
    group by user_id
)
select p.user_id, count(*) as prompt_count ,round(avg(p.tokens),2) as avg_tokens from prompts p
inner join user_avg a on a.user_id=p.user_id
group by p.user_id , a.avg_tokens
having count(*)>=3 and 
sum(p.tokens>a.avg_tokens)>=1
order by a.avg_tokens DESC
