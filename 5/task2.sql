use vk;

-- 1
-- update users set dob = TIMESTAMPADD(SECOND, FLOOR(RAND() * TIMESTAMPDIFF(SECOND, '1956-04-30 14:53:27', '2010-04-30 14:53:27')), '1956-04-30 14:53:27');


select avg(timestampdiff(year, dob, now()))
from users;

-- 2

select count(*), dayofweek(DATE_FORMAT(dob,concat(YEAR(CURDATE()),'-%m-%d'))) as dayofweek
from users
group by dayofweek;

-- 3

SELECT ROUND(EXP(SUM(LOG(value))),1)
FROM storehouses_products as sp
WHERE value != 0