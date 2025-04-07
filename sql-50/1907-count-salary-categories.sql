-- select a1.category, coalesce(a2.account_counts, 0) as accounts_count from 
-- (select * from (
--     values ('Low Salary'),
--     ('Average Salary'),
--     ('High Salary')
-- )as categories(category)) as a1
-- left join
-- (
-- select (
--     case 
--         when income < 20000 then 'Low Salary'
--         when income >= 20000 and income <= 50000 then 'Average Salary'
--         when income > 50000 then 'High Salary'
--     end 
-- ) as category,
-- count(*) as account_counts
-- from accounts
-- group by category
-- ) as a2
-- on a1.category = a2.category;


SELECT 'Low Salary' AS category, COUNT(account_id) AS accounts_count  
FROM Accounts
WHERE income<20000
UNION
SELECT 'Average Salary' AS category, COUNT(account_id) AS accounts_count  
FROM Accounts
WHERE income BETWEEN 20000 AND 50000
UNION
SELECT 'High Salary' AS category, COUNT(account_id) AS accounts_count  
FROM Accounts
WHERE income >50000;