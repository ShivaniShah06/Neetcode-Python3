# IMPORTANT FACTS

## **IMPORTS**

- `from collections import Counter`
   - If you use this as `counter = Counter(<list_of_int>)` it returns a dictionary with the values in the list as keys and its frequency in the list as values
- `from collections import defaultdict`
   - Details under Dictionary/Hashmaps section

## **IMPORTANT IN-BUILT FUNCTIONS**
- ord() : Gives the ASCII value of the character. Eg: ord('a')

## **List**
- The search is of O(n) time complexity
- The search with index is O(1) time complexity

## **Dictionary/Hashmaps**
- Dictionary `cannot` have anything that it `mutable as its key`
- defaultdict (from collections import defaultdict) are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists. By default, all keys in dictionaries need to be initialized. In order to avoid that, use `Defaultdict` to have keys initialized by default
- The search is O(1) time complexity
- Retreiving data:
   - hashmap.keys() - returns all of the keys from the dictionary in form of a list
   - hashmap.values() - returns all of the values from the dictionary in form of a list
   - hashmap.items() - returns a list of the all key-value pairs as tuples

## **Two Pointer technique/pattern**
- Can be used for arrays, string, and some linked list questions
- Refer to this video to understand in detail: https://www.youtube.com/watch?v=-gjxg6Pln50



