#-------------------------
#-------------------------
#------strings formatting-----------
#-------------------------
#-------------------------

name = "hagar"
age = "24" # دلوقت انا لما بحط علامات تنصيص بيتقلب فورا اي حاجه جواها لاسترينج عشان كده مطلعش معايا ايرور تحت لما دمجت رقم واسم ف نفس السطر 

rank = "10"

print("my name is: " + name )
print("my name is: " + name + " my age is : " + age )

Name = "HAGAR"
Age = 24
Rank = 10 # هنا دلوقت دول ارقام مش سترينج ف مينفعش احطهم ف سطر بدون فلوتينج 

print("My Name is : " + Name )
#print("My Name Is : " + Name + " My Age Is : " + Age )  error type  هنا يجي دور الفلوتينج 


print("My Name Is : %s " % "Hagar")
print( "My Name Is : %s " % Name )
print( "My Name Is : %s  and my Age Is : %d " % (Name , Age ) )
print( "My Name Is : %s  and my Age Is : %d  and My Rank Is : %f" % (Name , Age , Rank ) )

# %s >> str
# %d >> int
# %f >> float


N = "HAGAR"
L = "Python"
Y = 10 
print("My Name is %s I am a %s developer with %d years Exp " % ( N , L , Y ) )

# control floating point number 
mynumber = 19
print("my number is : %d " % mynumber) 
print("my number is : %f " % mynumber)
print("my number is : %.2f " % mynumber)



# Truncate string  بحدد اللي عيزاه من الاسترينج 

MYlongstring = " hello can you hear me i was woundring "
print("message is %s " %MYlongstring )
print("message is %.10s " % MYlongstring) 