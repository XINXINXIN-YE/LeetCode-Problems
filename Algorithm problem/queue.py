
# List首端作为队尾，末端作为队首
# enqueue复杂度为O(n) dequeue复杂度为O(1)
# 若队首和队尾反过来，上述复杂度也反过来。
class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def front(self):
        return self.items[-1]
    
    def rear(self):
        return self.items[0]

""" # 热土豆问题
def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        
        simqueue.dequeue()
    
    return simqueue.dequeue()

print(hotPotato(['Bob', 'Seth', 'Peter', 'Charles', 'Krystal', 'Bill'], 7)) """

# 双端队列回文判断
# 首先定义双端队列
class DeQueue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        self.items.insert(0, item)
    
    def addRear(self,item):
        self.items.append(item)

    def removeRear(self):
        return self.items.pop()
    
    def removeFront(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
