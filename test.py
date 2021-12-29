def func(n):
    i=0
    while i < n :
        yield i
        i+=1

for i in func(10):
    print(i)