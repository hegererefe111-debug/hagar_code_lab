#-----------------------------------
#--------------dictionary--------------
# [1] dict items are enclosed in curly bracet
# [2] dict items are contains ket : value
# [3] dict key need to be immutable => (no, str, tuple) no list
# [4] dict value can have any data types
# [5] dict key need to be unique
# [6] dict is not ordered you access its element with key 
#----------------------------------------------------------------
# ===============================================================
# 🚨 DE Saved My Life Notes (Data Engineering Best Practices)
# ===============================================================

# 1. The .get() method is your pipeline's seatbelt:
# Note: Never use user['key'] with external data (APIs / JSON). 
# If the key is missing, the whole pipeline will CRASH. 
# Always use user.get('key', default_value) to keep the data flowing safely.

# 2. The Nested Dict is how raw data looks before going to SQL:
# Note: Data from the web (APIs) always comes as a Nested Dictionary (JSON format). 
# Your main job as a DE is to un-nest this data (Flattening) so it can fit into SQL tables (Rows & Columns).

# 3. The .items() method is the key to Data Cleaning:
# Note: When you need to clean, transform, or fix data row by row, 
# use "for key, value in dict.items():". It is the fastest way to loop through keys and values together.



# dictionary

user = { 
    " name" : "hagar" ,
     "age" : 23 ,
     "country" : "Egypt" , 
     "skills" : ["PYTHON", "Html", "JS"] , 
     "rating" : 10.3

}

print(user)
print(user['country'])
print(user.get("country"))

print(user.keys())
print(user.values())

# two-Dimentional Dictionary

languages = {
"one" : {
   'name' : "Html" , 
   "progress" :"80%"
} ,

"two" : {
    "name" : "css", 
    "progress" : "90%"
} ,
"three" : {
    "name" : "js", 
    "progress" : "94%"
} 

}
print(languages)

print(languages['one'])
print(languages["three"]["name"]) # to find len for element inside element use 2[] NO , BETWEEN

#dict length

print(len(languages))
print(len(languages["two"]))  


# create dictionary from variables 
framework1 ={
" name" : "hagar" ,
     "age" : 23 ,
     "country" : "Egypt" , 
     "skills" : ["PYTHON", "Html", "JS"] , 
     "rating" : 10.3
}

framework2 = {
" name" : "titi" ,
     "age" : 55 ,
     "country" : "Egypt" , 
     "skills" : ["PYTHON", "Html", "JS"] , 
     "rating" : 100

}

framework3 = {
" name" : "shimaa" ,
     "age" : 25 ,
     "country" : "Egypt" , 
     "skills" : ["PYTHON", "Html", "JS"] , 
     "rating" : 10


}

All_Framework = {
'ONE' : framework1,
"TWO" : framework2 ,
"three" : framework3

}

print(All_Framework)
print("=" * 60)
# --------dict methods-------------

# clear()

user1 = {
    "name" : "hagar"
}
print(user1)
# user1.clear()

print(user1)

# update ()

user1.update({"age" : 35})
print(user1)

 # we can use list to add
user1["country"] = "Egypt"
print(user1)

# copy
main = {
"name" : "esraa",
"age" : 12

}

b = main.copy()
print(main)
print(b)

main.update({"fav color" : "brown"})
print(main)
print(b)

print(main.keys() , main.values())
print("=" * 60)


# setdefault()

user2 = {
"name" : " amir" ,
"age" : 34

}
user2.setdefault("name" ,"ahmed") # we have name in the original so nothing changed
user2.setdefault("fav color" , "black")# we do not have fav color in user2 so it is added
print(user2)

#popitem()
print(user2.update({"skills" : " nothing"}))
print(user2.popitem())

# items()

view = { 

"name" : "alaa" ,
"age" : "23"

}
 
All_Items = view.items()

print(view)
view['length'] = 24
print(view)
view.update({"book" : "black moon"})
print(view)

print(All_Items)


#fromkeys() => dict.fromkeys---if l have variable as i can name it key 
# same as values so we can make dict

a = ("mykey1", "mykey2", "mykey3")
b = "x" ,"b"
print(dict.fromkeys(a,b))

print(type(dict.fromkeys(a,b)))

 