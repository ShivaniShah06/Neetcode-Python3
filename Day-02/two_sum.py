## Date: April 28th 2024 ##
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
######################### Examples #############################
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
################################################################


from typing import List

##### Brute-force #####
class Solution:
    def two_sum_bruteforce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

    ##### Self-developed logic #####
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # for each number
            diff = target - nums[i] # check if target - number difference is present in the list
            if diff in nums:
                if nums.index(diff) != i: # if the index value of the number and the difference is not the same, then return the indices of difference and the number
                    ans = [i,nums.index(diff)]
                    return ans
        return "None of the 2 values add up to become the value of target."
    


###### Calling the function ######
nums = [2,7,11,15]
target = 9
solution = Solution()
print(solution.two_sum_bruteforce(nums,target))
print(solution.two_sum(nums,target))