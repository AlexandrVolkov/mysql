-- Пусть задан некоторый пользователь. Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим пользователем.

use vk;

select t.user_id , count(t.id) c from (
	select from_user_id as user_id, id
	from messages
	where from_user_id in (
	select initiator_user_id from friend_requests where target_user_id = 1 and status = 'approved'
	union
	select target_user_id from friend_requests where initiator_user_id = 1 and status = 'approved'
	)
	and to_user_id = 1
	union
	select to_user_id as user_id, id
	from messages
	where to_user_id in (
	select initiator_user_id from friend_requests where target_user_id = 1 and status = 'approved'
	union
	select target_user_id from friend_requests where initiator_user_id = 1 and status = 'approved'
	)
	and from_user_id = 1
) as t
group by t.user_id
order by c desc
limit 1


-- Подсчитать общее количество лайков, которые получили пользователи младше 10 лет..

select count(likes.id)
from likes
join media on likes.media_id = media.id
where media.user_id in (select users.id from users where timestampdiff(year, dob, now()) < 10)



-- Определить кто больше поставил лайков (всего) - мужчины или женщины?

select count(likes.id) c, users.sex
from likes
join users on users.id = likes.user_id
where likes.user_id in (select users.id from users)
group by users.sex
order by c desc
limit 1