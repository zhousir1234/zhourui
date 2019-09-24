from queue import Queue
#队列先进后出
from queue import LifoQueue
q1=Queue(maxsize=4)
q1.put(1)
q1.put(2)
q1.put(3)
print(q1.full())
print(q1.get())
print(q1.qsize())
print(q1.get())
print(q1.get())
print("*"*40)
for i in range(4):
    q1.put(i)
while not q1.empty():
    print(q1.get())
print("*"*40)
q2=LifoQueue()
for i in range(5):
    q2.put(i)
while not q2.empty():
    print(q2.get())
