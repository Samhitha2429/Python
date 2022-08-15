DROP DATABASE IF EXISTS `Employee_tab`;
CREATE DATABASE `Employee_tab`; 
USE `Employee_tab`;
SET NAMES utf8 ;
SET character_set_client = utf8mb4 ;
create table `Employee`(
`ID` int(4) not null, 
`Name` varchar(20),
`salary` int(4),
 `managerId` int(4),
primary key(`ID`)
)
ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
insert into Employee (ID,Name,salary,managerId)values(1,'Sam',70000,3),(2,'pratham',80000,4),(3,'akasay',60000,NULL),
(5,'Saha',90000,NULL);
create table `Manager`(
`managerId` int(4) not null,
`salary` int(6),
primary key(`managerId`)
)ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
insert into Manager(managerId,salary) values(1,4050),(2,3423),(3,4000),(4,3050);