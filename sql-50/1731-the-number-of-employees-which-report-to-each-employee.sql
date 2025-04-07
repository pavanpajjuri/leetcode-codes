select a.employee_id, a.name, count(b.employee_id) as reports_count, avg(b.age)::INT as average_age
from employees a
join employees b
on a.employee_id = b.reports_to
group by a.employee_id, a.name
order by a.employee_id;
