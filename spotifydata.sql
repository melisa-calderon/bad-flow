-- MariaDB dump 10.17  Distrib 10.4.8-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: spotifydoja
-- ------------------------------------------------------
-- Server version	10.4.8-MariaDB-1:10.4.8+maria~bionic-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Top_Tracks`
--

DROP TABLE IF EXISTS `Top_Tracks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Top_Tracks` (
  `Track_Name` text DEFAULT NULL,
  `Explicit` tinyint(1) DEFAULT NULL,
  `Popularity` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Top_Tracks`
--

LOCK TABLES `Top_Tracks` WRITE;
/*!40000 ALTER TABLE `Top_Tracks` DISABLE KEYS */;
INSERT INTO `Top_Tracks` VALUES ('Kiss Me More (feat. SZA)',1,75),('Streets',1,89),('Dick (feat. Doja Cat)',1,87),('Need To Know',1,75),('You Right',1,84),('Say So',1,84),('Boss Bitch',0,83),('motive (with Doja Cat)',1,82),('Del Mar',1,81),('Ain\'t Shit',1,80);
/*!40000 ALTER TABLE `Top_Tracks` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-01 21:15:42
