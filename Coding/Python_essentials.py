# Hash-backed maps
from queue import Queue
dictionary = {
    "harry": 101,
    "garry": 102,
    "larry": 103
}

print(dictionary["harry"])

dictionary["larry"] = 104
# all keys
for x in dictionary:
    print(x)
# all values
for x in dictionary:
    print(dictionary[x])

print("-----------------------")
# Queue
# Initialize queue
q = Queue(maxsize=3)
print(q.qsize())
# add elements to queue
q.put(3)
q.put(5)
q.put(7)
# return bool for full queue
print(q.full())
# Remove elements from queue
q.get()
# Return bool for empty queue
print(q.empty())

print("-----------------------")
# approach 1
stack = [1,2,3,4,5]
stack.pop()
stack.append(6)
print(stack)

# approach 2

class Stack:
    def __init__(self):
        self.stack = []

    # check if empty
    def isempty(self):
        return len(self.stack)==0
    # push element
    def push(self,p):
        self.stack.append(p)
    # pop element
    def pop(self):
        return self.stack.pop()


