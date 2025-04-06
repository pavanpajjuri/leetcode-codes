with cte as (
    select customer_id,
    case 
        when min(order_date) = min(customer_pref_delivery_date) then 'immediate'
        else 'scheduled'
    end as order_type
    from delivery
    group by customer_id
)

select
round(sum(case when order_type = 'immediate' then 1 end)*100.0/count(order_type) ,2) as immediate_percentage
from cte;
