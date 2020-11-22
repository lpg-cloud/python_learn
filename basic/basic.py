'''
用到的内置函数
'''
from math import e, nan, sqrt
import math


str(123)#从给的对象初始化一个字符串
int()#将给的参数(数值或字符串)转换成整型
float()#将给的参数(数值或字符串)转换成浮点型
'''
浮点型计算不准问题可以借助导入decimal或借助导入fraction
'''
bool()

list()#从给的对象初始化一个列表
#用[]创建list

tuple()#从给的对象初始化一个元组
#用()创建元组，'('，')'可以省略，如 “1，2，3”，表示创建(1,2,3)

bin()#将数值转换成二进制，返回字符串类型
#二进制的定义方式,以0b开始,0b0110

oct()#将数值转换成八进制，返回字符串类型
#八进制的定义方式，以0o开始，0o10

hex()#将数值转变成十六进制
#十六进制的定义方式以0x开始，0x10

abs()#取绝对值
sqrt()#求平方根，参数为正整数,参数为负数时有的平台上会返回\nan
nan#表示not a number

id()#获取传入对象的内存地址
sorted()#排序，返回一个新的对象
reversed()#反转，返回一个新的对象
str.lstrip()#去除前导字符
str.rstrip()#去除前导字符
str.strip()#去除前后的空格等

"".isidentifier()#判断是否是合法的标识符
import keyword
keyword.iskeyword()#判断是否是关键字
"".isspace()#判断是否是空白或制表符
"".isalpha()#判断是否由字母组成
"".isalnum()#判断是否是由字母和数字组成
"".isdecimal()#判断是否是数字
"".isdigit()##判断是否是由数字组成的字符串
"".isnumeric#判断是否全部由数字组成


range()#返回一个range类型，不可变的整数序列
start,stop,step=0,9,1
list(range(start,stop,step))
#[0, 1, 2, 3, 4, 5, 6, 7, 8]

pow()#幂次方计算


math.ceil()#返回大于或等于给定数的最小整数
math.floor()#与ceil相反，返回小于等于给定数的最大整数
math.sqrt()#求算数平方根


help('keywords') #查询python中的关键字 或导入keyword打印keyword.kwdlist


'''
科学计数法
n+e+m 表示n*(10**m)

布尔运算符包括 and, or, not

多个变量能同时赋值，但是赋值符号“=”左右两边的元素个数得一致
获取关键字方法

标识符命名规则：
区分大小写
不能含有关键字
不能以数字开头
不能有空格、制表符、数学符号、中划线

命名规范：
小写单词用下划线链接

python中的None 是一个表示数据值的不存在对象，占用内存空间
None可以用来初始化，或重置变量
[[None]*5*4]
'''
'''
列表的操作
'''
l=[1,2,3,4,5,6]
l.append(7) #往列表中添加一个对象
l.extend([8,9,10,11])#一次想列表中添加多个元素
l
l.insert(5,20)#想指定index的位置添加要给对象
#给列表中的切片赋值
l[4:6]=[100,101,102,103]#将原来列表中的[4,5)删除然后插入后面传入的列表

l.remove(102)#删除列表中找到的第一个传入的元素，如果没有找到会报错，
l.pop()#从数组中移出一个元素，并返回该元素,可以指定索引
del l[0:7] #也可以使用del关键字删除列表中的对象

'''
使用生成器能够节省内存空间，因为生成器使用到某个元素时才进行推算该元素的值
'''

def fib(n):
  """
  生成器函数
  """
  i=1
  a,b=1,1;
  while(i<n):
    yield a
    a,b=b,a+b
    i+=1

a=fib(6)

import sys
try:
  while(next(a)):
    print(1)
except StopIteration as e:
  
  print(e)
