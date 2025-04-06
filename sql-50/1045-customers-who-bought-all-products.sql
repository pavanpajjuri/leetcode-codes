select a2.customer_id
from product a1
left join customer a2
on a1.product_key = a2.product_key
group by a2.customer_id
having count(distinct a1.product_key) = (select count(distinct(product_key)) from product a3);
