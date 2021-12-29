
from multiprocessing import Process,current_process,Lock
import json
import time
import os
import random

# def task():
#     print('%s is running' % current_process().pid)    #查看当前进程
#     print('%s is running' % os.getpid())        #查看当前进程
#     print('%s is running' % os.getppid())     #查看父进程
#     time.sleep(3)


def search(i):
    with open('data.json','r',encoding='utf8') as f:
       dic = json.load(f)
    print(i,'check:',dic.get('ticket_num'))
    pass

def buy(i):
    with open('data.json','r',encoding='utf8') as f:
       dic = json.load(f)
    time.sleep(0.5)
    if dic.get('ticket_num')>0:
        dic['ticket_num'] -=1
        with open('data.json','w',encoding='utf8') as f:
            json.dump(dic,f)
        print(i,'购票成功')
    else:
        print(i,'购票失败')

# def run(i):
#     search(i)
#     buy(i)

def run(i,mutex):
    search(i)
    #为买票环节加锁
    mutex.acquire()
    buy(i)
    mutex.release()


if __name__ == '__main__':

    # p = Process(target=task)
    # p.start()
    # p.terminate()     #结束当前进程
    # p.is_alive()      #判断是否存活

    # for i in range(10):
    #     p= Process(target=run,args=(i,))
    #     p.start()

    mutex = Lock()

    for i in range(10):
        p= Process(target=run,args=(i,mutex))
        p.start()
