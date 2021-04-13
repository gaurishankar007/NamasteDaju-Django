-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: restaurant
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ac_profile`
--

DROP TABLE IF EXISTS `ac_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ac_profile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `gender` varchar(10) NOT NULL,
  `profile_pic` varchar(100) NOT NULL,
  `created_date` datetime(6) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `staff` tinyint(1),
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `Ac_profile_user_id_c29a35e6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ac_profile`
--

LOCK TABLES `ac_profile` WRITE;
/*!40000 ALTER TABLE `ac_profile` DISABLE KEYS */;
INSERT INTO `ac_profile` VALUES (2,NULL,NULL,'haribahadur123',NULL,NULL,'','static/images/uploads/profiles/default_profile.jpg','2021-03-25 11:49:58.307669',3,0),(3,'Gauri Shankar','Sharma','gauri007','gaurisharma358@gmail.com','9816346714','Male','static/images/uploads/profiles/C5_yljPOWR.png','2021-03-25 11:50:27.879066',4,0),(5,NULL,NULL,'samir002',NULL,NULL,'','static/images/uploads/profiles/default_profile.jpg','2021-04-12 22:07:18.775316',6,0),(6,NULL,NULL,'softwarica',NULL,NULL,'','static/images/uploads/profiles/default_profile.jpg','2021-04-12 22:08:21.389334',7,1);
/*!40000 ALTER TABLE `ac_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add reservation',7,'add_reservation'),(26,'Can change reservation',7,'change_reservation'),(27,'Can delete reservation',7,'delete_reservation'),(28,'Can view reservation',7,'view_reservation'),(29,'Can add gallery',8,'add_gallery'),(30,'Can change gallery',8,'change_gallery'),(31,'Can delete gallery',8,'delete_gallery'),(32,'Can view gallery',8,'view_gallery'),(33,'Can add menu',9,'add_menu'),(34,'Can change menu',9,'change_menu'),(35,'Can delete menu',9,'delete_menu'),(36,'Can view menu',9,'view_menu'),(37,'Can add stories',10,'add_stories'),(38,'Can change stories',10,'change_stories'),(39,'Can delete stories',10,'delete_stories'),(40,'Can view stories',10,'view_stories'),(41,'Can add catering',11,'add_catering'),(42,'Can change catering',11,'change_catering'),(43,'Can delete catering',11,'delete_catering'),(44,'Can view catering',11,'view_catering'),(45,'Can add message',12,'add_message'),(46,'Can change message',12,'change_message'),(47,'Can delete message',12,'delete_message'),(48,'Can view message',12,'view_message'),(49,'Can add order',13,'add_order'),(50,'Can change order',13,'change_order'),(51,'Can delete order',13,'delete_order'),(52,'Can view order',13,'view_order'),(53,'Can add cart',14,'add_cart'),(54,'Can change cart',14,'change_cart'),(55,'Can delete cart',14,'delete_cart'),(56,'Can view cart',14,'view_cart'),(57,'Can add profile',15,'add_profile'),(58,'Can change profile',15,'change_profile'),(59,'Can delete profile',15,'delete_profile'),(60,'Can view profile',15,'view_profile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$216000$O0RLLZEUYjgh$rdsnAGTD2zYEPnhgEONTxRKz0GUP5hwW+mUCUbfg1SY=','2021-04-13 09:12:01.134407',1,'gaurishankar007','','','gaurisharma358@gmail.com',1,1,'2021-03-25 11:43:45.287201'),(3,'pbkdf2_sha256$216000$56j6xSKGQuVb$heSyTkbG4mzciPotmQ8fJ22qE2m6wTRfLG7xAQvdXAc=','2021-04-12 21:56:23.374256',0,'haribahadur123','','','',0,1,'2021-03-25 11:49:58.187990'),(4,'pbkdf2_sha256$216000$d3gQQm6Q0qZj$gVUUV3XlZh0m/L0ftpfQE4BfIeIdh/RPVhNTkbHdfI0=','2021-04-13 09:06:37.903548',0,'gauri007','','','',0,1,'2021-03-25 11:50:27.758353'),(6,'pbkdf2_sha256$216000$I9FfN51etO7l$gazW926z9oAHAfAh6GpdTTWfezeOPKij5VASno3+k/8=','2021-04-13 04:38:49.610324',0,'samir002','','','',0,1,'2021-04-12 22:07:18.582078'),(7,'pbkdf2_sha256$216000$kvzTCrwpqmX7$1ah4Aq/Y7w98qFDyL3OPDqcOPf4A56XTPkzruLYrucc=','2021-04-13 04:37:55.789611',0,'softwarica','','','',1,1,'2021-04-12 22:08:21.261431');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (15,'Ac','profile'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(14,'Nd','cart'),(11,'Nd','catering'),(8,'Nd','gallery'),(9,'Nd','menu'),(12,'Nd','message'),(13,'Nd','order'),(7,'Nd','reservation'),(10,'Nd','stories'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-03-25 11:42:19.191159'),(2,'auth','0001_initial','2021-03-25 11:42:19.825101'),(3,'Ac','0001_initial','2021-03-25 11:42:22.184695'),(4,'Ac','0002_profile_staff','2021-03-25 11:42:22.523901'),(5,'Nd','0001_initial','2021-03-25 11:42:22.598701'),(6,'Nd','0002_gallery_menu','2021-03-25 11:42:22.760661'),(7,'Nd','0003_auto_20210312_1309','2021-03-25 11:42:22.771655'),(8,'Nd','0004_stories','2021-03-25 11:42:22.861391'),(9,'Nd','0005_auto_20210313_1820','2021-03-25 11:42:22.966111'),(10,'Nd','0006_auto_20210313_1846','2021-03-25 11:42:23.796122'),(11,'Nd','0007_auto_20210313_1847','2021-03-25 11:42:23.826041'),(12,'Nd','0008_auto_20210313_1850','2021-03-25 11:42:24.107366'),(13,'Nd','0009_auto_20210314_1310','2021-03-25 11:42:27.214975'),(14,'Nd','0010_auto_20210314_1323','2021-03-25 11:42:27.227887'),(15,'Nd','0011_auto_20210314_1417','2021-03-25 11:42:28.133158'),(16,'Nd','0012_auto_20210316_1909','2021-03-25 11:42:30.128025'),(17,'Nd','0013_auto_20210316_1944','2021-03-25 11:42:30.586139'),(18,'Nd','0014_auto_20210319_0841','2021-03-25 11:42:30.703040'),(19,'Nd','0015_auto_20210320_2034','2021-03-25 11:42:30.931428'),(20,'Nd','0016_auto_20210320_2148','2021-03-25 11:42:32.090335'),(21,'Nd','0017_auto_20210320_2259','2021-03-25 11:42:33.098946'),(22,'Nd','0018_auto_20210321_1059','2021-03-25 11:42:33.301405'),(23,'Nd','0019_auto_20210321_1101','2021-03-25 11:42:33.995772'),(24,'Nd','0020_auto_20210321_1142','2021-03-25 11:42:34.216441'),(25,'Nd','0021_order_order_date','2021-03-25 11:42:34.288248'),(26,'Nd','0022_auto_20210321_1200','2021-03-25 11:42:34.319166'),(27,'Nd','0023_auto_20210321_1213','2021-03-25 11:42:34.331134'),(28,'Nd','0024_auto_20210323_1734','2021-03-25 11:42:34.342104'),(29,'Nd','0025_auto_20210323_1747','2021-03-25 11:42:34.819983'),(30,'Nd','0026_auto_20210323_1810','2021-03-25 11:42:35.186362'),(31,'Nd','0027_auto_20210323_1920','2021-03-25 11:42:36.085796'),(32,'Nd','0028_auto_20210323_2127','2021-03-25 11:42:37.018838'),(33,'Nd','0029_auto_20210323_2234','2021-03-25 11:42:37.669862'),(34,'Nd','0030_cart','2021-03-25 11:42:37.962079'),(35,'Nd','0031_auto_20210325_1541','2021-03-25 11:42:38.619528'),(36,'Nd','0032_auto_20210325_1555','2021-03-25 11:42:38.940668'),(37,'Nd','0033_auto_20210325_1710','2021-03-25 11:42:40.340797'),(38,'Nd','0034_remove_order_foodname','2021-03-25 11:42:40.620696'),(39,'Nd','0035_order_foodname','2021-03-25 11:42:40.833278'),(40,'admin','0001_initial','2021-03-25 11:42:40.925036'),(41,'admin','0002_logentry_remove_auto_add','2021-03-25 11:42:41.358257'),(42,'admin','0003_logentry_add_action_flag_choices','2021-03-25 11:42:41.378187'),(43,'contenttypes','0002_remove_content_type_name','2021-03-25 11:42:42.170907'),(44,'auth','0002_alter_permission_name_max_length','2021-03-25 11:42:42.371685'),(45,'auth','0003_alter_user_email_max_length','2021-03-25 11:42:42.556410'),(46,'auth','0004_alter_user_username_opts','2021-03-25 11:42:42.573337'),(47,'auth','0005_alter_user_last_login_null','2021-03-25 11:42:42.761832'),(48,'auth','0006_require_contenttypes_0002','2021-03-25 11:42:42.770808'),(49,'auth','0007_alter_validators_add_error_messages','2021-03-25 11:42:42.788761'),(50,'auth','0008_alter_user_username_max_length','2021-03-25 11:42:42.997201'),(51,'auth','0009_alter_user_last_name_max_length','2021-03-25 11:42:43.186124'),(52,'auth','0010_alter_group_name_max_length','2021-03-25 11:42:43.223038'),(53,'auth','0011_update_proxy_permissions','2021-03-25 11:42:43.240987'),(54,'auth','0012_alter_user_first_name_max_length','2021-03-25 11:42:43.681031'),(55,'sessions','0001_initial','2021-03-25 11:42:43.769794'),(56,'Nd','0036_auto_20210325_1957','2021-03-25 14:13:11.926514'),(57,'Nd','0037_auto_20210325_1958','2021-03-25 14:13:38.623983'),(58,'Nd','0038_remove_cart_quantity','2021-03-25 14:50:58.578176');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4hles97niaywnx8y649qii2jem4n316o','.eJxVjDsOwjAQRO_iGln-xoaSnjNY6901DiBHipMKcXcSKQVMOe_NvEWCdalp7TynkcRFaHH67TLgk9sO6AHtPkmc2jKPWe6KPGiXt4n4dT3cv4MKvW5rj1SM8YPFaJXK5JyPGIhNYCjqXEAb58hn5zHEqBnZBbVl0DaqbK34fAHcnTcu:1lUW17:6E0rjUMhTg5aQQB12eqFI0AS_nZzXzwG7LFRKZMXGxM','2021-04-22 14:52:21.784512');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nd_cart`
--

DROP TABLE IF EXISTS `nd_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nd_cart` (
  `id` int NOT NULL AUTO_INCREMENT,
  `phone` varchar(10) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `username_id` int DEFAULT NULL,
  `foodname_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Nd_cart_username_id_fc338c6f_fk_auth_user_id` (`username_id`),
  KEY `Nd_cart_foodname_id_3c4e63eb_fk_Nd_menu_id` (`foodname_id`),
  CONSTRAINT `Nd_cart_foodname_id_3c4e63eb_fk_Nd_menu_id` FOREIGN KEY (`foodname_id`) REFERENCES `nd_menu` (`id`),
  CONSTRAINT `Nd_cart_username_id_fc338c6f_fk_auth_user_id` FOREIGN KEY (`username_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nd_cart`
--

LOCK TABLES `nd_cart` WRITE;
/*!40000 ALTER TABLE `nd_cart` DISABLE KEYS */;
INSERT INTO `nd_cart` VALUES (53,NULL,NULL,3,2),(54,NULL,NULL,3,7);
/*!40000 ALTER TABLE `nd_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nd_catering`
--

DROP TABLE IF EXISTS `nd_catering`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nd_catering` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(254) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time(6) DEFAULT NULL,
  `event_type` varchar(50) DEFAULT NULL,
  `catering_type` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `catering_order_date` datetime(6) DEFAULT NULL,
  `completion` tinyint(1) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `username_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Nd_catering_username_id_4313accd` (`username_id`),
  CONSTRAINT `Nd_catering_username_id_4313accd_fk_auth_user_id` FOREIGN KEY (`username_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nd_catering`
--

LOCK TABLES `nd_catering` WRITE;
/*!40000 ALTER TABLE `nd_catering` DISABLE KEYS */;
INSERT INTO `nd_catering` VALUES (5,'gaurisharma371@gmail.com','9804756134','2021-04-30','03:46:00.000000','Conferences','On-promise',NULL,'2021-04-12 21:58:21.708317',0,'Pink','Floyd',3),(8,'gaurisharma371@gmail.com','9804756134','2021-04-17','09:46:00.000000','Birthday Parties','On-promise',NULL,'2021-04-13 03:58:57.511118',1,'Pink','Floyd',4);
/*!40000 ALTER TABLE `nd_catering` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nd_gallery`
--

DROP TABLE IF EXISTS `nd_gallery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nd_gallery` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `uploaded_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nd_gallery`
--

LOCK TABLES `nd_gallery` WRITE;
/*!40000 ALTER TABLE `nd_gallery` DISABLE KEYS */;
INSERT INTO `nd_gallery` VALUES (1,'One','static/images/uploads/gallery/1.png','2021-03-25 12:02:44.474436'),(2,'two','static/images/uploads/gallery/2.png','2021-03-25 12:02:59.023938'),(3,'Three','static/images/uploads/gallery/3.png','2021-03-25 12:03:11.377960'),(4,'Four','static/images/uploads/gallery/4.png','2021-03-25 12:03:21.726902'),(5,'Five','static/images/uploads/gallery/5.png','2021-03-25 12:03:29.958608'),(6,'Six','static/images/uploads/gallery/6.png','2021-03-25 12:03:37.889043'),(7,'Seven','static/images/uploads/gallery/image_1.jpg','2021-03-25 12:04:00.050326'),(8,'Eight','static/images/uploads/gallery/insta-2.jpg','2021-03-25 12:04:14.727715'),(9,'Nine','static/images/uploads/gallery/insta-4.jpg','2021-03-25 12:04:28.443073'),(10,'Ten','static/images/uploads/gallery/insta-6.jpg','2021-03-25 12:04:41.943399'),(11,'Eleven','static/images/uploads/gallery/food_9.jpg','2021-04-12 19:12:10.555425'),(12,'Twelve','static/images/uploads/gallery/food_23.jpg','2021-04-12 21:47:04.688355'),(13,'Thirteen','static/images/uploads/gallery/food_32.jpg','2021-04-12 21:47:26.070629'),(14,'Fourteen','static/images/uploads/gallery/food_29.jpg','2021-04-12 21:47:38.327564'),(15,'Fifteen','static/images/uploads/gallery/food_4.jpg','2021-04-12 21:47:56.336357'),(16,'Sixteen','static/images/uploads/gallery/food_2.jpg','2021-04-12 21:48:05.229059'),(17,'Seventeen','static/images/uploads/gallery/food_5.jpg','2021-04-12 21:48:17.425482'),(18,'Eighteen','static/images/uploads/gallery/food_21.jpg','2021-04-12 21:48:34.259518'),(19,'Nineteen','static/images/uploads/gallery/food_22.jpg','2021-04-12 21:49:09.582145'),(20,'Tweenty','static/images/uploads/gallery/Sandwich-bread-fast-food_3840x2160.jpg','2021-04-12 21:49:25.838010'),(21,'Twenty one','static/images/uploads/gallery/Bangkok-Moves-Up-the-Food-Chain-2.jpg','2021-04-12 22:13:20.285468');
/*!40000 ALTER TABLE `nd_gallery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nd_menu`
--

DROP TABLE IF EXISTS `nd_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nd_menu` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `category` varchar(200) DEFAULT NULL,
  `uploaded_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nd_menu`
--

LOCK TABLES `nd_menu` WRITE;
/*!40000 ALTER TABLE `nd_menu` DISABLE KEYS */;
INSERT INTO `nd_menu` VALUES (1,'MOMOS','Vegetables, Meat, Flower',150,'static/images/uploads/menu/breakfast-5.jpg','Breakfast','2021-03-25 11:46:37.304870'),(2,'Chaumin','Noddles, Vegetables',100,'static/images/uploads/menu/breakfast-1.jpg','Lunch','2021-03-25 11:47:00.340533'),(3,'Pasta','Noddles, Vegetables',100,'static/images/uploads/menu/breakfast-2.jpg','Dinner','2021-03-25 11:47:30.531102'),(4,'Ice-Cream','Milk, Chocolate',80,'static/images/uploads/menu/breakfast-3.jpg','Deserts','2021-03-25 11:47:53.463684'),(5,'Coffee','Milk, Chocolate',80,'static/images/uploads/menu/coffe.jpg','Drinks & Tea','2021-03-25 11:48:14.409366'),(6,'Gorkha Wine','Alcolhol,',400,'static/images/uploads/menu/food_19.jpg','Wine Card','2021-03-25 11:48:42.560128'),(7,'Chocolate','Milk, Chocolate',200,'static/images/uploads/menu/food_22.jpg','Deserts','2021-04-12 19:09:45.223182'),(10,'Fish','Vegetables, Meat, Flower',200,'static/images/uploads/menu/1013412.jpg','Dinner','2021-04-12 22:12:10.619667');
/*!40000 ALTER TABLE `nd_menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nd_message`
--

DROP TABLE IF EXISTS `nd_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nd_message` (
  `id` int NOT NULL AUTO_INCREMENT,
  `subject` varchar(50) DEFAULT NULL,
  `messages` longtext,
  `messaged_date` datetime(6) DEFAULT NULL,
  `username_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Nd_message_username_id_c77f5356` (`username_id`),
  CONSTRAINT `Nd_message_username_id_c77f5356_fk_auth_user_id` FOREIGN KEY (`username_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nd_message`
--

LOCK TABLES `nd_message` WRITE;
/*!40000 ALTER TABLE `nd_message` DISABLE KEYS */;
INSERT INTO `nd_message` VALUES (4,'Want to get job','please give me a job in your restaurant. I am highly skilled.','2021-04-12 22:06:39.331713',4),(5,'job','aksdjflksjfksadjflkajsdlkfjsldkf','2021-04-13 03:58:30.214427',4);
/*!40000 ALTER TABLE `nd_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nd_order`
--

DROP TABLE IF EXISTS `nd_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nd_order` (
  `id` int NOT NULL AUTO_INCREMENT,
  `phone` varchar(10) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `completion` tinyint(1) DEFAULT NULL,
  `username_id` int DEFAULT NULL,
  `ordered_date` datetime(6),
  `foodname_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Nd_order_username_id_15c296d4` (`username_id`),
  KEY `Nd_order_foodname_id_faf67a46_fk_Nd_menu_id` (`foodname_id`),
  CONSTRAINT `Nd_order_foodname_id_faf67a46_fk_Nd_menu_id` FOREIGN KEY (`foodname_id`) REFERENCES `nd_menu` (`id`),
  CONSTRAINT `Nd_order_username_id_15c296d4_fk_auth_user_id` FOREIGN KEY (`username_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nd_order`
--

LOCK TABLES `nd_order` WRITE;
/*!40000 ALTER TABLE `nd_order` DISABLE KEYS */;
INSERT INTO `nd_order` VALUES (36,'9804756134',1,'Balkot, Kathmandu',1,3,'2021-04-12 17:30:09.350625',1),(38,'9804756134',1,'Kathmadu, putalisadak, street 45004',0,4,'2021-04-12 18:48:15.514906',2),(48,'9816346714',1,'Kathmadu, putalisadak, street 45004',1,4,'2021-04-12 22:04:17.450226',4),(49,'9816346714',1,'Kathmadu, putalisadak, street 45004',0,4,'2021-04-12 22:04:17.527582',6);
/*!40000 ALTER TABLE `nd_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nd_reservation`
--

DROP TABLE IF EXISTS `nd_reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nd_reservation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(254) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time(6) DEFAULT NULL,
  `person` varchar(2) DEFAULT NULL,
  `reserved_date` datetime(6) DEFAULT NULL,
  `completion` tinyint(1),
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `username_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Nd_reservation_username_id_bb97796c` (`username_id`),
  CONSTRAINT `Nd_reservation_username_id_bb97796c_fk_auth_user_id` FOREIGN KEY (`username_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nd_reservation`
--

LOCK TABLES `nd_reservation` WRITE;
/*!40000 ALTER TABLE `nd_reservation` DISABLE KEYS */;
INSERT INTO `nd_reservation` VALUES (3,'gaurisharma371@gmail.com','9804756134','2021-04-23','00:02:00.000000','3','2021-04-12 19:14:52.246777',1,'Pink','Floyd',3),(5,'gaurisharma358@gmail.com','9816346714','2021-04-24','03:53:00.000000','2','2021-04-12 22:05:24.361823',0,'Gauri Shankar','Sharma',4);
/*!40000 ALTER TABLE `nd_reservation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nd_stories`
--

DROP TABLE IF EXISTS `nd_stories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nd_stories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `detail` longtext,
  `uploaded_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nd_stories`
--

LOCK TABLES `nd_stories` WRITE;
/*!40000 ALTER TABLE `nd_stories` DISABLE KEYS */;
INSERT INTO `nd_stories` VALUES (1,'Mother','static/images/uploads/stories/bg_4.jpg','My mother-in-law is one of the top servers at one of the top chains of semi-luxurious restaurants. A lot of the people that go there are well-enough off that they think they’re untouchable and can get away with anything.\r\n\r\nIn comes this table who decides their server is just a little too black. They take it upon themselves to let the poor young man know just how much his blackness bothered them before demanding a new server. The server goes to the back and (like everyone else who’s ever worked in a restaurant) starts venting on his way to a manager','2021-03-25 12:06:32.215103'),(2,'Drop','static/images/uploads/stories/image_2.jpg','“I don’t need to write your order because I won’t be putting it in. I just wanted to show you how a decent human being is supposed to treat others, even when they don’t like the other person.”\r\n\r\nWith that, she turned around to walk away. They stop her to demand the big boss in the building, to which she responded by pointing out her manager: the biggest angry-looking black man wearing a suit that day.\r\n\r\nThe table got up and left without a word.','2021-03-25 12:07:10.179397'),(3,'MOMO','static/images/uploads/stories/food_20.jpg','It might seem a strange thing to say for a restaurant, but your customers aren’t just interested in your food.  They want to know your history, why you started your restaurant, what your values are and what your vision is. A great menu and a beautifully decorated restaurant are obviously important, but sharing your restaurant’s story is effective, adding some marketing magic to your mix. Your restaurant’s story is what makes you unique.','2021-03-25 12:07:56.460252'),(4,'Hahaha','static/images/uploads/stories/food_7.jpg','Begin at the Beginning. Your customers want to feel part of your journey, so start at the beginning. Share the key moment you knew you wanted to open your restaurant and why. Were you inspired by anyone in your life, or did you have a lightbulb moment? Sharing all these parts of your story, including highlights and any low points is important to create an authentic connection with your customers.','2021-03-25 12:08:31.404055'),(6,'Gauri','static/images/uploads/stories/50-504459_fast-food-4k.jpg','It might seem a strange thing to say for a restaurant, but your customers aren’t just interested in your food. They want to know your history, why you started your restaurant, what your values are and what your vision is. A great menu and a beautifully decorated restaurant are obviously important, but sharing your restaurant’s story is effective, adding some marketing magic to your mix. Your restaurant’s story is what makes you unique. Storytelling creates an instant emotional and engaging connection with your customers. Customers resonate with a great story and having one makes it easier to develop strong marketing campaigns through social media channels so it’s important to get it right.','2021-04-12 22:14:00.652600');
/*!40000 ALTER TABLE `nd_stories` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-13 17:51:22
