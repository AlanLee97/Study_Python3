"""
1. 输出格式美化
Python两种输出值的方式: 表达式语句和 print() 函数。
第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。
#  repr() 函数可以转义字符串中的特殊字符
#  repr() 的参数可以是 Python 的任何对象
"""
# hello = "hello \npython"
#
# print(str(hello))
# print(repr(hello))  # 输出'hello \npython'

# 字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
# 还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
# 另一个方法 zfill(), 它会在数字的左边填充 0，：
# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
#     print(repr(x*x*x).rjust(4))




# # str.format() 的基本使用如下:
# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4f}'.format(x, x*x, x*x*x))
#
# # 可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化


"""
读和写文件read(), write()
open() 将会返回一个 file 对象，基本语法格式如下:

open(filename, mode)
filename：包含了你要访问的文件名称的字符串值。
mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。

"""
# file = open("D:/Test/test.txt", "w")
# file.write("人生苦短，我学python")
# file.close()


"""
文件对象的方法read()
为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
"""
# file = open("D:/Test/test.txt", "r")
# # str1 = file.read()
# # f.readline()  从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
# str2 = file.readline()  # 输出 1 ：人生苦短，我学python！
# # readlines() 读取所有行
# # str3 = file.readlines()
# # print(str1)
# print(str2)
# file.close()
"""
# f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
# f.seek()
# 如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
# from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾
如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)：表示从文件的结尾往前移动x个字符
from_what 值为默认为0，即文件开头。下面给出一个完整的例子：
"""
# file = open("D:/Test/test.txt", 'rb+')
# file.write(b"0123456789abcdefghijk")
# print(file.seek(5))      # 移动到文件的第六个字节
# print(file.read(1))
# print(file.seek(-3, 2))      # 移动到文件的倒数第三字节
# print(file.read(1))

# 当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短:
with open("D:/Test/test.txt","r") as file:
    data = file.read()
print(data)
file.close()



