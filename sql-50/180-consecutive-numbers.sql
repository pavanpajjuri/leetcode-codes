select distinct num as ConsecutiveNums
from (
    select *, 
        lag(num,1) over (order by id) as prev1,
        lag(num,2) over (order by id) as prev2
    from logs
)
where num = prev1 and prev1 = prev2;
