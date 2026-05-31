# 常见数据类型
from os import name

print("Hello World")
print(type("Hello World"))

print(type(10))
print(type(3.14))
print(type(True))
print(type(False))
print(type(None))

num = -100
print(type(num))

# 常见数据类型 ---》 isinstance(数据，类型） ---》 bool值 ---> 判断数据是否是指定的类型，如果是：True, 否则：False
print(isinstance(num,int))
print(isinstance(num,float))
print(isinstance(num,complex))


# 字符串
# 定义字符串的三种方式
s1 = "Hello World" #双引号定义
s2 = 'Python' # 单引号定义
s3 = """  
Hello World
    欢迎大家进入到Python课程学习！
    大家记得一键三连哦 ~
"""  # 三引号定义（多行字符串）
print(s1)
print(s2)
print(s3)

# 定义字符串 ---》 It's very good
msg = 'It\'s very good'
print(msg)

msg2 ="It's very good"
print(msg2)

msg3 = "Hello 的意思是\"你好\""
print(msg3)

print("\t欢迎大家进入到Python课程学习! \n\t大家记得一键三连哦") # \n 换行  \t 按了Tab缩进

# 字符串拼接
s1 = "人生苦短" "我用python" ",ok"
print(s1)

msg4 = "人生苦短"
msg5 = "我用Python"
print("鬼叔说：" + msg4 + " , " + msg5)

# 案例： ---》 str（int 数字） ---> 将int类型转为字符串类型

age = 18

print("我今年" + str(age) + "岁")

# 字符串格式化 ---》方式1 %s 占位符

name1= "涛哥"
age1 = 18
print("大家号，我是%s , 今年%s岁" % (name1,age1))

# 字符串格式化 ---》方式2 f".. {变量名/表达式}.." 推荐写法

name2= "涛哥"
age2 = 18
print(f"大家好，我是{name2}，今年 {age2}岁")