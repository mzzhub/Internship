insert into company4(name, age, occupation, id) values("jhon", 20, "ds", 3);
alter table company4 add salary int;
update company4 set salary = 10000 where id = 3;
select * from company4;
alter table combany4 add email varchar(3);
select * from company4;
update company set email = "gk.com" where id = 10;
select * from company4;

update company4 set email = "gk.com" where id = 12;
select * from company4;

create table temp_table[coll for primary key]
select * from table;
select * from company4 where salary = 1000 and occupation = "dev";


-- like method
select * from company4 where name like "a%";

-- like "_________"
select * from company4 where nname like "__a%"
select * from company4 order by salary desc



select sum(salary) from company4
select max(salary) from company4
select count(salary) from company4
avg(salary) from company4
select * from company4

delete from conpany where id = 24
select * from company4
alter table company4 drop email
select * from company4