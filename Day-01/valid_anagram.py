## Date: April 27th 2024 ##
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

############## Example ##############
# Input: s = "anagram", t = "nagaram"
# Output: true
#####################################
# Input: s = "rat", t = "car"
# Output: false
#####################################
# Solution reference: https://www.youtube.com/watch?v=fHgVx_aFSlA
# Summary of solution: Create a dictionary and iterate through the first list to record the characters as keys and number of times they are
# seen as count. Iterate through the second dictionary and if the character does not exist in the dictionary, return false. Else, decrement the
# count of the the character based on the number of times it is seen. Finally, iterate through the values in dictionary and return false if any
# value is not equal to zero else, return true.
#####################################

class Solution:
    def isAnagram(self, s: str,t: str):
        dict_value = {} # create empty dictionary
        
        for letter in s: # check if the letter in `s`` exist in the dictionary
            if letter not in dict_value: # if not, add the letter as key and its value as 1
                dict_value[letter] = 1
            else:
                dict_value[letter] += 1 # if it exist, increment the value of that letter
        
        for letter in t: # check if the letters in t exist in dictionary
            if letter not in dict_value: # if not, return false
                return False
            else: # if it does exist, decrement its value
                dict_value[letter] -= 1
        
        for value in dict_value.values(): # iterate through the values in the dictionary 
            if value != 0: # return False if any value is anything other than 0 else return True
                return False
        return True
                

s = "ram"
t = "mar"
a = "rat"
b = "car"
solution = Solution()
print(solution.isAnagram(s,t))
print(solution.isAnagram(a,b))
