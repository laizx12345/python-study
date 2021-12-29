

count = 1 

def func():
    # 局部名称空间可以引用全局名称空间的变量，但是不能修改
    count +=1
    
    print(count)

func()