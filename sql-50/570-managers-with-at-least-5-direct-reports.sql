select a.name
from employee a
join employee b
on a.id = b.managerId
group by a.id, a.name
having count(a.id) >= 5;