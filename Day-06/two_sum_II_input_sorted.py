## Date: May 23rd 2024 ##
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.
##################### Examples ######################
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
#####################################################
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
#####################################################
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
#####################################################
# Solution reference: https://youtu.be/-gjxg6Pln50?si=KDbPi8lAE5i1SRXj&t=214
# Summary of solution: Use two pointer technique to compare addition of values at both the pointers with the target. Since its a sorted array, based on the
# value of addition, increment or decrement the left and the right pointer respectively.
#####################################################

from typing import List

class Solution:
    # Using two pointer technique
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1

# Calling the function
solution = Solution()
numbers1 = [2,7,11,15]
target1 = 9
numbers2 = [2,3,4]
target2 = 6
numbers3 = [-1,0]
target3 = -1
print(solution.twoSum(numbers1, target1))
print(solution.twoSum(numbers2, target2))
print(solution.twoSum(numbers3, target3))
