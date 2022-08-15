USE `person_table2`;
select p.firstName as 'First Name',
       p.lastName as  'Last Name',
       a.city,
       a.state
      from person as p
	  left join address a on a.personId=p.personId;
