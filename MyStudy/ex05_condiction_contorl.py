"""
小试牛刀
写一个斐波纳契数列

"""

"""
a, b = 0, 1
while b < 10:
    print(b, end=' ')   # 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
    a, b = b, a + b
"""

"""
1. 条件控制语句 Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。
Python中if语句的一般形式如下所示：
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
"""
print("猜数字游戏\n")
final_num = 56
flag = True
while flag:
    num = int(input("请输入一个整数："))
    if num > final_num:
        print("数字大了")
        flag = True
    elif num < final_num:
        flag = True
        print("数字小了")
    elif num == final_num:
        flag = False
        print("猜对啦，要猜的数字为 ", final_num)
    else:
        flag = True
        print("继续猜数字吧")
