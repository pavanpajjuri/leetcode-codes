select t1.id
from weather t1
join weather t2 on t1.recordDate = t2.recordDate + 1
where t1.temperature > t2.temperature;
