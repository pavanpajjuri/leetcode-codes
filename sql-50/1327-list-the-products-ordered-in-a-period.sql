select a1.product_name, sum(a2.unit) as unit
from products a1
join orders a2 on a1.product_id = a2.product_id
where a2.order_date between '2020-02-01' and '2020-02-29'
group by a1.product_name
having sum(a2.unit) >= 100;