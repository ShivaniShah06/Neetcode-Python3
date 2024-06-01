# Date: June 1st 2024 ##
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

##################### Examples ######################
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#####################################################
# Input: nums = [1], k = 1
# Output: [1]
#####################################################
# Solution reference: https://www.youtube.com/watch?v=jSto0O4AJbM
# Summary of solution: Use two pointer and sliding window technique. Maintain two dictionaries with the alphabets and value of their count for both the strings. With each loop, move right pointer and add value to 
# the dictionary for `s` string. Maintain 2 variables to store the alphabets needed and how many alphabets current window has from the needed one. Change value of the `have` variable based on
# the current window and keep comparing.
#####################################################

from typing import List
from collections import deque

class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = right = 0 # Initiate left and right pointers
        q = deque() # Use deque class
        output = [] # Initiate list for output

        while right < len(nums): # Run the loop until right pointer reaches the last element in the nums
            # If there is any element in the `q` AND if the right most element in the `q` is smaller than the current element, then pop the smaller element
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right) # If right most element in the `q` is bigger than the current element, then append the current element's index to the `q`

            # Making sure that window size remains intact. Verify that the value of the left pointer is less than the left most element in the `q`. 
            # If not, then pop the left most element from the `q`
            if left > q[0]:
                q.popleft()

            # Making sure that we only append value to the `output` list when window size is k. Since index size corresponding to the value of k will always
            # be k-1, we use this condition. Eg: For k=3, index will be 0 to 2 so right will be 3-1 = 2
            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1 # Increment the left pointer value once we append value to the output list and when the value of right pointer is equal to k
            right += 1 # Always increment the right pointer value
        return output
    
# Calling functions
solution = Solution()
nums1 = [1,3,-1,-3,5,3,6,7]
k1 = 3
nums2 = [1]
k2 = 1
print(solution.maxSlidingWindow(nums1,k1))
print(solution.maxSlidingWindow(nums2,k2))
