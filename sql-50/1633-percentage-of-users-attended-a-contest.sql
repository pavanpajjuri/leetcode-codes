select contest_id, round( count(a.user_id)*100.0 / (select count(*) from users) ,2) as percentage
from register a
left join users b
on a.user_id = b.user_id
group by contest_id 
order by percentage desc, contest_id;