"""
1. 函数：
语法
Python 定义函数使用 def 关键字，一般格式如下：
def 函数名（参数列表）:
    函数体
"""
# def myFunction():
#     print("hello python")
# myFunction()

"""
2. 带参数的函数
"""
# str = "python"
# def myFunction(str):
#     print("我在学 ", str)
# myFunction(str)

"""
3. python 传不可变对象实例
可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
python 函数的参数传递：
不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

"""
# def changeInt(a):
#     a = 10
#
# b = 2
# changeInt(b)
# print("b = ", b)

"""
4. 传可变对象实例
可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了
"""

# def changefunc(mylist):
#     mylist.append([1, 2, 3, 4, 5])
#     print("函数内取值为：", mylist)
#     return
#
# mylist = [10,20,30]
# print("调用函数前：函数外取值为：", mylist)
# changefunc(mylist)
# print("调用函数后：函数外取值为：", mylist)
# # 输出：
# # 函数内取值为： [10, 20, 30, [1, 2, 3, 4, 5]]
# # 函数外取值为： [10, 20, 30, [1, 2, 3, 4, 5]]

"""
5. 关键字参数 + 默认参数
关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
"""
# def myFunc(name, age, sex = "male"):    # sex = "male"为默认参数
#     print("name: ", name)
#     print("age: ", age)
#     print("sex: ", sex)
#     return
#
# myFunc(name = "nibuguai", age = 22)


"""
6. 不定长参数
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名
"""

# def myfunc ( name, *other) :
#
#     print("name: ", name)
#     print("other: ", other)
#
# name = "nibuguai"
# myfunc(name, 22, "male")
# 输出：
# name:  ('nibuguai',)
# other:  (22, 'male')

# 还有一种就是参数带两个星号 **基本语法如下：
# def functionname([formal_args,] **var_args_dict ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]

# def myfunc ( name, **other) :
#
#     print("name: ", name)
#     print("other: ", other)
#
# name = "nibuguai"
# myfunc(name, age = 22, sex = "male")
# # 输出
# # name:  nibuguai
# # other:  {'age': 22, 'sex': 'male'}

# 声明函数时，参数中星号 * 可以单独出现，
# 如果单独出现星号 * 后的参数必须用关键字传入。
# 例如:
# def f(a, b, *, c):
#     print(a + b + c)
#
# # f(1,2,3)    # 报错
# f(1, 2, c = 3)


"""
7. 匿名函数
python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
语法
lambda 函数的语法只包含一个语句，如下：
lambda [arg1 [,arg2,.....argn]]:expression
"""
# people = lambda name, age, sex: print("name: ", name, "\nage: ", age, "\nsex: ",sex)
# print(people("nibuguai", 22, "male"))

"""
8. return语句
return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None
这里不做演示
"""

"""
9. 变量作用域
Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内置作用域（内置函数所在模块的范围）
以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内置中找。
"""
# g_count = 0     # 全局作用域
# def outer():
#     o_count = 1     # 闭包函数外的函数中
#     print(o_count)
#     def inner():
#         i_count = 2     # 局部作用域
#         print(i_count)
#     inner()   # 这里调用内层函数
# outer()


# 内置作用域是通过一个名为 builtin 的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能够使用它。在Python3.0中，可以使用以下的代码来查看到底预定义了哪些变量:
#
# import builtins
# dir(builtins)

# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
# 也就是说这些语句内定义的变量，外部也可以访问，如下代码：
# if True:
#     str = "hello python"
# def myfunc():
#     str1 = "hello python"
#
# print(str)
# # print(str1)       # 找不到str1

"""
10. global 和 nonlocal关键字
当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。

以下实例修改全局变量 num：
"""
# num = 1
# def myfunc():
#     global num
#     num = 2333
#
# # 未使用global 关键字声明
# # myfunc()
# # print(num)      # 输出 num = 1
#
# # 使用global之后
# myfunc()
# print(num)      # 输出 num = 2333

# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）
# 中的变量则需要 nonlocal 关键字了，如下实例：
# def outer():
#     num = 10
#     def inner():
#         nonlocal num
#         num = 2333
#         print(num)
#     inner()
#     print(num)
# outer()

"""
特殊情况
"""
a = 10
def test():
    global a      # 如果不使用这条语句  或者不把 a 当成参数传进来的话会报错
    # UnboundLocalError: local variable 'a' referenced before assignment

    a = a + 1
    print(a)
test()











