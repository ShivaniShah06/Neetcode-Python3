# Date: June 26th 2024 ##
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

##################### Examples ######################
# Input: piles = [3,6,7,11], h = 8
# Output: 4
#####################################################
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
#####################################################
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
#####################################################
# Solution reference: https://www.youtube.com/watch?v=U2SozAs9RzA
# Summary of solution: Have left and right pointers. Left pointer can be 1 or `total number of bananas/hours` and right pointer can be maximum number of bananas from piles.
# Assume this as an array `k` and apply binary search on this `k`. Move left and right pointers based on comparison between
# the hours obtained by calculating how many hours does koko take by eating `k` bananas in an hour and `h` provided in the question.
#####################################################

from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # You can also keep l = 1 but it does not make sense. The minimum number of bananans koko should eat to complete all the bananas in given hours
        # would be total number of bananas in all the piles divided by the number of hours
        l = math.ceil(sum(piles)/h)
        r = max(piles) # Maximum number of bananas koko can eat in an hour is maximum number of bananas from the piles of bananas
        # Initializing result variable with maximum bananas in pile because maximum number of bananas koko can eat in an hour is maximum bananas in piles
        result = r

        # Run the loop until left pointer is less than or equal to right pointer
        # For piles = [3,6,7,11], k will look like this: [1....11]. We run binary search on this k 
        # and calculate hours for each value of k for each value in piles and check if hours are 
        # less than `h`. If they are, it means that koko is eating faster but she prefers to eat slow, so we
        # reduce the number of bananas she eats per hour by moving right pointer on the left of `k` as `k` number
        # of bananas per hour leads to less number of hours than what koko has to eat total bananas. If hours is
        # greater than `h` then we increase the speed of eating bananas by moving left pointer to the next value from
        # `k`
        while l <= r:
            k = (l + r) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                result = min(result, k)
                r = k - 1
            else:
                l = k + 1
        return result
