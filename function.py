
'''
def example(a,b):
    return(a,b)
print(type(example(3,4)))  #函数返回多个值的时候，是以元祖的方式返回的

def test(*arga):
    print(arga)
    return(arga)
print(type(test(1,2,3,4))) #可以看见其函数的返回值是一个元组

a = 10
b = 20
if (a and b):
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

# 修改变量 a 的值
a = 0
if (a and b):
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")
if (a or b):
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")
if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")

a=10;b=20;list=[1,2,20]
if(a in list):
    print('a在列表中')
else:
    print('a不在列表中')

a=20;b=20;
if(a is b):
    print('有共同的标识')
else:
    print('没有共同标识')
if (id(a) == id(b)):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识") #is用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。

a=1.03;  print(int(a))
print("我的专业是 %s，共 %d 学分" % ("电信",520))

list = ['Google', 'Runoob', 1997, 2000]
print(list)
del list[2]
print("删除第三个元素 : ", list)

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
dict['Age'] = 8;               # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
del dict['Name'] # 删除键 'Name'
dict.clear()     # 删除字典
del dict         # 删除字典
#print ("dict['Age']: ", dict['Age'])

a,b=0,1
while b<10:
    print(b,end=',')
    a,b=b,a+b

print('\n')
a=0;b=1
while b<10:
    print(b,end=',')
    a=b;b=a+b

age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

# 退出提示
input("点击 Enter 键退出")

#猜数游戏
number=7;guess=5
while guess!=number:
    guess=int(input('请输入想猜的数字：'))
    if guess == number:
        print('哇哦，好厉害，恭喜你猜对喽***')
    elif guess > number:
        print('你猜的数值偏高哦***')
    elif guess < number:
        print('你猜的数值偏低哦***')
input('点击 Enter键退出')

n=100;sum=0;counter=1
while counter <= n:
    sum+=counter
    counter+=1
print('1 到 %d 的和为: %d' % (n,sum))

count=0
while count<3:
    print(count,'小于3')
    count+=1
else:
    print(count,大于3')

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

for i in range(10,15,2):
    print(i)
a=['google','firefox','360','safari']
for i in range(len(a)):
    print(i,a[i])

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break
    else:
        print(n,'是质数')

list=[1,2,3,4]
it=iter(list) #创建迭代器对象
print(next(it)) #输出迭代器的下一个元素
print(next(it))
for x in it:
    print(x,end='')

import sys
list=[1,2,3,4]
it=iter(list)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

import sys
def fibonacci(n):
    a,b,counter=0,1,0
    while True:
        if(counter>n):
            return
        yield a
        a,b=b,a+b
        counter+=1
f=fibonacci(10) #f是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(f),end=' ')
    except StopIteration:
        sys.exit()

def area(width,height):
    return width*height
print('area:',area(4,5))
def my(name):
    print('love you:',name)
my('yangyinna')
w=3;h=4
print('width=',w,'height=',h,'area=',area(w,h))

def printme(str):
    print(str);
    return;
printme('调用用户自定义函数')
printme('再次调用同一函数')

def changeme(mylist):
    mylist.append([1,2])
    print('函数内取值：',mylist)
    return
mylist=[10,20]
changeme(mylist)
print('函数外取值：',mylist)

def myabs(x):
    if x>=0:
        return x
    else:
        return -x
print('-2的绝对值：', myabs(-2))
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print('x:',5,'的','n:',3,'次方为：',power(5))
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('yangyinna', 24, job= 'engineer',major='testing',favourite='singing')

x=88
def func1():
    global x
    x=99
print('func1',func1())
print(x)

sum=lambda arg1,arg2:arg1+arg2 #匿名函数
print('相加后的结果为:',sum(20,30))

def sum( arg1, arg2 ):
   total = arg1 + arg2
   return total;
print ("函数内 : ", sum(10,20))

# 调用sum函数
total = sum( 60, 20 );
print ("函数外 : ", total)

def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print ("函数内 : ", total)
   return total;

# 调用sum函数
total = sum( 1, 2 );
print ("函数外 : ", total)

x = int(2.9)  # 内建作用域
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中

    def inner():
        i_count = 2  # 局部作用域

#函数
def hello(str):
    print(str)
hello('world')
num=1
def fun1():
    global num #需要使用全局变量符号
    print(num)
    num=2323
    print(num)
fun1()

def outer1():
    num=10
    def inner1():
        nonlocal num #nonlocal声明
        num=200
        print(num)
    inner1()
    print(num)
outer1()
var1=[1,2,3]
var2=[4,5,6]
print([x*y for x in var1 for y in var2])
print([var1[i]*var2[i] for i in range(len(var1))])

# 遍历技巧
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for x, v in knights.items():
    print(x, v)
for x, v in enumerate(['tic', 'tac', 'toe']):
    print(x, v)
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
for i in reversed(range(1, 10, 2)):
    print(i)
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

import sys
print(sys.path)
#Filename:using_name.py
import feibo
print(feibo.fib(500))
if __name__ == '__main__':
    print('程序正在运行')
else:
    print('我来自另一模块')
print(dir(feibo)) #可以找到模块内定义的所有名称,以一个字符串列表的形式返回
print(dir(sys))

from collections import Iterable #判断某数据类型是否可迭代
print(isinstance('abx',Iterable))
from collections import Iterator
print(isinstance('abx',Iterator))
print(isinstance(iter([321]),Iterator)) #Iterable变成Iterator可以使用iter()函数
for (I,V) in enumerate(['a','b','c']):  #同时迭代索引和元素本身
    print(I,V)
print(list(range(1,20,2)))
'''
print([x * x for x in list(range(1,20)) if x % 2 ==0])
g = (x * x for x in list(range(1,20)) if x % 2 ==0)
for G in g:
    print(G) #简单的生成器,Iterable变成Iterator可以使用iter()函数

