select id, sum(frnd_count) as num
from 
(select requester_id as id, count(accepter_id) as frnd_count
from requestaccepted
group by requester_id

UNION all

select accepter_id as id, count(requester_id) as frnd_count
from requestaccepted
group by accepter_id
)

group by id
order by num desc
limit 1;