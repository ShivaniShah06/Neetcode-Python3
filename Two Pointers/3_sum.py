## Date: May 24th 2024 ##
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
##################### Examples ######################
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
#####################################################
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#####################################################
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#####################################################
# Solution reference: https://www.youtube.com/watch?v=wCe-MeqXgMc
# Summary of solution: Sort the array and then run one loop for each value in the array. Inside this loop, run another loop with the same logic as the `Two Sum II Input is Sorted` problem (using two pointers).
# Where 0 is the target value
#####################################################
from typing import List

class Solution:

    # Time Complexity: O(nlogn) + O(n^2) = O(n^2)
    # Space Complexity: O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_nums = nums.sort()
        
        for i in range(len(sorted_nums)): # Run for loop for each element in the sorted list
            if i != 0 and sorted_nums[i] == sorted_nums[i-1]: # As no duplicates are allowed, make sure that if index is not 0, then the current element and the earlier element are not same
                continue
            
            l = i + 1 # left pointer set to the index next to the ith index
            r = len(sorted_nums) - 1 # right pointer set to the last index

            # Run while loop until left pointer < right pointer
            while l < r:
                threeSum = sorted_nums[i] + sorted_nums[l] + sorted_nums[r] # Get addition of values at ith, lth, and rth index and then apply same logic as `Two Sum II Sorted Input` problem
                if threeSum < 0: # If the value of sum is less than zero, increase the value by incrementing left pointer
                    l += 1
                elif threeSum > 0: # If the value of sum is greater than zero, decrease the value by decrementing right pointer
                    r -= 1
                else:
                    result.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]]) # If the addition of values is zero, append the values to the result array
                    l += 1 # Increment the left pointer to check further values
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]: # If the value at the left pointer is same as the value previous to the left pointer, then skip this value and increment the value of the left pointer.
                        l += 1 # Doing this because we don't want to get the same combination of values in the output
        
        return result
    
# Calling the function
solution = Solution()
nums1 = [-1,0,1,2,-1,-4]
nums2 = [0,1,1]
nums3 = [0,0,0]
print(solution.threeSum(nums1))
print(solution.threeSum(nums2))
print(solution.threeSum(nums3))

