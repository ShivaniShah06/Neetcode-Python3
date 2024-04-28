## Date: April 28th 2024 & April 29th 2024##
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

##################### Examples ######################
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#####################################################
# Input: strs = [""]
# Output: [[""]]
#####################################################
# Input: strs = ["a"]
# Output: [["a"]]
#####################################################


from typing import List

class Solution:
    def group_anagram(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        






solution = Solution()
strs = ["a"]
strs1 = [""]
print(solution.group_anagram(strs))
print(solution.group_anagram(strs1))

