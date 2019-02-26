
"""
1. import 语句
想使用 Python 源文件，只需在另一个源文件里执行 import 语句
"""
# import test
# test.hello()
# num = test.sumf()
# print(num)

"""
2. from … import 语句
Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：
这样就调用模块中的变量和函数等时可以不用每次都加上模块名
可以直接使用变量或函数等
"""
# from test import hello,sumf
# hello()
# num = sumf()
# print(num)

# from … import * 语句
# 把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明
# from test import *
# hello()
# num = sumf()
# print(num)


"""
3. __name__属性
一个模块被另一个程序第一次引入时，其主程序将运行。
如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
"""
# if __name__ == '__main__':
#    print('程序自身在运行')
# else:
#    print('我来自另一模块')

"""
4. dir() 函数
内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
"""
import sys, test
print(dir(test))
print("\n")
print(dir(sys))



