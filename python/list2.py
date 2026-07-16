#------------------------------
#-----------list methds--------
#------------------------------

#append() # اضافه عنصر ف اللسته 

mylove=["NEVER","EVER","FOUND"]
mylove.append("why?")
print(mylove)
print(mylove[0])
print(mylove[0:3])
mymiss=["NVER","HAS","AN","ENDING"]
mymiss.append(False)
print(mymiss)
mylove.append(mymiss) #  جوا الليسته القديم هضيفت ليسته كامله كعنصر 
print(mylove)
print(mylove[4][3])


#extend() بضيف ليسته لليسته بيبقوا واحده 
a=[1,2,3,4,5,6]
b=['A','B','c','d']
c=['one','TWO']
a.extend(b)
a.extend(c)
print(a)

#remove
x=[1,2,3,4,5,'HAGAR',True,'laaaa','HAGAR']
x.remove('HAGAR')
print(x)

#sort ترتيب
y=[1,2,199,-45,13, 100]
y.sort() #بيرتب من ص ل ك
print(y)
y.sort(reverse=True) # رتبهم معكوسين ك ل ص
print(y)
#سورت بيرتب حروف او ارقام وليس الاتنين سوا
#reverse()

z=[ 10, 1, 9, 80, 100,'HAGAR', 100]
z.reverse() # اخره يشقلب فقط
print(z) 


#clear()
h=[1,2,3,4]
h.clear()
print(h)

#copy
n = [ 1 , 2 , 3 , 4 , 5 ]
k = n.copy()

print(n)
print(k)
n.append(6)
print(n)  #main list
print(k)  # copied list

#count()
d = [1,2,3,4,5,6,7,1,2,1]
print(d.count(1))

#index()
e = ["HHHH","AAAAA","HHHHH","AAAAA"]
print(e.index("HHHH"))
# print(e.index("KKK")) #مش ف اللسته

#insert()

f = [1,2,3,4,5,"A",'B']
f.insert(0 , "test")
print(f)
f.insert(-1,"test")
print(f)

#pop
g =[1,2,3,4,"G","H","J","K" ]
print(g.pop(2))
print(g.pop(-1))# بيطلعلي العنصر اللي عيزاه من الليست
