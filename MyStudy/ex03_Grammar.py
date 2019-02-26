"""
1. 行与缩进
python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。
"""
if True:
    print("True")
else:
    print("False")
print("\n")


"""
2. 多行语句
Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句
"""
str = "长语句" + \
        "使用\\" + \
        "来实现换行"
print(str)
print("\n")
'''
在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)
'''
str = ["这里" + "不需要\\" + "来换行"]
print(str)
print("\n")


"""
3. 
数字(Number)类型
python中数字有四种类型：整数、布尔型、浮点数和复数。
int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j
"""
int_val = 22
bool_val = True
float_val1 = 1.23
float_val2 = 3E-2
complex_val = 1 + 2j
print(int_val,bool_val,float_val1,float_val2,complex_val)


"""
4. 字符串(String)
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python中的字符串不能改变。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
"""
str = "Hello Python!"
print(str[0:-1])    # 输出第一个到倒数第二个的所有字符 输出Hello Python
print(str[0])       # 输出字符串第一个字符
print(str[2:5])     # 输出从第三个开始到第五个的字符
print(str[2:])      # 输出从第三个开始的后的所有字符
print(str * 2)      # 输出字符串两次
print("你好," + str)          # 连接字符串
print('Hello\nPython！')     # 使用反斜杠(\)+n转义特殊字符
print(r'Hello\nPython！')    # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


"""
5. 等待用户输入
执行下面的程序在按回车键后就会等待用户输入
input()的返回值始终是字符串，所以type(number)永远是<class 'str'>！
"""
'''
str = input("\n请输入字符串\n按下enter键后退出\n->")
print(str);
int_val = input("请输入一个数字\n->")
int_val = int(int_val)      #必须强制类型转换
print("你输入的数字为",int_val)
'''

"""
6. 同一行显示多条语句
Python可以在同一行中使用多条语句，语句之间使用分号(;)分割
"""
x = 2; y = 3; z = x + y; print(z);


"""
7. Print 输出
print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
"""
#不换行输出
print(x,end=" ")
print(y,end=" ")
print("\n")

"""
8. import 与 from...import
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
"""
#导入 sys 模块
import sys
print("命令行参数为")
for i in sys.argv:
    print(i)
print("\npython路径为",sys.path)

#导入 sys 模块的 argv,path 成员
from sys import argv,path
print("命令行参数为")
for i in argv:
    print(i)
print("\npython路径为",path)















