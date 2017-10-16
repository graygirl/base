print ("my first progress"); #输出我的第一个编程
print ("base knowledge"); #输出我的第一个编程
'''
if True: #0表示假,整数1表示假
    print("true")
else:
    print("false")

#input("\n\n 按下Enter健后退出")

import sys; x="yangyinna";sys.stdout.write(x +'\n')

x="a"
y="b"
print(x + y)
print(x, end=" ")
print(y, end=" ""\n")

import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

from sys import argv, path  # 导入特定的成员
print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path

counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "yangyinna"  # 字符串
print(counter)
print(miles)
print(name) 

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

a =b= 111
print(isinstance(b,int))
print(a+b)  #+-*/ //除法取整 %  **乘方

str = "yangyinna"
print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后面的所有字符
print (str * 2)      # 输出字符串两次
print (str + "TEST") # 连接字符串
print(r'yangyin\na') # 字符串中的数值不能改变

list = ['abcd', 786, 2.23, 'yangyinna', 70.2]
tinylist = [123, 'yangyinna']
print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表，列表中值的可以改变
a=[2,6,1314,1.23];a[0]=5;a[2:4]=[21,21]; #a[2:4]=[]
print(a)
'''
'''
tuple = ('dcba', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')
print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组,元组中的元素不能改变
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉
if("Rose in student"):
    print("在集合中")
else:
    print("不在集合中")
a=set('abcd');b=set('ab')
print(a - b)  # a和b的差集
print(a | b)  # a和b的并集
print(a & b)  # a和b的交集
print(a ^ b)  # a和b中不321同时存在的元素

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.baidu.com'}
print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

print('两数之和为 %.2f' % (float(input("输入第一个数字： "))+float(input("输入第二个数字： "))))

import calendar #日历模块
monthrange=calendar.monthrange(2017,9)
print(monthrange) #第一个是该月的星期几的日期码，第二个是该月的日期码
'''
from myabs import myabs
print(myabs(-10))

