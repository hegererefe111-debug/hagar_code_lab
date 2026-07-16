#---------------------------
#-----strings methods ------
#---------------------------

# index( text=substring  , start , end )
a = "ya rab ya karim"
print(a.index("a"))

print(a.index("y" , 0 ,8))
print(a.index ("r" , 0 , 4)) # ملحووووظة مهمه الايرور اللي ف الانديكس مخلاش الاكواد اللي جايه بعد تشتغل خدي بالك فايند بتعمل نفس الحاجه والايرور بيطلع سالب واحد


# find ( substring , start , end )

b = "ya rab ya karim"
print(b.find("b"))

print(b.find("y" , 0 ,8))
print(b.find ("r" , 0 , 3))


# rjust() ljust()---------width and fill char

c = " law kol wahed fe el haw ekhtar"

print(c.rjust(40 , "#"))# نفس فكره السنتر

print(c.ljust(40 , "#"))

# splitline () بترجعلك كل اللاينز بتاعتك في الليست

e="""first line 
second line
third line"""

print(e.splitlines())
print(type(e.splitlines()))



f = "first line\nsecond line\nthird line"

print(f.splitlines())

# expandtabs()
g = " i\twish\tif\ti\tcould\tgo\tback"

print(g.expandtabs(2)) #  بيتتحكم في عدد التبس يعني حط مسافات 2 بين كل كلمه

one =" I Love Pthon And 3G"
two =" i love pthon and 3g"
print(one.istitle())
print(two.istitle())

three = " "

print(three.isspace())

five = "i Love python "
six = " i love python "
print(five.islower())
print(six.islower())

seven="hagar_arafa"
eight ="hagarArafa190"
nine=" hagar--arafa100"


print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x="AaaaaBbbbbb"

print(x.isalpha())


j="AaaaaBbbbb1191"

z="AaaaaBbbbbb"

print(z.isalnum())

print(j.isalnum()) # بتتعرف ع الحروف بس او ارقام بس او الاتنين سوا بدووو مسافاتتتتت راجعيها تاني 


#replace( old value , new value , count )

x = " hello one two three one one "

print(x.replace("one", "1" ))

print(x.replace("one", "1" , 1 ))

print(x.replace("one", "1" , 2 ))

# join (interable) # بترجعهم سترينجس

mylist = ["hagar" , "shimaa" , "titi"]

print(" " .join(mylist))

print("-" .join(mylist))

print(type("-" .join(mylist) ))