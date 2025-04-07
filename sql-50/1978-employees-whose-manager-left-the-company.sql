select employee_id
from employees
where salary < 30000 and manager_id is not null and manager_id not in (select distinct employee_id from employees)
order by employee_id;