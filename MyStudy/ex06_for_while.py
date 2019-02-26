
"""
1. while 循环
同样需要注意冒号和缩进。另外，在Python中没有do..while循环。
"""
# n = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter += 1    # 没有counter++ 的方式
# print("1 到 %d 之和为： %d" % (n, sum))

"""
2. while 循环使用 else 语句
在 while … else 在条件语句为 false 时执行 else 的语句块：
"""
# count = 0
# while count < 5:
#     print(count, "小于5")
#     count += 1
# else:
#     print(count, "大于或等于5")

"""
3. 简单语句组
类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中， 如下所示：
注意：无限循环你可以使用 CTRL+C 来中断循环。
"""
# flag = 1
# while (flag): print("hello python")

"""
4. for 语句
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
语法：
for <variable> in <sequence>:
    <statements>
else:
    <statements>

"""
# languages = ["C","C++","java","php","python","javascript"]
# for i in languages:
#     print(i, end=" ")

# 以下 for 实例中使用了 break 语句，break 语句用于跳出当前循环体：
# languages = ["C","C++","java","php","python","javascript"]
# for i in languages:
#     print(i, end=" ")
#     if i == "python":
#         break           # 输出C C++ java php python


"""
5. 
range()函数
如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:
"""
# for i in range(5):
#     print(i)
# 你也可以使用range指定区间的值：
# for i in range(5, 9):     # 左闭右开
#     print(i)

# 也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
# for i in range(5, 9, 2):
#     print(i)
# for i in range(-5, -9, -2):
#     print(i)

# 您可以结合range()和len()函数以遍历一个序列的索引,如下所示:
# languages = ["C","C++","java","php","python","javascript"]
# for i in range(len(languages)):
#     print(i, " => ", languages[i])

"""
6. break,continue语句不演示
"""


"""
pass 语句
Python pass是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句，如下实例
"""
# while True:
#     pass    # 等待键盘中断 (Ctrl+C)



