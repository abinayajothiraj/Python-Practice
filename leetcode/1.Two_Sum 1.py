#1.  TWO SUM
# Algorithm:

"""
1.Take a number
2.Find what number you need by using [target-number]
3.check if you saw the number before in the dictionary
4.if yes -> done
5.else -> store it in the dictionary

"""

def two_sum(nums,target):
    val_index ={}
    for i,v in enumerate(nums):
        remaining = target - v
        if remaining in val_index:
            return [val_index[remaining],i]
        val_index[v] = i

print(two_sum([2,7,11,15],9))
print(two_sum([3,2,4],6))
print(two_sum([3,3],6))

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
