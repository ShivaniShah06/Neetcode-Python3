# Date: June 15th 2024 ##
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
# return the area of the largest rectangle in the histogram.

##################### Examples ######################
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
#####################################################
# Input: heights = [2,4]
# Output: 4
#####################################################
# Solution reference: https://www.youtube.com/watch?v=zx5Sw9130L0
# Summary of solution: 
#####################################################

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 # To track the maxArea so far
        stack = [] # Stores pair of index, height

        # iterate through each index, height in the input array starting with index = i
        # As long as stack is non-empty and the current height is less than the height on the top of the stack,
        # keep popping the value from the top of the stack and change start index to the index of the height just popped from the stack
        # because this means that for current height, we can create a rectangle backwards until that index
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        # Calculate maxArea for values left in the stack. These can be stretched until the end of the histogram
        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea

solution = Solution()
heights1 = [2,1,5,6,2,3]
heights2 = [2,4]
print(solution.largestRectangleArea(heights1))
print(solution.largestRectangleArea(heights2))