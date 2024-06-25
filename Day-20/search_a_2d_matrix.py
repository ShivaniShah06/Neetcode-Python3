# Date: June 24th 2024 ##
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

##################### Examples ######################
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#####################################################
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#####################################################
# Solution reference: https://www.youtube.com/watch?v=Ber2pi2C0j0
# Summary of solution: 
#####################################################

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix) # Rows in matrix will be same as the values in the list (if we visualize)
        COLS = len(matrix[0]) # Columns will be of the same size of each list of list
        top = 0 # Initialize top pointer
        bottom = ROWS - 1 # Initialize bottom pointer which will be 1 less than the length of the row (as we are considering indices)

        # Running binary search from top to bottom and finding the row where the target value falls in
        # Since the entire matrix is sorted in ascending order, we compare the taget value with the first and the last value in the row
        # If the target value is greater than the last value in the row, then change the value for the top pointer to the next row as all values are sorted
        # else change the value for the bottom pointer to the previous row value
        while top <= bottom:
            row = (top + bottom)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        # If value did not fall in any of the rows, then return false
        if not (top <= bottom):
            return False
        # Running another binary search for the row where the target value exist
        # Calculate row from the updated top and bottom values where our first while loop ended
        row = (top + bottom)//2
        l = 0 # Left pointer
        r = COLS - 1 # Right pointer in the row will be at the last value in the list i.e. column - 1
        while l <= r:
            mid = (l + r)//2
            if target < matrix[row][mid]: # If value in current row at mid position is greater than target, then change the right pointer to mid - 1
                r = mid - 1
            elif target > matrix[row][mid]: # If value in current row at mid position is less than target, then change the left pointer to mid + 1
                l = row + 1
            else: # If current value is same as the target, return True
                return True
        return False

solution = Solution()
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3
matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target2 = 13
print(solution.searchMatrix(matrix1,target1))
print(solution.searchMatrix(matrix2,target2))
