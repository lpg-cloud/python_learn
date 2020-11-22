# try:
#   myfile=open("basic.py","r",encoding="UTF-8")
#   print(myfile)
#   # for line in file:
#   #   a=file.readline();
#   #   print(a)
#   print(myfile.read())
# except Exception as e:
#   print(e)
# finally:
#   myfile.close()

# from functools import partial
# def f(a,b=5):
#   print("a=",a,"b=",b)
# f_new=partial(f,2,5)

# f_new()

# class a():
#   name="asdf"
#   def __init__(self) -> None:
#     pass
#   def getName(self):
#     """
#     docstring
#     """
#     return self.name
#   def setName(self,name):
#     self.name=name
#     return name

# lpg=a()
# pgl=a()
# lpg.setName("lpg")
# print(pgl.getName());
# print(lpg.getName());


# class A(object):
#   def f(self):
#     """
#     docstring
#     """
#     print("A.f")

# class B(A):
#   def A(self):
#     """
#     docstring
#     """
#     print("B.f")

# class C(A):
#   def f(self):
#     print("c.f")

# class D(B,C):
#   """
#   jhbjhbjk
#   """
#   def f(self):
#     super(B,self).f()
#     print("D")

# '''
# 装饰器
# '''

# def log(func):
#   def wrapper(*args,**kwargs):
#     print("%s is called" % func.__name__)
#     print("参数  %s  %s" % (args))
#     return func(*args,**kwargs)
#   return wrapper

# @log
# def A(a,b):
#   """
#   docstring
#   """
#   print("A is called!!!")

# A("第一个参数","第二个参数")


import time,os
import multiprocessing

# print(multiprocessing.current_process().pid)
# print(os.getpid())
# print(os.getppid())
# print("end")

def do_someth(arg,arg1):
  """
  docstring
  """
  print("childprocess is start!!!")
  print(multiprocessing.Process.pid,multiprocessing.Process.name)
  print('chileProcess is stoped')
# pc=multiprocessing.Process(target=do_someth,args=(1,2),name="do_someThing")

# if __name__ == "__main__":
    
#     pc.start()
#     time.sleep(3)
#     print("parentProcess is start!!!...")


"""
multiprocessing.Process(target=,args=,name=)
target,指定run()调用的方法，默认没有函数被调用
name，指定创建进程实例的对象名，默认名称是Process-数值
args,指定target位置参数，用元组表示默认不接受任何参数
"""

from multiprocessing import Process,current_process
import time
class myProcess(Process):
  def __init__(self,name,args):
    """
    name还要返还给父类中的init方法中，args可以赋值到self对象中
    """
    super().__init__(name=name)
    print("进程对象被创建了")
  def run(self) -> None:
    print('pid: ',current_process().pid)
    print("name: ",current_process().name)
    print('end')
    


if __name__ == "__main__":
  # p=myProcess(name='自己创建的进程类',args=123)
  # print(os.fork())
  # p.start()

  import threading
  print(threading.current_thread().getName())