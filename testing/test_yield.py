#!/usr/bin/env python


def fun():
    for i in range(3):
        print(f'i = {i}')
        #return 相当于暂停并记住 上次执行的位置
        yield
        print('end')

f = fun()
#获取生成器的下一个值
next(f)
next(f)
next(f)
