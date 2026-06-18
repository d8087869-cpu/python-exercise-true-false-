#1 
is_online = True
has_access = False
print(is_online and has_access)
print(is_online or has_access)
#3 
status = False 
print(not False)
#4
age=20 
has_id =True
print(age>= 18 and has_id)
level = 3 
print(level >=1 and level <=5)
#6 
a = 0
b = "hello"
c = "" 
print(bool(a))
print(bool(b))
print(bool(c))
#7
x = None
y = 42 
print(x or y) 
# None is false so what we have left with its only or = 42 
#8 
username = ""
default = "guest" 
print(username or default)
# 9
print(True and False or True)
print((True and False)or True)
#becuase and is first 
