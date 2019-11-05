-- 1
begin;

insert into sample.users (id, name)
select s_u.id, s_u.name from shop.users as s_u
where s_u.id=1;

delete from shop.users where id = 1;

commit;

-- 2
create or replace view catalog_view as select
 p.name, c.name from products p
 join catalogs c on p.catalog_id = c.id;

 select * from catalog_view;