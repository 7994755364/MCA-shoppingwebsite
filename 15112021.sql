/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - shopping_app
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`shopping_app` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `shopping_app`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add buyer',7,'add_buyer'),(20,'Can change buyer',7,'change_buyer'),(21,'Can delete buyer',7,'delete_buyer'),(22,'Can add cart',8,'add_cart'),(23,'Can change cart',8,'change_cart'),(24,'Can delete cart',8,'delete_cart'),(25,'Can add category',9,'add_category'),(26,'Can change category',9,'change_category'),(27,'Can delete category',9,'delete_category'),(28,'Can add delivery_boy',10,'add_delivery_boy'),(29,'Can change delivery_boy',10,'change_delivery_boy'),(30,'Can delete delivery_boy',10,'delete_delivery_boy'),(31,'Can add feedback',11,'add_feedback'),(32,'Can change feedback',11,'change_feedback'),(33,'Can delete feedback',11,'delete_feedback'),(34,'Can add location',12,'add_location'),(35,'Can change location',12,'change_location'),(36,'Can delete location',12,'delete_location'),(37,'Can add login',13,'add_login'),(38,'Can change login',13,'change_login'),(39,'Can delete login',13,'delete_login'),(40,'Can add order_sub',14,'add_order_sub'),(41,'Can change order_sub',14,'change_order_sub'),(42,'Can delete order_sub',14,'delete_order_sub'),(43,'Can add orders',15,'add_orders'),(44,'Can change orders',15,'change_orders'),(45,'Can delete orders',15,'delete_orders'),(46,'Can add payment',16,'add_payment'),(47,'Can change payment',16,'change_payment'),(48,'Can delete payment',16,'delete_payment'),(49,'Can add product',17,'add_product'),(50,'Can change product',17,'change_product'),(51,'Can delete product',17,'delete_product'),(52,'Can add rating',18,'add_rating'),(53,'Can change rating',18,'change_rating'),(54,'Can delete rating',18,'delete_rating'),(55,'Can add shops',19,'add_shops'),(56,'Can change shops',19,'change_shops'),(57,'Can delete shops',19,'delete_shops'),(58,'Can add order_assign',20,'add_order_assign'),(59,'Can change order_assign',20,'change_order_assign'),(60,'Can delete order_assign',20,'delete_order_assign'),(61,'Can add bank',21,'add_bank'),(62,'Can change bank',21,'change_bank'),(63,'Can delete bank',21,'delete_bank'),(64,'Can add offer',22,'add_offer'),(65,'Can change offer',22,'change_offer'),(66,'Can delete offer',22,'delete_offer');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `bank` */

DROP TABLE IF EXISTS `bank`;

CREATE TABLE `bank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bank_name` varchar(50) NOT NULL,
  `account_no` varchar(50) NOT NULL,
  `pin_no` varchar(50) NOT NULL,
  `balance` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `bank` */

insert  into `bank`(`id`,`bank_name`,`account_no`,`pin_no`,`balance`) values (1,'canara','12345','111','670.0'),(2,'SBI','67890','222','49900.0'),(3,'south indian','98765','333','60950.0');

/*Table structure for table `buyer` */

DROP TABLE IF EXISTS `buyer`;

CREATE TABLE `buyer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `buyer_name` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `house_no_name` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `pin` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `LOGIN_ID_id` int(11) NOT NULL,
  `district` varchar(50) NOT NULL,
  `post` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `buyer_LOGIN_ID_id_21b73a14_fk_login_id` (`LOGIN_ID_id`),
  CONSTRAINT `buyer_LOGIN_ID_id_21b73a14_fk_login_id` FOREIGN KEY (`LOGIN_ID_id`) REFERENCES `login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `buyer` */

insert  into `buyer`(`id`,`buyer_name`,`phone`,`email`,`house_no_name`,`place`,`pin`,`image`,`LOGIN_ID_id`,`district`,`post`) values (1,'abc','122365','asadhbs@gmail.com','125','kalpetta','673121','/media/img_m8qbZ9N.png',7,'wayanad','kalpetta'),(2,'xyz','525454','ada@gmail.com','11654','civil','673122','/media/img_xylileN.png',8,'wayanad','kaynatty'),(3,'Jaseera ','7994755603','jaseerakt97@gmfch.h','Txvh','Ambileri ','673122','/media/20211101-120932.jpg',16,'Wayanad','Muttil'),(4,'Anu','9995881006','jaseerakt7@gmail.com ','Sun34','Kakkavayal','673122','/media/20211101-120317.jpg',17,'Wayanad','Muttil');

/*Table structure for table `cart` */

DROP TABLE IF EXISTS `cart`;

CREATE TABLE `cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` varchar(50) NOT NULL,
  `BUYER_ID_id` int(11) NOT NULL,
  `PRODUCT_ID_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cart_BUYER_ID_id_cd0e8b3c_fk_buyer_id` (`BUYER_ID_id`),
  KEY `cart_PRODUCT_ID_id_8a3d291c_fk_product_id` (`PRODUCT_ID_id`),
  CONSTRAINT `cart_BUYER_ID_id_cd0e8b3c_fk_buyer_id` FOREIGN KEY (`BUYER_ID_id`) REFERENCES `buyer` (`id`),
  CONSTRAINT `cart_PRODUCT_ID_id_8a3d291c_fk_product_id` FOREIGN KEY (`PRODUCT_ID_id`) REFERENCES `product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=latin1;

/*Data for the table `cart` */

insert  into `cart`(`id`,`quantity`,`BUYER_ID_id`,`PRODUCT_ID_id`) values (45,'5',3,3),(48,'2',3,3),(49,'4',3,3);

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_name` varchar(50) NOT NULL,
  `image` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`id`,`cat_name`,`image`) values (2,'books','/media/20211105-161553.jpg'),(4,'grocery','/media/20211105-161606.jpg'),(5,'footwear','/media/20211105-142827.jpg'),(6,'textiles','/media/20211105-161641.jpg'),(7,'Bags','/media/20211105-161934.jpg'),(19,'electronics','/media/20211115-115746.jpg');

/*Table structure for table `delivery_boy` */

DROP TABLE IF EXISTS `delivery_boy`;

CREATE TABLE `delivery_boy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `delboy_name` varchar(50) NOT NULL,
  `house_no_name` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `post` varchar(50) NOT NULL,
  `pincode` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `LOGIN_ID_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `delivery_boy_LOGIN_ID_id_896ade55_fk_login_id` (`LOGIN_ID_id`),
  CONSTRAINT `delivery_boy_LOGIN_ID_id_896ade55_fk_login_id` FOREIGN KEY (`LOGIN_ID_id`) REFERENCES `login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `delivery_boy` */

insert  into `delivery_boy`(`id`,`delboy_name`,`house_no_name`,`place`,`post`,`pincode`,`phone`,`email`,`image`,`LOGIN_ID_id`) values (1,'arun','11b','calicut','calicut','3456','1124567','khnk@gmail.com','/media/aa_T6fb6Ve.JPG',4),(3,'uhj','xgfg','adfsdx','safdv','1312','5768','bb','/media/img_xylileN.png',6),(4,'anu','kjlj','calicut','calicut','6523','212365','asxv@gmail.com','/media/20211023-152809.jpg',9),(5,'manu','kjlj','calicut','calicut','6523','212365','asxv@gmail.com','/media/20211023-152936.jpg',10);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(21,'newapp','bank'),(7,'newapp','buyer'),(8,'newapp','cart'),(9,'newapp','category'),(10,'newapp','delivery_boy'),(11,'newapp','feedback'),(12,'newapp','location'),(13,'newapp','login'),(22,'newapp','offer'),(15,'newapp','orders'),(20,'newapp','order_assign'),(14,'newapp','order_sub'),(16,'newapp','payment'),(17,'newapp','product'),(18,'newapp','rating'),(19,'newapp','shops'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2021-10-22 03:52:12.522990'),(2,'auth','0001_initial','2021-10-22 03:52:25.225215'),(3,'admin','0001_initial','2021-10-22 03:52:27.959339'),(4,'admin','0002_logentry_remove_auto_add','2021-10-22 03:52:28.021837'),(5,'contenttypes','0002_remove_content_type_name','2021-10-22 03:52:29.693624'),(6,'auth','0002_alter_permission_name_max_length','2021-10-22 03:52:30.724826'),(7,'auth','0003_alter_user_email_max_length','2021-10-22 03:52:31.755952'),(8,'auth','0004_alter_user_username_opts','2021-10-22 03:52:31.818444'),(9,'auth','0005_alter_user_last_login_null','2021-10-22 03:52:32.599693'),(10,'auth','0006_require_contenttypes_0002','2021-10-22 03:52:32.662164'),(11,'auth','0007_alter_validators_add_error_messages','2021-10-22 03:52:32.740250'),(12,'auth','0008_alter_user_username_max_length','2021-10-22 03:52:33.849547'),(13,'auth','0009_alter_user_last_name_max_length','2021-10-22 03:52:34.849510'),(14,'newapp','0001_initial','2021-10-22 03:53:03.261093'),(15,'newapp','0002_auto_20211020_2147','2021-10-22 03:53:05.010943'),(16,'newapp','0003_rating_review','2021-10-22 03:53:06.026495'),(17,'sessions','0001_initial','2021-10-22 03:53:07.057668'),(18,'newapp','0004_product_shop_id','2021-10-22 07:31:42.961012'),(19,'newapp','0005_auto_20211022_1619','2021-10-22 10:49:11.092180'),(20,'newapp','0006_order_assign','2021-10-23 06:35:57.977314'),(21,'newapp','0007_auto_20211023_1207','2021-10-23 06:37:19.490825'),(22,'newapp','0008_auto_20211025_0941','2021-10-25 04:11:38.689443'),(23,'newapp','0009_bank','2021-10-26 07:10:31.717739'),(24,'newapp','0010_category_image','2021-11-05 08:48:09.030485'),(25,'newapp','0011_offer','2021-11-06 08:48:20.658485');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('6lvyf8jk0nkyg6z75f933cu21f5hzdj6','NzZhYjkwNDI3NGRlZTRlNjllNzM3YjUzOTYwNDM0MGNmNGFmODA1Mjp7ImNfaWQiOiIyIiwiZF9pZCI6IjEiLCJzaG9wX2lkIjozLCJwaWQiOiI1Iiwib2lkIjoiMiIsImxnIjoieWVzIiwibG9nb3V0IjoiMCJ9','2021-11-29 10:29:46.291607'),('dljkwpc01mlnp04pd6bolnj4vi3l8p0s','YmJlNjk1ZjgyZTQ5Yjg0ODU4NTAzODk3MTQ3OTE5NjZjYzc0NmZmYzp7ImxnIjoieWVzIn0=','2021-11-29 09:08:12.278826'),('v1nrpnypsork6nvn3oj1cqccjo08v71b','ZmI0MmJmNGZlMmE3ZjIyYzk0OGZhOGUzZTBlY2M3YzFiZDcxZDIzNzp7ImxnIjoibm8iLCJsb2dvdXQiOiIwIiwic2hvcF9pZCI6M30=','2021-11-29 09:31:38.283964');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `BUYER_ID_id` int(11) NOT NULL,
  `PRODUCT_ID_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `feedback_BUYER_ID_id_92f20745_fk_buyer_id` (`BUYER_ID_id`),
  KEY `feedback_PRODUCT_ID_id_d89d2f9a_fk_product_id` (`PRODUCT_ID_id`),
  CONSTRAINT `feedback_BUYER_ID_id_92f20745_fk_buyer_id` FOREIGN KEY (`BUYER_ID_id`) REFERENCES `buyer` (`id`),
  CONSTRAINT `feedback_PRODUCT_ID_id_d89d2f9a_fk_product_id` FOREIGN KEY (`PRODUCT_ID_id`) REFERENCES `product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`id`,`feedback`,`date`,`BUYER_ID_id`,`PRODUCT_ID_id`) values (1,'Gfv','2021-11-04',3,2),(2,'bad','2021-10-31',4,2),(3,'Oygbk','2021-11-04',3,5);

/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) NOT NULL,
  `time` varchar(50) NOT NULL,
  `latitude` varchar(50) NOT NULL,
  `longitude` varchar(50) NOT NULL,
  `DELIVERY_ID_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `location_DELIVERY_ID_id_0e9bfa34_fk_delivery_boy_id` (`DELIVERY_ID_id`),
  CONSTRAINT `location_DELIVERY_ID_id_0e9bfa34_fk_delivery_boy_id` FOREIGN KEY (`DELIVERY_ID_id`) REFERENCES `delivery_boy` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `location` */

insert  into `location`(`id`,`date`,`time`,`latitude`,`longitude`,`DELIVERY_ID_id`) values (2,'2021-11-15','10:16:18','11.258963430046236','75.78387839980346',3);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `usertype` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'user','user1','shop'),(3,'hhj1@gmail.com','12345','rejected'),(4,'khnk@gmail.com','5340','deliveryboy'),(6,'bb','11','deliveryboy'),(7,'buyer1','123','user'),(8,'buyer2','654','user'),(9,'asxv@gmail.com','3493','deliveryboy'),(10,'asxv@gmail.com','9330','deliveryboy'),(16,'aaa','a','user'),(17,'jaseerakt7@gmail.com ','9995881006','user'),(18,'woodland@gmail.com','woodland','shop');

/*Table structure for table `offer` */

DROP TABLE IF EXISTS `offer`;

CREATE TABLE `offer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity_1` varchar(50) NOT NULL,
  `quantity_2` varchar(50) NOT NULL,
  `discount` varchar(50) NOT NULL,
  `PRODUCT_ID_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `offer_PRODUCT_ID_id_8715fcb6_fk_product_id` (`PRODUCT_ID_id`),
  CONSTRAINT `offer_PRODUCT_ID_id_8715fcb6_fk_product_id` FOREIGN KEY (`PRODUCT_ID_id`) REFERENCES `product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `offer` */

insert  into `offer`(`id`,`quantity_1`,`quantity_2`,`discount`,`PRODUCT_ID_id`) values (1,'1','5','5',6),(2,'2','6','2',5),(3,'7','10','5',5),(4,'6','10','8',6);

/*Table structure for table `order_assign` */

DROP TABLE IF EXISTS `order_assign`;

CREATE TABLE `order_assign` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `DELBOY_ID_id` int(11) NOT NULL,
  `ORDER_ID_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `newapp_order_assign_DELBOY_ID_id_3d6a3e57_fk_delivery_boy_id` (`DELBOY_ID_id`),
  KEY `newapp_order_assign_ORDER_ID_id_1110fc02_fk_orders_id` (`ORDER_ID_id`),
  CONSTRAINT `newapp_order_assign_DELBOY_ID_id_3d6a3e57_fk_delivery_boy_id` FOREIGN KEY (`DELBOY_ID_id`) REFERENCES `delivery_boy` (`id`),
  CONSTRAINT `newapp_order_assign_ORDER_ID_id_1110fc02_fk_orders_id` FOREIGN KEY (`ORDER_ID_id`) REFERENCES `orders` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `order_assign` */

insert  into `order_assign`(`id`,`status`,`date`,`DELBOY_ID_id`,`ORDER_ID_id`) values (1,'pending','20211023-122302',1,1),(2,'delivered','2021-11-03',3,5),(3,'delivered','20211104-144925',3,11),(4,'delivered','20211104-145310',3,13),(5,'delivered','20211104-150119',3,13),(6,'delivered','20211106-094901',3,14),(7,'delivered','2021-11-04',3,16),(9,'delivered','20211111-111912',3,15),(10,'delivered','2021-11-06',3,20),(11,'pending','20211111-112034',3,28),(12,'pending','20211111-112236',3,24),(13,'pending','20211112-145518',1,16);

/*Table structure for table `order_sub` */

DROP TABLE IF EXISTS `order_sub`;

CREATE TABLE `order_sub` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` varchar(50) NOT NULL,
  `ORDER_ID_id` int(11) NOT NULL,
  `PRODUCT_ID_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_sub_ORDER_ID_id_7df01a5c_fk_orders_id` (`ORDER_ID_id`),
  KEY `order_sub_PRODUCT_ID_id_707d1f6e_fk_product_id` (`PRODUCT_ID_id`),
  CONSTRAINT `order_sub_ORDER_ID_id_7df01a5c_fk_orders_id` FOREIGN KEY (`ORDER_ID_id`) REFERENCES `orders` (`id`),
  CONSTRAINT `order_sub_PRODUCT_ID_id_707d1f6e_fk_product_id` FOREIGN KEY (`PRODUCT_ID_id`) REFERENCES `product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

/*Data for the table `order_sub` */

insert  into `order_sub`(`id`,`quantity`,`ORDER_ID_id`,`PRODUCT_ID_id`) values (1,'4',1,2),(4,'2',3,2),(5,'2',5,2),(9,'3',8,3),(13,'1',11,5),(14,'2',11,6),(15,'3',12,3),(16,'1',13,5),(17,'3',18,6),(18,'3',19,6),(19,'4',20,6),(20,'4',21,6),(21,'4',22,6),(22,'2',23,6),(23,'2',24,6),(24,'2',25,6),(25,'2',26,6),(26,'2',27,6),(27,'2',28,6),(28,'8',29,3),(29,'1',30,6),(30,'1',31,3);

/*Table structure for table `orders` */

DROP TABLE IF EXISTS `orders`;

CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) NOT NULL,
  `amount` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `BUYER_ID_id` int(11) NOT NULL,
  `SHOP_ID_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_BUYER_ID_id_30636bcf_fk_buyer_id` (`BUYER_ID_id`),
  KEY `orders_SHOP_ID_id_2834b968_fk_shops_id` (`SHOP_ID_id`),
  CONSTRAINT `orders_BUYER_ID_id_30636bcf_fk_buyer_id` FOREIGN KEY (`BUYER_ID_id`) REFERENCES `buyer` (`id`),
  CONSTRAINT `orders_SHOP_ID_id_2834b968_fk_shops_id` FOREIGN KEY (`SHOP_ID_id`) REFERENCES `shops` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;

/*Data for the table `orders` */

insert  into `orders`(`id`,`date`,`amount`,`status`,`BUYER_ID_id`,`SHOP_ID_id`) values (1,'2021-10-08','400','assigned',1,2),(2,'2021-10-10','500','pending',2,2),(3,'2021-10-21','750','pending',2,2),(4,'2021-10-22','300','completed',1,2),(5,'2021-11-03','1000.0','pending',3,2),(8,'2021-11-03','1650.0','pending',3,1),(11,'2021-11-03','1850.0','assigned',3,3),(12,'2021-11-03','1650.0','pending',3,1),(13,'2021-11-04','450.0','assigned',3,3),(14,'2021-11-05','900.0','assigned',3,3),(15,'2021-11-05','900.0','assigned',3,3),(16,'2021-11-05','900.0','assigned',3,3),(17,'2021-11-05','1400.0','pending',3,3),(18,'2021-11-05','2100.0','pending',3,3),(19,'2021-11-05','2100.0','pending',3,3),(20,'2021-11-08','2800.0','pending',3,3),(21,'2021-11-08','2800.0','pending',3,3),(22,'2021-11-08','2800.0','pending',3,3),(23,'2021-11-08','1400.0','pending',3,3),(24,'2021-11-08','1400.0','assigned',3,3),(25,'2021-11-08','1330.0','pending',3,3),(26,'2021-11-08','1330.0','pending',3,3),(27,'2021-11-08','1330.0','pending',3,3),(28,'2021-11-08','1330.0','assigned',3,3),(29,'2021-11-12','4400.0','pending',3,1),(30,'2021-11-12','700.0','pending',3,3),(31,'2021-11-12','550.0','pending',3,1);

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` varchar(50) NOT NULL,
  `account_no` varchar(50) NOT NULL,
  `ORDER_ID_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `payment_ORDER_ID_id_f76efc08_fk_orders_id` (`ORDER_ID_id`),
  CONSTRAINT `payment_ORDER_ID_id_f76efc08_fk_orders_id` FOREIGN KEY (`ORDER_ID_id`) REFERENCES `orders` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`id`,`amount`,`account_no`,`ORDER_ID_id`) values (6,'1850.0','98765',11),(7,'1650.0','98765',12),(8,'450.0','67890',13),(9,'900.0','12345',14),(10,'900.0','12345',15),(11,'900.0','67890',16),(12,'1400.0','12345',17),(13,'2100.0','12345',18),(14,'2100.0','12345',19),(15,'2800.0','12345',20),(16,'2800.0','12345',21),(17,'2800.0','12345',22),(18,'1400.0','12345',23),(19,'1400.0','12345',24),(20,'1330.0','12345',25),(21,'1330.0','12345',26),(22,'1330.0','12345',27),(23,'1330.0','12345',28),(24,'4400.0','67890',29),(25,'700.0','67890',30),(26,'550.0','98765',31);

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(50) NOT NULL,
  `product_rate` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `PRODUCT_CATEGORY_id` int(11) NOT NULL,
  `SHOP_ID_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_PRODUCT_CATEGORY_id_d5baabb1_fk_category_id` (`PRODUCT_CATEGORY_id`),
  KEY `product_SHOP_ID_id_1f143cbb_fk_shops_id` (`SHOP_ID_id`),
  CONSTRAINT `product_PRODUCT_CATEGORY_id_d5baabb1_fk_category_id` FOREIGN KEY (`PRODUCT_CATEGORY_id`) REFERENCES `category` (`id`),
  CONSTRAINT `product_SHOP_ID_id_1f143cbb_fk_shops_id` FOREIGN KEY (`SHOP_ID_id`) REFERENCES `shops` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`id`,`product_name`,`product_rate`,`image`,`PRODUCT_CATEGORY_id`,`SHOP_ID_id`) values (2,'novel','500','/media/20211022-141637.jpg',2,2),(3,'top','550','/media/20211103-123352.jpg',6,1),(4,'kurthi','780','/media/20211103-123419.jpg',6,1),(5,'chappel','450','/media/20211103-124053.jpg',5,3),(6,'shoe','700','/media/20211103-124115.jpg',5,3);

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `SHOP_ID_id` int(11) NOT NULL,
  `USER_ID_id` int(11) NOT NULL,
  `review` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rating_SHOP_ID_id_04bffd54_fk_shops_id` (`SHOP_ID_id`),
  KEY `rating_USER_ID_id_073cdb63_fk_buyer_id` (`USER_ID_id`),
  CONSTRAINT `rating_SHOP_ID_id_04bffd54_fk_shops_id` FOREIGN KEY (`SHOP_ID_id`) REFERENCES `shops` (`id`),
  CONSTRAINT `rating_USER_ID_id_073cdb63_fk_buyer_id` FOREIGN KEY (`USER_ID_id`) REFERENCES `buyer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`id`,`rating`,`date`,`SHOP_ID_id`,`USER_ID_id`,`review`) values (1,'4','2021-10-21',1,1,'good'),(2,'3','2020-12-3',3,2,'nice'),(3,'2','2021-9-28',3,1,'sdf'),(4,'3','2021-8-11',3,2,'saf'),(5,'2','2021-11-12',3,3,'Really nice product'),(6,'3','2021-11-12',2,3,'Ljvn khbn');

/*Table structure for table `shops` */

DROP TABLE IF EXISTS `shops`;

CREATE TABLE `shops` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gst_in` varchar(50) NOT NULL,
  `shop_name` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `post` varchar(50) NOT NULL,
  `pincode` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `latitude` varchar(100) NOT NULL,
  `longitude` varchar(100) NOT NULL,
  `LOGIN_ID_id` int(11) NOT NULL,
  `category` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shops_LOGIN_ID_id_3619e91c_fk_login_id` (`LOGIN_ID_id`),
  CONSTRAINT `shops_LOGIN_ID_id_3619e91c_fk_login_id` FOREIGN KEY (`LOGIN_ID_id`) REFERENCES `login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `shops` */

insert  into `shops`(`id`,`gst_in`,`shop_name`,`place`,`post`,`pincode`,`phone`,`email`,`image`,`latitude`,`longitude`,`LOGIN_ID_id`,`category`) values (1,'123','cff','khhj','clt','234','12345','ikhhj','/media/an.jpg','11.5517','76.0403',2,'footwear'),(2,'123','sindur','klpt','edg','673121','12345','hhj1@gmail.com','/media/img.png','11.6103','76.0828',3,'textiles'),(3,'4567','woodland','meppadi','meppadi','65445','77777777','woodland@gmail.com','/media/20211103-123812.jpg','11.5550','76.1349',18,'footwear');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
