from threading import Thread,Semaphore
import time
import random



sm = Semaphore(3)

def task(name):
    sm.acquire()
    print('%s is useing' % name)
    time.sleep(2)
    sm.release()


if __name__ == '__main__':
    for i in range(20):
        t= Thread(target = task,args=(i,))
        t.start()