with cte as (select
    (case when (min(a1.event_date)+1) in 
    (select a2.event_date from activity a2 where a1.player_id = a2.player_id) then 1 
    else 0 
    end)*1.0 as fraction
from activity a1
group by player_id
)

select round(avg(fraction),2) as fraction
from cte;