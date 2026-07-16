#-----------------------------------
#-------------joins-----------------
#------inner join ------------------
select * from customers c 
join orders o on c.CustomerID = o.CustomerID;

#--------left join---------------

select * from customers c 
left join orders o on c.CustomerID = o.CustomerID;

select c.CustomerID , o.CustomerID  from 
customers c left join orders o on c.CustomerID = o.CustomerID;


select * from orders o
left join customers c on o.CustomerID = c.CustomerID ;

select concat(c.FirstName," ",c.LastName) as full_name , o.Quantity 
from customers c 
inner join orders o on c.CustomerID = o.CustomerID; 
select c.FirstName , c.LastName , o.Quantity 
from customers c 
inner join orders o on c.CustomerID = o.CustomerID;

select * from products;
select concat(c.FirstName," " ,c.LastName) as full_name ,o.Quantity , p.productName , p.Price ,
(o.Quantity * P.Price ) as Total_Price 
from customers c inner join orders o on c.CustomerID = o.CustomerID
inner join products p on p.productID = o.productID ;


select * from customers c 
left join orders o on c.CustomerID = o.CustomerID 
where o.CustomerID is null ;

select p.category,  sum(o.Quantity * p.Price ) as Full_Price 
from products p 
inner join orders o on p.ProductID = o.ProductID 
group by p.category ;

select c.Country,  sum(o.Quantity * p.Price ) as Full_Price 
from products p 
inner join orders o on p.ProductID = o.ProductID 
join customers c on c.CustomerID = o.CustomerID 
group by 1
having Full_Price > 500
order by Full_Price asc;

#--------------------------
#---------Cases-------------
select ProductName , price , 
case
    when price > 750 then 
    "too_much" 
    when price between 200 and 750 
    then "good"
else "super_price" 
end as price_list 
    
from products ;
