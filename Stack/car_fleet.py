# Date: June 14th 2024 ##
# There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

# You are given two integer array position and speed, both of length n, where position[i] is the starting mile of the ith car 
# and speed[i] is the speed of the ith car in miles per hour.

# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

# A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

# If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

# Return the number of car fleets that will arrive at the destination.

##################### Examples ######################
# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

# Output: 3

# Explanation:

# The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
# The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
#####################################################
# Input: target = 10, position = [3], speed = [3]

# Output: 1

# Explanation:

# There is only one car, hence there is only one fleet.
#####################################################
# Input: target = 100, position = [0,2,4], speed = [4,2,1]

# Output: 1

# Explanation:

# The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
# Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
#####################################################
# Solution reference: https://www.youtube.com/watch?v=Pr6T-3yB9RM
# Summary of solution: Summary in the comments!
#####################################################

from typing import List

class Solution:
    # Time Complexity: O(nlogn) -> `n` for iterating through the array and `logn` for sorting the array based on the position
    # Space Complexity: O(n)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create an array with pair of position,speed of car using list comprehension
        positionSpeed = [[p,s] for p,s in zip(position, speed)]
        stack = [] # Declare stack to store car fleets
        # Sort the pair of [position,speed] of cars using sorted method. This will sort `positionSpeed` array based on value of position
        # Iterate through the sorted array in reverse order
        # Calculate the time required to reach the target during each iteration and append it to stack
        # Since we are moving from left to right (reverse) in the array `positionSpeed` the distance remaining to cover to reach to the target
        # would keep increasing as we move towards right. After appending the value to the top of the stack, we check if the car that has to cover more distance
        # takes less time than the one that has to cover less distance. If this condition becomes true, then we pop the value of the 
        # car that is moving faster i.e. the car that has to cover more distance (as its speed will change to car that is moving slower as per the question)
        for p,s in sorted(positionSpeed)[::-1]:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    

solution = Solution()
target1 = 12
position1 = [10,8,0,5,3]
speed1 = [2,4,1,1,3]
target2 = 10
position2 = [3]
speed2 = [3]
target3 = 100
position3 = [0,2,4]
speed3 = [4,2,1]
print(solution.carFleet(target1, position1, speed1))
print(solution.carFleet(target2, position2, speed2))
print(solution.carFleet(target3, position3, speed3))