select a2.name as Department, a1.name as Employee, a1.salary as salary
from(
select *,
dense_rank() over(partition by departmentid order by salary desc) as rank
from employee) as a1
join department a2
on a1.departmentid = a2.id
where a1.rank <= 3
order by department, salary desc;