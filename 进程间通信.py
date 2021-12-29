
from multiprocessing import Process,current_process,Lock,Queue,JoinableQueue
import time
import os
import random

'''
#队列queue模块

# from multiprocessing import Queue
import queue
q  = queue.Queue(maxsize = 5)   #设置最大数据容量5，有默认值

q.put(111)   #向队列中存数据，队列如果满了，后续存放数据会一直等待

q.get()   #从队列中取一个数据，队列如果为空，取的话会一直等待新数据到来
q.get(timeout=3)  #没有数据等待3秒后报错
q.get_nowait() #没有数据直接报错

q.full()    
q.empty()
'''

def producer(name,food,q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        print(name,'生产了',food,i)
        q.put([name,food+str(i)])
    

def consummer(name,q):
    while True:
        food = q.get()
        # if food is  None:
        #     break
        time.sleep(0.5)
        print(name,'吃了',food[0],'做的',food[1])
        q.task_done()
if __name__ == '__main__':
    # q = Queue()
    q = JoinableQueue()
    p1 = Process(target = producer,args = ("厨师1","包子",q,))
    p2 = Process(target = producer,args = ("厨师2","馒头",q,))
    p3 = Process(target = producer,args = ("厨师3","饺子",q,))
    c1 = Process(target=consummer,args = ('食客1',q,))
    c2 = Process(target=consummer,args = ('食客2',q,))
    c1.daemon = True
    c2.daemon = True
    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    #等待生产完毕 ,队列中加入特定符号
    p1.join()
    p2.join()
    # q.put(None)
    # q.put(None)
    # print(q.get())
    q.join()
    print('过程执行完毕')
    '''
    JoinableQueue每当你往该队列中存入数据的时候内部会有一个计数器+1
    当你调用task_done的时候计数器-1
    q.join()当计数器为0的时候才往后运行
    '''


