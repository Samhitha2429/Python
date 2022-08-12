DROP DATABASE IF EXISTS `World`;
CREATE DATABASE `World`; 
USE `World`;
SET NAMES utf8 ;
SET character_set_client = utf8mb4 ;
CREATE TABLE `city` (
  `name` varchar(50) NOT NULL ,
  `continent` varchar(50),
   `area` bigint(4),
    `population` bigint(40),
    `gdp` bigint(4),
    PRIMARY KEY (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 INSERT INTO `city` VALUES ('Afghanistan','Asia',652230,25500100,20343000000);
INSERT INTO `city` VALUES ('Albania','Europe',28748,2831741,12960000000);
INSERT INTO `city` VALUES ('Algeria','Africa',2381741,37100000,188681000000);
INSERT INTO `city` VALUES ('Andorra','Europe',468,78115,3712000000);
INSERT INTO `city` VALUES ('Angola','Europe',1246700,20609294,10099000000);