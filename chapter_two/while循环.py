# 设置标准输出编码为 UTF-8
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# while 循环 : 打印10遍"人生苦短，我用python"
i = 1
while i <= 10:
    print(f"人生苦短，我用python{i}")
    i += 1
else:
    print("循环结束了") # 11


# while...else...案例: 计算1-100之间所有偶数的和
num = 1
total = 0
while num <= 100:
    if num % 2 == 0:
        total += num
    num += 1
else:
    print("1-100之间所有偶数的和为: ", total) # 2550



"""
    如下：是一个长度为10，宽度为5的矩形，使用while循环打印这个矩形
    **********
    **********
    **********
    **********
    **********
"""

"""
# 1.接受键盘录入的m,n
m = int(input("请输入长: "))
n = int(input("请输入宽: "))


# 2.打印矩形
# print("*", end="") end="" 代表不换行, 继续在同一行输出
i = 1
while i <= n:
    j = 1
    while j <= m:
        print("*", end="  ")
        j += 1
    else:
        print() # 换行
    i += 1
else:
    print("矩形打印结束了")
"""
# 嵌套循环：打印99乘法表
for i in range (1,10):
    for j in range(1,i + 1):
        print(f"{j} * {i} = {i * j}", end="\t")
    else:
        print() # 换行


