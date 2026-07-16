#----------------------
#--strings methods--
#----------------------

#strip() rstrip() lstrip() 

a= "   i wake up early today   "
print(a.strip())# بيشيل المسافات يمين وشمال 
print(a.rstrip())#شيل مسافات يمين
print(a.lstrip())#شيل مسافات شمال
print(len(a.strip())) #len بتعد الجملة بالمسافات بردو

b="#i wake up early today6678"
print(b.strip("6678"))# بيشيل المسافات يمين وشمال 
print(b.rstrip("#"))#شيل مسافات يمين
print(b.lstrip("#"))#شيل مسافات شمال
print(len(b.strip("#"))) #len بتعد الجملة بالمسافات بردو

#title اول حرف من كل كلمة كابيتال وكمان الحروف بعد الارقام
c= "i 7hope i 4could 6dissapear"
print(c.title())
c= "i 7hope i 4could 6dissapear"
print(c.capitalize()) # اول كل كلممة كابيتال الا لو قبلها رقم

#zfill
c,d,e , f= "1" , "11" , "111" , "1111"
print(c)
print(d)
print(e)
print(f)
print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

#upper() بيجول كل الحروف كابيتال 
H="hagarARAFA" 
print(H.upper())

# lower() كل الحروف سموول
H='HABIBI'
print(H.lower())