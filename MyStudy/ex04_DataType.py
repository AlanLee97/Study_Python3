"""
1. 多个变量赋值
Python允许你同时为多个变量赋值
"""
a = b = c = "hello"
print(a,b,c)

# 也可以为多个对象指定多个变量
a,b,c = 1,2.5,"hello"
print(a,b,c)

"""
标准数据类型
Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）

Python3 的六个标准数据类型中：
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
"""

"""
1. Number（数字）
Python3 支持 int、float、bool、complex（复数）。
在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
"""
a,b,c,d = 20,4.5,True,4+3j
print(type(a),type(b),type(c),type(d))
# 此外还可以用 isinstance 来判断
print(isinstance(a,int))
# 可以通过使用del语句删除单个或多个对象
del a;
# print(a)    # 输出 NameError: name 'a' is not defined

# 运算
print(2 / 4)    # 除法，得到一个浮点数
print(2 // 4)    # 除法，得到一个整数
print(2 ** 5)   # 乘方


"""
3. String（字符串）
与 C 字符串不同的是，Python 字符串不能被改变(不能被重新赋值)
Python 没有单独的字符类型，一个字符就是长度为1的字符串。
"""
str = "hello python"
print(str)          # 输出字符串
print(str[0:-1])    # 输出第一个到倒数第二个的所有字符
print(str[0])       # 输出字符串第一个字符
print(str[2:5])     # 输出从第三个开始到第五个的字符
print(str[2:])      # 输出从第三个开始的后的所有字符
print(str * 2)      # 输出字符串两次
print(str + "TEST")    # 连接字符串


"""
4. List（列表）
List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
"""
list = ["hello", 123, 2.45, True]
list2 = ["hello", 123]
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(list * 2)
print(list + list2)

# 与Python字符串不一样的是，列表中的元素是可以改变的：
list[1] = "python"
print(list)

# Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
sub = list[1:3:1]   # 后面的 1 表示为间隔 1
print(sub)


"""
5. Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
"""
tuple = ("hello", 123, 2.45, True)
tuple2 = ("hello", 123)
print(tuple)             # 输出完整元组
print(tuple[0])          # 输出元组的第一个元素
print(tuple[1:3])        # 输出从第二个元素开始到第三个元素
print(tuple[2:])         # 输出从第三个元素开始的所有元素
print(tuple * 2)         # 输出两次元组
print(tuple + tuple2)    # 连接元组


"""
6. Set（集合）
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""
studentSet = {"Tom","Jim","Mary","Tom","Jack"}
print(studentSet)   # 输出集合，重复的元素被自动去掉
# 成员测试
if "Rose" in studentSet:
    print("Rose在集合中")
else:
    print("Rose不在集合中")

# set可以进行集合运算
a = set("abcdefg")
b = set("efg")
print(a)
print(b)
# print(a + b)
print(a - b)
# print(a | b)
# print(a & b)
# print(a ^ b)


"""
7. Dictionary（字典）
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
"""
dict = {}
dict[1]= "hello"
dict["two"] = "python"
dict["3"] = "hello python"
dict2 = {1:"hello","two":"python","3":"hello python"}
print(dict[1])
print(dict["two"])
print(dict["3"])
print(dict2)
print(dict2.keys())
print(dict2.values())

# 构造函数 dict() 可以直接从键值对序列中构建字典
dict([("str1",1),("str2",2),("str3",3)])
{
    "str1":1,"str2":2,"str3":3
}
print(dict)















