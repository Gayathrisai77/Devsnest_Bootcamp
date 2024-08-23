#Given a string reverse it using stack:
# Input: A string, e.g., "hello".
# Output: The reversed string, e.g., "olleh".

# def reverse_string(string):
#     stack = []
#     for i in string:
#         stack.append(i)
#     rev = " "
#     while len(stack) != 0:
#         rev += stack.pop()
#     return rev
# string = "hello"
# print(reverse_string(string))


# Explain the push, pop, and peek operations in a stack.
# Input: Operations like push(3), push(4), peek(), pop().
# Output: Values returned by operations, e.g., peek() returns 4, pop() removes 4.

# stack = []
# maxsize = 5
# def push(x):
#   if len(stack) == maxsize:
#     print("stack is full")
#   else:
#     stack.append(x)
#     return x
# def pop():
#   if len(stack) == 0:
#     print("stack is empty")
#   else:
#     stack.pop()
# def peek():
#   if len(stack) == 0:
#     print("stack is empty")
#   else:
#     print(stack[-1])
# print(push(3))
# print(push(2))
# print(push(1))
# print(push(4))
# print(peek())
# print(pop())

  # Given a stack of integers, sort it so that the smallest elements are at the top.
  # Input: A stack, e.g., [5, 3, 1, 4, 2].
  # Output: The sorted stack, e.g., [1, 2, 3, 4, 5].
# def sorted_stack(stack):
#   aux_stack = []
#   while len(stack) > 0:
#     smallest = stack[-1]
#     for i in range(len(stack)):
#       if stack[i] < smallest:
#         smallest = stack[i]
#     aux_stack.append(smallest)
#     stack.remove(smallest)
#   return aux_stack
# print(sorted_stack([5,3,1,4,2]))


######### first non repeating character in a string using queue ###########
from collections import deque,defaultdict   #we have to import the data structure from the collections
def first_nonrepeated_character(string):
    queue = deque()              #we are creating queue to store characters
    frequency = defaultdict(int)  #to store the frequency means count
    for char in string:
        frequency[char] += 1     # it will store the count of each string
        queue.append(char)
        
        while queue and frequency[queue[0]]>1:  #run this loop until queue and count greaterthan 1
            queue.popleft()                     # if count more than 1 then removee it
    if not queue:
        return None                       #if there is no value return none
    else:
        return queue[0]                  # if there is anything return first
string = "aavvbbgeeryy"
result = first_nonrepeated_character(string)
print("first non repeating charcter is:",result)
    











