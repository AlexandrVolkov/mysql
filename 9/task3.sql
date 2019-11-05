-- 1
drop function if exists my_new_function;
DELIMITER $$
create function my_new_function
returns varchar(255)
begin
	declare cur_hour int;
	set cur_hour = hour(now())
	if ()
end

--С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", с 12:00 до 18:00 функция должна возвращать фразу "Добрый день", с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи".
