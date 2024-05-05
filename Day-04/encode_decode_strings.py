## Date: May 03 2024 ##
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
# Please implement encode and decode
# Because the string may contain any of the 256 legal ASCII characters, your algorithm must be able to handle any character that may appear
# Do not rely on any libraries, the purpose of this problem is to implement the "encode" and "decode" algorithms on your own

########################### Examples #############################
# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation: One possible encode method is: "lint:;code:;love:;you"
##################################################################
# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation: One possible encode method is: "we:;say:;:::;yes"
##################################################################
# Solution reference: https://www.youtube.com/watch?v=B1k_sxOSgv8
# Summary of solution: Encode the strings in list by appending the number of characters in each string and a '#'.
# While decoding, look for the '#' sign to differentiate between different strings. Use integer in the encoded string to add the next `n` characters in the
# current string.
##################################################################

from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s #for every member in the list, adding `number of characters in the member + #` to encode it
        return res
    
    def decode(self, strs: str) -> List[str]:
        res,i = [],0
        while i < len(strs): 
            j = i
            if strs[j] != "#":
                j += 1
            length = int(strs[i:j])
            res.append(strs[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res


    
# Calling functions

solution = Solution()
trial1 = ["lint","code","love","you"]
string1 = solution.encode(trial1)
print(string1)
decoded1 = solution.decode(string1)
print(decoded1)
trial2 = ["we", "say", ":", "yes"]
string2 = solution.encode(trial2)
print(string2)
decode2 = solution.decode(string2)
print(decode2)