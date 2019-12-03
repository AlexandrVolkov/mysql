-- 1. общее текстовое описание БД и решаемых ею задач
-- Сервис по проведению теста ДНК на наличие генетических заболеваний

-- 3. Таблицы

-- список пользователей
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `firstname` varchar(50) DEFAULT NULL,
  `lastname` varchar(50) DEFAULT NULL,
  `email` varchar(120) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `sex` enum('m','f') NOT NULL DEFAULT 'm',
  `dob` datetime NULL DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `is_deleted` bit(1) NOT NULL DEFAULT b'0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `users_phone_idx` (`phone`),
  KEY `users_firstname_lastname_idx` (`firstname`,`lastname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `user` (id, firstname, lastname, email, phone, sex, dob) VALUES
    (1, 'Alexandr', 'Volkov', 'alexandr25011987@gmail.com', '+380638144180', 'm', '1987-01-25'),
    (2, 'Oleh', 'Stanov', 'oleh9999@gmail.com', '+380678144180', 'm', '1985-05-21'),
    (3, 'Ivan', 'Pletnyov', 'felix1999@gmail.com', '+380668144180', 'm', '1983-02-16'),
    (4, 'Alexandr1', 'Volkov1', 'alexandr250119871@gmail.com', '+380638144181', 'm', '1987-01-25'),
    (5, 'Oleh1', 'Stanov1', 'oleh99919@gmail.com', '+380678144183', 'm', '1985-05-23'),
    (6, 'Ivan1', 'Pletnyov1', 'felix1919@gmail.com', '+380668144134', 'm', '1983-09-16');

-- список координирующих врачей
DROP TABLE IF EXISTS `doctor`;
CREATE TABLE `doctor` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `firstname` varchar(50) DEFAULT NULL,
  `lastname` varchar(50) DEFAULT NULL,
  `email` varchar(120) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `sex` enum('m','f') NOT NULL DEFAULT 'm',
  `dob` datetime NULL DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `is_deleted` bit(1) NOT NULL DEFAULT b'0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `users_phone_idx` (`phone`),
  KEY `users_firstname_lastname_idx` (`firstname`,`lastname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `doctor` (id, firstname, lastname, email, phone, sex, dob) VALUES
    (1, 'Olha', 'Vasiltsun', 'olha@gmail.com', '+380638544180', 'm', '1985-01-20'),
    (2, 'Nikolay', 'Petrento', 'nik111@gmail.com', '+380675464180', 'm', '1982-05-11'),
    (3, 'Michael', 'Pivkach', 'michael123@gmail.com', '+380668148980', 'm', '1983-08-16');

-- пациенты(пользователи) врачей
DROP TABLE IF EXISTS `patient_list`;
CREATE TABLE `patient_list` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `doctor_id` bigint(20) unsigned NOT NULL,
  `user_id` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `doctor_user` (`doctor_id`, `user_id`),
  CONSTRAINT `patient_list_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `patient_list_ibfk_2` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `patient_list` (id, doctor_id, user_id) VALUES
    (1, 1, 3),
    (2, 1, 2),
    (3, 2, 1),
    (4, 2, 6),
    (5, 3, 4),
    (6, 3, 5);

-- адрес пользователей
DROP TABLE IF EXISTS `address`;
CREATE TABLE `address` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL,
  `country` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL ,
  `street` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `address_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `address` (id, user_id, city, country, street) VALUES
    (1, 1, 'Ukraine', 'Mukachevo', 'Odesskaya'),
    (2, 1, 'Ukraine', 'Odessa', 'Lustdorfsakay'),
    (3, 4, 'Ukraine', 'Kiev', 'Mira'),
    (4, 3, 'Ukraine', 'Kharkov', 'Voznesenskaya'),
    (5, 6, 'Ukraine', 'Zaporozhe', 'Centralnaya'),
    (6, 5, 'Ukraine', 'Lvov', 'Bandery');

-- список возможных статусов выполнения заказа
DROP TABLE IF EXISTS `order_status`;
CREATE TABLE `order_status` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `status` varchar(255) DEFAULT NULL ,
  `comment` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `order_status` (id, status, comment) VALUES
    (1, 'new', 'New order'),
    (2, 'pending_payment', 'Waiting for payment'),
    (3, 'payed', 'Order payed'),
    (4, 'in_progress', 'Order in progress'),
    (5, 'completed', 'Order is completed');

-- заказ на проведение ДНК теста
DROP TABLE IF EXISTS `order`;
CREATE TABLE `order` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL,
  `status_id` bigint(20) unsigned NOT NULL ,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  CONSTRAINT `order_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `order_ibfk_2` FOREIGN KEY (`status_id`) REFERENCES `order_status` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `order` (id, user_id, status_id) VALUES
    (1, 3, 1),
    (2, 1, 3),
    (3, 4, 5),
    (4, 2, 2),
    (5, 6, 4);

DROP TABLE IF EXISTS `order_archive`;
CREATE TABLE `order_archive` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL,
  `status_id` bigint(20) unsigned NOT NULL ,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=Archive DEFAULT CHARSET=latin1;

-- оплата теста
DROP TABLE IF EXISTS `payment`;
CREATE TABLE `payment` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `order_id` bigint(20) unsigned NOT NULL,
  `total` bigint(20) unsigned NOT NULL ,
  `is_payed` bit(1) NOT NULL DEFAULT b'0',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `payment` (id, order_id, total, is_payed) VALUES
    (1, 1, 2500, b'1'),
    (2, 4, 5000, b'0'),
    (3, 3, 3400, b'1'),
    (4, 5, 1020, b'1');

DROP TABLE IF EXISTS `payment_archive`;
CREATE TABLE `payment_archive` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `order_id` bigint(20) unsigned NOT NULL,
  `total` bigint(20) unsigned NOT NULL ,
  `is_payed` bit(1) NOT NULL DEFAULT b'0',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=Archive DEFAULT CHARSET=latin1;

-- список генетических заболеваний
DROP TABLE IF EXISTS `disease`;
CREATE TABLE `disease` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL ,
  `code` varchar(255) DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `disease` (id, name, code) VALUES
    (1, 'Pathological Food Unacceptancy', 'SCN2A'),
    (2, 'Individual Disorder', 'SPATA5'),
    (3, 'Lexical Malfunction', 'SKRT3'),
    (4, 'Biological Incompatibility', 'KRT4S');

-- выявленные заболевания пользователя
DROP TABLE IF EXISTS `user_disease`;
CREATE TABLE `user_disease` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL,
  `disease_id` bigint(20) unsigned NOT NULL,
  `level` varchar(255) DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `user_disease_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `user_disease_ibfk_2` FOREIGN KEY (`disease_id`) REFERENCES `disease` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO `user_disease` (id, user_id, disease_id, level) VALUES
    (1, 4, 1, 5),
    (2, 4, 4, 8),
    (3, 4, 3, 1),
    (4, 6, 2, 9),
    (5, 6, 1, 2),
    (6, 6, 3, 5);

-- заключение врача
DROP TABLE IF EXISTS `conclusion`;
CREATE TABLE `conclusion` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `patient_list_id` bigint(20) unsigned NOT NULL,
  `content` text DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `conclusion_ibfk_1` FOREIGN KEY (`patient_list_id`) REFERENCES `patient_list` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `conclusion` (id, patient_list_id, content) VALUES
    (1, 5, 'No reportable genetic variants were identified by this analysis, however, this individual may still be at risk for certain medical
conditions based on other factors such as family history, genetic causes not evaluated with this test, or other environmental
influences. Follow up of this individual and surveillance of their family members may still be indicated');

-- 5. скрипты характерных выборок (включающие группировки, JOIN'ы, вложенные таблицы)

-- список пользователей которые оплатили заказы
select * from `user` as u
join `order` as o on o.user_id = u.id
join `payment` as p on o.id = p.order_id
where p.is_payed = 0;

-- кол-во пациентов у врачей
select d.firstname, count(u.id) from `user` as u
join `patient_list` as pl on pl.user_id = u.id
join `doctor` as d on pl.doctor_id = d.id
group by d.id;

-- получено денег всего за заказы
select sum(p.total) from `order` as o
join `payment` as p on o.id = p.order_id and p.is_payed = 1;


-- 6. представления (минимум 2)

create or replace view HigherThenAverageOrders(id, total)
AS
select o.id, p.total from `order` as o
join `payment` as p on o.id = p.order_id and p.is_payed = 1
where p.total > (
select avg(p.total) from `order` as o
join `payment` as p on o.id = p.order_id and p.is_payed = 1
);

select * from HigherThenAverageOrders;


create or replace view Top3MostCommonDisease(id, total)
AS
select d.name, count(ud.user_id) as popularity
from user_disease as ud
join disease as d on ud.disease_id = d.id
group by ud.disease_id
order by popularity desc
limit 3;

select * from Top3MostCommonDisease;


-- 7. хранимые процедуры / триггеры

DROP TRIGGER IF EXISTS after_delete_payment;

DELIMITER $$
$$
CREATE DEFINER=`root`@`localhost` TRIGGER after_delete_payment
AFTER DELETE
ON `payment` FOR EACH ROW
insert into payment_archive
(id, order_id, total, is_payed, created_at, updated_at)
values (old.id, old.order_id, old.total, old.is_payed, old.created_at, old.updated_at)$$
DELIMITER ;

delete from payment where rand() > 0.5;

DROP TRIGGER IF EXISTS after_delete_order;

DELIMITER $$
$$
CREATE DEFINER=`root`@`localhost` TRIGGER after_delete_order
AFTER DELETE
ON `order` FOR EACH ROW
insert into order_archive
(id, user_id, status_id)
values (old.id, old.user_id, old.status_id)$$
DELIMITER ;

delete `order` from `order`
left join `payment` as p on `order`.id = p.order_id
where p.id is null and status_id = 5;

