# Date: June 2nd 2024 ##
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

##################### Examples ######################
# Input: s = "()[]{}"
# Output: true
#####################################################
# Input: s = "()"
# Output: true
#####################################################
# Input: s = "(]"
# Output: false
#####################################################
# Solution reference: https://www.youtube.com/watch?v=WTzjTskDFMg
# Summary of solution: Use list as stack and map parantheses in a dictionay for comparison. Iterate through each character in the string, compare with the value at the top of the
# stack and return True or False accordingly. Make sure that the stack is empty in the end.
#####################################################

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # You get to know that you need to use stack because you need to compare next value with the with the previous one. If using for loop to append to
    # a list, you have to compare current value with the top of the stack
    def validParantheses(self, s: str) -> bool:
        stack = [] # Initialize stack using list
        closeToOpen = {"]" : "[", "}" : "{", ")" : "("} # Map of matching parantheses

        # For loop to go through each character in the string
        # If the curent character is a closing bracket, check if the value for that bracket in the dictionary is a same as the top value in the stack
        # If yes, then pop that value from the stack and proceed to the next one else return False
        for c in s:
            if c in closeToOpen: 
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            # We append everything to the stack without checking if that value exist in the dictionary and so, in final return statement, we make
            # sure that the stack is empty before returning True
            else: 
                stack.append()
        return True if not stack else False