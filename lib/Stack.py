class Stack:
    limit = 100
    def __init__(self, items = [], limit = None):
        self.items = items
        self.limit = limit
        
    def isEmpty(self):
        return len(self.items) == 0


    def push(self, item):
        if self.limit is None or len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stack is full")


    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.limit is not None and len(self.items) == self.limit

    def search(self, target):
        try:
            index = self.items.index(target)
            return self.size() - index - 1
        except ValueError:
            return -1

# stk = Stack([1,2,3,4,5])
# print(stk.size())
    
stk = Stack([1], 1)    
stk.push(1)
stk.push(2)
print(stk.full())