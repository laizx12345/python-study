

count = 1


def func1():
    # 局部名称空间可以引用全局名称空间的变量，但是不能修改

    global count  # 在局部空间可以对全局变量修改
    count += 1

    print(count)


def func2():

    global aaaa   # 在局部空间声明一个全局变量
    aaaa = 1

    print(aaaa)


func1()
print(count)

func2()
print(aaaa)


def func3():
    abc = 123

    def func4():
        nonlocal abc    # 使用非全局的局部变量
        # global abc    # 这种情况下使用global会报错，global 只能引用全局变量
        abc += 1
        print(abc)
    func4()

func3()
