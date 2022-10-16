# 1. Two Sum
# Easy

# 38990

# 1251

# Add to List

# Share
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

def twoSum(nums, target):
    # Store the indices of every element in an sorted array
    # as a tupele since, we have to return the indices of pair of values
    array = []
    for indx, value in enumerate(nums):
        array.append((value, indx))
    array.sort()  # sort the array in increasing order

    left, right = 0, len(array) - 1
    while left < right:
        sum2 = array[left][0] + array[right][0]

        if sum2 == target:
            return [array[left][1], array[right][1]]
        if sum2 > target:
            right -= 1
        else:
            left += 1


print(twoSum([2, 7, 15, 11], 9))