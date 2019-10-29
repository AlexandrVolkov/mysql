select distinct u.id from users as u
join orders as o on u.id = o.user_id;


select p.id, catalogs.id
from products as p
join catalogs as c on c.id = p.catalog_id
where p.name = 'Nvidia GTX 1070';




select (select name from cities where label = f.from) as city_from,
(select name from cities where label = f.to) as city_to
from flights as f;
