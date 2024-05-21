## Date: May 21st 2024 ##

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.
##################### Examples ######################
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#####################################################
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#####################################################
# Solution reference: https://www.youtube.com/watch?v=P6RZZMu_maU
# Summary of solution: Use hashset to reduce time complexity while searching for values. For each value in the input, check if the
# preceeding value exists in the set. If not, it is the beginning of the sequence. Then track the length of the sequence until the next value is available.
# Return the longest sequence
#####################################################

# Time Complexity: O(n)
# Space Complexity: O(n)
from typing import List

class Solution:
    def longest_consecutive_sequence(self, nums: List[int]) -> int:
        numSet = set(nums) # Store values in input as hashset to search for values in less time complexity i.e. O(1)
        longest = 0 # Store the length of the longest consecutive sequence

        for n in nums:
            if (n - 1) not in numSet: # If the value before the current value does not exist in the numset
                length = 0 # Mark this value as the beginning of the sequence
                while (n + length) in numSet: # while the value + length exist in the numSet, keep increasing the value for the length of the sequence
                    length += 1
                longest = max(length, longest) # Record the maximum value from length and the longest variables in the longest variable
        return longest
    

# Calling the function
solution = Solution()
nums1 = [100,4,200,1,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]
print(solution.longest_consecutive_sequence(nums1))
print(solution.longest_consecutive_sequence(nums2))

