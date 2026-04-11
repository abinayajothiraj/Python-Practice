"""

1.Even or Odd
2.Sum of list (without sum)
3.Count vowels
4.Reverse a string

5.Palindrome check
6.Remove duplicates
7.Factorial
8.Count words

9.First non-repeating character
10.FizzBuzz
11.Second -largest number

12.Two Sum
13.Find duplicates
14.Anagram check

"""
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