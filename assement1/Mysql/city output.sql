SELECT  
name AS big_country, area, population 
FROM 
world.city
WHERE 
area > 3000000 OR population > 25000000