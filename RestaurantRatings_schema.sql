-- MySQL dump 10.13  Distrib 8.0.0-dmr, for osx10.11 (x86_64)
--
-- Host: localhost    Database: RestaurantRatings
-- ------------------------------------------------------
-- Server version	8.0.0-dmr

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Categorizes`
--

DROP TABLE IF EXISTS `Categorizes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Categorizes` (
  `restaurant_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`restaurant_id`,`tag_id`),
  KEY `tag_id` (`tag_id`),
  CONSTRAINT `categorizes_ibfk_1` FOREIGN KEY (`restaurant_id`) REFERENCES `Restaurant` (`restaurant_id`),
  CONSTRAINT `categorizes_ibfk_2` FOREIGN KEY (`tag_id`) REFERENCES `Tag` (`tag_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Dish`
--

DROP TABLE IF EXISTS `Dish`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Dish` (
  `dish_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text,
  `price` decimal(10,2) NOT NULL,
  `restaurant_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`dish_id`),
  KEY `restaurant_id` (`restaurant_id`),
  CONSTRAINT `dish_ibfk_1` FOREIGN KEY (`restaurant_id`) REFERENCES `Restaurant` (`restaurant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Offers`
--

DROP TABLE IF EXISTS `Offers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Offers` (
  `restaurant_id` int(11) NOT NULL,
  `dish_id` int(11) NOT NULL,
  PRIMARY KEY (`restaurant_id`,`dish_id`),
  KEY `dish_id` (`dish_id`),
  CONSTRAINT `offers_ibfk_1` FOREIGN KEY (`restaurant_id`) REFERENCES `Restaurant` (`restaurant_id`),
  CONSTRAINT `offers_ibfk_2` FOREIGN KEY (`dish_id`) REFERENCES `Dish` (`dish_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Restaurant`
--

DROP TABLE IF EXISTS `Restaurant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Restaurant` (
  `restaurant_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text,
  `address` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `created_on` date NOT NULL,
  PRIMARY KEY (`restaurant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Review`
--

DROP TABLE IF EXISTS `Review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Review` (
  `review_id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `rating` int(11) NOT NULL,
  `created_on` date NOT NULL,
  `review_text` text,
  `num_upvotes` int(11) DEFAULT '0',
  `user_id` int(11) DEFAULT NULL,
  `restaurant_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`review_id`),
  KEY `user_id` (`user_id`),
  KEY `restaurant_id` (`restaurant_id`),
  CONSTRAINT `review_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`),
  CONSTRAINT `review_ibfk_2` FOREIGN KEY (`restaurant_id`) REFERENCES `Restaurant` (`restaurant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ReviewedDish`
--

DROP TABLE IF EXISTS `ReviewedDish`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ReviewedDish` (
  `review_id` int(11) NOT NULL,
  `dish_id` int(11) NOT NULL,
  PRIMARY KEY (`review_id`,`dish_id`),
  KEY `dish_id` (`dish_id`),
  CONSTRAINT `revieweddish_ibfk_1` FOREIGN KEY (`review_id`) REFERENCES `Review` (`review_id`),
  CONSTRAINT `revieweddish_ibfk_2` FOREIGN KEY (`dish_id`) REFERENCES `Dish` (`dish_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ReviewedRestaurant`
--

DROP TABLE IF EXISTS `ReviewedRestaurant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ReviewedRestaurant` (
  `review_id` int(11) NOT NULL,
  `restaurant_id` int(11) NOT NULL,
  PRIMARY KEY (`review_id`,`restaurant_id`),
  KEY `restaurant_id` (`restaurant_id`),
  CONSTRAINT `reviewedrestaurant_ibfk_1` FOREIGN KEY (`review_id`) REFERENCES `Review` (`review_id`),
  CONSTRAINT `reviewedrestaurant_ibfk_2` FOREIGN KEY (`restaurant_id`) REFERENCES `Restaurant` (`restaurant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Tag`
--

DROP TABLE IF EXISTS `Tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Tag` (
  `tag_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`tag_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `user_id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `created_on` date NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Writes`
--

DROP TABLE IF EXISTS `Writes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Writes` (
  `user_id` int(11) NOT NULL,
  `review_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`review_id`),
  KEY `review_id` (`review_id`),
  CONSTRAINT `writes_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`),
  CONSTRAINT `writes_ibfk_2` FOREIGN KEY (`review_id`) REFERENCES `Review` (`review_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-02 14:37:31
