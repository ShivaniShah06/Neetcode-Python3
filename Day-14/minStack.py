# Date: June 2nd 2024 ##
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

##################### Examples ######################
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#####################################################
# Solution reference: https://www.youtube.com/watch?v=qkLl7nAwDPo
# Summary of solution: Use list to implement this. Maintain 2 stacks. One is the main one to which you append and pop and another one is where you track the 
# minimum in the main stack at each value. So whenever you append or pop from the main stack, you also update another stack
#####################################################

class MinStack:
    # Implementing stack using list
    def __init__(self):
        self.stack = [] # Initialize stack from list
        # Since we need to perform every operation in O(1) time, also defining a stack to record minimum at current value in the actual stack
        # So whenever a value is popped from the main stack, we pop a value from minStack as well and we will still know the previous minimum
        self.minStack = [] 

    def push(self, val: int) -> None:
        self.stack.append(val) # append the value to the main stack
        if self.minStack: # the minStack could be empty while adding the first element, so having this condition
            val = min(val, self.minStack[-1]) # Compare current value with the value at the top of the min stack and calculate minimum between them
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop() # pop value from the top of the stack
        # pop value from top of the minStack as now the top value on the main stack is gone and the minimum for the previous value of the main stack
        # could be different
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1] # return the top value from the stack. Since it is LIFO and we are using list to implement it, it will be the last value in the list

    def getMin(self) -> int:
        return self.minStack[-1] # As we are maintaining a separate stack to track the minimum value in the stack, the value at the top of this stack can be returned