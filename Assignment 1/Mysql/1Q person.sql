DROP DATABASE IF EXISTS `Person_tab`;
CREATE DATABASE `Person_tab`; 
USE `Person_tab`;
SET NAMES utf8 ;
SET character_set_client = utf8mb4 ;
create table `person`(
`personID` int(4) not null, 
`lastName` varchar(20),
`firstName` varchar(20),
primary key(`personID`)
)
ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
insert into person (personID,lastName,firstName)values(1,'Sam','Kamala'),(2,'pratham','K'),(3,'akasay','S'),
(5,'Saha','Amit');
create table `address`(
`addressId` int(4) not null,
`personID` int(4),
`city` varchar(20),
`state` varchar(20),
primary key(`addressId`)
)ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
insert into address(addressId,personID,city,state) values(1,2,'Alakapuri','Hyd'),(2,1,'lb nagar','Hyd'),(3,3,'vizay','andhar'),(4,5,null,null);