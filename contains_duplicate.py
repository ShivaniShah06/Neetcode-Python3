## Date: April 27th 2024 ##
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
######## Examples ########
# Input: nums = [1,2,3,1]
# Output: true
##########################
# Input: nums = [1,2,3,4]
# Output: false
##########################
# Solution reference: https://www.youtube.com/watch?v=XDoF8-oy404
# Summary of the solution: Sort the numbers and compare each number with the next number.
##########################


from typing import List


class Solution:
    ### Solution-1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # Using in-built func for list
        for i in range(len(nums) - 1): # using `len(nums) - 1`` in range because nums[i] is compares with nums[i+1] and this will give error for the last value if not using `len(nums) - 1`
            if nums[i] == nums[i+1]: # if current value is same as the next value in the sorted list
                return True
        return False # return false if haven't returned True yet
    
    ### Solution-2: ## self-developed logic ## NOT EFFICIENT
    def containsDuplicate2(self, nums: List[int]) -> bool:
        while nums: # while the list is not empty
            val_to_compare = nums[0] # assign first value in the list to a variable called `val_to_compare`
            nums = nums[1::] # remove first element from the list using index slicing
            if val_to_compare in nums: # check if the removed value exist in the list
                return True
        return False # return false if haven't returned True yet and the list is empty now
    
    ### Solution-3: ## This solution does not modify the original list ##
    def containsDuplicate3(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)): # as set only has unique values, if there are duplicate values in the list, the length of set will be less than the actual list
            print(nums)
            return True
        print(nums)
        return False

        

# Create an instance of class Solution and call its method
list1 = [1,2,3,1]
list2 = [1,2,3,4]
list3 = [1,3,3,4,3,2,4,2]

solution = Solution()
print("********** Answers from Solution-1 **********")
print(solution.containsDuplicate(list1))
print(solution.containsDuplicate(list2))
print(solution.containsDuplicate(list3))
print("********** Answers from Solution-2 **********")
print(solution.containsDuplicate2(list1))
print(solution.containsDuplicate2(list2))
print(solution.containsDuplicate2(list3))
print("********** Answers from Solution-3 **********")
list4 = [1,2,3,1]
list5 = [1,2,3,4]
list6 = [1,3,3,4,3,2,4,2]
print(solution.containsDuplicate3(list4))
print(solution.containsDuplicate3(list5))
print(solution.containsDuplicate3(list6))