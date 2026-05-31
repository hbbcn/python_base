# for循环: 遍历输入的字符串

# msg = input('请输入一个字符串：')
#
# for s in msg:
#     print(s)
# else:
#     print("字符串遍历结束!!!")

# range函数:
# range(start, stop, step)  # start: 起始值, stop: 结束值(不包含), step: 步长
# range(stop): 从0开始, 到stop结束(不包含), 步长为1
# range(start, stop): 从start开始, 到stop结束(不包含), 步长为1

# 案例1：计算1-100之间所有奇数的和
total = 0
for num in range(1, 101):
    if num % 2 != 0:
        total += num
else:
    print("1-100之间所有奇数的和为: ", total) # 2500

# 简化
for num in range(1, 101, 2):
    total += num
else:
    print("1-100之间所有奇数的和为: ", total)

