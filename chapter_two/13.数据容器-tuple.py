# 元组基本操作 -tuple ---> 元素不可重复，有序，不可修改
# 定义
t1 = (1, 2, 3, 4, 5, 6,2)
print("元组: ", t1)
print("元组长度: ", len(t1),"元组类型: ", type(t1))

# 索引访问
print("索引访问: ", t1[0])
print("索引访问: ", t1[-1])

# 切片
print("切片: ", t1[0:3:2])

#count() 统计元素在元组中出现的次数
print("count() 统计元素在元组中出现的次数: ", t1.count(2))

# index() 获取元素在元组中的索引位置
print("index() 获取元素在元组中的索引位置: ", t1.index(2)) # 只会返回第一个2的索引位置

# 注意点 - 定义一个空元组和一个只有一个元素的元组 ps : 定义一个只有一个元素的元组时, 需要在元素后面添加逗号, 否则Python会将括号当做普通的括号来处理, 而不是元组的定义语法
t2 = ()
print(t2)
print(type(t2)) # <class 'tuple'>
t3 = (1,) # 元组
print(t3)
print(type(t3)) # <class 'tuple'>

# -----------元组 tuple组包与解包------------
# 1. 组包: 将多个值合并到一个容器中
# 2. 解包: 将一个容器中的值拆分成多个变量
num_tuple = (1, 2, 3, 4, 5)
num_tuple2  = 1, 2, 3, 4, 5 # 组包 - 省略了括号
print("元组: ", num_tuple)
print("num_tuple2: ", num_tuple2)

# 解包操作  - 将元组中的元素依次赋值给多个变量, 变量的数量必须与元组中的元素数量一致
a, b, c, d, e = num_tuple
print("解包后的变量: ", a, b, c, d, e)
# * 变量名  - 将元组中剩余的元素收集到一个列表中
first,second,*others,last = num_tuple
print("first: ", first)
print("second: ", second)
print("others: ", others)
print("last: ", last)

# -------------------------------------------- 元组案例 --------------------------------------
# 案例1 现有两个变量a,b,a的值为10,b的值为20,请交换a,b的值
a = 10
b = 20
a,b = b,a # 交换a,b的值
print("a: ", a)
print("b: ", b)

# 案例2: 输入一个元组, 输出元组中的最大值和最小值
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("元组中的最大值: ", max(t))
print("元组中的最小值: ", min(t))
print("元组中的平均值: ", sum(t) / len(t))
print("元组中的和: ", sum(t))
print("元组中的元素个数: ", len(t))
print("元组中的元素个数: ", t.count(1))
print("元组中的索引位置: ", t.index(1))

"""
# 案例3: 根据学生信息，完成如下需求
# 1. 定义一个元组，包含学生的学号、姓名、年龄、性别、各科成绩等信息
# 2. 输出学生的姓名和成绩
# 3.最高分, 最低分, 平均分
# 4.查找成绩优秀（平均分大于等于90分）的学生姓名
"""
student_info = (
    ("2021001", "张三", 18, "男", 95, 88, 92),
    ("2021002", "李四", 19, "女", 85, 90, 87),
    ("2021003", "王五", 17, "男", 78, 82, 80),
    ("2021004", "赵六", 20, "女", 92, 94, 96),
    ("2021005", "孙七", 16, "男", 65, 70, 68),
    ("2021006", "周八", 18, "女", 80, 85, 82),
    ("2021007", "吴九", 19, "男", 75, 80, 78),
    ("2021008", "郑十", 20, "女", 90, 95, 98),
)
# 方式1 :
for s in student_info:
    print("学生姓名: ", s[0])
    print("学生成绩: ", s[4:7])
    print("最高分: ", max(s[4:7]))
    print("最低分: ", min(s[4:7]))
    print("平均分: ", round(sum(s[4:7]) / len(s[4:7]), 2)) # 保留两位小数
    print("优秀学生: ")
    for s in student_info:
        if sum(s[4:7]) / len(s[4:7]) >= 90:
            print("优秀学生: ", s[0])

chinese_score = [s[4] for s in student_info]
# 保留两位小数两种写法 - round(.., 2) ; f-string - {:.2f}
print(f"语文平均分:", f"{sum(chinese_score) / len(chinese_score):.2f}")

# 方式2
for ID,name,age,sex,chinese,math,english in student_info:
    print(f"{ID}\t {name}\t {age}\t{sex}\t{chinese}\t{math}\t{english}")
    print("最高分: ", max(chinese, math, english))
    print("最低分: ", min(chinese, math, english))
    print("平均分: ", round(sum([chinese, math, english]) / 3, 2))
    if sum([chinese, math, english]) / 3 >= 90:
        print("优秀学生: ", name)