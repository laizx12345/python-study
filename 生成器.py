

# def func1(x):
#     x += 1
#     yield x
#     yield x+1
#     yield x+1


# g_obj = func1(5)   # 生成器函数对象

# print(g_obj.__next__())   # 一个next对应一个yield
# print(g_obj.__next__())
# print(g_obj.__next__())


# def func2(*args):
#     x = 0
#     k = 1
#     if len(args) == 1:
#         num = args[0]
#     if len(args) == 2:
#         x = args[0]
#         num = args[1]
#     if len(args) == 3:
#         x = args[0]
#         num = args[1]
#         k = args[2]
#     while x < num:
#         yield x
#         x += k


# for i in func2(1000):
#     print(i)

# for i in range(1000):
#     print(i)


def func3():
    a = yield 1
    print(a)
    b = yield 2
    print(b)
    c = yield 3


f = func3()
print(next(f))   # yield 1
print(next(f))   # a = None ，print(a)，yield 2
print(f.send('sdfsdf'))  # b = 'sdfsdf'，print(b), yield 3

# send 和 next 都可以执行一个yield，但是send可以给上一个yield 传入值
# 先进行yield 操作，当下一个next 或者send 到来时，执行上一个yield 与下一个yield 之间的代码
# 第一次取值必须是next，如果是send会报错