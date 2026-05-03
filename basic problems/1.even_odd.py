
#1. Even or odd:

"""
steps:
1.Enter the input
2. convert  the input to integer
3. divide the number by 2 
4. if the remainder is 0 -> even
5. else -> odd
"""

def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"

num = int(input("Enter a number: "))
print(even_odd(num))


# 2.Given a list of numbers, return whether each number is even or odd

"""
1  take a list of numbers as input
2. create a empty list
3. use loop[ iterate through the list] : for each number in the list
        i) if num is divisible by 2 - add "number is even" to the list
        ii) else : add "number is odd" to the list
4. return the result list

"""

def even_odd_list(nums):
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append(f"{n} is even")
        else:
            result.append(f"{n} is odd")
    return result
print(even_odd_list([3,4,5,2,64,632,32,77,97,53]))

# 3. count Even and odd

#Return how many even and odd numbers are in the list

"""
1. take a list of numbers as input
2. initialize two variables
        i) even_count=0
        ii) odd_count=0
3. for each number in the list
        i) if number is divisible by 2 - increment even_count by 1
        ii) else - increment odd_count by 1
4.return even_count and odd_count

"""

def count_even_odd(nums):
    even_count = 0
    odd_count = 0
    for n in nums:
        if n % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
even_count , odd_count = count_even_odd([3,4,5,2,64,632,32,2,4,77,97,53]) # this is called tuple unpacking
print(even_count) #7
print(odd_count) # 5

# normally it will give o/p as tuple when we use return even_count and odd_count
# like it will take as return (even_count,odd_count) so o/p (7,5)

# print(count_even_odd([3,4,5,2,64,632,32,2,4,77,97,53])) if we use this instead of unpacking



# 3. separate even and odd numbers  from the list


"""
1. take a list of numbers as input
2. create a dictionary with :
        i) key"even" : [] empty list
        ii) key"odd" : [] empty list
3.for  each number in the list:
        i) if number is divisible by 2 - add it to the even list 
        ii)else - add it to the odd list
4. return the dictionary


"""

def separate_even_odd(nums):
    result = {
        "even" : [],
        "odd"  : []
    }
    for n in nums:
        if n % 2 == 0:
            result["even"].append(n)
        else:
            result["odd"].append(n)
    return result
print(separate_even_odd([3,4,5,2,64,632,32,77,97,53]))

#4.