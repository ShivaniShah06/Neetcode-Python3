# Date: May 27th 2024 ##
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

##################### Examples ######################
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
#####################################################
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
#####################################################
# Solution reference: https://www.youtube.com/watch?v=gqXU1UyA8pk
# Summary of solution: Use two pointer & sliding window technique together. Maintain a dictionary to store the frequency of the letters in the current window and use window_size - most_freq_letter_in_current_window
# formula to compute how many characters needs to be changed in order to make a repeating sequence. If the difference is greater than k, move the left pointer else, keep moving right pointer
#####################################################

from typing import List

class Solution:
    def longestChar(self, s: str, k: int) -> int:
        # Time Complexity: O(26n)
        # Space Complexity: O(26) i.e. O(1) => If s contains only lowercase English letters, the maximum number of unique characters is 26. 
        # Thus, in this case, the space complexity of the dictionary would be O(26), which is effectively O(1) since 26 is a constant.

        start = 0 # Left pointer
        end = 0 # Right pointer
        longestChar = 0 # Variable to track the longestChar seen so far by replacing <= k letters in the window
        count = {} # Dictionary to store the letters and their frequency for the current window. We will use this to determine how many characters need to be changed in order to get the longestChar of repeating letters.
        # We can do this by getting the maximum value from the frequency of letters and subtracting it from the length of the window - which will give the number of less frequrnct letters in the window i.e. that needs to be replaced
        while end < len(s): # Whilst right pointer is less than the length of the given string
            if s[end] in count: # If the letter at the right pointer exist in the dictionary, then increment the frequency value for that letter
                count[s[end]] += 1
            else: # If the letter does not exist in the dictionary, then add it with value 1 i.e. it has repeated once
                count[s[end]] = 1
            if (end - start + 1) - max(count.values()) > k: # If the windowSize - most_frequent_character_inside_window is greater than k (allowed character replacements), then decrease the count for the value of that character in the 
                # dictionary and move the left pointer towards right
                count[s[start]] -= 1
                start += 1
            longestChar = max(longestChar, end - start + 1) # Calculate longest repeating character sequence by comparing maximum value from itself and the window size
            end += 1 # Increment the right pointer
        return longestChar

    def longestChar_more_efficient(self, s: str, k: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        start = 0
        end = 0
        longestChar = 0
        count = {}
        max_frequency = 0 # => Due to this variable, we reduce the space complexity to O(1). Learn imp facts about this here: https://youtu.be/gqXU1UyA8pk?si=YGbD9eTVTtxn80Yk&t=747

        while end < len(s):
            if s[end] in count:
                count[s[end]] += 1
            else:
                count[s[end]] = 1
            max_frequency = max(max_frequency, count[s[end]])
            if (end - start + 1) - max_frequency > k:
                count[s[start]] -= 1
                start += 1
            longestChar = max(longestChar, end - start + 1)
            end += 1
        return longestChar

# Calling functions
solution = Solution()
s1 = "ABAB"
k1 = 2
s2 = "AABABBA"
k2 = 1
s3 = "SHIVANI"
k3 = 3
print(solution.longestChar(s1,k1))
print(solution.longestChar(s2,k2))
print(solution.longestChar(s3,k3))
print(solution.longestChar_more_efficient(s1,k1))
print(solution.longestChar_more_efficient(s2,k2))
print(solution.longestChar_more_efficient(s3,k3))


