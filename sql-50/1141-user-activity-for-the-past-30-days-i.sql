select activity_date as day,
count(distinct(user_id)) as active_users
from activity
where activity_date between date '2019-07-27' - 29 and date '2019-07-27'
group by day;
