select t1.machine_id, round((avg(t1.timestamp)-avg(t2.timestamp))::NUMERIC,3) as processing_time
from activity t1
join activity t2
on t1.machine_id = t2.machine_id and t1.process_id = t2.process_id
where t1.activity_type = 'end' and t2.activity_type = 'start' 
group by t1.machine_id;
