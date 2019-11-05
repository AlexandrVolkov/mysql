-- 1
drop function if exists my_new_function;
DELIMITER $$
create function my_new_function()
returns varchar(255)
begin
    declare text varchar(255);
	declare cur_hour int;
	set cur_hour = hour(now());
	if cur_hour < 6 then set text="Good night";
	elseif cur_hour < 12 then set text="Good morning";
	elseif cur_hour < 18 then set text="Good afternoon";
	else set text="good evening";
	end if;
	return (text);
end$$
DELIMITER ;

select my_new_function();

-- 2

drop trigger if exists beforeinsertname;
DELIMITER $$
CREATE TRIGGER beforeinsertname
AFTER INSERT
ON products FOR EACH row
begin
	if (new.description  is null and new.name is null) then
		signal sqlstate '45000' set message_text = 'Both fields name and description can not be empty';
	end if;
end$$
DELIMITER ;

