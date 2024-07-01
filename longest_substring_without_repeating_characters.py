# Date: May 26th 2024 ##
# Given a string s, find the length of the longest substring without repeating characters.

##################### Examples ######################
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#####################################################
# Input: s = "bbbbb"
# Output: 1
#####################################################
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#####################################################
# Solution reference: https://youtu.be/302mmnX1voo?si=PyqzCgxs5iCvsf6F
# Summary of solution: Using sliding window technique. We maintain a dictionary with letters as key and their indices as values. We keep 2 pointers: start and end.
# end keeps on incrementing and start stays at the old value until it finds a value that is present in the dictionary and whose index's value is greater than start.
# Then calculate the maxLength and also increment the start pointer value
#####################################################

from typing import List

class Solution:
    # Time Complexity:
    # Space Complexity:
    def longest_substring(self, s: str) -> int:
        start = 0 # Pointer at the start of the string
        end = 0 # Pointer at the end of the string
        maxLength = 0 # Variable to maintain maximum length of the substring seen so far
        d = {} # Dictionary to maintain letters as key and the index of the letter seen latest (when repeated) as the value
        while end < len(s): # Run the loop until the end pointer reaches the last index
            # If the value at the end pointer in `s` exist in the dictionary and if the value for that letter in dictionary is greater than the 
            # value of the start pointer i.e. if the index of that letter in the dictionary is greater than the index at which the start pointer is pointing 
            # (that means that the letter is repeated!)
            if s[end] in d and d[s[end]] >= start: 
                start = d[s[end]] + 1 # Update the value of the start pointer to the index value of index next to the value for the letter in the dictionary
            maxLength = max(maxLength, end - start + 1) # Calculate the maxLength. end - start + 1 because we need to include end and start both
            d[s[end]] = end # Update the value for the letter in the dictionary to the latest index where it was last seen
            end += 1 # Increment the end pointer
        return maxLength
    
# Calling functions
solution = Solution()
s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
print(solution.longest_substring(s1))
print(solution.longest_substring(s2))
print(solution.longest_substring(s3))
