

# string modify:
a = "Hello Hello hello"
print(a.replace("H" , "J"))



b=",,,,,,,banan,.a....."
print(b.strip(",."))

# f strings

age= 20
txt=f"My name is abi, I'm {age} years old "
print(txt)
print(f"Hello, I'm {age}")


#  1.joins

fruits = ["apple", "banana", "cherry"]
print("-".join(fruits))

#2.Join numbers into a string separated by space

num= [1, 2, 3, 4]
x = (" ".join(str(i) for i in num))
print(x)

#3. Join only vowels from:

study ="education"
count= []
for i in study:
    if  i in "aeiou":
        count.append(i)
print("".join(count))

# by using comprehensions- shorthand for-if


study = "education"
result= "".join(i for i in study if i in "aeiou")
print(result)  # euaio

# if there is uppercase means

study = "education"
resukt = "".join( i for i in study if i.lower() in "aeiou")
print(resukt) # euaio

#3 consonants

find_consonants = "education123OOH"
count=[]
for i in find_consonants:
    if i.isalpha() and i.lower() not in "aeiou":
        count.append(i)
print("".join(count))

find_consonants = "education"
result = "".join(i for i in find_consonants if i.isalpha() and i.lower() not in "aeiou")
print(result)

"""
Convert this list into:

1-4-9-16

👉 Input:

nums = [1, 2, 3, 4]

💡 Hint: You need square of numbers + join()
"""

nums=[1,2,3,4]
sqr_nums = [i**2 for i in nums]
print("-".join(str(i) for i in sqr_nums))


# LIST COMPREHENSION

#num=int(input("Enter a number: "))


#BOOLEANS


"""
Take a number from user and print:

"Positive" if number > 0
"Zero" if number == 0
"Negative" if number < 0

"""

num = int(input("Enter a number: "))
if num>0:
    print("Positive")
elif num==0:
    print("Zero")
elif num<0:
    print("Negative")

# even or odd

nums= int(input("Enter a number: "))
if nums % 2 ==0:
    print("Even")
else:
    print("Odd")

#boolean conversion

values = [0, 1, "", "hi", [], [1,2], None]
for i in values:
    print(bool(i))

"""
Check Both Conditions

👉 Take two numbers:

Print "Valid" if both are positive
Else print "Invalid"

"""

a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
if a and b > 0:
    print("Positive")
else:
    print("Invalid")

"""
Take a password as input from the user.

If the length of the password is greater than 5 → print "Strong"
Otherwise → print "Weak"
"""

Password = input("Enter password: ")
if len(Password) > 5:
    print("Strong")
else:
    print("Weak")


"""
Truthy Values Test

👉 Take input from user:

If input is empty → print "Empty input"
Else → print "Valid input"

"""

char=input("Enter a word: ")
if char == "":
    print("Empty input")
else:
    print("Valid input")

"""
Write a function:

def is_adult(age):
Return True if age ≥ 18
Else return False

"""

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False
print(is_adult(16))

# or

def is_adultt(age):
    return age >= 18
age = int(input("Enter age: "))
print(is_adultt(age))


"""
Question 9: Multiple Conditions

👉 Take 3 numbers from user:

Print "All positive" if all are > 0
Else print "Not all positive"

"""

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if  a>0 and b > 0 and c>0:
    print("All Positive")
else:
    print("Not all positive")


"""
Check if a list is empty:

my_list = []
Print "Empty" if it is empty
Else print "Not Empty"

"""

my_list=[]
if my_list==[]:
    print("Empty")
else:
    print("Not Empty")

"""
Question 12: Using and, or

👉 Take a number from user:

Print "In range" if number is between 10 and 50
Else print "Out of range"
"""

num=int(input("Enter a number: "))
if num >= 10 and num <= 50:
    print("In range")
else:
    print("Out of range")


"""
rite a function:

def is_valid_string(s):

Return True if:

Not empty
Length > 3

Else return False
"""

def is_valid_string(s):
    if len(s)>3:
        return True
    else:
        return False
print(is_valid_string(""))

"""
Write a program:

Take username input
If username is not empty → print "Login success"
Else → print "Login failed"

"""

username= input("Enter username: ")
if username != "":
    print("Login success")
else:
    print("Login failed")


# else, nested if


x = 0
y = 5

if x:
    print("A")
elif y:
    if not x:
        print("B")
    else:
        print("C")
else:
    print("D") # o/p: B

# shorthand if else

print("B") if a > b else  print("A")

# shorthand if else


a=78
b=30
#print("B") if a > b else  print("A")
# pass:
if a>b:
    pass

# nested if
x=30
if x > 10:
    if x > 20:
        print("Greater than 20")