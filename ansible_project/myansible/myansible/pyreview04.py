#!/bin/env python3
#-*- coding:utf8 -*-
#复习python第四天
#******列表方法
alist = [100, 9, 6,9, 5, 200, 365, 23, 4]
alist.append(1000)  #追加
alist.append((1, 2)) #把元组追加到列表
print(alist)  #[100, 9, 6, 9, 5, 200, 365, 23, 4, 1000, (1, 2)]
alist.extend((1, 2)) #将序列对象中的每一项作为列表加入
print(alist)  #[100, 9, 6, 9, 5, 200, 365, 23, 4, 1000, (1, 2), 1, 2]
print(alist.remove((1, 2))) #删除列表中的某一项
print(alist)   #[100, 9, 6, 9, 5, 200, 365, 23, 4, 1000, 1, 2]
alist.index(1000)  #取出1000的下标 (9)
alist.reverse()  #反转列表
print(alist)  #[2, 1, 1000, 4, 23, 365, 200, 5, 9, 6, 9, 100]

alist.insert(2, 9)  #在下标为2的位置插入数据9
print(alist)  #[2, 1, 9, 1000, 4, 23, 365, 200, 5, 9, 6, 9, 100]
alist.sort()  #升序排列
print(alist)  #[1, 2, 4, 5, 6, 9, 9, 9, 23, 100, 200, 365, 1000]
alist.sort(reverse=True)  #降序排列
print(alist)  #[1000, 365, 200, 100, 23, 9, 9, 9, 6, 5, 4, 2, 1]
alist.count(9)  #统计9出现的次数 (3)
alist.pop()  #默认将最后一个数据弹出 (1)
alist.pop(2)  #弹出下标为2的数据 (200)
blist = alist.copy() #将alist的值拷贝出来,赋值给blist
print(blist)  #[1000, 365, 100, 9, 9, 9, 5, 4, 2]
blist.clear() #清空列表
print(blist)  #[]
alist #[1000, 365, 100, 9, 9, 9, 5, 4, 2]

#元组 :相当于静态的列表
atu = (10, 3, 20)
atu.count(100) #0
atu.index(3) #1
#单元素元组必须加逗号
a = (10)
type(a)
'<class 'int'>'
print(a) #10
a = (10,)
type(a)
'<class 'tuple'>'
print(len(a)) #1


#*****practice
#模拟栈
#python stack.py
#1.思考程序的运作方式
#2.分析程序有哪些功能,将功能编写成函数
#3.编写主程序代码,按相关的规则调用函数
def push_it():
    print('push')

def pop_it():
    print('pop')

def view_it():
    print('view')

def show_menu():
    pass

if __name__ == '__main__':
    show_menu()

#****dictionary
"""
-字典属于:容器,可变,映射
-字典的key不能重复
-字典的key必须是不可变的类型 
"""



