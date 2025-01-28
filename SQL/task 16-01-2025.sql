-- show all columns and rows in table
select * from salaries limit 150000;

-- show only employeename and job title columns
select employeename, jobtitle from salaries;

-- show the number of employees in the table
select count(id) from salaries;

-- show unique job titles in the table
select distinct(JobTitle) from salaries;

-- show the job title and overtime pay for all employees with overtime pay greater than 5000
select jobtitle, overtimepay from salaries where overtimepay > 5000;

-- show avg base pay for all employees
select avg(basepay) from salaries;

-- show the top 10 highest paid employees
select employeename, TotalPay from salaries order by TotalPay desc limit 10;

-- show the average of BasePay, Overtimepay and otherpay for each employee
select employeename, (basepay + overtimepay + otherpay)/3 from salaries;

-- show all employees who have manger in their job title
select employeename, jobtitle from salaries where jobtitle like "%MANAGER%";

-- show all employees with a job title not equal to manager
select employeename, jobtitle from salaries where jobtitle not like "MANAGER";

-- show all employees with total pay between 50000 and 75000
select employeename, totalpay from salaries where TotalPay > 50000 and totalpay < 75000;

-- show all employee with base pay less than 50000 or total pay greater than 100000
select employeename, basepay, totalpay from salaries where basepay < 50000 or totalpay > 100000;

-- show all employees ordered by their total pay benefits in descs order
select employeename, TotalPayBenefits from salaries order by TotalPayBenefits desc;

-- show all job titles with avg basepay of at least  100000 and order them by the avg base pay in descending order
select jobtitle, avg(basepay) from salaries group by jobtitle having avg(basepay) <= 100000 order by avg(basepay) desc;