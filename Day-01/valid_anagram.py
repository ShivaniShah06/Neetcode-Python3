class Solution():
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
