#!/bin/env python3
#-*- coding:utf8 -*-
#知识点总结
#***************print
x =3;y =4 #不推荐,还是应该写成两行
print('hello','world!') #逗号自动添加默认的分隔符:空格
print('hello' + 'world!') #加号表示字符拼接
print('hello','world',sep='***') #单词间用***分隔
print('#'*50) #*号表示重复50遍
print('how are you?',end='') #默认print会打印回车,end=''表示不要回车
#***************运算符
print(5/2) #25
print(5//2)#丢弃余数,只保留商
print(5 % 2)  # 求余数
print(5 ** 3)  # 5的3次方
print(5 > 3)  # 返回True
print(3 > 5)  # 返回False
print(20 > 10 > 5)  # python支持连续比较
print(20 > 10 and 10 > 5)  # 与上面相同含义
print(not 20 > 10)  # False
#***************input
number = input("请输入数字: ")  # input用于获取键盘输入
print(number)
print(type(number))  # input获得的数据是字符型
print(number + 10)  # 报错，不能把字符和数字做运算
print(int(number) + 10)  # int可将字符串10转换成数字10
print(number + str(10))  # str将10转换为字符串后实现字符串拼接
username = input('username: ')
print('welcome', username)   # print各项间默认以空格作为分隔符
print('welcome ' + username)  # 注意引号内最后的空格
#****************单双引号
sentence = 'tom\'s pet is a cat'  # 单引号中间还有单引号，可以转义
sentence2 = "tom's pet is a cat"  # 也可以用双引号包含单引号
sentence3 = "tom said:\"hello world!\""
sentence4 = 'tom said:"hello world"'
# 三个连续的单引号或双引号，可以保存输入格式，允许输入多行字符串
words = """
hello
world
abcd"""
print(words)
#****************list:容器 可变 序列(container variable sequence)
alist = [10, 20, 30, 'bob', 'alice', [1,2,3]]
len(alist)
alist[-1]  # 取出最后一项
alist[-1][-1]  # 因为最后一项是列表，列表还可以继续取下标
[1,2,3][-1]  # [1,2,3]是列表，[-1]表示列表最后一项
alist[-2][2]  # 列表倒数第2项是字符串，再取出字符下标为2的字符
alist[3:5]   # ['bob', 'alice']
10 in alist  # True
'o' in alist  # False
100 not in alist # True

#****************tuple
atuple = (10, 20, 30, 'bob', 'alice', [1,2,3])
len(atuple)
10 in atuple #10是否在atuple里
atuple[2]
print(atuple[3:5]) #('bob', 'alice')
# atuple[-1] = 100  # 错误，元组是不可变的
#********************dictionary****************
"""
字典属于:容器、可变、映射
字典的key不能重复
字典的key必须是不可变类型
"""
# 字典是key-value(键－值）对形式的，没有顺序，通过键取出值
adict = {'name': 'bob', 'age': 23}
len(adict)       #长度
'bob' in adict  # False
'name' in adict  # True
adict['email'] = 'bob@tedu.cn'  # 字典中没有key，则添加新项目
adict['age'] = 25  # 字典中已有key，修改对应的value
#************************if判断
if 3 > 0:
    print('yes')
    print('ok')

if 10 in [10, 20, 30]:
    print('ok')

if -0.0:
    print('yes')  # 任何值为0的数字都是False

if [1, 2]:
    print('yes')  # 非空对象都是True

if ' ':
    print('yes')  # 空格字符也是字符，条件为True
#**********************************条件表达式,三元运算符
a = 10
b = 20

if a < b:
    smaller = a
else:
    smaller = b

print(smaller)

s = a if a < b else b  # 和上面的if-else语句等价

print(s)
#扩展
s = a if a < b else (b if b < a else print('ok')) #可以套用
#******************for循环遍历数据对象
astr = 'hello'
alist = [10, 20, 30]
atuple = ('bob', 'tom', 'alice')
adict = {'name': 'john', 'age': 23}

for ch in astr:
    print(ch)

for i in alist:
    print(i)

for name in atuple:
    print(name)

for key in adict:
    print('%s: %s' % (key, adict[key]))
#*************range
range(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10))
range(6, 11)  # [6, 7, 8, 9, 10]
range(1, 10, 2)  # [1, 3, 5, 7, 9]
range(10, 0, -1)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#*****************9x9
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%s*%s=%s' % (j, i, i * j), end=' ')
    print()

# i=1 ->j: [1]
# i=2 ->j: [1,2]
# i=3 ->j: [1,2,3]
#************list-analysis
# 10+5的结果放到列表中
[10 + 5]
# 10+5这个表达式计算10次
[10 + 5 for i in range(10)]
# 10+i的i来自于循环
[10 + i for i in range(10)]
[10 + i for i in range(1, 11)]
# 通过if过滤，满足if条件的才参与10+i的运算
[10 + i for i in range(1, 11) if i % 2 == 1]
[10 + i for i in range(1, 11) if i % 2]
# 生成IP地址列表
['192.168.1.%s' % i for i in range(1, 255)]
#************************file-operation**********************
# 文件操作的三个步骤：打开、读写、关闭
# cp /etc/passwd /tmp
f = open('/tmp/passwd')  # 默认以r的方式打开纯文本文件
data = f.read()  # read()把所有内容读取出来
print(data)
data = f.read()  # 随着读写的进行，文件指针向后移动。
# 因为第一个f.read()已经把文件指针移动到结尾了，所以再读就没有数据了
# 所以data是空字符串
f.close()

f = open('/tmp/passwd')
data = f.read(4)  # 读4字节
f.readline()  # 读到换行符\n结束
f.readlines()  # 把每一行数据读出来放到列表中
f.close()

################################
f = open('/tmp/passwd')
for line in f:
    print(line, end='')
f.close()

##############################
f = open('图片地址', 'rb')  # 打开非文本文件要加参数b
f.read(4096)
f.close()

##################################
f = open('/tmp/myfile', 'w')  # 'w'打开文件，如果文件不存在则创建
f.write('hello world!\n')
f.flush()  # 立即将缓存中的数据同步到磁盘
f.writelines(['2nd line.\n', 'new line.\n'])
f.close()  # 关闭文件的时候，数据保存到磁盘

##############################
with open('/tmp/passwd') as f:
    print(f.readline())

#########################
f = open('/tmp/passwd')
f.tell()  # 查看文件指针的位置
f.readline()
f.tell()
f.seek(0, 0)  # 第一个数字是偏移量，第2位是数字是相对位置。
              # 相对位置0表示开头，1表示当前，2表示结尾
f.tell()
f.close()
#*******************character-string******************************
py_str = 'hello world!'
print(py_str)
py_str.capitalize() #行首字母大写
print(py_str.capitalize())
print(py_str.title()) #每个单词首字母大写
print(py_str.center(50)) #居中50格子默认用空格补齐
print(py_str.center(50,'#')) #居中50并且用#补全
print(py_str.ljust(50)) #左对齐右边默认空格补全
print(py_str.rjust(50,'*')) #右对齐并以*补全左边50
print(py_str.count('l')) #统计i出现的次数
print(py_str.count('lo'))
print(py_str.endswith('!')) #以!结尾么?
print(py_str.endswith('d!'))
print(py_str.startswith('a')) #是以a开头么?
print(py_str.islower()) #字母都是小写的?其他字符不考虑
print(py_str.isupper()) #字母都是大写的?其他字符不考虑
print('Hao123'.isdigit())  # 所有字符都是数字吗？
print('Hao123'.isalnum())  # 所有字符都是字母数字？
print('  \thello\t '.strip()) #默认去除两端空白字符,常用
print('hello\t  '.lstrip()) #去除左边
print('how are you ?'.split()) #默认分离 以空格为分割标志
print('hello.tar.gz'.split('.')) #分离 以·为分割标志
print('.'.join(['hello','tar','gz'])) #合并 是split和join是相反的
#***************************sequence-object*****************************
from random import randint

alist = list()  # []
list('hello')  # ['h', 'e', 'l', 'l', 'o']
list((10, 20, 30))  # [10, 20, 30]  元组转列表
astr = str()  # ''
str(10)  # '10'
str(['h', 'e', 'l', 'l', 'o'])  # 将列表转成字符串
atuple = tuple()  # ()
tuple('hello')  # ('h', 'e', 'l', 'l', 'o')
num_list = [randint(1, 100) for i in range(10)]
a = max(num_list)
i = min(num_list)
print(a,i)
#**********************character-string-format*************
"%s is %s years old" % ('bob', 23)  # 常用
"%s is %d years old" % ('bob', 23)  # 常用
"%s is %d years old" % ('bob', 23.5)  # %d是整数 常用
"%s is %f years old" % ('bob', 23.5)
"%s is %5.2f years old" % ('bob', 23.5)  # %5.2f是宽度为5，2位小数
"97 is %c" % 97
"11 is %#o" % 11  # %#o表示有前缀的8进制
"11 is %#x" % 11
"%10s%5s" % ('name', 'age')  # %10s表示总宽度为10，右对齐, 常用
"%10s%5s" % ('bob', 25)
"%10s%5s" % ('alice', 23)
"%-10s%-5s" % ('name', 'age')  # %-10s表示左对齐, 常用
"%-10s%-5s" % ('bob', 25)
"%10d" % 123
"%010d" % 123

a = "{} is {} years old".format('bob', 25)
b ="{1} is {0} years old".format(25, 'bob')
c = "{:<10}{:<8}".format('name', 'age')
d = "{:>10}{:>8}".format('name', 'age')
print(a) #bob is 25 years old
print(b) #bob is 25 years old
print(c) #name      age
print(d) #      name     age
#*****************shutil******************
import shutil

with open('/etc/passwd', 'rb') as sfobj:
    with open('/tmp/mima.txt', 'wb') as dfobj:
        shutil.copyfileobj(sfobj, dfobj) # 拷贝文件对象

shutil.copyfile('/etc/passwd', '/tmp/mima2.txt')
shutil.copy('/etc/shadow', '/tmp/')  # cp /etc/shadow /tmp/
shutil.copy2('/etc/shadow', '/tmp/')  # cp -p /etc/shadow /tmp/
shutil.move('/tmp/mima.txt', '/var/tmp/')  # mv /tmp/mima.txt /var/tmp/
shutil.copytree('/etc/security', '/tmp/anquan') # cp -r /etc/security /tmp/anquan
shutil.rmtree('/tmp/anquan')  # rm -rf /tmp/anquan
# 将mima2.txt的权限设置成与/etc/shadow一样
shutil.copymode('/etc/shadow', '/tmp/mima2.txt')
# 将mima2.txt的元数据设置成与/etc/shadow一样
# 元数据使用stat /etc/shadow查看
shutil.copystat('/etc/shadow', '/tmp/mima2.txt')
shutil.chown('/tmp/mima2.txt', user='zhangsan', group='zhangsan')
#***********************list-extent*****************
alist = [1, 2, 3, 'bob', 'alice']
alist[0] = 10
alist[1:3] = [20, 30]
alist[2:2] = [22, 24, 26, 28]
alist.append(100)
alist.remove(24)  # 删除第一个24
alist.index('bob')  # 返回下标
blist = alist.copy()  # 相当于blist = alist[:]
alist.insert(1, 15)  # 向下标为1的位置插入数字15
alist.pop()  # 默认弹出最后一项
alist.pop(2) # 弹出下标为2的项目
alist.pop(alist.index('bob'))
alist.sort()
alist.reverse()
alist.count(20)  # 统计20在列表中出现的次数
alist.clear()  # 清空
alist.append('new')
alist.extend('new')
alist.extend(['hello', 'world', 'hehe'])
#******************dictionary-extend*************
adict = dict()  # {}
dict(['ab', 'cd'])
bdict = dict([('name', 'bob'),('age', 25)])
{}.fromkeys(['zhangsan', 'lisi', 'wangwu'], 11)

for key in bdict:
    print('%s: %s' % (key, bdict[key]))

print("%(name)s: %(age)s" % bdict)

bdict['name'] = 'tom'
bdict['email'] = 'tom@tedu.cn'

del bdict['email']
bdict.pop('age')
bdict.clear()
#**********************dictionary-commonly used******************
adict = dict([('name', 'bob'),('age', 25)])
len(adict)
hash(10)  # 判断给定的数据是不是不可变的，不可变数据才能作为key
adict.keys() #提取所有key键
adict.values() #提取所有值value
adict.items()  #提取所有key:value
# get方法常用，重要
adict.get('name')  # 取出字典中name对应的value，如果没有则返回None
print(adict.get('qq'))  # None(赋值不会报错)
print(adict.get('qq', 'not found'))  # 没有qq，返回指定内容
print(adict.get('age', 'not found'))
adict.update({'phone': '13455667788'})
#*******************set***************
# 集合相当于是无值的字典，所以也用{}表示
myset = set('hello')
len(myset)
for ch in myset:
    print(ch)

aset = set('abc')
bset = set('cde')
aset & bset  # 交集
aset.intersection(bset)  # 交集
aset | bset  # 并集
aset.union(bset)  # 并集
aset - bset  # 差补
aset.difference(bset)  # 差补
aset.add('new')
aset.update(['aaa', 'bbb'])
aset.remove('bbb')
cset = set('abcde')
dset = set('bcd')
cset.issuperset(dset)  # cset是dset的超集么？
cset.issubset(dset)  # cset是dset的子集么？
#****************进制转换
hex(20) #10进制转16
oct(10) #转8进制
bin(10) #十进制转2进制
# 以下备查
>>> '%#o' % 10
# 转8进制
'0o12'
>>> '%#x' % 10
# 转16进制
'0xa'
>>> '%f' % (5/3)
'1.666667'
>>> '%.2f' % (5/3)
# 保留2位小数
'1.67'
>>> '%5.2f' % (5/3)
# 输出总宽度为5,小数位2位,不够宽度补空格
' 1.67'
>>> '%e' % 10000
'1.000000e+04'
# 科学计数法'1.000000e+04'
# 写入非文本文件
>>> f = open('/tmp/aaaa', 'wb')
>>> hi = '你好\n'
>>> hi.encode()
b'\xe4\xbd\xa0\xe5\xa5\xbd\n' # 共写入七个字节,在utf8编码中一个汉字占3字节,\n占1字节
>>> f.write(hi.encode())
7
# 导入模块的同时,为模块创建别名,不常用
>>> import getpass as gp
>>> p = gp.getpass()
Password: