SELECT 
    to_char(trans_date, 'YYYY-MM') AS month,
    country, 
    COUNT(id) AS trans_count,
    sum(case when state = 'approved' then 1 else 0 end) as approved_count,
    SUM(amount) AS trans_total_amount,
    sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
FROM 
    Transactions
GROUP BY 
    to_char(trans_date, 'YYYY-MM'), country;