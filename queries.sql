WITH target_dates AS (SELECT * FROM dates
WHERE id<=:endDateId AND :startDateId<=id),
target_table AS (SELECT * FROM tables
WHERE table_name = 'X')


SELECT COUNT(*)
FROM daily_usage du
JOIN users us ON du.person_id=us.id
JOIN target_table tt ON tt.id=du.table_id
JOIN target_dates td ON td.id=du.date_id





