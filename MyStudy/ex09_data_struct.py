"""
1. 列表
Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，
一句话概括即：列表可以修改，而字符串和元组不能。

"""
#
# mylist = [1, 2, 3, 4, 5, 6]
# mylist.append(7)    # 输出[1, 2, 3, 4, 5, 6, 7]
# mylist.reverse()    # 输出[7, 6, 5, 4, 3, 2, 1]
# mylist.remove(7)    # 输出[6, 5, 4, 3, 2, 1]
# mylist.insert(0, 0)  # 输出[0, 6, 5, 4, 3, 2, 1]
#
# print(mylist)


'''
将列表当做堆栈使用
列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，
最先进入的元素最后一个被释放（后进先出）。用 append() 方法可以把一个
元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。
例如：
'''
# stack = [3, 4, 5]
# stack.append(6)     # 相当于入栈
# stack.append(7)
# stack.pop()         # 相当于出栈
# stack.pop()


'''
将列表当作队列使用
也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表
用作这样的目的效率不高。在列表的最后添加或者弹出元素速度快，然而在列表里插入
或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。
'''
# queue = [3, 4, 5, 6]
# queue.append(7)     # 相当于入队
# queue.pop()         # 相当于出队

'''
列表推导式
列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。
每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。
这里我们将列表中每个数值乘三，获得一个新的列表：
'''
# mylist = [2, 4, 6]
# newlist = [3 * i for i in mylist]       # 输出[6, 12, 18]
# print(newlist)
#
# newlist = [[i, i**2] for i in mylist]   # 输出[[2, 4], [4, 16], [6, 36]]
# print(newlist)

# 可以用 if 子句作为过滤器
# mylist1 = [2, 4, 6]
# mylist2 = [1, 3, 5]
# newlist = [i * j for i in mylist1 for j in mylist2]     # 输出[2, 6, 10, 4, 12, 20, 6, 18, 30]
# print(newlist)

'''
嵌套列表解析
Python的列表还可以嵌套。
以下实例展示了3X4的矩阵列表：
'''
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# # 以下实例将3X4的矩阵列表转换为4X3列表：
# rmatrix = [[row[i] for row in matrix] for i in range(4)]
# print(rmatrix)
'''
输出
[
 [1, 5, 9],
 [2, 6, 10], 
 [3, 7, 11], 
 [4, 8, 12]
]
'''

'''
del 语句
使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。
这与使用 pop() 返回一个值不同。可以用 del 语句从列表中删除一个切割，
或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）。
例如：

'''
# mylist = [1, 2, 33]
# del mylist[0]   # 输出[2, 33]
# print(mylist)
# del mylist      # 也可以用 del 删除实体变量
# # print(mylist)     # 报错 NameError: name 'mylist' is not defined


"""
2. 元组和序列
元组由若干逗号分隔的值组成
"""
# mytuple = 2333, "hello python", True
# print(mytuple)      # 输出(2333, 'hello python', True)
#
# mytuple2 = "life is so short, i use python", mytuple
# print(mytuple2)     # 输出('life is so short, i use python', (2333, 'hello python', True))


"""
3. 集合
集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
集合也支持推导式
"""
# # 方式1
# myset = {2333, "hello python", True}
# print(myset)    # 输出{True, 2333, 'hello python'}
#
# # 方式2
# myset2 = set("hello python")      # set()最多只能有一个参数
# print(myset2)    # 输出{'n', 'l', ' ', 'e', 't', 'h', 'y', 'p', 'o'}


"""
4. 字典
另一个非常有用的 Python 内建数据类型是字典。
序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。
一对大括号创建一个空的字典：{}。
"""
# dict = {
#     "name": "nibuguai",
#     "age": 22,
#     "gender": "male"
# }
# print(dict)     # 输出{'name': 'nibuguai', 'age': 22, 'gender': 'male'}
#
# # 字典推导可以用来创建任意键和值的表达式词典
# dict1 = {i: i**2 for i in (2, 4, 6)}
# print(dict1)    # 输出{2: 4, 4: 16, 6: 36}
#


"""
遍历技巧
"""
# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
# dict = {
#     "name": "nibuguai",
#     "age": 22,
#     "gender": "male"
# }
# for key, value in dict.items():
#     print(key, " : ", value)

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
# for index, value in enumerate(["C", "C++", "java", "python"]):
#     print(index, ":", value)

# 同时遍历两个或更多的序列，可以使用 zip() 组合：
#
# languages = ["C", "C++", "java", "python"]
# rank = [4, 3, 1, 2]
# for l, r in zip(languages, rank):
#     print("{0} : {1}".format(l, r))

# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：
# languages = ["C", "C++", "java", "python"]
# for i in reversed(languages):
#     print(i)
#
# # 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：
# for i in sorted(languages):
#     print(i)






















