import multiprocessing
import threading
import time
import random
from threadpool import ThreadPool, makeRequests

print('父进程开始。。。')
args_list = []

for i in range(1, 11):
    args_list.append(i)
tp = ThreadPool(2)


def do_something(arg1):
    print(f"arg1 ：{arg1}")
    print("进程名称：", multiprocessing.current_process().name)
    print("进程名称：", multiprocessing.current_process().pid)
    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()
    print('方法%s结束!!! 耗时 %.2f秒' % (arg1, (end - start)))


request = makeRequests(do_something, args_list)

for req in request:
    tp.putRequest(req)
tp.wait()
print('父进程结束')

#
# print('自动创建并启用父线程', threading.current_thread().getName())
# time.sleep(3)
#
# '''
# thread表示线程
# 1.创建线程对象并启用线程
#
# 创建Thread实例，调用start方法，start调用thread中的run方法
# ，run方法调用action()方法
# '''
#
#
# class MyThread(threading.Thread):
#
#     def __init__(self, name, args):
#         super().__init__(name=name)  # 将name传给父类对象的init方法
#         self.args = args
#
#     def run(self) -> None:
#         print('子线程开始 %s' % threading.current_thread().getName())
#         print('执行了run中的各种代码!!!')
#         print('arg1= %s ,arg2 = %s' % (self.args[0], self.args[1]))
#
#         time.sleep(5)
#
#         print('子进程结束!!!')
#
#
# mp = MyThread(name='我的线程', args=('第一个参数', "第二个参数"))
#
# mp.start()


'''
创建线程的另一种方法创建一个threading.Thread()对象
关键字参数：
target：要执行的方法
args：传入target的位置参数 
name：自定义的线程名称 其实是传给 init方法了
kwargs：target的关键字参数 

daemon：是否开启线程守护 其实是传给

'''
# p = threading.Thread(target=do_something, args=('第一个参数', '第二个参数'), name='子线程')
# p.start()
# p.join(2)
# p.is_alive()


# if __name__ == '__main__':
#     print('父进程启动........')
#     pp = multiprocessing.Pool()
#     for i in range(1, 11):
#         pp.apply_async(do_something, args=(i,))
#     pp.close()
#     pp.join()
#     print('主进程结束了')
