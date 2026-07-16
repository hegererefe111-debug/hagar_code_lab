select * from orders;
select * from products ;
select * from orders ;
select * from customers ;
select FirstName,LastName,Country from customers;
#select count(*) from customers;
#select count(distinct country) from customers;# عد بون 
#select FirstName from customers;
#select substring(FirstName,1,2) from customers;
select * from customers
 where country = "USA";
 select * from products
 where price > 200 ;
 select * from products 
 where 250 < Price  and price < 500  ;
 select *  from products  ssss
 where price between 250 and 500;
 select count( distinct customerID) from customers ;
 select * from products 
 where price >= 250;
 select * from products
 where price !=250; 
 select * from products 
 where price <> 250 ;
 select * from products
 where ProductName = "Laptop" or ProductName = "Headphones" or ProductName = "Tablet"; 
 
 select * from products 
 where ProductName in ("Headphones" ,"Tablet" , "Laptop" );
 select * from products ;
 select * from products 
 where Category like "e%" ; 
 select * from products 
 where Category like "%e" ;
 select * from products
 where Category like "%e%" ; 
 

 



#select FirstName,substring(FirstName,1,2) as first_two from customers;
#select FirstName, LastName, concat(FirstName,' ',LastName) as full_name from customers; # 2colums in 1




