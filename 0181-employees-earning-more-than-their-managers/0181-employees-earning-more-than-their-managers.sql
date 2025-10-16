# Write your MySQL query statement below
-- select e1.name as Employee from  
-- Employee e1
-- where e1.salary > (
--     select  salary from  Employee e2
--     where e1.managerId = e2.id
-- )

select e1.name as Employee from  
Employee e1 join Employee e2
on e1.managerId = e2.id
where e1.salary > e2.salary