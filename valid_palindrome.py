## Date: May 23rd 2024 ##
#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
##################### Examples ######################
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#####################################################
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#####################################################
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
#####################################################
# Solution reference: https://www.youtube.com/watch?v=jJXJ16kPFWg
# Summary of solution: Develop own alphaNum function using ord() function to check for alphanumeric characters in the given string. Use that function along with
# two pointer technique to scan if value at the first pointer matches the value at the second one.
#####################################################

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def is_Palindrome(self, s: str) -> bool:
        newStr = ""
        for char in s:
            if char.isalnum(): # Using python's internal string function. Can be found using help(str)
                newStr += char.lower()
        #print(newStr)
        return  newStr == newStr[::-1] # Using python's internal function
    

    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def is_Palindrome_efficient(self, s: str) -> bool:
        # Using two pointer technique
        l = 0 # 0th index of the string
        r = len(s) - 1 # Last index of the string
        while l < r: # Make sure that left pointer is always smaller than right pointer
            while l < r and not self.alphaNum(s[l]): # Check if left pointer is smaller than right pointer and if the character at the left pointer is not alphanumeric
                l += 1 # increment the pointer as we don't want to compare non-alphanumeric character
            while r > l and not self.alphaNum(s[r]): # Check if the right pointer is greater than the left pointer and if the character at the right pointer is not alphanumeric
                r -= 1 # decrement the pointer as we don't want to compare non-alphanumeric character
            if s[l].lower() != s[r].lower():
                return False 
            l += 1
            r -= 1
        return True

        # Function to check if the character is an alphanumeric character. It checks if the character's ASCII value corresponds to
        # either A-Z, a-z or 0-9 and returns True. Otherwise returns False. Reference for ASCII values: https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    def alphaNum(self, c):
        if (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')):
            return True
        return False
    
    # Time complexity: O(n)
    # Space Complexity: O(n)
    def isPalindrome_self_developed(self, s: str) -> bool:
        if len(s) <= 1: # If length of the string is 0 or 1, return true
            return True
        else:
            string = ""
            for char in s:
                if char.isalnum():
                    string += char.lower()
            #print(string)
            pointer1 = 0
            pointer2 = len(string) - 1
            #print(pointer1)
            #print(pointer2)
            while pointer1 < pointer2:
                if string[pointer1] != string[pointer2]:
                    return False
                pointer1 += 1
                pointer2 -= 1
            return True

# Calling functions
solution = Solution()
s1 = "A man, a plan, a canal: Panama"
s2 = "1a2"
print(solution.is_Palindrome(s1))
print(solution.is_Palindrome(s2))
print(solution.is_Palindrome_efficient(s1))
print(solution.is_Palindrome_efficient(s2))
print(solution.isPalindrome_self_developed(s1))
print(solution.isPalindrome_self_developed(s2))