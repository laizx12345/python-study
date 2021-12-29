

# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)


# func(*(1, 2, 3), **{'a': 5, 'c': 6})


d = {
    'a':1,
    'b':2,
}

d2 = {
    **d
}
print(d2)