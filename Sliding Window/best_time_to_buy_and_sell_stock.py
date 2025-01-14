# Date: May 26th 2024 ##
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


##################### Examples ######################
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#####################################################
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#####################################################
# Solution reference: https://youtu.be/1pkOgXD63yU?si=XnbUc7-PpsGsdWgZ
# Summary of solution: Using concept similar to two pointers here. Initialize left pointer as 0 and right pointer as 1 and compare
# values on both the pointers. Increment pointer values based on element values on that pointers
#####################################################

from typing import List

class Solution:

    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def maxProfit_bruteforce(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]
                res = max(res, sell- buy)
        return res

    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def maxProfit(self, prices: List[int]) -> int:
        b = 0 # Initialize left pointer with 0th index
        s = 1 # Initialize right pointer with 1st index
        maxProfit = 0 # Initialize maxProfit with value 0

        while s < len(prices):  # Using this condition as we are not initializing our right pointer (i.e. `s`) as `len(prices)-1`. So we need to run the loop until `s` reaches the last element in the array. So we cannot use condition `b < s` because then we will get `index range` error
            if prices[b] >= prices[s]: # If value at pointer `b` is greater than or equal to value at pointer `s` 
                b = s # Set value of pointer `b` to the value of pointer `s` because we want to buy the stock at the least value available
            else: # If the value at pointer `s` is greater than the value at pointer `b``
                maxProfit = max(maxProfit, prices[s]-prices[b]) # Calculate the maxProfit between the current valuen of maxProfit and the difference of the current values of left and right pointer elements
            s += 1 # Increment the right pointer regardless of the condition

        return maxProfit
    
# Calling the function
solution = Solution()
prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
print(solution.maxProfit_bruteforce(prices1))
print(solution.maxProfit_bruteforce(prices2))
print(solution.maxProfit(prices1))
print(solution.maxProfit(prices2))