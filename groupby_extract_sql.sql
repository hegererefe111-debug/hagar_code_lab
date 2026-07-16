#--select and  from star * comaa;  extract ------
#------------ concat نجمع عمودين ف واحدج ------- substring ناخد اول حرفي من عمود معين---------------------------
#---extract-----------select * ,
select * , extract(year from registrationdate)  as  year from customers ;
select * , extract(month from registrationdate)  as  month from customers ;
 

select * , extract(day from registrationdate)  as  day from customers ;

#---------------group by-------------
select * from products;
select category, sum(price) from  products 
group by Category; 

select country,count(Country)from customers
group by country; 

#select category , sum(price) from products where price < 500 group by 1 having sum(price) < 500

#select category, sum(price) as total_price from products where price < 500group by 1having sum(price) <500

select category, sum(price)
 from products 
 where ProductName in ( "Laptop", "Tablet" , "Desk" ) 
 group by 1 
 
 
 having sum(price) > 500


