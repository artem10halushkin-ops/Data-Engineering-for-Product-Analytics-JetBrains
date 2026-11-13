SELECT person_id, table_id , date_id, maxpeakmemory_bytes, processed_input_lines , bytes_read, queued_time
,whole_time_query , spilled_bytes FROM mytable
WHERE DATE= :target_date
