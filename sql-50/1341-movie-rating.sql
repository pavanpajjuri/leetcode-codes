with cte as(
    select * 
    from movierating
    left join movies on movierating.movie_id = movies.movie_id 
    left join users on movierating.user_id = users.user_id
)

(select name as results
from cte
group by name
order by count(rating) desc, results asc
limit 1)
union all
(select title as results
from cte
where created_at between '2020-02-01' and '2020-02-28'
group by title
order by avg(rating) desc, results asc
limit 1);