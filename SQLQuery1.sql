create database Billing_System;

use Billing_System;

create table Admin_Account
(
  Admin_ID int AUTO_INCREMENT,
  Username varchar(20) not null,
  Passcode varchar(20) not null,
  Primary key (Admin_ID)
);



create table Cashier_Account
(
  Cashier_ID int AUTO_INCREMENT,
  Username varchar(20) not null,
  Passcode varchar(20) not null,
  Primary Key (Cashier_ID)
);



create table In_Stocks
(
  Item_ID int AUTO_INCREMENT,
  Items varchar(40) not null,
  Price decimal(10,2) not null,
  Item_image_link varchar(255) not null,
  Quantity numeric not null,
  PRIMARY KEY (Item_ID)
);



create table Items_soldout
(
  Item_ID int AUTO_INCREMENT,
  Item_name varchar(50) not null,
  Date_sold date not null,
  PRIMARY KEY (Item_ID)
);


INSERT INTO Admin_Account(Username, Passcode) VALUES ("Faisal", "123");


select * from items_soldout;
select * from Admin_Account;
select * from Cashier_Account;
select * from In_Stocks;