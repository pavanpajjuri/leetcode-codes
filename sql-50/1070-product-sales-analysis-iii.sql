select a.product_id,a.year as first_year,a.quantity,a.price
from sales a
join (select product_id, min(year) as year from sales group by product_id) b
on a.product_id = b.product_id
where a.year = b.year;


select product_id, year as first_year, quantity, price
from(
select *,
row_number() over(partition by product_id order by year) as rn
from sales
)
where rn = 1;