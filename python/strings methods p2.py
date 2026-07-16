#--------------------------------
#--------------------------------
#-- strings methods --
  
a = "hagar arafa lala"
print(a.split()) # بيقسم حسب الspace

b = "hagar-arafa-lala-gogo"
print(b.split("-")) # مع ان مفيس مسافات بس انا عرفته هيفصل بال داش


c ="menkom-le-ellah-noo-hhh-kkk"
print(c.split("-" ,3))

c ="menkom-le-ellah-noo-hhh-kkk"
print(c.rsplit("-" , 3)) # هتعمل سبليت عادي بس من اليمين

k ="menkom-le-ellah-noo-hhh-kkk"
print(k.rsplit("-" , 3)) # هتعمل سبليت عادي بس من اليمين


#------center() -----
e = "hagar"# عايزه اكتب حاجه قبلها وبعدها ب  حروف مثلا 
print(e.center(9)) # spaces
print(e.center(9 , "#")) # الرقم اللي جوا ده بتاع التوتال 
print(e.center(15 , '@'))

# count( )

f = " ya leily ya leily  "
print(f.count("ya"))
print(f.count("leily",9 ,20  )) # دور علي ليلي من المكان التاسع للعشرين

# swapecase()

s = "happy life"
l = "HAPPY LIFE"

print(s.swapcase()) 
print(l.swapcase())
# بيعكس اللي كاتبه كابيتال لاه سمول والعكس

# startswith() # 

p = "lala haha"

print(p.startswith("p")) # هل الجملة تبدا ب p 

print(p.startswith("l"))
print(p.startswith("a" ,3 , 8))



# endswith() # 

m = "lala haha"

print(m.endswith("a")) # هل الجمله تنتهي ب p 

print(m.endswith("l"))
print(m.endswith("h" ,0 , 6))
