select customer_id, count(Visits.visit_id) as count_no_trans
FROM Visits
LEFT JOIN Transactions on Visits.visit_id = Transactions.visit_id
where transaction_id is null
GROUP BY customer_id;
