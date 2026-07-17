#------------------------
print(bin(10))
lst = [1,2,3]
lst+= [4,5,6]
print(lst)

x = 5
x+=3
print(x)
x *=2 
print(x)
x >>1
print(x)

# ---------
a = 1,2,3
b= 4,5,6
print(type(a))
 
print(25 % 2 == 1)
print(46 % 2 == 1)

A = 25
print( 15 < A < 30)

print(-1 == ~0)

print(~0)
print(bin(~0))

# -----boolen--------
print(5==3)
print(3<4)
print(type(3<4))
print(True and True)
print( 5 > 2 and 3 < 4)
print( 5 > 2 and 7 < 4) # both has to be right
print( 2==2 or 1 <1 ) # one has to be right 

print( not 5 > 2)
print ( not 3<2)
print( 5 * 7 )
print( type( 5 * 7))

print ( (5 > 2 ) and ( 2.8 < 3))
print (( 3 > 1) or ( 1.5 < 0))
print( not ( 5 > 3))

B = [ 1,2,3 ]
k = [ 1,2,3 ]
print( B == k)
print(type(B==k))
print( B is k)
print( B is not k )

o = [ 1,2,3 ]
o = B 
print( o is B)

print( 1 in o)
print( type(1 in o))
print( 5 in o)
print( 5 not in o)
