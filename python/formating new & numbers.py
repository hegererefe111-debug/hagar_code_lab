#-----------------------
# strings formatting new 
Name = "HAGAR"
Age = 24
Rank = 10 # هنا دلوقت دول ارقام مش سترينج ف مينفعش احطهم ف سطر بدون فلوتينج 

print("My Name is : " + Name )
#print("My Name Is : " + Name + " My Age Is : " + Age )  error type  هنا يجي دور الفلوتينج 


print("My Name Is : {:s} " .format("Hagar"))
print( "My Name Is : {} " .format (Name ))
print( "My Name Is : {:s}  and my Age Is : {:d}" .format (Name , Age ) )
print( "My Name Is : {:s}  and my Age Is : {:d} and My Rank Is : {:f}" .format(Name , Age , Rank ))

# {s} >> str
# {d}>> int
# {f} >> float


N = "HAGAR"
L = "Python"
Y = 10 
print("My Name is {:s} I am a {:s} developer with {:.3f} years Exp " .format( N , L , Y ))

# control floating point number 
mynumber = 19
print("my number is : {} ".format (mynumber) )
print(f"my number is : {mynumber}")
print(f"my number is : {mynumber}")



# Truncate string  بحدد اللي عيزاه من الاسترينج 

MYlongstring = " hello can you hear me i was woundring "
print(f"message is { MYlongstring} " )
print(f"message is  {MYlongstring}") 


X , G , P  = 10 , 20 , 30 
print("hello {} {} {}".format(X , G , P ))

print("hello {0:d} {2:d} {1:d}".format(X , G , P ))
print("hello {0:.3f} {2:.6f} {1:.10f}".format(X , G , P ))

mymoney= 13545623400
print("my mner in thr bank is : {:d}" .format(mymoney))
print("my mner in thr bank is : {:_d}" .format(mymoney))
print("my mner in thr bank is : {:,d}" .format(mymoney))
 

print(type(5+4J)) #complex numbers
mycomplexnumber= 9+ 3J 
print(type(mycomplexnumber))
print("real part is {}".format(mycomplexnumber.real))
print("imaginary number is{}".format(mycomplexnumber.imag))

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))
print(float(10.50))
print(4+2j)
# print(int(4+2j)