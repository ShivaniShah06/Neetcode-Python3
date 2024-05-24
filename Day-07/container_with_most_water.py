## Date: May 24th 2024 ##
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.
##################### Examples ######################
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
#####################################################
# Input: height = [1,1]
# Output: 1
#####################################################
# Solution reference: https://www.youtube.com/watch?v=CVdul4pi8NU, https://www.youtube.com/watch?v=bl05vPClfpc
# Summary of solution: Use two pointer technique and the formula `area=height*width` to calculate this. Remember to use minimum value for height while calculating area.
# However, move pointers based on the maximum value of the height
#####################################################

from typing import List
class Solution:
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def container_with_most_water(self, height: List[int]) -> int:
        l = 0 # Initialize left pointer
        r = len(height) - 1 # Initialize right pointer
        max_area = 0 # Initialize variable to record maximum area

        while l < r:
            current_area = min(height[l], height[r]) * (r - l) # Calculate area for current values at left and right pointer. Idea is to take minimum value for height else the water will overflow. And difference between right and left pointers for width and then do `area = height * width`
            max_area = max(max_area, current_area) # Replace value for max_area if current_area is greater than max_area value

            # Give priority to the value of the height paramter
            if height[l] >= height[r]:  # If the value of height at left pointer is greater than the value of height at the right pointer, decrement the right pointer value. Keep max height.
                r -= 1
            else: # If value at the right pointer is bigger, keep that and increment the value of the left pointer
                l += 1
        return max_area

# Calling functions
solution = Solution()
height1 = [1,8,6,2,5,4,8,3,7]
height2 = [1,1]
height3 = [1,2,1]
print(solution.container_with_most_water(height1))
print(solution.container_with_most_water(height2))
print(solution.container_with_most_water(height3))