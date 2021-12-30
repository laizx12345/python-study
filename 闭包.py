
# 使用locals() 批量生成变量

def aaa():
    for i in range(10):
        locals().update({'a%s'%i:i})
    for i in locals().items():
        print(i)
aaa()


# 内层函数对外层函数的变量（非全局）的引用并返回，就形成了闭包


def f1():
    a = 1
    def f2():
        print(a)
    f2()
    return f2