class stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, items):
        self.items.append(items)
        print(items)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
s=stack()
print(s.isEmpty())
print("push")
s.push(1)
s.push(2)
s.push(3)
print("peek",s.peek())
print("pop")
print(s.pop())
print(s.pop())
print("size",s.size())
