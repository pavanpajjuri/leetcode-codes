select a1.product_id, coalesce(a2.new_price, 10) as price
from (select distinct product_id from products) a1
left join products a2
on a1.product_id = a2.product_id
and a2.change_date = (select max(change_date) from products where product_id = a1.product_id and change_date <= '2019-08-16');





with cte as (select *, row_number() over(partition by product_id order by change_date desc) as rn
from products
where change_date <= '2019-08-16'
)

select a1.product_id, coalesce(a2.new_price, 10) as price
from (select distinct(product_id) from products) a1
left join cte a2
on a1.product_id = a2.product_id
and a2.rn = 1;



select distinct on (a1.product_id) a1.product_id, coalesce(a2.new_price, 10) as price
from (select distinct product_id from products) a1
left join (select * from products where change_date <= '2019-08-16') a2
on a1.product_id = a2.product_id
order by a1.product_id, a2.change_date desc;