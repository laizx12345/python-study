from multiprocessing import Process
from threading import Thread
import time


def task(name):
    print('task is running')
    time.sleep(3)
    print('task is over')


class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
        pass
    def run(self):
        print('%s is running' % self.name)
        time.sleep(3)
        print('%s is over' % self.name)
if __name__ == '__main__':
    # t = Thread(target=task,args=('aaa',))
    t = MyThread('aaa')
    t.start()
    print('主')