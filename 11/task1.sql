use `vk`;

DROP TABLE IF EXISTS `logs`;

CREATE TABLE `logs` (
  `table_name` varchar(100) DEFAULT NULL,
  `pk` bigint(20) unsigned DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=ARCHIVE DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `catalog`;

CREATE TABLE `catalog` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TRIGGER IF EXISTS afterinsert;

DELIMITER $$
$$
CREATE DEFINER=`root`@`localhost` TRIGGER after_insert_catalog
AFTER INSERT
ON `catalog` FOR EACH ROW
insert into logs
(`table_name`, `pk`, `name`)
values ('catalog', new.id, new.name)$$
DELIMITER ;

DROP TABLE if exists `product`;

CREATE TABLE `product` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TRIGGER IF EXISTS afterinsert;

DELIMITER $$
$$
CREATE DEFINER=`root`@`localhost` TRIGGER after_insert_product
AFTER INSERT
ON `product` FOR EACH ROW
insert into logs
(`table_name`, `pk`, `name`)
values ('product', new.id, new.name)$$
DELIMITER ;


insert into `catalog` (`name`) values ('test_catalog_name');
insert into `product` (`name`) values ('test_product_name');