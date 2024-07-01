# Date: May 31st 2024 ##
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

##################### Examples ######################
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
#####################################################
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
#####################################################
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#####################################################
# Solution reference: https://www.youtube.com/watch?v=jSto0O4AJbM
# Summary of solution: Use two pointer and sliding window technique. Maintain two dictionaries with the alphabets and value of their count for both the strings. With each loop, move right pointer and add value to 
# the dictionary for `s` string. Maintain 2 variables to store the alphabets needed and how many alphabets current window has from the needed one. Change value of the `have` variable based on
# the current window and keep comparing.
#####################################################

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def minWindowSubstring(self, s: str, t: str) -> str:
        countT = {} # Dictionary to store alphabets and values in `t`
        window = {} # Dictionary to store alphabets and values in the current window
        
        for i in t: # Add alphabets and count from `t` to countT
            countT[i] = 1 + countT.get(i, 0)
        
        have = 0 # Variable to store the number of letters current window has from countT
         # Variable to store the number of letters from `t`. Using len(countT) here because in case where `t = "aaa"`, the value of need will be 3 if set to `len(t)` but in case of len(countT), it will be
         # 1. We can then compare the value for this alphabet from the respective dictionaries to compare the count
        need = len(countT)
        left = 0 # Left pointer
        result = [-1,-1] # Initiate result list
        resultLength = float("infinity") # Initiate resultLength to infinity as we need this variable with a value such that in the first loop, the first value is less than this value as we are looking for the minimum substring length

        for right in range(len(s)):
            current = s[right] # Assign current value at the right pointer to current variable
            window[current] = 1 + window.get(current, 0) # If the current letter exist in the window dictionary, then increment its value by 1 else add it with value 1

            # If current alphabet is in countT dictionary and the count for this alphabet is same as the count for this alphabet in the window dictionary, then increment value of the `have`
            # variable by 1
            if current in countT and window[current] == countT[current]:
                have += 1
            
            # While loop to run when the count for the number of alphabets in `t` and `s` in the current window are same
            while have == need:
                if right - left + 1 < resultLength: # If the current window lenght is less than resultLength, then update `result`` and `resultLength`` variables
                    result = [left, right]
                    resultLength = right - left + 1
                
                # pop left pointer values as we want our resultLength to be as small as possible. Note that this only runs until have == need condition is satisfied
                window[s[left]] -= 1
                # If after popping the left pointer value, the alphabet still exist in the `countT` and the count for this alphabet in `window` is less than the count for it in `countT`, that
                # means that we still need this alphabet and hence our condition need == have is not true anymore. Update the `have`` count by decrementing it
                if s[left] in countT and window[s[left]] < countT[s[left]]: 
                    have -= 1
                left += 1 # Increment the left pointer after popping a value from left
        left, right = result # Update the left and right pointer in the end to reflect values in the `result` variable
        # return `s` sliced as per window length only when resultLength was changed. If not, then return an empty string
        return s[left:right+1] if resultLength != float("infinity") else ""
    


# Calling functions
solution = Solution()
s1 = "ADOBECODEBANC"
t1 = "ABC"
s2 = "a"
t2 = "a"
s3 = "a"
t3 = "aa"
print(solution.minWindowSubstring(s1,t1))
print(solution.minWindowSubstring(s2,t2))
print(solution.minWindowSubstring(s3,t3))
