# 队列应用：打印机任务运行模拟
# 涉及的对象：打印机、任务、
import random

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

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm # 打印速度
        self.currentTask = None # 打印任务
        self.timeRemaining = 0 # 任务倒计时

    def tick(self):  # 打印1s
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self): # 打印机忙？
        if self.currentTask != None:
            return True
        else:
            return False
    
    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate

class Task():
    def __init__(self, time):
        self.timestamp = time # 生成时间戳
        self.pages = random.randrange(1, 21) # 打印页数
    
    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages
    
    def waitTime(self, currenttime):
        return currenttime - self.timestamp # 等待时间

def newPrintTask():
    num = random.randrange(1,181) # 1/180 的概率生成打印任务
    if num == 90: # 等于任意一个数字概率都等于 1/180
        return True
    else:
        return False

def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printqueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printqueue.enqueue(task)

        if (not labprinter.busy()) and (not printqueue.isEmpty()):
            nexttask = printqueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()
    
    aver = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(aver, printqueue.size()))

# START SIMULATION
for i in range(10):
    simulation(3600, 5)
