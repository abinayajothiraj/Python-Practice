
# COREY SCHAFER

# print(not True )
#
#
# username= input("Enter username: ")
# if username != "":
#     print("Login success")
# else:
#     print("Login failed")

name="Mick"

#print(dir(name))

#print(help(str))

print(abs(-2))


# list methods:
"""
1.append() -  adds value to the end of the list
2.insert() -  adds value to the specific place where we needed to add and it has two arguments [index, value that to be added]
3.extend() - adds two list to the end of the list
4.remove() - removes an element from the list
5.pop() - by default pops the last value of the list and we can also print that popped value by assigning it to a variable

"""

courses = ['history','math','physics','compsci']
courses_2 =['arts','education']

#courses.append(courses_2)
#courses.insert(0,courses_2)
courses.extend(courses_2)

print(courses)

# sorting list

"""
1.sort()            - sorts the list in alphabetical order, if it is numbers it will be sorted in ascending order
2.reverse()         - reverses the list
3.sort(reverse=True)- if we wanted to sort in descending order, use sort(reverse=True)
4.sorted function   - what if we need sorted version without altering the original list
5.min()
6.max()
7.sum()
8.index()           - to find index values in the list
9.in operator       - checks if the values is in our list and gives boolean output

"""

# enumerate function

for course in courses:
    print(course) # looping through list


for index, course in enumerate(courses):
    print(index,course) # enumerate function

for index, course in enumerate(courses, start=1):
    print(index,course) # enumerate function with index value starting with 1

#sets
"""
1. intersection()
2. difference()
3. union()
"""

cs_course={'history','math','physics','compsci'}
arts_course={'arts','education','history','math'}
print(cs_course.intersection(arts_course)) #{'history','math'}
print(cs_course.difference(arts_course))
print(cs_course.union(arts_course))



# for loop - nested loop

for x in ["big","red"]:
    for y in ["apple","banana"]:
        print(x,y)


# function
#1. eg 1
def my_function():
    print("hello")

my_function()


#2. using return

def add(a,b):
    return a + b

print(add(3,4))

# 3.

def greet(name):
    print("hello",name)

greet("ABI")

#4.

def func(x=[]):
    x.append(1)
    return x
print(func())
print(func())
print(func())

#5. default argument:

def greet(name='kai'):
   print(name)

greet()

# 6. positional argument:


def pet_info(animal,name):
    print("I have a" , animal)
    print("My", animal,"'s name is", name)

pet_info("Dog" , "Latte")

# 7. keyword arguments:

def pet_info(animal,name):
    print("I have a" , animal)
    print("My", animal,"'s name is", name)

pet_info(name="peter", animal ="Cat")

#8. position-only arguments (/)

def func(a,/):
    print(a)

func(10)

def func_2(a,b,/,c):
    print(a,b,c)

func_2(1,2,c=3) # correct
#func_2(a=1,b=1,c=3) -> wrong coz  before / it should only be position arg

#9. keyword only arguments (*)

def func_3(*,a):
    print(a)

func_3(a=10) # correct

#10. combination of both arg

def func_4(a,/,b,*,c):
    print(a,b,c)
func_4(1,2,c=4) # correct coz /  (before), * (after)

#11.

"""def func_5(a,b):
    print(a,b)
func_5([1,2,3]) # error coz b value is missing"""

#12.

"""def func(a, b):
    print(a, b)

func(1, a=2) # error - coz multiple value for argument 'a'"""

#13. if there are extra arguments there will be no output printed

"""def func(a, b):
    print(a, b)
    
func(1,2,3) # error - too many arguments
"""
#14.missing required argument

"""def func_9(a, b, c=3):
    print(a, b, c) 

func_9(1)  # error - Missing required argument b
"""

#15.

"""def func_10(a,b=[]):
    b.append(a)
    return b
print(func_10(1))
print(func_10(2))
"""

#16. *args, **kwargs


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math','Art',name='Abi',ag=22)
















