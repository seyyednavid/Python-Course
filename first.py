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


###### while and for in list
list = ["apple", "orange", 12, 1000]

i = 0;
# while i < len(list) :
#     print(list[i])
#     i += 1;


# for i in range(len(list)) :
#     print(list[i])


# for item in list:
#     print(item);

# [print(item) for item in list] 

# my_list = []
# for item in list:
#     if item != 12:
#         my_list.append(item)
# print(my_list)


# my_list = []
# [my_list.append(item) for item in list if item != 12]
# print(my_list)

# my_list = [item for item in list if item != 12 ]
# print(my_list)

list_num = [i for i in range(10) if i % 2 != 0 ]
# print(list_num);

############sorting

list_number = [3,1,9,5,4,8,2,0]
list_number.sort()
# print(list_number)

list_str = ["orange", "apple", "zebra", "monkey"]
# list_str.sort()
# list_str.sort(reverse=True)
# list_str.sort(key=str.lower)  # consider all strings as lowercase
list_str.reverse()




############ coping list

list_str = ["orange", "apple", "zebra", "monkey"]
# new_list  = list_str
# list_str.pop()
# print(new_list) # => ['orange', 'apple', 'zebra'] => because new_list is a pointer for list_str

# new_list  = list_str.copy()
# list_str.pop()
# print(new_list)  # ['orange', 'apple', 'zebra', 'monkey'] =>  make a new one

# x = ["orange", "apple", "zebra", "monkey"]
# y = list(x)
# print(y) 


    

################ combining 2 lists
# x = ["orange", "apple", "zebra", "monkey"]
# y = [1,2,3,6,9]
# z = x + y
# print(z)


#----------------------------------------------------------------------
#################  work with strings

# string slice
txt = "hello world!"
# new_txt = txt[ :5] # => hello
# new_txt = txt[-6: ] # =>  world!
# new_txt = txt[6:len(txt) - 1] # =>  world
# new_txt = txt[-8:7]  # => o w
# print(new_txt)


# string modify
txt = "hello world!"
# new_txt = txt.upper()
# new_txt = txt.lower()

# new_txt = txt.strip() # remove spaces from both side
# new_txt = txt.lstrip()
# new_txt = txt.rstrip()

# new_txt = txt.replace("l", "")  # => heo word!
# new_txt = txt.replace("l", "" , 1)  # => just remove one  => helo world!
# new_txt = txt.replace(" ", "")  # => helloworld!


text = "hello-world-python"
new_txt = text.split("-") # => ['hello', 'world', 'python']
# print(new_txt)

result = "";
for word in new_txt:
    result += word + " "
# print(result.strip());
    


############# string concatination

txt1 = "hello"
txt2 = "world!"
# txt3 = txt1 + " " + txt2 # hello world!
# age = 18
# print(txt3)

#  ===> we can not use + for concatinating str and num 
# txt3 = txt1 + " " +  txt2 + "" + age + " " + "years old" # => error
txt3 = txt1 + " " +  txt2 + " " + str(age) + " " + "years old" # => hello world! 29 years old
# print(txt3)


############ format for concatination
txt1 = "hello"
txt2 = "world!"
age = 18

# txt3= "I'm navid, my age is {}"
# txt3 = txt3.format(age)
# print(txt3) # => I'm navid, my age is 18

# txt4 = "I'm navid, my age is {} {} {}"
# txt4 = txt4.format(age, txt1, txt2)
# print(txt4) # => I'm navid, my age is 18 hello world!

txt4 = "I'm navid, my age is {2} {1} {0}"
txt4 = txt4.format(age, txt1, txt2)
print(txt4) # => I'm navid, my age is world! hello 18


############ using \ in string

text = "hello world\n!" # new line
text = "hello world\t!" # tab => hello world     !
text = "\\n goes new line" # \n goes new line
text = 'I\'m programmer' # I'm programmer
print(text)















