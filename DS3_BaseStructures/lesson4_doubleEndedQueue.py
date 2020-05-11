# class Deque:
#     def __init__(self):
#         self.items = []
#     def isEmpty(self):
#         return self.items == []
#     def size(self):
#         return len(self.items)
#     def addFront(self,item):
#         self.items.append(item)
#     def addRear(self,item):
#         self.items.insert(0,item)
#     def removeFront(self):
#         return self.items.pop(0)

# d = Deque()

# d.addFront(3)
# d.addFront(4)
# d.addRear('dogs')
# d.addRear('dog')
# print(d.isEmpty())
# print(d.size())



s = 'w我311232113我w'  
if s[::-1] == s:
    print(True)
else:
    print(False)