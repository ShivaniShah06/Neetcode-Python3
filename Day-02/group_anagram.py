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
# Solution reference: https://www.youtube.com/watch?v=9_iwjawJhdc, https://youtu.be/RcZsTI5h0kg?si=RNyP2jdobULx5h2m&t=407
# Summary of solution - group_anagram_improved: For every word in the given list, create a key inside a defaultdict. This key is a list of 26 characters with 0 bits for every character except
# the ones present in the word. Add word as the value for this key. Whenever a key is same, value will be appended to this list.
#####################################################

from typing import List
from collections import defaultdict

class Solution:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    def group_anagram(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            dic["".join(sorted(word))].append(word)
        return dic.values()
    
    # Time complexity: O(n)
    # Space complexity: O(n)
    def group_anagram_improved(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            lst = [0]*26 # 26 characters from a-z
            for char in word:
                lst[ord(char) - ord('a')] += 1 # ord maps characters to their ASCII values. Check this out to understand more https://youtu.be/9_iwjawJhdc?si=RXYfa0NFCLvNalL3&t=684
            lst = tuple(lst)
            dic[lst].append(word)
        return dic.values()
    
    def group_anagram_easy(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        result = []
        for s in strs:
            sorted_s = tuple(sorted(s)) # by default sorted() method returns list. As we want to add this as a key in a dictionary, we need to make it immutable hence converting it to tuple
            anagram_map[sorted_s].append(s)
        #print("anagram_map:",anagram_map)
        for value in anagram_map.values():
            result.append(value)
        return result




solution = Solution()
strs = ["a"]
strs1 = [""]
strs2 = ["eat","tea","tan","ate","nat","bat"]
print(solution.group_anagram(strs))
print(solution.group_anagram(strs1))
print(solution.group_anagram(strs2))
print(solution.group_anagram_improved(strs))
print(solution.group_anagram_improved(strs1))
print(solution.group_anagram_improved(strs2))
print(solution.group_anagram_easy(strs))
print(solution.group_anagram_easy(strs1))
print(solution.group_anagram_easy(strs2))