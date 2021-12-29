

import time
def aaa(f_type):
    def warpper1(fun):
        def timer(*args,**kwargs):
            s1 = time.time()
            res = fun(*args,**kwargs)
            s2 = time.time()
            print('time:',s2-s1)
            print(f_type)
            return res
            
        return timer
    return warpper1


@aaa('a')  
def show1(name):
    print('name:',name)
    time.sleep(2)
    return name+'123'

@aaa('b')  
def show2(name):
    print('name:',name)
    time.sleep(2)
    return name+'123'

@aaa('c')  
def show3(name):
    print('name:',name)
    time.sleep(2)
    return name+'123'

print(show1('abcd'))
print(show2('abcd'))
print(show3('abcd'))
