from threading import Thread,Event
import time

event = Event()

def light():
    print('红灯')
    time.sleep(3)
    print('绿灯')
    event.set()

def car(name):
    print('%s waitting' % name)
    event.wait()
    print('%s is running' % name) 



if __name__ == '__main__':
    t = Thread(target=light)
    t.start()

    for i in range(20):
        t=Thread(target=car,args=(i,))
        t.start()