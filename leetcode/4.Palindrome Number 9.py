# 1.Reverse the number: [ solving without converting it to string]

# Algorithm:

"""
1.check if the number is negative -> return false
2. store the original number
3. initialize reversed = 0
4. loop until becomes 0:
        * extract last digit (%10)
        * add to reversed ( reversed *10 + digit)
        * remove last digit (x//10)
5. compare reversed with original
6. return result
"""


def Palindrome_Number(x):
    if x<0:
        return False
    temp =x
    reversed_num = 0
    while x != 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x = x // 10
    return reversed_num == temp
print(Palindrome_Number(121))
print(Palindrome_Number(10))
print(Palindrome_Number(9))
print(Palindrome_Number(-121))


"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


"""


# 2.Two Pointer Approach:

# Algorithm:

"""
1.convert integer to string because int doesnt have index
2. initialize:
        * left =0
        * right = len(s) -1
3.loop:
        * compare s[left] and s[right]
        * if not equal -> false
        * move pointers inward
4. if loop finishes -> True
"""

def palindrome_number(x):
    s = str(x)
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
print(palindrome_number(121))
