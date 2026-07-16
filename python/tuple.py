#----------------------------------
#------tuple-------------
#----------------------------------

mytuple1 = ("hagar", "arafa")
mytuple2 = "hagar", "araf2a" # ممكن احط اقواس او لا 

print(mytuple1)
print(mytuple2)

print(type(mytuple1))
print(type(mytuple2))

#tuple indexing
mytuple3 = (1,2,3,4,5,6)
print(mytuple3[0]) #[] الاقواس دي اللي بتحدد مكتن العنصر
print(mytuple3[-3])

#TUPLES are a immutable >> u cant add or delet

#tuple assign values
mytuple4 = (1,2,3,4,5,6)
# mytuple4[2] = "THREE"
# print(mytuple4) #tuple objects does nt support item assigment


mytuple5 = (1,2,3,4,5,6,6,"hagar",12.03)
print(mytuple5[1])
print(mytuple5[-1])

#TUPLE with one element
mytuple = ( " hagar ",)
mytuple6 = "hagar", # لازم كوما عشان يعرف انها تبل

print(mytuple)
print(mytuple6)

print(type(mytuple))
print(type(mytuple6))

print(len(mytuple))
print(len(mytuple6))

# tuple cncatenation
a = (1,2,3,4,5)
b = (6,7)
c = a + b
d = a + ( "a" , "b", 'c' , True) + b

print(c)
print(d)

# tuple , list , string repet (*)
# بكرر العنصر 
mystring = " osama " 
mylist = [ 1,2 ]
mytuple0 = ( "a" ,"b" )

print(mystring*6) 
print(mylist*6)
print(mytuple0*6)


#methods >> count()

A = ( 1,2,3,4,2,5,3,6)
print(A.count(2))

 
 #methods >> index()
print(A.index(6))

# print("the position of index is : " + b.index(7))# error

print(F"the position of index is : { A.index(6)}")

print("the position of index is : {:d}".format( A.index(6)))

# tuple destruct
s = ( "A" , " B" , 4, " C") 
x , y, z = "A" , 'B' ,"C"
print(x)
print(y)
print(z)

v , n,_, m = s # حطيت _ عشان تلغي العنصر الزياده
print (v,n,m)