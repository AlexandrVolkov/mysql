use vk;

-- 1
update users set updated_at = current_timestamp, created_at = current_timestamp;

-- 2
-- update users set updated_at = '20.10.2017 8:10', created_at = '20.10.2017 8:10';

update users set
updated_at = STR_TO_DATE(updated_at, '%e.%c.%Y %H:%i'),
created_at = STR_TO_DATE(created_at, '%e.%c.%Y %H:%i');

ALTER TABLE users MODIFY COLUMN created_at DATETIME NULL;
ALTER TABLE users MODIFY COLUMN updated_at DATETIME NULL;

-- 3
-- insert into storehouses_products values (1, 0),(2,2500);
-- insert into storehouses_products values (3, 0),(4,30),(5, 500),(6,1);

select id, value from storehouses_products as sp
order by if(sp.value = 0, 0, 1) desc, value asc;

-- 5
SELECT * FROM storehouses_products WHERE id IN (5, 1, 2)
order by field(id, 5, 1, 2);