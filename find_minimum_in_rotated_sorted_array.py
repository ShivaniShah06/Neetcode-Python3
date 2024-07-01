# Date: June 29th 2024 ##
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

##################### Examples ######################
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
#####################################################
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
#####################################################
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
#####################################################
# Solution reference: https://www.youtube.com/watch?v=nIVW4P8b1VA
# Summary of solution: Use binary search. If the value at the left pointer is less than the value at the right pointer, then 
# compare result value with the value at the left pointer and return minimum. Else, find the find the mid point and retrieve minimum value
# between the result value and the mid value in result. If value at the mid point is greater than the value at the left pointer, then it
# means that it is in the sequence and lesser value is on its right so move left pointer to its right. Otherwise, the lesser value is at its
# left so move right pointer to mid point's left.
#####################################################

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
            
            mid = (l + r)//2
            result = min(result, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return result

solution = Solution()
nums1 = [3,4,5,1,2]
nums2 = [4,5,6,7,0,1,2]
nums3 = [11,13,15,17]
print(solution.findMin(nums1))
print(solution.findMin(nums2))
print(solution.findMin(nums3))