## Date: April 28th 2024 ##
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
######################### Examples #############################
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
################################################################
# Solution reference: https://www.geeksforgeeks.org/enumerate-in-python/, https://www.youtube.com/watch?v=KLlXCFG5TnA
# Summary of solution: For each value in the list, find the difference between target and the value itself and check if the difference
# is present in the list and if its index is not the same as the value that was subtracted from the target. If it is present, return the 
# index values for this difference value and the value that was subtracted from the target.
################################################################


from typing import List

##### Brute-force #####
class Solution:
    def two_sum_bruteforce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

    ##### Self-developed logic. DOES NOT WORK FOR EVERY TEST CASE#####
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # for each number
            diff = target - nums[i] # check if target - number difference is present in the list
            if diff in nums:
                if nums.index(diff) != i: # if the index value of the number and the difference is not the same, then return the indices of difference and the number
                    ans = [i,nums.index(diff)]
                    return ans
        return "None of the 2 values add up to become the value of target."
    
    #### MOST EFFICIENT SOLUTION ####
    def two_sum_efficient(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # value:index format
        for i, n in enumerate(nums): #i is index and n is value
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i # Adding the value and its index in hashmap. Doing this in order to prevent calculations with itself
    


###### Calling the function ######
nums = [2,7,11,15]
target = 9
solution = Solution()
print(solution.two_sum_bruteforce(nums,target))
print(solution.two_sum(nums,target))
print(solution.two_sum_efficient(nums, target))