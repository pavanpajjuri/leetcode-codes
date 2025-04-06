select a.user_id,
round(
    case 
    when count(b.action) = 0 then 0
    else sum(case 
             when b.action = 'confirmed' then 1 
             else 0 
             end)*1.0/count(b.action)
    end
    , 2
    ) as confirmation_rate

from signups a
left join confirmations b
on a.user_id = b.user_id
group by a.user_id;