# Python Practice

Daily Python practice repository — actively updated.

## What's inside
- **leetcode/** — LeetCode problem solutions (arrays, hashmaps, two pointers)
- **corey schafer/** — Exercises from Corey Schafer's Python tutorial series
- **basic problems/** — Core Python practice
- **practice/** — General Python experiments and exercises

## Currently learning
- Python core concepts and OOP
- Data Structures & Algorithms
- Flask (backend development)
- CS50 by Harvard (via edX)

### 1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a target.

#### Approach:
- Use a hashmap (dictionary)
- Store numbers and their indices
- For each element, check if (target - current) exists

#### Example:
Input: nums = [2,7,11,15], target = 9  
Output: [0,1]

#### File:
leetcode/1.Two_Sum_1.py

### 2. Max Consecutive Ones

Find the maximum number of consecutive 1's in a binary array.

#### Approach:
- Traverse the array
- Count consecutive 1’s
- Reset count when 0 appears
- Track maximum count

#### Example:
Input: nums = [1,1,0,1,1,1]  
Output: 3

#### File:
leetcode/2.Max_consecutive_ones_485.py
- 
### 3. Best Time to Buy and Sell Stock

Find the maximum profit by choosing a single day to buy and a different day to sell.

#### Approach:
- Track minimum price so far
- Calculate profit at each step
- Update maximum profit

#### Example:
Input: prices = [7,1,5,3,6,4]  
Output: 5

#### File:
leetcode/3.best_time_to_buy_and_sell_stock.py
-
### 4. Palindrome Number

Check whether a given integer is a palindrome (reads the same forward and backward).

#### Approaches:
- Reverse number (without converting to string)
- Two-pointer approach (convert to string)

#### Key Points:
- Negative numbers are not palindrome
- Numbers ending with 0 (except 0 itself) are not palindrome
- Compare original with reversed value

#### Example:
Input: x = 121  
Output: True  

Input: x = -121  
Output: False  

Input: x = 10  
Output: False  

#### File:
[Palindrome Number](leetcode/4.Palindrome Number 9.py)
-
