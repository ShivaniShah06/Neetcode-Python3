## Date: April 30th 2024 ##
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

##################### Examples ######################
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#####################################################
# Input: nums = [1], k = 1
# Output: [1]
#####################################################
# Solution reference: https://youtu.be/phNDYf1xzco?si=vk4xuuWhwpc58HfG
# Summary of solution: Create a list of size (length of give list+1). Treat its indices as count and put values on those indices based on the number of times a value is repeated in the given list
#####################################################

from typing import List
from collections import Counter

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def top_k_frequent_elements(self, nums: List[int], k: int) -> List[int]:
        # can also use a dictionary instead of "Counter" to avoid using internal library. Use a for loop to count the frequency of numbers
        counter = Counter(nums) # will give a dictionary with number as key and its count as value
        n = len(nums)
        print(counter)
        buckets = [0] * (n+1) # creating a list of size len(nums)+1 with 0 as values - idea is to treat index as count and add index values from nums. Nums which are repeating
        # index times should be added as a list on that index

        for num,freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
        
        print(buckets)

        result = []

        for i in range(n, -1, -1): # iterating through list in reverse. -1 is for reverse and another -1 in the middle is to iterate through nums until including 0
            if buckets[i] != 0: # if the value at ith index in the bucket is not zero, then add the value to a list called result. We used extend as bucket[i] could be a list and result is also a list. Extend adds two lists. It is like a union operation.
                result.extend(buckets[i])
            if len(result) == k: # as soon as the length of result list is same as the value of k, break the loop and return the value
                break
        return result




nums = [1,1,1,2,2,3]
solution = Solution()
print(solution.top_k_frequent_elements(nums,2))