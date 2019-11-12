#!/bin/env python3
#-*- coding:utf8 -*-
#学python3的第十天
"""

## OOP：面向对象编程

- 实现了数据属性和行为属性的融合
- 类：具有相同属性的对象集合
- 实例/对象：类的一个具体实现
- 方法：就是在类中定义的函数

### 组合

- 两个类有明显的不同
- 一个类的属性是另一个类的实例，用组合

### 子类

- 两个类非常相似，只是有一些不同
- 通过一个类派生出另一个类，也可以说一个类继承于另一个类

### 多重继承

- 子类可以有多个父类
- 子类自动继承所有父类的方法
- 对象查找方法时，按自下向上、自左向右的方式查找

### 特殊方法

- 为了实现类的内部功能，python定义了很多以双下划线开头、结尾的方法
- 这些方法被称作magic魔法方法

## 正则表达式

```shell
# 为MAC地址加冒号
192.168.1.1     000C29123456
192.168.1.2     5254A3802B32

:%s/\(..\)\(..\)\(..\)\(..\)\(..\)\(..\)$/\1:\2:\3:\4:\5:\6/
"""

#完全备份和增量备份程序
"""
(nsd1906) [root@room8pc16 day03]# mkdir -p /tmp/demo/backup
(nsd1906) [root@room8pc16 day03]# cp -r /etc/security /tmp/demo/
"""
# import os
# import tarfile
# import pickle
# import hashlib
# from time import  strftime
#
# def check_md5(fname): #思考
#     '计算文件md5值的函数,接受文件名　返回md5值'
#     m = hashlib.md5()
#
#     with open(fname,'rb') as fobj:
#         while 1:
#             data = fobj.read(4096)
#             if not data:
#                 break
#             m.update(data)
#
#     return m.hexdigest()
#
# def full_backup(src,dst,md5file):
#     #拼接处备份文件名的绝对路径
#     fname = os.path.basename(src)
#     fname = '%s_full_%s.tar.gz' % (fname,strftime('%Y%m%d'))
#     fname = os.path.join(dst, fname)
#
#     #完全备份,就是把整个目录压缩
#     tar = tarfile.open(fname,'w:gz')
#     tar.add(src)
#     tar.close()
#
#     #计算每个文件的md5值
#     md5dict = {}
#     for path,folders,files in os.walk(src):
#         for file in files:
#             key = os.path.join(path,file)
#             md5dict[key] = check_md5(key)
#
#     #将md5值存入文件
#     with open(md5file,'wb') as fobj:
#         pickle.dump(md5dict,fobj)
#
# def incr_backup(src,dst,md5file):
#     # 拼接出备份文件的绝对路径
#     fname = os.path.basename(src)
#     fname = '%s_incr_%s.tar.gz' % (fname,strftime('%Y%m%d'))
#     fname = os.path.join(dst, fname)
#
#     # 计算每个文件的md5值
#     md5dict = {}
#     for path, folders, files in os.walk(src):
#         for file in files:
#             key = os.path.join(path, file)
#             md5dict[key] = check_md5(key)
#
#     #取出前一天的md5值
#     with open(md5file,'rb') as fobj:
#         old_md5 = pickle.load(fobj)
#
#     #找出新增文件和改动的文件进行备份
#     tar = tarfile.open(fname, 'w:gz')
#     for key in md5dict:
#         if md5dict[key] != old_md5.get(key):
#             tar.add(key)
#     tar.close()
#
#     #更新md5文件
#     with open(md5file,'wb') as fobj:
#         pickle.dump(md5dict,fobj)
#
# if __name__ == '__main__':
#     src = '/tmp/demo/security'
#     dst = '/tmp/demo/backup'
#     md5file = '/tmp/demo/backup/md5.data'
#     if strftime('%a') == 'Mon':
#         full_backup(src,dst,md5file)
#     else:
#         incr_backup(src,dst,md5file)

#OOP:面向对象编程
"""
- 实现了数据属性和行为属性的融合
- lib:具有相同属性的对象集合
- 实例/对象:lib的一个具体实现
- 方法：就是在类中定义的函数
"""
# #文字游戏：
# class Warrior: #战士
#     def __init__(self,name,weapon):
#         'self不是关键字,可以是任何名字,表示实例本身'
#         #绑定在对象身上的属性　再类中任意位置可用
#         self.name = name
#         self.weapon = weapon
#
#     def speak(self,words):
#         #方法自己的参数、变量就是函数的局部变量
#         print('我是%s,%s' % (self.name,words))
#
#     def attack(self,target):
#         print('正在攻击:%s' % target)
#
# class Weapon:
#     def __init__(self,name,strength,type):
#         self.name = name
#         self.strength = strength
#         self.type = type
#
"""组合
- 两个类有明显的不同
- 一个类的属性是另一个类的实例，用组合
"""
# if __name__ == '__main__':
#     #创建实例时　自动调用__init__方法,实例自动作为第一个参数
#     ji = Weapon('方天画戟','力量:88','物理伤害')
#     lb = Warrior('吕布','方天画戟') #创建实例
#     lb = Warrior('吕布',ji)
#     print(lb.name)
#     print(lb.weapon.name,lb.weapon.strength,lb.weapon.type)
#     lb.speak('马中赤兔,人中吕布')
#     print('*'*30)
#     zf = Warrior('张飞',"丈八蛇矛")
#     print(zf.name,zf.weapon)
#     zf.speak('我是阉人张飞张翼德')
#     print('*'*30)
#     lb.attack('董卓')
#     zf.attack('吕布')

# #多重继承(先看本体　再看继承　自左向右　自下向上)
# class A:
#     def func1(self):
#         print('A func')
#
#
# class B:
#     def func2(self):
#         print('B func')
#     def func4(self):
#         print('B func4')
#
#
# class C(A, B,):
#     def func3(self):
#         print('C func')
#     def func4(self):
#         print('C func4')
#
#
#
# if __name__ == '__main__':
#     c1 = C()
#     c1.func1()
#     c1.func2()
#     c1.func3()
#     c1.func4()


# #实例用法
# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
#
#     def __str__(self):
#         return '《%s》' % self.title
#
#     def __call__(self):
#         print('《%s》是%s编写的'% (self.title,self.author))
#
#
# if __name__ == '__main__':
#     pybook = Book('Python基础教程','Magnus') #调用__init__
#     print(pybook) #调用__str__
#     pybook() #调用__call__
#
#正则表达式
#给mac地址加冒号
"""vim中使用
%s/(..)(..)(..)(..)(..)(..)/\1:\2:\3:\4:\5:\6/
"""


#*************************复习一天所学********************************
# #完全备份/增量备份程序
# import os
# import tarfile
# import hashlib
# import pickle
# from time import strftime
#
# def check_md5(fname):
#     '计算文件md5值的函数,接收文件名,返回md5'
#     m = hashlib.md5()
#
#     with open(fname,'rb') as fobj:
#         while 1:
#             data = fobj.read(4096)
#             if not data:
#                 break
#             m.update(data)
#
#     return m.hexdigest()
#
# def full_backup(src,dst,md5file):
#     #拼接出备份文件的绝对路径
#     fname = os.path.basename(src)
#     fname = '%s_full_%s.tar.gz' % (fname,strftime('%Y%m%d'))
#     fname = os.path.join(dst,fname)
#
#     #完全备份,就是把整个目录压缩
#     tar = tarfile.open(fname,'w:gz')
#     tar.add(src)
#     tar.close()
#
#     #计算每个文件的md5值
#     md5dict = {}
#     for payh,folders,files in os.walk(src):
#         for file in files:
#             key = os.path.join(payh,file)
#             md5dict[key] = check_md5(key)
#
#     #将md5值存入文件
#     with open(md5file,'wb')as fobj:
#         pickle.dump(md5dict,fobj)
#
# def incr_backup(src,dst,md5file):
#     #凭借出备份文件的绝对路径
#     fname = os.path.basename(src)
#     fname = '%s_incr_%s.tar.gz' % (fname,strftime('%Y%m%d'))
#     fname = os.path.join(dst,fname)
#
#     #计算每个文件的md5值
#     md5dict = {}
#     for path,folders,files in os.walk(src):
#         for file in files:
#             key = os.path.join(path,file)
#             md5dict[key] = check_md5(key)
#
#     #取出前一天的md5值
#     with open(md5file,'rb')as fobj:
#         old_md5 = pickle.load(fobj)
#
#     #找出新增文件和改动文件进行备份
#     tar = tarfile.open(fname,'w:gz')
#     for key in md5dict:
#         if md5dict[key] != old_md5.get(key):
#             tar.add(key)
#     tar.close()
#
#     #更新md5文件
#     with open(md5file,'wb') as fobj:
#         pickle.dump(md5dict,fobj)
#
# if __name__ == '__main__':
#     src = '/tmp/demo/security'
#     dst = '/tmp/demo/backup'
#     md5file = '/tmp/demo/backup/md5.data'
#     if strftime('%a') != 'Mon':
#         full_backup(src, dst,md5file)
#     else:
#         incr_backup(src,dst,md5file)

# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
#
#     def __str__(self):
#         return '《%s》' % self.title
#
#     def __call__(self):
#         print('《%s》是%s编写的' % (self.title,self.author))
#
# if __name__ == '__main__':
#     pybook = Book("Python基础教程",'Magnus') #调用__init__
#     print(pybook) #调用　__str__
#     pybook()  #调用__call__

# class A:
#     def __init__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
# class B(A):
#     def __init__(self, a, b, c, d, e):
#         # 调用父类方法进行初始化
#         # A.__init__(self, a, b, c, d)  # 与下面写法等价
#         super(B, self).__init__(a, b, c, d)
#         self.e = e
#
# if __name__ == '__main__':
#     b1 = B(10, 20, 30, 40, 50)
#     print(b1.a, b1.e)

# class A:
#     def func1(self):
#         print('A func')
#
#     def func4(self):
#         print('AAAAAAAAAAAAA func4')
#
# class B:
#     def func2(self):
#         print('B func')
#
#     def func4(self):
#         print('BBBBBBBBBBBBB func4')
#
# class C(B, A):
#     def func3(self):
#         print('C func')
#
#     def func4(self):
#         print('CCCCCCCCCCCCC func4')
#
# if __name__ == '__main__':
#     c1 = C()
#     c1.func1()
#     c1.func2()
#     c1.func3()
#     c1.func4()

# class A:
#     def __init__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
# class B(A):
#     def __init__(self, a, b, c, d, e):
#         # 调用父类方法进行初始化
#         # A.__init__(self, a, b, c, d)  # 与下面写法等价
#         super(B, self).__init__(a, b, c, d)
#         self.e = e
#
# if __name__ == '__main__':
#     b1 = B(10, 20, 30, 40, 50)
#     print(b1.a, b1.e)

# class Warrior:
#     def __init__(self, name, weapon):
#         'self不是关键字，可以是任何名字，表示实例本身'
#         # 绑定在对象身上的属性，在类中任意位置可用
#         self.name = name
#         self.weapon = weapon
#
#     def speak(self, words):
#         # 方法自己的参数、变量就是函数的局部变量
#         print('我是%s, %s' % (self.name, words))
#
#     def attack(self, target):
#         print('正在攻击: %s' % target)
#
# if __name__ == '__main__':
#     # 创建实例时，自动调用__init__方法，实例自动作为第一个参数
#     lb = Warrior('吕布', '方天画戟')  # 创建实例
#     print(lb.name)
#     print(lb.weapon)
#     lb.speak('马中赤兔，人中吕布')
#     print('*' * 30)
#     zf = Warrior('张飞', '丈八蛇矛')
#     print(zf.name, zf.weapon)
#     zf.speak('我是燕人张飞张冀德')
#     print('*' * 30)
#     lb.attack('董卓')
#     zf.attack('吕布')

# class Role:
#     def __init__(self, name, weapon):
#         self.name = name
#         self.weapon = weapon
#
#     def speak(self, words):
#         print('我是%s, %s' % (self.name, words))
#
#     def attack(self, target):
#         print('正在攻击: %s' % target)
#
# class Warrior(Role):
#     '子类可以继承父类(基类)的所有方法'
#     def move(self):
#         print('陆地移动')
#
# class Mage(Role):
#     pass
#
# if __name__ == '__main__':
#     lb = Warrior('吕布', '方天画戟')
#     lj = Mage('李靖', '宝塔')
#     lb.speak('马中赤兔，人中吕布')
#     lj.speak('宝塔镇河妖')
#     lb.move()

#子类父类用法(非常实用的缩减代码量方式)
"""子类
- 两个类非常相似，只是有一些不同
- 通过一个类派生出另一个类，也可以说一个类继承于另一个类
"""
# a = '='*30
#
# class Game:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
#
#     def __str__(self):
#         return '\033[34;1m《%s》' % self.title
#
#     def __call__(self):
#         print('\033[34;1m《%s》是%s编写的文字小游戏\033[0m' % (self.title,self.author))
#
# class Role:
#     def __init__(self,name,weapon,state):
#         self.name = name
#         self.weapon = weapon
#         self.state = state
#
#     def speak(self,words):
#         print('\033[35;1m我是%s,%s\033[0m' % (self.name,words))
#
#     def attack(self,target):
#         print('\033[31;2m正在攻击:%s...\033[0m' % target)
#
# class Weapon:
#     def __init__(self,name,strength,type):
#         self.name = name
#         self.strength = strength
#         self.type = type
#
# class State:
#     def __init__(self,value1,value2):
#         self.blood = value1
#         self.magic = value2
#
#
#
# class Warrior(Role,Weapon,State):
#     '子类可以继承父类(基类)的所有方法'
#     pass
#
# class Mager(Role,Weapon,State):
#     pass
#
# class Archer(Role,Weapon,State):
#     pass
#
#
# if __name__ == '__main__':
#     pygame = Game("\033[34;1m三国文字杀",'csdnak') #调用__init__
#     print(pygame) #调用__str__
#     pygame() #调用__call__
#
#     q = Weapon('\033[33;1m卧龙枪','力量72','物理攻击\033[0m')
#     state = State('\033[31;1m[血量:120%\033[0m','\033[34;1m魔法:100%]\033[0m')
#     zx = Warrior('\033[32;1m赵信\033[0m',q,state)
#     print('[%s]'% a)
#     print(zx.name,end='')
#     print(zx.state.blood,zx.state.magic)
#     print(zx.weapon.name,zx.weapon.strength,zx.weapon.type,sep='-')
#     zx.speak('\033[35;1m枪出龙炉,兔死狗烹!')
#     print('[%s]'% a)
#     zx.attack('吕布')
#
#
#     b = Weapon('\033[33;1m魔法棒','法术85','魔法攻击\033[0m')
#     state = State('\033[31;1m[血量:100%\033[0m','\033[34;1m魔法:150%]\033[0m')
#     gh = Mager('\033[32;1m光辉女郎\033[0m',b,state)
#     print('[%s]' % a)
#     print(gh.name,end='')
#     print(gh.state.blood, gh.state.magic)
#     print(gh.weapon.name,gh.weapon.strength,gh.weapon.type,sep='-')
#     gh.speak('\033[35;1m美貌与天下并存！')
#     print('[%s]' % a)
#     zx.attack('赵信')
#
#
#     g = Weapon('\033[33;1m霸王弓','射程100','远程攻击\033[0m')
#     state = State('\033[31;1m[血量:100%\033[0m','\033[34;1m魔法:140%]\033[0m')
#     hb = Archer('\033[32;1m寒冰射手\033[0m',g,state)
#     print('[%s]' % a)
#     print(hb.name,end='')
#     print(hb.state.blood, hb.state.magic)
#     print(hb.weapon.name,hb.weapon.strength,hb.weapon.type,sep='-')
#     hb.speak('\033[35;1m霸王硬上弓,美女变妇女!')
#     print('[%s]' % a)
#     hb.attack('光辉女郎')


