#---------------------
#strings indexing & slicing
#all data in python is object
#objects contains elements
# every elemnt has its owm index
#python use zero based indexing(idex starts from zero)
#use square brackets to access element
#-----------------------

# indexing(access single item)
mystring='feeling bad'
print(mystring[0]) # index 0 => f 
print(mystring[6]) # index 6 => n 
print(mystring[-1]) # index -1 => first character frm end

#slicing (access multiple sequence item)
#[start:end]
#[start:end:steps]

print(mystring[4:9])# عدد الحروف اللي هيطلع الفرق بينن الرقمين والمسافة بتحسب
print(mystring[1:3])
print(mystring[5:7])# بنعد من الصفر لغاية منوصل ل اول حرف عايزينه ونرجع نعد لبعد اخر حرف هنقف عنده
# لو مكتبتش بداية هيعتبرها بداية من الصفرلحد نهاية الرقم اللي كتبته
print(mystring[:8])
print(mystring[8:])
print(mystring[:])  # full print
print(mystring[0::1])  # full print بيمشي خطوة واحدة بس

print(mystring[::1])  # full print
print(mystring[::2])  # كل خطوتين
print(mystring[::3])  # كل تلت خطوات
