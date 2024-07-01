## Date: May 04 2024 ##
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

########################### Examples #############################
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
##################################################################
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
##################################################################
# Solution reference: https://www.youtube.com/watch?v=bNvIQI2wAjk
# Summary of solution: Use a single output list to store values by multiplying value with previous values. Use a prefix and postfix and 2 different for loops to do so
##################################################################
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: # eg: nums = [1,2,3,4]
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix # [1,1,2,6]
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix # [24,12,8,6]
            postfix *= nums[i]
        return res

# Calling the function
solution = Solution()
input1 = [1,2,3,4]
output1 = solution.productExceptSelf(input1)
print(output1)
input2 = [-1,1,0,-3,3]
output2 = solution.productExceptSelf(input2)
print(output2)