age, name = 10 , "Navid";
a = b = 20

#----------------------------------------------------------------
############### naming rule ===>   A-Z a-z _ 0-9
#----------------------------------------------------------------

############### data types

#### Numeric => int, float, complex

x = - 12345  # int
y = 12.9     # float
z = 2 + 1j       # complex
# print(type(x)); # <class 'int'>
# print(type(x).__name__); # int
# print(type(y).__name__); # float
# print(type(z).__name__); # complex


#### String
c = "salam    25£$%^&*"
d = """dear gaynor;
I hope you are doing well.
Thank you for your follow-up"""
# print(type(c).__name__); # str
# print(type(d).__name__); # str


# conver str to int and vice versa  => int(), float(), str()
age = "29"      #str
age = int(age)  #int
# print(type(age).__name__)

e = 12 
e = str(12)
f = float(12)
# print(type(e).__name__)
# print(type(f).__name__)

#### boolean  => bool() => True or False
# "" => False  ,  " " => True  ,  [] => False  ,  {}=> False
g = "salam"
i = None
h = bool(g)
j = bool(i)
# print(h) # True
# print(j) # False


#### list  => 0,1         -2,-1<=
my_list = [0,"hello", [3], True,"apple"]
result1 = my_list[1] 
result2 = my_list[-4]
result3 = my_list[1:4]
result4 = my_list[-4:-1] 
result5 = my_list[1:] 
result6 = my_list[:] 
# print(result1)  => hello
# print(result2)  => hello
# print(result3)  => ['hello', [3], True]  
# print(result4)  => ['hello', [3], True]  
# print(result4)  => ["hello", [3], True,"apple"]
# print (result6) => [0, 'hello', [3], True, 'apple']

# Replacement in list
x = ["hello", "apple2", 12, 1.9, True, ["hello", 12, "orange"]]
y = [100, 1000, "red"]
x[2:4] = [5,8]
# print(x) # => ['hello', 'apple1', 5, 8, True, ['hello', 12, 'orange']]

# Add a new one into list
x.insert(1,False)
# print(x)  # => ['hello', False, 'apple2', 5, 8, True, ['hello', 12, 'orange']] 
x.append(1000) # add at the end
x.extend(y) # add an list's elements to another list
# print(x) # => ['hello', False, 'apple2', 5, 8, True, ['hello', 12, 'orange'], 1000, 100, 1000, 'red']

# Removing from list
a = ["hello", "apple2", 12, 1.9, True, ["hello", 12, "orange"]]
a.remove(12)
# print(a) # => ['hello', 'apple2', 1.9, True, ['hello', 12, 'orange']]
a.pop()
a.pop(0) 
# print(a) # => ['apple2', 1.9, True]
del a[0]
# print(a) # => [1.9, True] remove from memory
# del a # => remove  list a from memory
a.clear() # => []
# print(a)

#----------------------------------------------------------------------

############### comment 

# this is my comment
"""
this is my 
comment
"""
#----------------------------------------------------------------------

############### operators

# operators  =>  + , - , * , /(float) , //(int) , % , ** 

k = 2
j = 5
# print (k ** j)  # => 32



############### assignment operators  =>  = , +=, -= , *= , /= , ...
l = 4
l *= 2
# print(l)  # => 8


############### comparison operators => == , != , >= , <= 

x = 12
y = 13
z = x == z # => False
z = x != z # => True
# print(z)


#----------------------------------------------------------------------

# python conditions

# if

# age = 19
# if age > 18 :
#     print("Yes")
# elif 15 < age < 18 :
#     print("It's ok")
# else:
#     print("No")

# if in one line
# print("Excelletn") if age > 18 else print("good") 


# if age > 18 : print("Yes")


# if age >= 18 :
#     if age >= 25 :
#         print("All services")
#     else:
#         print("Partial services")
# else:
#     print("No service")


#----------------------------------------------------------------------

# python loops => while , for => break , continue

# ############### while 
# i = 1
# while i < 6:
#     if i == 4:
#         i += 1
#         continue;
#     print(i)
#     i += 1
# else:
#     print("End of loop")

#  1 2 3 5 End of loop
    

# i = 1
# while i < 6:
#     if i == 4:
#         break;
#     print(i)
#     i += 1
# else:
#     print("End of loop")

#  1 2 3 
    

###############for loop
    
# range(5) => 0, 1, 2, 3, 4
# range(2,5) =>  2, 3, 4
# range(2,10,2) =>  2, 4, 6, 8
# range(2,10,3) =>  2, 5, 8

# for j in range(5):
#     if j == 3:
#         continue;
#     print(j)
# 0, 1, 2, 4
    
# for j in range(5):
#     if j == 3:
#         break;
#     print(j)
# 0, 1, 2


###### for in list

    
