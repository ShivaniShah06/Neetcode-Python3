# Date: June 16th 2024 ##
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

##################### Examples ######################
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#####################################################
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#####################################################
# Solution reference: https://www.youtube.com/watch?v=DnvWAd-RGhk
# Summary of solution: As the list is sorted in ascending order, assign the begin and end index values to two variables and find the midpoint. If the
# midpoint value is greater than the target, then change the end index variable value to mid point index - 1. If the midpoint value is
# less than the target, then change the begin index variable value to mid point index + 1 otherwise, return the mid index.
#####################################################
from typing import List

class Solution:
    # Time Complexity: O(logn)
    def binary_search(self, nums: List[int], target: int) -> int:
        begin_index = 0
        end_index = len(nums) - 1

        while begin_index <= end_index:
            mid_index = begin_index + (end_index - begin_index)//2
            mid = nums[mid_index]

            if mid > target:
                end_index = mid_index - 1
            elif mid < target:
                begin_index = mid_index + 1
            else:
                return mid_index
        return -1

# Calling the function
solution = Solution()
nums1 = [-1,0,3,5,9,12]
target1 = 9
nums2 = [-1,0,3,5,9,12]
target2 = 2
print(solution.binary_search(nums1, target1))
print(solution.binary_search(nums2, target2))