#---------------------------------------------------------------------
#--------------------control flow -----------------------
#>>>>if....>>>>elif.....>>>>else
#......make decistion

uname = "hagar"
isstudent ='yes'
ucountry = "KSA"
cname = "python course"
cprice = 100
cdiscount = 30

if ucountry == "Egypt" or ucountry == "KSA"  or ucountry == "qatar": #if they have same discount


   print(f"hello {uname} because you are from {ucountry}")

   if isstudent == 'yes' :

    print(f"the course \"{cname}\" the price is : ${cprice - 90}")

   else :

           print(f"the course \"{cname}\" price is : ${cprice-80}") 

elif ucountry == "kuwait" or  ucountry == "bahrain" :
   
       print(f"hello{uname} because you are from {ucountry}") 

       print(f"the course \"{cname}\" price is : $ {cprice-50}")

else :

   print(f"hello {uname} becuase you are from {ucountry}")
   print(f"the course \"{cname}\" price is : ${cprice-30}")


   
#ternary conditional operator >> short if

country = "Egypt"

if country == "Egypt" :
    print(f"the weather in {country} is 15")
          
elif country == "KSA" :
   print(f"the weather in {country} is 30")

else :
   print("the country is not in the list") 

   
# the short if 
print("the weather in Egypt is 15" if country is "Egypt" else"the country is not in the list")

movierate = 18
age = 19
if age < movierate : 
    print("movie is not good for u ") # condition if true 
else : 
    print("the movie is good for u \"happy watching\" ") # condition if false 


    print("the movie is not good for u" if age < movierate else "the movie is good for u \"Enjoy Watching\"")