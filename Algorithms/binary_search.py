# Date: June 5th 2024 ##
# In a nutshell, this search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of the elements after just one comparison. 

# Compare x with the middle element.
# If x matches with the middle element, we return the mid index.
# Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
# Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.

##################### Examples ######################
# Input: sequence = [ 2, 3, 4, 10, 40 ], item = 10
# Output: 3 ---> Returns index of number 10 in the list
#####################################################
# Solution reference: https://www.youtube.com/watch?v=DnvWAd-RGhk
# Summary of solution: 
#####################################################
from typing import List

class Solution:
    def binary_search(self, sequence: List[str], item: int) -> int:
        begin_index = 0
        end_index = len(sequence) - 1

        while begin_index <= end_index:
            midpoint_index = begin_index + (end_index - begin_index) // 2
            midpoint = sequence[midpoint_index]
            if midpoint == item:
                return midpoint_index
            elif midpoint < item:
                begin_index = midpoint_index + 1
            else:
                begin_index = midpoint_index - 1
        return None
    
# Calling the function
solution = Solution()
sequence1 = [ 2, 3, 4, 10, 40]
item1 = 10
sequence2 = [2, 3, 4, 5, 10, 12]
item2 = 12
print(solution.binary_search(sequence1, item1))
print(solution.binary_search(sequence2, item2))
