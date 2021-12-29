from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time


# pool = ThreadPoolExecutor(5)
pool = ProcessPoolExecutor()
def task(n):
    print('n=',n)
    time.sleep(2)
    return n**2

def call_back(n):
    print('call_back:',n.result())
if __name__ == "__main__":
    t_list=[]
    for i in range(10):
        res = pool.submit(task,i).add_done_callback(call_back)
        t_list.append(res)

    # pool.shutdown()
    # for i in t_list:
    #     print(i.result())