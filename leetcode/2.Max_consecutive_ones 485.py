# 485.MAX CONSECUTIVE ONES

#Algorithm:
"""
1. start counting ones
2. If you hit 0 -> forget the old count and start fresh
3. keep track of the largest count you ever saw

"""

def max_consecutive_ones(nums):
    count = 0  # current streak
    ans = 0    # max streak
    for n in nums:
        if n == 1:
            count += 1  # increase
        else:
            count = 0   # reset
        ans = max(count, ans)
    return ans
print(max_consecutive_ones([1,1,0,1,1,1]))
print(max_consecutive_ones([1,0,1,1,0,1]))

"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

"""

# without max()
"""

def max_consecutive_ones(nums):
    count = 0  # current streak
    ans = 0    # max streak
    for n in nums:
        if n == 1:
            count += 1
        else:
            count = 0
        if count > ans:
            ans = count
    return ans
print(max_consecutive_ones([1,1,0,1,1,1]))




"""