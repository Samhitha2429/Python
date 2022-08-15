USE `Employee_tab`;
select e.Name as 'Employee'
FROM Employee as e,
     manager as m
WHERE e.salary>m.salary
and e.managerId=m.managerId;