-- Выполню на выходных. Не успеваю на протяжении недели.

-- Повторить все действия по доработке БД vk.
use vk;
alter table users add is_deleted bit default 0 not null;

-- Заполнить новые таблицы.
-- Не нашёл новые таблицы, все таблицы были заполнены в предыдущем задании

-- Повторить все действия CRUD.
insert into users (id, firstname, lastname, email, phone)
values (190, 'Alex', 'Volkov', 'alexandr@gmail.com', 0987656456)

select * from users where lastname = 'Volkov'

update users
set firstname = 'Alexandr'
where lastname = 'Volkov'

delete from users
where lastname = 'Volkov'

-- Подобрать сервис-образец для курсовой работы.
-- Сервис по проведению теста ДНК на наличие генетических заболеваний
-- Таблицы
-- user (id, name, etc) список пользователей
-- doctor (id, name, etc) список координирующих врачей
-- patient_list (id, doctor_id, user_id, etc) пациенты(пользователи) врачей
-- address (id, user_id, city, etc) адрес пользователей
-- order_status(id, status, etc) список возможных статусов выполнения заказа
-- order (id, user_id, status_id, created_at, etc) заказ на проведение ДНК теста
-- payment (id, order_id, status, total, etc) оплата теста
-- disease (id, name, code, etc) список генетических заболеваний
-- users_disease (id, user_id, disease_id, level, etc) выявленные заболевания пользователя
-- conclusion (id, patient_list_id, content, etc) заключение врача