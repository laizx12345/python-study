from multiprocessing import Process
import time


def task(name,n):
    print('%s is running' % name)
    time.sleep(n)
    print('%s is over ' % name)


if __name__ == '__main__':
    s_time = time.time()
    p1 = Process(target=task, args=('jason1 ',2))
    p2 = Process(target=task, args=('jason2 ',3))

    p1.daemon = True  #将进程设置为守护进程
    p2.start()
    p1.start()  # 告诉操作系统帮你创建一个进程异步

    p1.join()  #主进程等待子进程结束后运行
    p2.join()
    print('主',time.time()-s_time)
