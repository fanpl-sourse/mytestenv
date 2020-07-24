#!/usr/bin/env python
# encoding: utf-8
'''
@author: fanpl
@file: main.py
@time: 2020/7/8 22:28
@desc:
'''
# from time import sleep, ctime
#
# import logging
#
# import _thread
#
# logging.basicConfig(level=logging.INFO)
#
# def loop1():
#     logging.info('start loop1 #########'+ctime())
#     sleep(3)
#     logging.info('end loop1 ######'+ctime())
#
# def loop2():
#     logging.info('start loop2 #########'+ctime())
#     sleep(4)
#     logging.info('end loop2 ######'+ctime())
#
# def main():
#     logging.info('start all ######' + ctime())
#     # loop1()
#     # loop2()
#     _thread.start_new_thread(loop1,())
#     _thread.start_new_thread(loop2,())
#     sleep(6)
#     logging.info('end all ######' + ctime())
#
# if __name__ == '__main__':
#     main()


# from time import sleep, ctime
# import logging
# import _thread
# logging.basicConfig(level=logging.INFO)
#
# #定义循环多少次，每次等待多少秒
# loops = [2,4]
#
# def loop(nloop,nsec,lock):
#     """
#     :param nloop: 代表进行的是第一个任务
#     :param nsec: 代表当前循环是多少秒
#     :param lock: 代表当前循环的锁
#     :return:
#     """
#     logging.info('start loop'+ str(nloop) +'#########'+ctime())
#     sleep(nsec)
#     logging.info('end loop'+ str(nloop) +'######'+ctime())
#     #当当前任务完成时，释放锁
#     lock.release()
#
# def main():
#     logging.info('start all ######' + ctime())
#     locks = []
#     nloops = range(len(loops))
#
#     # 构建锁
#     for i in nloops:
#         lock = _thread.allocate_lock()
#         lock.acquire()
#         locks.append(lock)
#
#     # 执行子进程
#     for i in nloops:
#         _thread.start_new_thread(loop,(i,loops[i],locks[i]))
#
#     # 监听子进程是否运行完成
#     for i in nloops:
#         while locks[i].locked():
#             pass
#     logging.info('end all ######' + ctime())
#
#
# if __name__ == '__main__':
#     main()



# import threading
# from time import sleep, ctime
# import logging
# import _thread
# logging.basicConfig(level=logging.INFO)
#
# #定义循环多少次，每次等待多少秒
# loops = [2,4]
#
# def loop(nloop,nsec):
#     """
#     :param nloop: 代表进行的是第一个任务
#     :param nsec: 代表当前循环是多少秒
#     :return:
#     """
#     logging.info('start loop'+ str(nloop) +'#########'+ctime())
#     sleep(nsec)
#     logging.info('end loop'+ str(nloop) +'######'+ctime())
#
# def main():
#     logging.info('start all ######' + ctime())
#     nloops = range(len(loops))
#
#     threads = []
#
#     # 装载线程
#     for i in nloops:
#         t = threading.Thread(target=loop,args=(i,loops[i]))
#         threads.append(t)
#
#     # 进程必须启动
#     for i in nloops:
#         threads[i].start()
#
#     #线程没有执行完成，则会阻塞在这个位置
#     for i in nloops:
#         threads[i].join()
#
#     logging.info('end all ######' + ctime())
#
#
# if __name__ == '__main__':
#     main()



import threading
from time import sleep, ctime
import logging
logging.basicConfig(level=logging.INFO)

#定义循环多少次，每次等待多少秒
loops = [2,4]

def loop(nloop,nsec):
    """
    :param nloop: 代表进行的是第一个任务
    :param nsec: 代表当前循环是多少秒
    :return: 
    """
    logging.info('start loop'+ str(nloop) +'#########'+ctime())
    sleep(nsec)
    logging.info('end loop'+ str(nloop) +'######'+ctime())

class Mythread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)

def main():
    logging.info('start all ######' + ctime())
    nloops = range(len(loops))

    threads = []

    # 装载线程
    for i in nloops:
        t =  Mythread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)

    # 进程必须启动
    for i in nloops:
        threads[i].start()

    #线程没有执行完成，则会阻塞在这个位置
    for i in nloops:
        threads[i].join()

    logging.info('end all ######' + ctime())


if __name__ == '__main__':
    main()