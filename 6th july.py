######### finding kth smallest element ########
# import heapq
# def kthsmallestelement(array,k):
#     maxheap = []
#     for num in array:
#         heapq.heappush(maxheap,-num)
#         if len(mxheap) > k:
#             heapq.heappop(maxheap)
            
#     return -maxheap[0]
# array = [1, 3, 6, 5, 9, 8]
# k = 3
# print(kthsmallestelement(array,k))

############## Valid parenthesis ########
# def isvalidparenthesis(s):
#     stack = []
#     openings = {"(":")","[":"]","{":"}"}
#     for char in s:
#         if char in openings:
#             stack.append(char)
#         else:
#             if not stack or openings[stack.pop()] != char:
#                 return False
                
#     return len(stack) == 0
    
# print(isvalidparenthesis("[{()}]"))

###########   implementing a queue using two stacks ##################
class stackqueue:
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
            
    def print_queue(self):
        print("queue :",self.stack2[::-1]+self.stack1)
        
            
myqueue = stackqueue()
myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.print_queue()
myqueue.dequeue()
myqueue.print_queue()
myqueue.enqueue(3)
myqueue.print_queue()
































            
    