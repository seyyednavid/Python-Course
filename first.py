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

################################################ tuples => like list 

my_list = ["red", 12 , 9.5]
my_tupple = ("red", 12 , 9.5)
# print(my_list[1])    # => 12
# print(my_tupple[1])  # => 12

#### when we have only one element in tuple, compiler  consider it as a str class
tuple_str = ("hi")
# print(type(tuple_str)) # => <class 'str'>
tuple_num = (1)
# print(type(tuple_str)) # => <class 'str'>
# for converting it to tupple we need to add , in front of the only element
tuple_str = ("hi",)
# print(type(tuple_str)) # => <class tupple>

# tupples are not changable, we can not add or remove, we can not change the elements

# we can get some parts of tuppple 
my_tupple = ("red", 12 , 9.5)
# print(my_tupple[0:2])  # => ('red', 12)
# if "red" in  my_tupple:
    # print ("Yes");

# changing tupple elements with list
my_tupple = ("red", 12 , 9.5)
my_tupple_to_list = list(my_tupple) # convert to list and make desired changes
my_tupple_to_list[0] = "blue"
my_tupple = tuple(my_tupple_to_list) # convert to tupple 
# print(my_tupple) # => ('blue', 12, 9.5)

# pack and unpake tupples => destructuring
my_tupple = ("red", 12 , "blue") # => packing
(item1, item2, item3) = my_tupple  # => destructuring (exact number in both side)
# print(item1) "red"
# print(item2)  "12"
# print(item3)  "blue"
(item1, item2, item3, *item4 ) = ("red", 12 , "blue", "hi", True , 56)
# print(item1)
# print(item2)
# print(item3) 
# print(item4)  # => ['hi', True, 56] list, iy's not tupple
(item1, *item2, item3) = ("red", 12 , "blue", "hi", True , 56)
# print(item1)  # "red"
# print(item2)  # [12, 'blue', 'hi', True]
# print(item3)  # True

# tuple concatination
my_tuple1 = ("red", 12 , "blue", 12, "red", 12)
my_tuple2 = ("test",)
my_tuple3 = my_tuple1 + my_tuple2;
# print(my_tuple3) # ('red', 12, 'blue', 12, 'red', 12, 'test')

# repetition
tuple = ("test",)
tuple1 = 3 * tuple;
# print(tuple1) # ('test', 'test', 'test')


my_tuple1 = ("red", 12 , "blue", 12, "red", 12)
# print(my_tuple1.count("red"))    # 2
# print(my_tuple1.count(12))  
#      # 3
# print(my_tuple1.index("blue"))   # 2
# print(my_tuple1.index("red"))    # 0
# print(my_tuple1.index(12))       # 1
# print(my_tuple1.index(12,2))     # 3  find 12 after index 2
# print(my_tuple1.index(12,2,4))   # 3  find 12 after index 2 , before index 4


######################################################## set
my_set = {1,2,True,2}
# print(type(my_set)) # <class 'set'>
my_set = {}
# print(type(my_set)) # <class 'dict'>
my_set = set ()
# print(type(my_set)) # <class 'set'>

###### we do not have index for getting elements in set
###### we can not consider any index for reaching or changing them. can not change elements
###### we only can add or remove items in set 
###### we can not have repetitive items into a set

my_set = {1,2,True,2}

# for item in my_set:
#     if item == 1:
#         print("YES") # YES

myset = {1,2,3,True,2,1,1,4}
# print(len(myset)) # 4 did not consider repetitive items and True
# print(myset)      # {1, 2, 3, 4}  why did not consider True as an item ?
###### because True == 1 , so set cinsider True as 1

myset = {2,3,True,2,1,1,4}
# print(myset) # {True, 2, 3, 4} 
# print(2 in myset)  # True
myset.add(5)
# print(myset) # {True, 2, 3, 4 , 5} 



########### Add item in set => add , update
myset = {1,2,3}
newset = {3,4,5}
#### Using add
# for item in newset:
#     myset.add(item)
# print(myset)  # {1, 2, 3, 4, 5}
#### using update
# myset.update(newset)  # newset can be a set , a list or a tuple 
# print(myset) # {1, 2, 3, 4, 5} 



########### remove item in set  => remove , discard , pop , clear , del
# when we use discard for removing an item that we do not have it, we do not face error
myset = {1,2,3}
myset.remove(3)
# print( myset) # => {1,2}
# myset.remove(4)  we'll face error under the title "we do not have this item"

#### discard
myset = {1,2,3}
myset.discard(3)
# print(myset)  # {1, 2}
myset.discard(4)
# print(myset) # {1, 2} , we do not face error

#### pop remove an item randomly
myset = {1,2,3}
myset.pop()
# print(myset) # {2, 3}

#### clear , remove all items
myset = {1,2,3}
myset.clear()
# print(myset) # set()

#### clear , remove all items
myset = {1,2,3}
myset.clear()
# print(myset) # set()

#### del , remove from memory
myset = {1,2,3}
del myset
# print(myset)  # name 'myset' is not defined

############################################## update, union, intersection_update, symmetric_difference_update,
##################### symmetric_difference, copy 
myset1 = {1,2,3}
myset2 = {2,4}

#### update => work on previous sets
# myset1.update(myset2) 
# print(myset1) # {1, 2, 3, 4}

#### union => creating new set
# newset = myset1.union(myset2)
# print(newset)  # {1, 2, 3, 4}

#### intersection_update
# myset2.intersection_update(myset1)
# print(myset2) # {2}

#### intersection
# newset = myset1.intersection(myset2)
# print(newset) # {2}

#### symmetric_difference_update => union - intersection
# myset1.symmetric_difference_update(myset2)
# print(myset1) # {1, 3, 4}

####  symmetric_difference
# newset = myset1.symmetric_difference(myset2)
# print(newset) # {1, 3, 4}

####  copy
# newset = myset1.copy()
# myset1.pop()
# print(myset1) # {2, 3}
# print(newset) # {1, 2, 3}



######################################################## dictionary

my_dict = {}     # <class 'dict'>
my_dict = dict() # <class 'dict'>
# print(type(my_dict))

my_dict = {"navid": "good news", "lida": "world", "maz":"friend"}
# print(my_dict["navid"]) # good news
# print(my_dict.get("lida")) # world

######### keys(), values(), items()
my_dict = {"navid": "good news", "lida": "world", "maz":"friend"}
myKeys = my_dict.keys()     #  dict_keys(['navid', 'lida', 'maz'])
myValues = my_dict.values() # dict_values(['good news', 'world', 'friend'])
myItems = my_dict.items()   # dict_items([('navid', 'good news'), ('lida', 'world'), ('maz', 'friend')])
# print(myItems)

# print("YES") if "navid" in my_dict.keys() else print("YES");
# print("YES") if "world" in my_dict.values() else print("NO");
# if ('maz', 'friend') in my_dict.items(): print("YES");



####### change values , add new one or update them 
my_dict = {"navid": "good news", "lida": "world", "maz":"friend"}
my_dict["maz"] = "best friend"
# print(my_dict) # {'navid': 'good news', 'lida': 'world', 'maz': 'best friend'}
my_dict.update({"arash":"cousin"}) # new key => new item
# print(my_dict) # {'navid': 'good news', 'lida': 'world', 'maz': 'best friend', 'arash': 'cousin'}
my_dict.update({"arash":"bro"}) # repetitive key, update the previous one
# print(my_dict) # {'navid': 'good news', 'lida': 'world', 'maz': 'best friend', 'arash': 'bro'}


####### remove items from dict => pop, popitem, del, clear
my_dict = {"navid": "good news", "lida": "world", "maz":"friend"}
my_dict.pop("navid") 
# print(my_dict) # {'lida': 'world', 'maz': 'friend'}
my_dict.popitem()  # remove the last one
# print(my_dict) # {'lida': 'world'}

####### loop through a dict
my_dict = {"navid": "good news", "lida": "world", "maz":"friend"}
# for item in my_dict.keys():
    # print(item)       # navid lida maz

# for item in my_dict.values():
#     print(item)      # good news world friend

# for item in my_dict.items():
#     print(item) # ('navid', 'good news') ('lida', 'world') ('maz', 'friend')

# for key,value in my_dict.items():
#     print(key, value) 
# navid good news
# lida world
# maz friend


####### copy 
my_dict = {"navid": "good news", "lida": "world", "maz":"friend"}
# newdict = my_dict
# my_dict.popitem()
# print(newdict) # {'navid': 'good news', 'lida': 'world'}

# newdict = my_dict.copy();
# my_dict.popitem()
# print(my_dict) # {'navid': 'good news', 'lida': 'world'}
# print(newdict) # {'navid': 'good news', 'lida': 'world', 'maz': 'friend'}

######### twisted dict
# students = {
#     "student1": {
#         "name": "navid",
#         "age" : 35,
#         "courses" : ["devops", "math", "machine learning"]
#     },
#     "student2" : {
#         "name": "Lida",
#         "age" : 32,
#         "courses" : ["AI", "deep learning", "machine learning"]
#     }
# }
# print(students["student2"]["name"])  # lida


student1 = {
    "name": "navid",
     "age" : 35,
     "courses" : ["devops", "math", "machine learning"]
}
student2 = {
    "name": "lida",
     "age" : 32,
     "courses" : ["AI", "deep learning", "machine learning"]
}

students = {
    "student1": student1,
    "student2": student2
}
# print(students["student2"]["name"])  # lida



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
# print(txt4) # => I'm navid, my age is world! hello 18


############ using \ in string

text = "hello world\n!" # new line
text = "hello world\t!" # tab => hello world     !
text = "\\n goes new line" # \n goes new line
text = 'I\'m programmer' # I'm programmer
# print(text)



#----------------------------------------------------------------------
#################  functions

# def my_function(age):
#     print(f"your age is {age}")
# my_function(12) # your age is 13


# def employee(name, age=18):
#     print(f"{name} is {age} yeras old.")
# employee("navid") # navid is 18 yeras old.
# employee("navid", 34) # navid is 34 yeras old.


##### having uncertain number of aruments => args is a list
def average(name,*args):
    ave = sum(args) / len(args)
    # print(f"{name}: average number is {ave}")
average("arash", 15,16,17,17,19,20)  # arash: average number is 17.333333333333332


##### args as a dict
def get_average(name, **kwargs):
    sum = 0
    for num in kwargs.values():
        sum += num
    avg = sum / len(kwargs)
    # print(f"{name}: average is {avg}") # maz: average is 19.2
get_average("maz", math=20, AI=19, devops=18, CSS=19, HTML=20)


#### send a list directly
# def my_function(mylist):
#     for item in mylist:
#         print(item)
# my_list = [1,3,4,"hello"]
# my_function(my_list)
# 1
# 3
# 4
# hello

#### sent a dict
# def my_function(mydict):
#     sum = 0
#     for value in mydict.values():
#         sum += value
#     avg = sum / len(mydict)
#     print(avg)
# mydict = {"math":20, "AI":19, "Devops":18}
# my_function(mydict) # 19.0


##### using return for functions
def my_sum(list):
    sum = 0
    for item in list:
        sum += item;
    return sum

def my_len(list):
    counter = 0
    for item in list:
        counter += 1;
    return counter;

mylist = [1,4,5,8,9]
sum = my_sum(mylist)
len = my_len(mylist)
avg = sum / len
# print(avg) # 5.4

#################################     recursion 
# 3! = 1 * 2 * 3
# 4! = 3! * 4
# 5! = 4! * 5
# first way => ordinery
def fact(num):
    result = 1
    for item in range(1,num+ 1):
        result *= item
    return result;
# print(fact(3))

# second way => recursion
def fact(num):
    result = 1
    if num > 1 :
        print(result)
        result = num * fact(num - 1)
    return result;
# print(fact(3))

#################################     lambda functions => ananomous function
sum = lambda a , b : a + b;
# print(sum(1,3))   # 4

multi = lambda a, b, c: a * b * c;
# print(multi(2,3,4)) # 24


#################################     OOP => object oriented programming

# class CarBmw :
#     doors_number = 2
#     wheels_number = 4
# car1 = CarBmw()
# car2 = CarBmw()
# car3 = CarBmw()
# car4 = CarBmw()
# print(car1.doors_number)
# print(car2.doors_number)
# print(car1.wheels_number)
# print(car2.wheels_number)

################# Add  constructor and method

class CarBmw:
    def __init__(self, c="black"):
        self.color = c

    def car_des(self):
        return f"this car is the newest BMW car with {self.color} color, {self.wheels_number} wheels and {self.doors_number} doors." 

    doors_number = 2
    wheels_number = 4

car1 = CarBmw("white");
# print(car1.color)
# print(car1.car_des())

############################# remove or change object properties


class CarBmw:
    def __init__(self, c="black"):
        self.color = c

    def car_des(self):
        return f"this car is the newest BMW car with {self.color} color, {self.wheels_number} wheels and {self.doors_number} doors." 
    
    doors_number = 2
    wheels_number = 4


car1 = CarBmw("white");
car1.doors_number = 4;
car1.color = "pink";
# print(car1.doors_number) # 4
# print(car1.color)        # pink
# del car1.doors_number    # can not remove it as it was nod defined in method
# del car1.color           # can remove it because it was defined in constructor method
# print(car1.doors_number) # 2
# print(car1.color)        # 'CarBmw' object has no attribute 'color'


##########################  python inheritance

class Human:
    def __init__(self, fname, lname):
        self.first_name = fname;
        self.last_name = lname;

    def print_name(self): 
        print(f"{self.first_name} {self.last_name}")

class Student:
    def __init__(self, fname, lname, feild):
        self.first_name = fname;
        self.last_name = lname
        self.feild = feild
    
    def print_name(self): 
        print(f"{self.first_name} {self.last_name}")
    
    def print_details(self):
        print(f"{self.first_name}{self.last_name} , feild is {self.feild}")
        

# student1 = Student("lida","shahmiri", "ML");
# student1.print_details()

# human1 = Human("navid", "hejazi")
# human1.print_name()



########## write standard way

class Human:
    def __init__(self, fname, lname):
        self.first_name = fname;
        self.last_name = lname;

    def print_name(self): 
        print(f"{self.first_name} {self.last_name}")


class Student(Human):
    def __init__(self,name,family,field):
        super().__init__(name,family)
        self.field = field

    def print_details(self):
        print(f"{self.first_name}{self.last_name} , feild is {self.field}")

human1 = Student("navid", "hejazi", "Math")
# human1.print_details();


######### multi inheritance

class A:
    def test(self):
        print("from class A")

class B:
    def test(self):
        print("from class B")

class C(A,B):
    pass

c= C()
# c.test() # same func in both, choose first parent =>> from class A



class A:
    def test(self):
        print("from class A")

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

d= D()
# d.test() #  from class A



class A:
    def test(self):
        print("from class A")

class B(A):
    pass

class C(A):
    def test(self):
        print("from class C")

class D(B,C): 
    pass

d= D()
# d.test() #   from class C - first check all parents, if does not exist, check parent's parent



class A:
    def test(self):
        print("from class A")

class B(A):
    pass

class C(A):
    def test(self):
        print("from class C")

class D(B,C): 
    def test(self):
        print("from class D")

d= D()
d.test() # from class D
# print(D.__mro__) # show parents  ==> (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# print(D.mro()) # show parents ==>  [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


# ----------------------------------------------
# env variable
# pip install python-dotenv
import os;
from dotenv import load_dotenv, dotenv_values

# load_dotenv()
# print(os.getenv("MY_SECRET_KEY")) #12435465dxfbgd656
# print(os.getenv("COMBINED")) # 127.0.0.1:9999

config = dotenv_values(".env")
print(config) #OrderedDict({'MY_SECRET_KEY': '12435465dxfbgd656', 'HOST': '127.0.0.1', 'PORT': '9999', 'COMBINED': '127.0.0.1:9999'})
print(config["HOST"]) # 127.0.0.1

