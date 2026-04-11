#1. *args, **kwargs


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math','Art',name='Abi',ag=22)

#2.

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses=['Math','Art']
info={'name':'Abi','age':22}

student_info(*courses,**info)

#3.

def func(*args):
    print(args)
func(1,2,3)   # (1,2,3) which will be tuple

#4.

def func(a,b,*args):
    print(a,b,args)

func(1,2,3,4,5,6)

#5.

"""def func(a,b,c):
    print(a+b+c)
lst=[1,2,3]

func(lst) """ # error coz we need to first unpack it


def func(a,b,c):
    print(a+b+c)
lst=[1,2,3]

func(*lst) #6

#6.

def func(**kwargs):
    print(kwargs)

d={'a':1,'b':2,'c':3}

func(**d)    #{'a':1,'b':2,'c':3}  [if we dont unpack we will get error, but here we have unpacked]

#7.

def func(a,*args,**kwargs):
    print(a,args,kwargs)

func(1,2,3,x=4,y=5,z=6)


#8.


def func(*args):
    print(len(args))

func(1,2,3,)  #3


#9. local scope

def myfunc():
    x=100          # Here x is a local variable inside the function. It can only be accessed within myfunc(). If I try to use it outside, it will give an error.”
    print(x) # 100
myfunc()


#10. Enclosed Scope


def myfunc():
    x=200
    def myinnerfunc():  #The inner function can access variables from the outer function. This is called enclosing scope.
        print(x)   # 200
    myinnerfunc()
myfunc()

#11.global scope


x=300

def myfunc():
    print(x) #300

myfunc()   #x is a global variable. It can be accessed both inside and outside the function.
print(x)  #300


#12.same variable name [local vs global]

x=500

def myfunc():
    X=600
    print(X) #600
myfunc()   #“Python treats them as different variables. Inside the function, local x = 200 is used. Outside, global x = 300 is used.”

print(x) #500

#13. global keyword -(create global variable)

def myfunc():
    global x  #Using global, we create a variable in the global scope from inside a function
    x=900

myfunc()
print(x)  #900

#14.Modify global variable

y=1000
def myfunc():
    global y  #Without global, we cannot modify a global variable. Here global x allows us to change its value.”
    y=1200
myfunc()
print(y) # 1200

#15. nonlocal keyword


def myfunc1():
    x="Abi"
    def myfunc2():
        nonlocal x #nonlocal allows modifying variables from the outer function. Without it, Python would create a new local variable.
        x="klaus"
    myfunc2()
    return x
print(myfunc1()) #klaus


#16. LEGB RULE:


"""
“Python follows LEGB:

Inner prints local value
Outer prints enclosing value
Final print shows global value”

"""

x="global"
def outer():
    x ="Enclosing"
    def inner():
        x="local"
        print("Inner: ",x)
    inner()
    print("Outer: ",x)
outer()
print("Global: ",x)



#ARRAYS:

#ARRAY METHODS:

"""
1.append()
2.clear()
3.copy()
4.count()
5.extend()
6.index()
7.insert()
8.pop()
9.remove()
10.sort()
11.reverse()



"""

#1.append() - add element at end

cars = ["BMW","Ford"]
cars.append('volvo')
print(cars)


#2. clear() - removes all element

cars.clear()
print(cars)   #[]

#3.

a=[10,20,30]
print(a.pop()) # 30
print(a)   # [10,20]


x=[1,2,3]
y = x * 2
print(x)




