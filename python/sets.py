#---------------------------------------
#----sets {}-----------
#-----not ordered not indexed----------
# ---no indexing no slicing------------
#---set has only immutable data types ( no,str,tuple) not list or dict
#--set item is unique--------

# Data Engineering Focus: 
# 1. Removing Duplicates (Get Unique Values)
# 2. Data Reconciliation (Comparing two systems using difference & intersection)


myset1 = {" hagar", "arafa", 100}
print(myset1)

#print(myset1[0]) 

MTTUPLE = (1, 2, 3, 4)
print(MTTUPLE[0:3])

# myset2 = { 'OSAMA', 100 , 1.5 , True , [1,2]}
# print(myset2) # only immutable data types
myset3 = { 'OSAMA', 100 , 1.5 , True , (1,2)}
print(myset3)

myset2 = { 'OSAMA', 100 , 1.5 , True , (1,2) , 100}
print(myset2)

#-----set methods-----
#clear()

a = { 1 , 2 , 3 }
a.clear()
print (a)

# union
b = { "one" , "two" ,"three"}
c = {1, 2, 3}
x = {"zero","cool"}
print(b|c)
print(b.union(c))
print(b.union(c,x))

#add----only 1 element
d = { 1, 2, 3, 4}
d.add(5)
d.add(8)
print(d)

#--copy shallow copy 
e = { 1, 2, 3, 4}
f = e.copy()
e.add(10)
print(e)
print(f)

#  remove ---- for a spacific element

g = { 1 , 2 , 3 , 4}
g.remove(1)
# g.remove(7)  no 7 in g ---show error 
print(g)
 
 #discard --- as remove but no show error
n = { 1, 2, 3, 4}
n.discard(1)
n.discard(7)
print(n)

#pop() remove for a random element cause its a set nooo index
l = {1 , 2, 3, 4}
l.pop()
print(l)

# update --- as union we can add list 
k = { 1 , 2, 4}
s = {"ww","ee"}
k.update(s)
k.update(["DDD","QQQ"])
print(k)


print("*"  * 50) # seperator

# difference
m = { 1 , 2 , 3 , 4 }
v = { 2 , 3 , 5 , 7 }
print(m.difference(v)) # same as m-v
print(v - m)

# difference_update

q= { 1 , 2 , 3 , 4 }
w = { 2 , 3 , 5 , 7 }
q.difference_update(w)   # update original set
print(q) # same as q-w
print(q - w)

print("#" * 50)

# intersection  >>> t & o
t = { 1, 2, "ee", 10}
o = { 1 , "ee", 4, 3}
print(t.intersection(o))

# intersection_update
t = { 1, 2, "ee", 10}
o = { 1 , "ee", 4, 3}
t.intersection_update(o)
print(t)
 

print("=" * 50)

# symmetric difference >> remove the intersected part then print the rest

h = { 1 , 2 , "rrr" , 123}
z = { 1 , 5 , "rrr" , 123 , 77}
print(h)
print(h.symmetric_difference(z)) # h ^ z
print(h ^ z)


p = { 1 , 2 , "rrr" , 123}
r = { 1 , 5 , "rrr" , 123 , 77}
print(p)
p.symmetric_difference_update(r)
print(p)

print("=" * 50)

#----issuperset()------>> true or false the whole second set has to be in the other set

y = { 1 , 2 , 3 , 4 ,5}
u = { 5 , 6 }
q = { 1 , 2 , 3 , 4 }
print(y.issuperset(q))
print(y.issuperset(u))

print("=" * 50 )

#----subset------>> the snd set has to be in the first set 

print(q.issubset(y)) 
print(y.issubset(q))
print("=" * 50 )

#---isdisjoint---->> 
print(y.isdisjoint(q))# if there is no common say true or are they seperated
print(u.isdisjoint(q))


#--_______-_-----____-__-__-----__-___--___________------______------_____--_--__--_
