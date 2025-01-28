select * from mobile;
select Brands from mobile;
select * from mobile order by price desc limit 10;
select * from mobile where Brands = "samsung" order by price desc;
select * from mobile where Operating_System_Type = "iOS" order by 5G_Availability desc;
alter table mobile add primary key(Phone_name);mobile
create table table01 (Phone_name text, 
Brands text, 
Price int 
);
create table teble02 (Phone_name text, 
Internal_Storage text,
5G_Availability text,
RAM_Storage text,
Country_of_Origin text);

select mobiles.Phone_name from mobiles 
select empunion.id, emp30.location, empunion.name, 
