select user_id as user_id,
upper(left(name,1)) || lower(substring(name from 2)) as name
from users
order by user_id;