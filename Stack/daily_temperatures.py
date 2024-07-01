# Date: June 13th 2024 ##
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you 
# have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

##################### Examples ######################
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
#####################################################
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
#####################################################
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
#####################################################
# Solution reference: https://www.youtube.com/watch?v=cTBiBSnjO3c
# Summary of solution: Use stack to store the list of lists in [temperature, index] format and compare temperature value at the top of stack. If
# the current value is greater, pop the value from the top of the stack and update result for that index in the output array by making necessary calculations and
# add current value to the top of the stack
#####################################################
from typing import List

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) # Initiate a list of length equal to the length of the input list with 0s in it
        stack = [] # [temp, idx]

        # For each index, temperature in the input list
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # If the stack is non-empty and current temperature is greater than the temperature on the top of the stack
                stackTemp, stackIdx = stack.pop() # Then pop the value from the top of the stack and update value in the result list for the index that was popped
                res[stackIdx] = (i - stackIdx)
            stack.append([t,i]) # Add value at the top of the stack if the previous value in the stack is greater than the current value
            # print(stack)
        return res

solution = Solution()
temperatures1 = [73,74,75,71,69,72,76,73]
print(solution.dailyTemperatures(temperatures1))