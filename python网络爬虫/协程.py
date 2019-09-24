from gevent import monkey
monkey.patch_all()
#猴子类
import gevent
import time
#定义函数，表示要执行的任务
def task(msg):
    for i in range(10):
        print(msg)
        time.sleep(3)

g1=gevent.spawn(task,'协程1')
g2=gevent.spawn(task,'协程2')
gevent.joinall((g1,g2))