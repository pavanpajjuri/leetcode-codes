select a.product_id, round(
    -- case
    -- when sum(a.price*b.units) is null then 0 
    -- else sum(a.price*b.units)*1.0/sum(b.units) 
    -- end
    coalesce(sum(a.price*b.units)*1.0/sum(b.units), 0)
    , 2) as average_price
from Prices a
left join unitssold b
on a.product_id = b.product_id
and b.purchase_date between a.start_date and a.end_date
group by a.product_id;