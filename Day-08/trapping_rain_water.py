# Date: May 25th 2024 ##
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

##################### Examples ######################
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
#####################################################
# Input: height = [4,2,0,3,2,5]
# Output: 9
#####################################################
# Solution reference: https://www.youtube.com/watch?v=ZI2z5pq0TqA
# Summary of solution: Most efficient solution includes two pointer method. Track maxLeft and maxRight values from the values of the left and right pointers and 
# calculate water units by using something similar to the formula min(maxRight, maxLeft) - height[current_element] and add to the final trapped_water variable
#####################################################


from typing import List

class Solution:

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def trapping_rain_water(self, height: List[int]) -> int:
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        maxLeft = [0]*len(height)
        maxRight =[0]*len(height)
        minLeftRight = []
        trapped_water = 0

        # Update maxLeft array
        for i in range(len(height)):
            if i == 0: # If the element is the first element from left, set maxLeft[0] as 0 because there is no element on left
                maxLeft[i] = 0
            else: # If i is not 0, set maxLeft[i] to the maximum value from maxLeft[i-1] and height[i-1]
                maxLeft[i] = max(maxLeft[i-1], height[i-1])
        
        # Update maxRight array
        for i in range(len(height)-1, -1, -1): # Run loop from the end
            if i == len(height) -1: # If the element is the last element in the array, set maxRight[len(height)] as 0 as there is no element on its right
                maxRight[len(height)-1] = 0
            else: # If i is not the last element in the array, set maxRight[i] as maximum value from maxRight[i+1] and height[i+1]
                maxRight[i] = max(maxRight[i+1], height[i+1])
        
        # Update minLeftRight array
        for i in range(len(height)): # Find the minimum value from maxLeft and maxRight for each index
            minLeftRight.append(min(maxLeft[i], maxRight[i]))

        # Final for loop to update trapped_water
        # What we do here is subtract height of the current element from the minimum of the left and right of the current element. If it is less than 0,
        # then we continue the loop and don't do anything else we add it to the value of the trapped_water
        for i in range(len(height)):
            water_unit = minLeftRight[i] - height[i]
            if water_unit > 0:
                trapped_water += water_unit
            else:
                continue
        return trapped_water
    

    # Using two pointer method
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def trapping_rain_water_efficient(self, height: List[int]) -> int:
        # height = [0,1,0,2,1,0,1,3,2,1,2,1]
        trapped_water = 0
        l = 0 # Left pointer pointing to the 0th index
        r = len(height) - 1 # Right pointer pointing to the last index
        maxLeft = height[l] # maxLeft is initialized with the first value in the list 
        maxRight = height[r] # maxRight is initialized with the last value in the list

        while l < r:
            if maxLeft <= maxRight: # If maxLeft is less than or equal to maxRight => As we anyway need to find the minimum from maxLeft and maxRight
                l += 1 # Increment the left pointer by 1
                maxLeft = max(maxLeft, height[l]) # Make sure that the maxLeft is set to the maximum value from itself and height of the current element
                water_unit = maxLeft - height[l] # As we updated maxLeft earlier, the possibility of negative answer is gone and hence no case to check that. Directly calculate the water units
                trapped_water += water_unit # Add water_units to the trapped_water
            else:
                r -= 1 # If the value at the right pointer is less than the value at the left pointer, decrement the right pointer
                maxRight = max(maxRight, height[r]) #  Make sure that the maxRight is set to the maximum value from itself and height of the current element
                water_unit = maxRight - height[r]
                trapped_water += water_unit
        return trapped_water


    
# Calling function
solution = Solution()
height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
height2 = [4,2,0,3,2,5]
print(solution.trapping_rain_water(height1))
print(solution.trapping_rain_water(height2))
print(solution.trapping_rain_water_efficient(height1))
print(solution.trapping_rain_water_efficient(height2))