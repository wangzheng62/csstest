create database crm;
use crm;
create table userlist(
						user_id int not null primary key AUTO_INCREMENT,
						username varchar(20) not null unique,
						passwd varchar(20) not null,
						auth int not null);
insert into userlist (username,passwd,auth) values ('admin','123456','1');						

create table department(
						department_id int not null primary key AUTO_INCREMENT,
						departname varchar(20) not null unique
						);
insert into department (departname) values ('管理账户');
create table employee(
						employee_id int not null primary key AUTO_INCREMENT,
						user_id int,
						foreign key(user_id) references userlist(user_id),
						name varchar(20) not null unique,
						passwd varchar(20) not null,
						phone varchar(20) not null,
						sex varchar(10),
						department_id int,
						foreign key(department_id) references department(department_id)
						);
create table customer(
						customer_id int not null primary key AUTO_INCREMENT,
						corp varchar(50) not null unique,
						customer varchar(20) not null,
						phone varchar(20) not null,
						employee_id int,
						foreign key(employee_id) references employee(employee_id),
						text varchar(200),
						createtime datetime default CURRENT_TIMESTAMP
						);
create table schedule(
						id int not null primary key AUTO_INCREMENT,
						employee_id int,
						foreign key(employee_id) references employee(employee_id),
						customer_id int,
						foreign key(customer_id) references customer(customer_id),
						text varchar(200) not null,
						endtime date not null,
						createtime datetime default CURRENT_TIMESTAMP
						);
create table orderlist(
						id int not null primary key AUTO_INCREMENT,
						employee_id int,
						foreign key(employee_id) references employee(employee_id),
						customer_id int,
						foreign key(customer_id) references customer(customer_id),
						ordertext varchar(200) not null,
						price1 varchar(10),
						time1 datetime,
						price2 varchar(10),
						time2 datetime,
						price3 varchar(10),
						time3 datetime,
						status varchar(10),
						finalprice varchar(10),
						finaltime datetime,
						createtime datetime default CURRENT_TIMESTAMP
						);