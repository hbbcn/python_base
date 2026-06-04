# 列表操作
# 定义列表 -list
list1 =[1,2,4,4,5,"AA",True]
print(type(list1))

# 访问列表中的元素
print(list1[0]) # 1
print(list1[5]) # "AA" 正向索引
print(list1[-1]) # True 反向索引

# 修改
list1[0] = "Python"
print(list1)

# 删除
del list1[0]
print(list1)

# 遍历
for item in list1:
    print(item)


# ----------------------列表 list 切片----------------------
list1 =[1,2,4,4,5,"AA",True]

# 切片操作
print(list1[0:3:1])
print(list1[:3:])
print(list1[:3])

print(list1[::2])

print(list1[:-2:3])

# -------------列表常用方法----------------
list2 =[1,2,4,4,5,"AA",True]
# append() 在列表末尾添加一个元素
list2.append("Python")
print("append添加Python后: ", list2)

# insert() 在列表指定位置添加一个元素
list2.insert(0,"Java")
print("insert 插入Java后: ", list2)

# remove() 删除列表中指定的元素
list2.remove(4) # 只会删除第一个4
print("remove 删除4后: ", list2)

# pop(n) 删除列表中指定位置的元素, 并返回被删除的元素(默认删除列表末尾的元素)
e = list2.pop(1)
print("pop 删除的元素: ", e)
print("pop 删除后: ", list2)
e=list2.pop()
print("pop 删除的元素: ", e)
print("pop 删除后: ", list2)

# sort() 对列表进行排序
list3 = [5,2,9,1,3]
list3.sort()
print("sort 排序：", list3)

# reverse() 反转列表
list3.reverse()
print("reverse 反转：", list3)
# --------------------------------------- 列表 list 案例 --------------------------------------
#案例1. 将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序, 输出其中的最小值、最大值 和 平均值。

# 1. 定义列表
# num_list = []
#
# # 2. 将用户输入的10个数字存入列表
# for i in range(10):
#     num = int(input("请输入一个有效的数字: "))
#     num_list.append(num)
#
# print("数字列表: ", num_list)
#
# # 3. 排序
# num_list.sort()
# print("排序后的数字列表: ", num_list)
#
# # 4. 输出其中的最小值、最大值 和 平均值。---> sum() 求和 ; len() 获取元素的个数(列表的长度)
# print("最小值: ", num_list[0])
# print("最大值: ", num_list[-1])
# print("平均值: ", sum(num_list)/len(num_list))



#案例2: 合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#
# # 1. 合并列表
# for num in num_list2:
#     num_list1.append(num)
#
# print("合并后的原始列表: ", num_list1)
#
# # 2. 去重重复记录
# new_list = [] # 去重重复记录后的列表
#
# for num in num_list1:
#     # 判断new_list中是否存在num元素, 如果不存在, 再添加
#     if num not in new_list: # 判断元素是否存在于列表中, 如果存在, 则返回True; 不存在, 返回False
#         new_list.append(num)
#
# print("去重重复记录后的列表: ", new_list)



# #案例2(简化): 合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#
# # 1. 合并列表
# # 解包: 将列表这一类容器解开成一个一个独立的元素
# # 组包: 将多个值合并到一个容器
# num_list = [*num_list1, *num_list2]
#
# print("合并后的原始列表: ", num_list)
#
# # 2. 去重重复记录
# new_list = [] # 去重重复记录后的列表
#
# for num in num_list:
#     # 判断new_list中是否存在num元素, 如果不存在, 再添加
#     if num not in new_list: # 判断元素是否存在于列表中, 如果存在, 则返回True; 不存在, 返回False
#         new_list.append(num)
#
# print("去重重复记录后的列表: ", new_list)



#案例2(简化): 合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#
# # 1. 合并列表
# num_list = num_list1 + num_list2
# print("合并后的原始列表: ", num_list)
#
# # 2. 去重重复记录
# new_list = [] # 去重重复记录后的列表
#
# for num in num_list:
#     # 判断new_list中是否存在num元素, 如果不存在, 再添加
#     if num not in new_list: # 判断元素是否存在于列表中, 如果存在, 则返回True; 不存在, 返回False
#         new_list.append(num)
#
# print("去重重复记录后的列表: ", new_list)



# 案例3: 生成1-20的平方列表。 --> range(1,21)
# 方式一: 传统方式
# num_list = []
# for i in range(1,21):
#     num_list.append(i**2)
#
# print(num_list)
#
# # 方式二: 列表推导式 ---> 就是按照一定的规则快速生成一个列表的方法 --> 语法格式1: [要插入的值 for i in 序列/列表]
# num_list2 = [i**2 for i in range(1,21)]
# print(num_list2)



# 案例4: 从一个数字列表中提取所有偶数，并计算其平方，组成一个新的列表。 ---> 判断偶数: num % 2 == 0
# 列表推导式 ---> 就是按照一定的规则快速生成一个列表的方法 --> 语法格式2: [要插入的值 for i in 序列/列表 if 条件]
num_list = [12, 32, 45, 77, 80, 92, 33, 57, 97, 98, 110, 111, 122]
new_list = [i**2 for i in num_list if i % 2 == 0]

print(new_list)

print(num_list[::])
