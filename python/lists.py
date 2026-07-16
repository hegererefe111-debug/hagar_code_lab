#----------------------------
#---------------------------
#--------List---------------
#--------------------------

mylist = ['one', 'TWO' , 'ONE' , 1 , 100.4 , False] # diff types
print(mylist)
print(mylist[1])
print(mylist[-1])
print(mylist[1:4])
print(mylist[:6])
print(mylist[0:6])

print(mylist[-1])
print(mylist[::1]) # بيطبع اللسته كلها
print(mylist[::2]) # هيفوت واحد كل شوية
print(mylist[::3])# هيفوت اتنين 
 
# mylist[1] = 2
# print(mylist) # اقدر اعدل في الليسته 
# mylist[-1] = True
# print(mylist)

# mylist[0:3]= []

mylist[0:3]= ["a"," b" ,"c"] 
print(mylist) # تبديل ف الليست

mylist[0:4] = [ 'Q',"H","P"]
print(mylist)# لو غيرت عناصر قليللة عن العدد بتتساب فاضية 
