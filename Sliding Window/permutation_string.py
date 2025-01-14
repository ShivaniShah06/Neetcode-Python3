# Date: May 28th 2024 ##
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

##################### Examples ######################
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
#####################################################
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
#####################################################
# Solution reference: https://www.youtube.com/watch?v=UbyhOgBN834&t=935s
# Summary of solution: Use two pointer and sliding window technique. Maintain two arrays of size 26 for each string and use ord to associate index to each character from a-z. Have a variable to track the total matches at each iteration by comparing values in these arrays.
# As soon as the variable that tracks the match is equal to 26, return true.
#####################################################

class Solution:
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 # Left pointer
        r = 0 # Right pointer
        s1Count = [0]*26 # List to store the count of alphabets in the current window in s1 string
        s2Count = [0]*26 # List to store the count of alphabets in the current window in s2 string
        matches = 0 # Tracks the number of indices that have same values in s1Count and s2Count

        if len(s1) > len(s2): # If the length of s1 is greater than s2, it wont be possible to have the same characters sequential in s2
            return False # So return false
        
        for i in range(len(s1)): # Update s1Count and s2Count arrays for the numbers of characters in s1 string
            # we are also modifying s2Count array here as it will allow us to use right pointer from len(s1) in the upcoming for loop. That will mean that our sliding window from
            # the beginning will be same as the length of s1 string
            s1Count[ord(s1[i]) - ord('a')] += 1 # For the character at ith index in s1 string, increment the value for s1Count on the corresponding index
            s2Count[ord(s2[i]) - ord('a')] += 1 # For the character at ith index in s2 string, increment the value for s2Count on the corresponding index
        
        # Update the matches variable to have the current match value. If the value at an index in both the arrays are same, then increment matches by 1
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0
            

        # For loop for the main logic. Here, the loop initiates r at len(s1) inclusively and goes until len(s2)
        for r in range(len(s1), len(s2)):
            if matches == 26: # Check if all the values in s1Count and s2Count are equal
                return True
            
            index = ord(s2[r]) - ord('a') # Get index value for the value for the character at rth index in s2 array
            s2Count[index] += 1 # Increment the value for the corresponding index in s2Count
            if s1Count[index] == s2Count[index]: # If counts in both the arrays are same for this index then increment the matches variable value by 1
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]: # If (value at this index in s1Count array + 1) is same as the current value of s2Count array at this index,
                # that means that these values were same before incrementing the value of s2Count[index] in this loop earlier and so decrement the matches variable value
                matches -= 1

            # Repeat the same logic as above for the left pointer. The only difference is that we should be moving ahead in our string by incrementing the value of the left pointer, 
            # so we update the count for that particular index by decrementing 1 from it and the logic follows while comparing these values and updating the matches variable
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            l += 1 # Increment the value for the left pointer

        return matches == 26 # If matches == 26, return true. Else false. We don't return False directly because after the for loop ends, we are not checking if matches == 26 or not

            
# Calling functions
solution = Solution()
s1 = "ab"
s2 = "eidbaooo"
s3 = "ab"
s4 = "eidboaoo"
print(solution.checkInclusion(s1,s2))
print(solution.checkInclusion(s3,s4))
