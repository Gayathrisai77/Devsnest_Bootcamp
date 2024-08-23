########## implementation of a basic stack using class method ############

class stack:
    def __init__(self):
        self.stack = []
        
    def push(self,data):
        self.stack.append(data)
        
    def pop(self):
        if self.isempty():
            return "stack is empty"
        return self.stack.pop()
        
    def peek(self):
        if self.isempty():
            return "stack is empty"
        return self.stack[-1]
        
    def isempty(self):
        return len(self.stack) == 0
        
    def size(self):
        return len(self.stack)
        
mystack = stack()
mystack.push("a")
mystack.push("b")
mystack.push("c")
mystack.push("d")
mystack.push("e")
mystack.push("f")
print("stack:",mystack.stack)
print("length of the stack is:",mystack.size())
print("pop:",mystack.pop())
print("peek element:",mystack.peek())
print("is empty:",mystack.isempty())
#----------------------------------------------------------------------------------------------------------------------------------
########## Reversing a stack ############

class stack:
    def __init__(self):
        self.stack = []
        
    def push(self,data):
        self.stack.append(data)
        
    def pop(self):
        if self.isempty():
            return "stack is empty"
        return self.stack.pop()
    def reverse(self):
        self.stack.reverse()
        
mystack = stack()
mystack.push("a")
mystack.push("b")
mystack.push("c")
mystack.push("d")
mystack.push("e")
mystack.push("f")
print("original stack:",mystack.stack)
mystack.reverse()
print("reversed stack:",mystack.stack)

#-----------------------------------------------------------------------------------------------------------------------------------
###### REVERSING A STRING USING STACKS ################
#Input: A string, e.g., "hello".
# Output: The reversed string, e.g., "olleh".
def reverse_string(string):
    stack = []
    for i in string:
        stack.append(i)
    rev = " "
    while len(stack) != 0:
            rev += stack.pop()
    return rev
    
string = "hello"
print(reverse_string(string))

#----------------------------------------------------------------------------------------

# 2)Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
def reversestring(s):
    
    left = 0
    right = len(s)-1
    while left < right:
        s[left],s[right] = s[right],s[left]
        left += 1
        right -= 1
        
s = ["h","e","l","l","o"]
print("original string:",s)
reversestring(s)
print("reversed string:",s)



#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Explain the push, pop, and peek operations in a stack.
# Input: Operations like push(3), push(4), peek(), pop().
# Output: Values returned by operations, e.g., peek() returns 4, pop() removes 4.
class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,data):
        self.stack.append(data)
   
    def pop(self):
        return self.stack.pop()
        
    def peek(self):
         return self.stack[-1]
         
         
mystack = Stack()
mystack.push(3)
mystack.push(4)
print("stack is :",mystack.stack)
mystack.peek()
print("peek element is:",mystack.peek())
print("remove:",mystack.pop())

#--------------------------------------------------------------------------------------------------------------------------------------

# Given a stack of integers, sort it so that the smallest elements are at the top.
  # Input: A stack, e.g., [5, 3, 1, 4, 2].
  # Output: The sorted stack, e.g., [1, 2, 3, 4, 5].
def sorted_stack(stack):
        aux_stack = []
        while len(stack) > 0:
            smallest = stack[-1]
            for i in range(len(stack)):
                if stack[i] < smallest:
                   smallest = stack[i]
            aux_stack.append(smallest)
            stack.remove(smallest)
        return aux_stack
        
stack = [5,3,1,4,2]
print("sorted stack is:",sorted_stack(stack))

#-----------------------------------------------------------------------------------------------------------------------------------------------------
####### implementing a queue using two stacks ##########
class Stack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self,data):
        self.stack1.append(data)
        
    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                return None
            while self.stack1:
                
                self.stack2.append(self.stack1.pop())
                
        return self.stack2.pop() 
            
    def print_q(self):
        print("queue from from front to rear:",self.stack2[::-1] + self.stack1)
            
myqueue = Stack()
myqueue.enqueue("jk")
myqueue.enqueue("V")
myqueue.enqueue("jimin")
myqueue.print_q()
print("deleted one is:",myqueue.dequeue())
myqueue.print_q()

#----------------------------------------------------------------------------------------------------------------------------------------------------
####### VALID PARENTHESIS ##############
def isvalidparenthesis(s):
    stack = []
    openings = {"(":")","{":"}","[":"]"}   # maping openings to corresponding closings
    for char in s:
        if char in openings:   # if open parenthesis
            stack.append(char)
        else:   # if closed one with this one we will check the top elemnt in stack by poping out. if both matched ok if not return false
            if not stack or openings[stack.pop()] != char:
                return False
    return len(stack) == 0     # if all matched stack will be empty then true
        
        
print(isvalidparenthesis("()"))
print(isvalidparenthesis("([])"))
print(isvalidparenthesis("(])"))

#-------------------------------------------------------------------------------------------------------------------------------------------------
######### Removing all adjacent duplicates in a string #############
# Input: s = "azxxzy"
# Output: "ay"
def removingduplicates(s):
    stack = []
    for char in s:
        if not stack or stack[-1] != char:
            stack.append(char)
        else:
            stack.pop()
    return stack
    
s = "azxxzy"
print(removingduplicates(s))

#############   NEXT GREATER ELEMENT ########################
# Input: arr[] = [ 4 , 5 , 2 , 25 ]
# Output: (1).4  –> 5 (2). 5 –>  25 (3). 2 –> 25 (4).25 –>  -1
                      
def nextgreaterelement(arr):
    stack = []
    result = [-1]*len(arr)
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    return result
    
arr = [30,4,5,2,25]
print(nextgreaterelement(arr))
#---------------------------------------------------------------------------------------
#input =  [ 13 , 7, 6 , 12 ]
def nextgreaterelement(nums):
    stack = []
    result = [-1]*len(nums)
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    return result
    
nums = [13,8,6,12]
print(nextgreaterelement(nums))

#-----------------------------------------------------------------------------------------------------------------
class Minstack:
    def __init__(self):
        self.stack = []
        self.minstack = []
        
    def push(self,data):
        self.stack.append(data)
        if not self.minstack or data <= self.minstack[-1]:
            self.minstack.append(data)
            
    def pop(self):
        if not self.stack:
            return None
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        return self.stack.pop()
        
    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]
        
    def getmin(self):
        if not self.minstack:
            return None
        return self.minstack[-1]
        
        
min_stack = Minstack()
min_stack.push(1)
min_stack.push(2)
min_stack.push(3)
min_stack.push(4)
min_stack.push(-5)

print("current stack:",min_stack.stack)
print("current stack:",min_stack.minstack)

print("get min:",min_stack.getmin())
print("popped elemnet:",min_stack.pop())
print("min value after popping:",min_stack.getmin())

#------------------------------------------------------------------------------------------------------------------------------------------------
###################### POSTFIX EXPRESSION / REVERSE POLISH NOTATION #######################
def postfix(expression):
    stack = []
    def operation(operator,operand1,operand2):
        if operator == "+":
            return operand1+operand2
        if operator == "-":
            return operand1 - operand2
        if operator == "*":
            return operand1*operand2
        if operator == "/":
            return operand1*operand2
            
    for c in expression:
            if c.isdigit():
               stack.append(int(c))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = int(operation(c,operand1,operand2))
                stack.append(result)
    return stack.pop()
        
expression = "235+*59-72*"
print(postfix(expression))
               
            