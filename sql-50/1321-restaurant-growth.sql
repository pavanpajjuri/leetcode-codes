with last_6_days as (select distinct visited_on
from customer
order by visited_on asc
offset 6
)

select a1.visited_on, sum(a2.amount) as amount, ROUND(SUM(a2.amount) / 7., 2) as average_amount
from last_6_days as a1
join customer as a2
on a2.visited_on between a1.visited_on-6 and a1.visited_on
group by a1.visited_on;