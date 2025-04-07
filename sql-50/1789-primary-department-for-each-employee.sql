select employee_id,department_id
from employee
where primary_flag = 'Y' or employee_id in (
    select employee_id from employee
    group by employee_id
    having count(department_id) = 1
);



(select employee_id, max(
    CASE
    WHEN primary_flag = 'Y' then department_id
    END
) as department_id
from employee
group by employee_id
having count(*) > 1
)
UNION
(select employee_id, max(department_id) as department_id
from employee
group by employee_id
having count(*) = 1
);