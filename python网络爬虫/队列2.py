from queue import PriorityQueue
class Job(object):
    def __init__(self,level,name):
        self.level=level
        self.name=name
    def __lt__(self, other):
        self.level<other.level

q3 = PriorityQueue()
q3.put(Job(3,'合格'))
q3.put(Job(2,'良好'))
q3.put(Job(4,'不及格'))
q3.put(Job(1,'优秀'))
while not q3.empty():
    a=q3.get()
    print("输出成绩",a.name)
