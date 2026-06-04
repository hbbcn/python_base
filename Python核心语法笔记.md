# Python 核心语法笔记

---

## 目录

- [第一章 数据存储与运算](#第一章-数据存储与运算)
  - [1.1 字面量](#11-字面量)
  - [1.2 变量](#12-变量)
  - [1.3 标识符](#13-标识符)
  - [1.4 数据类型](#14-数据类型)
  - [1.5 数据类型转换](#15-数据类型转换)
  - [1.6 输入与输出](#16-输入与输出)
  - [1.7 运算符](#17-运算符)
- [第二章 流程控制语句](#第二章-流程控制语句)
  - [2.1 条件判断](#21-条件判断)
  - [2.2 结构模式匹配](#22-结构模式匹配)
  - [2.3 循环](#23-循环)
- [第三章 数据存储容器](#第三章-数据存储容器)
  - [3.1 列表（list）](#31-列表list)
  - [3.2 字符串（str）](#32-字符串str)
  - [3.3 元组（tuple）](#33-元组tuple)
  - [3.4 集合（set）](#34-集合set)
  - [3.5 字典（dict）](#35-字典dict)
  - [3.6 容器通用操作](#36-容器通用操作)
- [第四章 函数](#第四章-函数)
  - [4.1 函数基础](#41-函数基础)
  - [4.2 函数进阶](#42-函数进阶)
- [第五章 模块](#第五章-模块)
  - [5.1 模块导入](#51-模块导入)
  - [5.2 自定义模块](#52-自定义模块)
  - [5.3 包（package）](#53-包package)
- [第六章 面向对象基础](#第六章-面向对象基础)
  - [6.1 面向对象编程思想](#61-面向对象编程思想)
  - [6.2 类与对象](#62-类与对象)
  - [6.3 实例方法](#63-实例方法)
  - [6.4 魔法方法](#64-魔法方法)
  - [6.5 实例属性与类属性](#65-实例属性与类属性)
  - [6.6 异常处理](#66-异常处理)

---

## 第一章 数据存储与运算

### 1.1 字面量

> 字面量：指程序中，直接书写的固定值（数据）。

| 字面量类型 | 说明 | 示例 |
| :--- | :--- | :--- |
| 整数（int） | 整数 | `10`、`18`、`-5`、`0` |
| 浮点数（float） | 小数 | `8.5`、`3.14`、`1.0`、`-3.5` |
| 布尔（bool） | 逻辑真或假 | `True`、`False` |
| 字符串（str） | 描述文本 | `"人生苦短，我用Python"` |
| 空值（NoneType） | 表示空或无值 | `None` |

> **注意**：布尔类型本质是数字类型，`True` 在数学运算中自动转为 `1`，`False` 转为 `0`。

```python
# 布尔类型参与数学运算
print(True + 1)    # 2
print(False - 1)   # -1
```

---

### 1.2 变量

> 变量：程序中用来存储单个数据的容器，通常会把经常发生变化的数据存储在变量中。

**定义格式**：

```python
变量名 = 变量的值
num = 1114.1
```

**注意事项**：

- 一个变量只能存储一个值（后赋的值会覆盖先赋的值）
- 变量定义时必须赋值才可使用
- 一条语句可以定义多个变量，也可以连续赋值：`a, b = 1, "Python"`
- Python 是**动态类型语言**，变量类型可以在运行过程中改变（但项目开发中，推荐变量只存储一种类型的数据）

> **关键理解**：变量是指存储数据的容器（空间），而不是容器里面存储的数据。

```python
# 变量可以存储不同类型的数据
num = 1114.1
print(num)       # 1114.1

num = num + 1
print(num)       # 1115.1

num = "OK"
print(num)       # OK

num = True
print(num)       # True
```

**案例：变量交换**

```python
# 方式一：借助第三方变量
a = 10
b = 20
c = a    # c = 10
a = b    # a = 20
b = c    # b = 10
print(a, b)  # 20 10

# 方式二：利用组包与解包（推荐）
a, b = b, a
```

---

### 1.3 标识符

> 标识符是程序员在代码中为变量、函数、类等元素所起的名字。

**命名规则（必须遵守）**：

- 只能包含字母（a-z, A-Z）、数字（0-9）、下划线（_）
- 不能以数字开头
- 不能使用关键字（`True`、`False`、`None`、`and`、`or`、`if`、`else` 等）
- 严格区分大小写（`age`、`Age`、`AGE` 是三个变量）

**命名规范（建议遵守）**：

| 场景 | 命名规范 | 示例 |
| :--- | :--- | :--- |
| 变量名 | 全小写，单词间用下划线分隔（蛇形命名法） | `my_name`、`student_score` |
| 类名 | 每个单词首字母大写（大驼峰命名法） | `UserInfo`、`UserAccount` |

---

### 1.4 数据类型

Python 中常用的数据类型：

| 类型 | 描述 | 示例 |
| :--- | :--- | :--- |
| `int` | 整数 | `695`、`-5`、`0` |
| `float` | 浮点数 | `3.14`、`-3.5`、`1.0` |
| `bool` | 布尔值 | `True`、`False` |
| `str` | 字符串 | `"Python"` |
| `NoneType` | 空值 | `None` |
| `list` | 列表 | `[1, 2, 3]` |
| `tuple` | 元组 | `(1, 2, 3)` |
| `set` | 集合 | `{1, 2, 3}` |
| `dict` | 字典 | `{"name": "张三"}` |

**查看数据类型**：

```python
type(变量)   # 返回变量的数据类型

print(type("Hello"))   # <class 'str'>
print(type(10))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type(True))       # <class 'bool'>
print(type(None))       # <class 'NoneType'>
```

**判断数据类型**：

```python
isinstance(数据, 类型)  # 返回布尔值，判定数据是否是指定类型

num = -100
print(isinstance(num, int))     # True
print(isinstance(num, float))    # False
print(isinstance(num, bool))     # False
```

#### 字符串的定义

```python
# 三种定义方式
s1 = "Hello"        # 双引号
s2 = 'Python'       # 单引号
s3 = """            # 三引号（多行字符串）
Hello:
    欢迎大家进入到Python课程的学习!
    大家记得一键三连哦 ~
"""

# 转义字符：\'  \"  \n(换行)  \t(Tab缩进)
msg = 'It\'s very good'
msg2 = "Hello 的意思就是 \"您好\""
print("\t欢迎大家进入到Python课程的学习!\n\t大家记得一键三连哦 ~")
```

#### 字符串拼接

```python
# 方式一：直接拼接
s1 = "人生苦短" "我用Python" ", OK"
print(s1)

# 方式二：+ 号拼接
msg1 = "人生苦短"
msg2 = "我用Python"
print("龟叔说: " + msg1 + " , " + msg2)
```

---

### 1.5 数据类型转换

| 函数 | 说明 | 示例 |
| :--- | :--- | :--- |
| `int(x)` | 将 x 转换为整数 | `int("10")` → `10` |
| `float(x)` | 将 x 转换为浮点数 | `float("3.14")` → `3.14` |
| `str(x)` | 将 x 转换为字符串 | `str(10)` → `"10"` |
| `bool(x)` | 将 x 转换为布尔值 | `bool(0)` → `False` |

> **注意**：不是所有类型之间都能互相转换，例如 `int("abc")` 会报错。

---

### 1.6 输入与输出

**输出 — `print()`**：

```python
# 基本输出
print("Hello World")

# 格式化输出方式一：%s 占位符
name = "涛哥"
age = 18
pro = "软件工程"
hobby = "Python、Java"
print("大家好, 我是 %s , 今年 %s 岁, 学习的专业是 %s , 爱好 %s" % (name, age, pro, hobby))

# 格式化输出方式二：f-string（推荐）
print(f"大家好, 我是 {name} , 今年 {age} 岁, 学习的专业是 {pro} , 爱好 {hobby}")
```

**输入 — `input()`**：

```python
# input() 接收的内容始终为字符串类型，需要手动类型转换
name = input("请输入你的名字：")
age = int(input("请输入你的年龄："))
```

**案例：银行卡ATM取款**

```python
# 总金额
total = 10000

# 1. 输入密码
password = input("请输入您的银行卡密码: ")
print(f"密码正确, {password}")

# 2. 输入取款金额
num = input("请输入您的取款金额: ")

# 3. 计算余额并输出 --> num 转为 int类型
print(f"取款后银行卡余额为: {total - int(num)}")
```

---

### 1.7 运算符

#### 算术运算符

| 运算符 | 描述 | 示例 |
| :--- | :--- | :--- |
| `+` | 加 | `10 + 4` → `14` |
| `-` | 减 | `10 - 4` → `6` |
| `*` | 乘 | `10 * 4` → `40` |
| `/` | 除 | `10 / 4` → `2.5` |
| `//` | 整除 | `10 // 4` → `2` |
| `%` | 取余 | `10 % 4` → `2` |
| `**` | 幂 | `10 ** 4` → `10000` |

> **优先级**：`**` → `*` `/` `//` `%` → `+` `-`

> **浮点数精度问题**：由于计算机底层基于二进制存储与处理，二进制无法准确表示所有小数，浮点数运算可能损失精度。如 `0.1 + 10 / 4**2` 的结果可能存在极小误差。

#### 赋值运算符

| 运算符 | 描述 | 示例 |
| :--- | :--- | :--- |
| `=` | 赋值 | `num = 1 + 2` |
| `+=` | 加法赋值 | `num += 2` 等效于 `num = num + 2` |
| `-=` | 减法赋值 | `num -= 2` 等效于 `num = num - 2` |
| `*=` | 乘法赋值 | `num *= 2` 等效于 `num = num * 2` |
| `/=` | 除法赋值 | `num /= 2` 等效于 `num = num / 2` |
| `%=` | 取余赋值 | `num %= 2` 等效于 `num = num % 2` |
| `//=` | 整除赋值 | `num //= 2` 等效于 `num = num // 2` |
| `**=` | 幂赋值 | `num **= 2` 等效于 `num = num ** 2` |

#### 比较运算符

| 运算符 | 描述 | 示例 |
| :--- | :--- | :--- |
| `==` | 等于 | `100 == 100` → `True` |
| `!=` | 不等于 | `100 != 100` → `False` |
| `>` | 大于 | `100 > 100` → `False` |
| `>=` | 大于等于 | `100 >= 100` → `True` |
| `<` | 小于 | `100 < 100` → `False` |
| `<=` | 小于等于 | `100 <= 100` → `True` |

> 比较运算符返回布尔值 `True` 或 `False`。

#### 逻辑运算符

| 运算符 | 描述 | 示例 |
| :--- | :--- | :--- |
| `and` | 逻辑与（并且） | 两边都为 True 才为 True |
| `or` | 逻辑或（或者） | 任一为 True 即为 True |
| `not` | 逻辑非（取反） | `not True` → `False` |

**案例：判断数字范围**

```python
# 判断数字是否在 10-20 之间
n = int(input("请输入一个整数: "))

# and 连接 —— 两个条件同时成立
print(f"{n}在10-20之间: ", n >= 10 and n <= 20)
# 也支持链式比较
print(f"{n}在10-20之间: ", 10 <= n <= 20)

# or 连接 —— 只要有一个成立
print(f"{n}不在10-20之间: ", n < 10 or n > 20)
```

---

## 第二章 流程控制语句

### 2.1 条件判断

#### if 语句基本格式

```python
if 条件:
    条件成立时执行的代码
```

**案例：B站登录**

```python
ok_account = "18888888888"
ok_password = "666888"

account = input("请输入您的B站账号: ")
password = input("请输入您的B站密码: ")

if account == ok_account and password == ok_password:
    print("登录成功 ~")
    print("进入B站首页 ~")
```

#### if...else 语句

```python
if 条件:
    条件成立时执行的代码
else:
    条件不成立时执行的代码
```

**案例：闰年判断**

```python
year = int(input("请输入需要判定的年份: "))

# 非整百年份且能被4整除 → 闰年；整百年份必须被400整除 → 闰年
if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    print(f"{year} 是闰年")
else:
    print(f"{year} 是平年")
```

#### if...elif...else 语句

```python
if 条件1:
    条件1成立时执行的代码
elif 条件2:
    条件2成立时执行的代码
else:
    以上条件都不成立时执行的代码
```

**案例：三角形类型判断**

```python
a = int(input("请输入第一个边的边长: "))
b = int(input("请输入第二个边的边长: "))
c = int(input("请输入第三个边的边长: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print(f"{a} {b} {c} 这三个边长构成等边三角形 ~")
    elif a == b or b == c or a == c:
        print(f"{a} {b} {c} 这三个边长构成等腰三角形 ~")
    else:
        print(f"{a} {b} {c} 这三个边长构成普通三角形 ~")
else:
    print(f"{a} {b} {c} 这三个边长不能构成三角形 !!!")
```

> **注意事项**：
> - 判断条件的结果必须是布尔类型
> - 不要忘记条件后的冒号 `:`
> - 代码块需要缩进 4 个空格（按 Tab 键自动转换）
> - `elif` 可以有多个，`else` 可选
> - `pass` 是空语句，起到语法占位的作用

---

### 2.2 结构模式匹配

> Python 3.10 新增的 `match-case` 语句，类似于其他语言的 `switch-case`。

```python
match 变量:
    case 值1:
        执行代码1
    case 值2:
        执行代码2
    case _:
        以上都不匹配时执行的代码  # _ 表示通配符
```

**案例1：工作日程安排**

```python
day = input("请输入星期几(1-7): ")

match day:
    case "1":
        print("周一: 工作会议日")
    case "2":
        print("周二: 学习培训日")
    case "3":
        print("周三: 项目开发日")
    case "4":
        print("周四: 代码审查日")
    case "5":
        print("周五: 总结规划日")
    case "6" | "7":        # | 表示或，匹配多个值
        print("周末: 休息放松")
    case _:
        print("输入有误!!!")
```

**案例2：简易计算器**

```python
num1 = float(input("请输入第一个数: "))
num2 = float(input("请输入第二个数: "))
oper = input("请输入运算符(+ - * /) : ")

match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2 != 0:   # if 条件成立才匹配此 case（守卫条件）
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("操作不支持!!!")
```

---

### 2.3 循环

#### while 循环

```python
while 循环条件:
    循环体（满足条件时执行的代码）
else:
    循环正常结束后执行的代码（break 终止时不执行）
```

**案例：1-100偶数累加**

```python
total = 0
i = 1

while i <= 100:
    if i % 2 == 0:   # 偶数
        total += i
    i += 1

print(f"1-100之间的偶数的累加之和: {total}")
```

#### for 循环

```python
for 元素 in 待处理数据集:
    循环体
else:
    循环正常结束后执行的代码（break 终止时不执行）
```

#### range 语句

> 生成指定规则的数字序列。

| 用法 | 说明 | 示例 |
| :--- | :--- | :--- |
| `range(end)` | 从 0 到 end-1 | `range(5)` → 0, 1, 2, 3, 4 |
| `range(start, end)` | 从 start 到 end-1 | `range(2, 8)` → 2, 3, 4, 5, 6, 7 |
| `range(start, end, step)` | 从 start 到 end-1，步长为 step | `range(0, 10, 2)` → 0, 2, 4, 6, 8 |

**案例：1-100奇数之和**

```python
total = 0
for i in range(1, 101, 2):   # 步长为2，直接跳过偶数
    total += i
print("1-100之间的奇数累加之和: ", total)
```

**案例：100-500之间3的倍数之和**

```python
total = 0
for i in range(100, 501):
    if i % 3 == 0:
        total += i
print("100-500 之间所有3的倍数的数字之和: ", total)
```

#### 嵌套循环

```python
# 打印长方形
m = int(input("请输入长方形的长度: "))
n = int(input("请输入长方形的宽度: "))

for j in range(n):       # 控制行
    for i in range(m):   # 控制列
        print("*", end="  ")   # end="" 表示不换行
    print()                    # 换行
```

> `print()` 默认自带换行效果（`end="\n"`），设置 `end=""` 可取消换行。

**打印九九乘法表**

```python
for i in range(1, 10):        # 外层循环 - 控制行
    for j in range(1, i + 1): # 内层循环 - 控制列
        print(f"{j} x {i} = {j * i}", end="\t")
    print()
```

#### break 和 continue

| 关键字 | 作用 |
| :--- | :--- |
| `break` | 结束整个循环，跳出循环体（break跳出循环时，while/for后面的else中的代码将不会执行） |
| `continue` | 中断本次循环，直接进入下一次循环 |

> **注意**：`break` 和 `continue` 只能出现在循环中。

**案例：用户名密码登录（break + continue）**

```python
while True:
    username = input("请输入正确的用户名: ")
    password = input("请输入正确的密码: ")

    # 校验: 输入的用户名和密码不能为空
    if username == "" or password == "":
        print("输入的用户名和密码不能为空！请重新输入")
        continue   # 结束当前循环, 直接进入下一轮循环

    # 判断用户名和密码的正确性
    if username == "admin" and password == "666888":
        print("登录成功，进入B站首页~")
        break      # 跳出循环
    elif username == "zhangsan" and password == "123456":
        print("登录成功，进入B站首页~")
        break
    elif username == "taoge" and password == "888666":
        print("登录成功，进入B站首页~")
        break
    else:
        print("用户名或密码错误, 请重新输入!")
```

**案例：猜数字游戏**

```python
import random
random_num = random.randint(1, 100)   # 生成1-100的随机数

while True:
    num = int(input("请输入一个数字: "))

    if num > random_num:
        print("您输入的数字太大了!")
    elif num < random_num:
        print("您输入的数字太小了!")
    else:
        print("恭喜您, 猜对了, 666")
        break   # 跳出循环

print("随机生成的数字是: ", random_num)
```

---

## 第三章 数据存储容器

> 数据容器：一种可以容纳多份数据的数据类型，容纳的每一份数据称为一个元素。

| 容器 | 有序 | 可修改 | 支持重复 |
| :--- | :--- | :--- | :--- |
| 列表（list） | ✅ | ✅ | ✅ |
| 字符串（str） | ✅ | ❌ | ✅ |
| 元组（tuple） | ✅ | ❌ | ✅ |
| 集合（set） | ❌ | ✅ | ❌ |
| 字典（dict） | ✅ (Python 3.7+) | ✅ | 键不可重复 |

---

### 3.1 列表（list）

#### 定义与索引

```python
# 定义列表
s = [56, 90, 88, 65, 90, "A", "Hello", True]

# 正向索引（从 0 开始）
print(s[0])    # 56

# 反向索引（从 -1 开始）
print(s[-1])   # True

# 修改元素
s[5] = "ABC"
print(s)

# 删除元素
del s[6]
print(s)

# 遍历
for item in s:
    print(item)
```

> **注意**：如果指定的索引超出范围，将会报错 `list assignment index out of range`。

#### 切片

```python
# 语法：列表[开始索引:结束索引:步长]
s = ["A", "C", "H", "K", "L", "B", "D", "X", "C", "U"]

s[0:5:1]     # ["A", "C", "H", "K", "L"]
s[:5:1]      # 省略开始索引，默认为 0
s[:5:]       # 省略步长，默认为 1
s[:5]        # 最简写法
s[0:5:2]    # ["A", "H", "L"]   步长为2
s[0:-2:1]   # 使用反向索引
```

> 切片结果**不包含**结束索引对应的元素。步长为正数从前往后截取，为负数从后往前截取。

#### 常用方法

| 方法 | 说明 | 示例 |
| :--- | :--- | :--- |
| `append(元素)` | 在列表末尾添加一个元素 | `s.append(188)` |
| `insert(索引, 元素)` | 在指定索引之前插入元素 | `s.insert(2, 80)` |
| `remove(元素)` | 移除列表中第一个匹配到的元素 | `s.remove(90)` |
| `pop(索引)` | 删除指定索引的元素并返回（默认最后一个） | `s.pop(1)` |
| `sort()` | 排序（原列表改变） | `s.sort()` / `s.sort(reverse=True)` |
| `reverse()` | 反转列表 | `s.reverse()` |
| `clear()` | 清空列表 | `s.clear()` |
| `index(元素)` | 返回元素的索引 | `s.index("A")` |
| `count(元素)` | 统计元素出现次数 | `s.count("A")` |
| `copy()` | 浅拷贝列表 | `new_list = s.copy()` |

**案例1：输入10个数字，排序后输出最小值、最大值、平均值**

```python
num_list = []
for i in range(10):
    num = int(input("请输入一个有效的数字: "))
    num_list.append(num)

print("数字列表: ", num_list)

num_list.sort()
print("排序后的数字列表: ", num_list)

print("最小值: ", num_list[0])
print("最大值: ", num_list[-1])
print("平均值: ", sum(num_list) / len(num_list))
```

**案例2：合并两个列表并去重**

```python
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# 合并方式一：循环追加
for num in num_list2:
    num_list1.append(num)

# 合并方式二：解包
num_list = [*num_list1, *num_list2]

# 合并方式三：+ 号
num_list = num_list1 + num_list2

# 去重
new_list = []
for num in num_list:
    if num not in new_list:   # not in 判断元素不在列表中
        new_list.append(num)
print("去重后的列表: ", new_list)
```

#### 列表推导式

```python
# 语法格式1：[要插入的值 for 变量 in 序列]
# 语法格式2：[要插入的值 for 变量 in 序列 if 条件]

# 生成1-20的平方列表
num_list = [i**2 for i in range(1, 21)]

# 从数字列表中提取所有偶数，并计算其平方
num_list = [12, 32, 45, 77, 80, 92, 33, 57, 97, 98, 110, 111, 122]
new_list = [i**2 for i in num_list if i % 2 == 0]
```

---

### 3.2 字符串（str）

> 字符串是**不可变类型**（无法修改），具有有序性、可迭代性。所有操作都返回新字符串，原字符串不变。

#### 基本操作

```python
s = "Hello-Python"

# 索引
print(s[4])      # 正向索引 → o
print(s[-8])     # 反向索引 → o

# 遍历
for i in s:
    print(i)

# 切片
print(s[0:5:1])   # Hello
print(s[6::1])    # Python
print(s[::-1])    # nohtyP-olleH  (反转)
print(s[-1:-7:-1])# nohtyP  (负步长从后往前截取)
```

#### 常用方法

| 方法 | 说明 | 示例 |
| :--- | :--- | :--- |
| `find(子串)` | 查找子串第一次出现的索引位置，找不到返回 -1 | `s.find("-")` |
| `count(子串)` | 统计子串出现次数 | `s.count("o")` |
| `upper()` | 转为大写 | `s.upper()` |
| `lower()` | 转为小写 | `s.lower()` |
| `split(分隔符)` | 按指定字符串切割，返回列表 | `s.split("-")` |
| `strip()` | 去除两端空白字符 | `s.strip()` |
| `replace(旧, 新)` | 替换字符串中的指定子串 | `s.replace("-", "_")` |
| `startswith(前缀)` | 判断是否以指定前缀开头 | `s.startswith("Hello")` |
| `endswith(后缀)` | 判断是否以指定后缀结尾 | `s.endswith("Python")` |
| `zfill(宽度)` | 左侧填充 0 到指定宽度 | `"5".zfill(3)` → `"005"` |

**案例：邮箱格式验证**

```python
mail = input("请输入邮箱: ")

# 方式一：count 统计
if mail.count("@") == 1 and mail.count(".") >= 1:
    print(f"{mail} 是合法的邮箱")
else:
    print(f"{mail} 是非法的邮箱")

# 方式二：in 运算符（判断子串是否存在）
if mail.count("@") == 1 and "." in mail:
    print(f"{mail} 是合法的邮箱")
else:
    print(f"{mail} 是非法的邮箱")
```

---

### 3.3 元组（tuple）

#### 定义与特点

```python
# 定义元组
t1 = (80, 95, 78, 50, 76, 80, 85, 20)

# 索引访问
print(t1[0])    # 80
print(t1[-1])   # 20

# 切片
print(t1[0:5:1])

# 只有一个元素时，必须加逗号
t2 = ()          # 空元组
t3 = (100,)     # 单元素元组，注意逗号不能省略
```

- 元组是**不可变**的，定义后不能修改、添加、删除元素
- 支持索引和切片（与列表相同）
- 元素可重复、有序

#### 常用方法

| 方法 | 说明 | 示例 |
| :--- | :--- | :--- |
| `count(元素)` | 统计元素出现次数 | `t1.count(80)` |
| `index(元素)` | 获取元素的索引 | `t1.index(80)` |

#### 组包与解包

```python
# 组包：将多个值合并到一个容器
t = 5, 7, 9, 10, 2, 23, 12    # 省略括号也可以

# 基础解包：变量数量与元素个数一致
a, b, c, d, e, f, g = t

# 扩展解包：* 收集剩余的所有元素，封装到列表中
first, second, *other, last = t
print(first)    # 5
print(other)    # [9, 10, 2, 23]
print(last)     # 12

*other, last2, last1 = t
print(other)    # [5, 7, 9, 10, 2]
print(last2)    # 23
print(last1)    # 12
```

**案例：变量交换（组包与解包）**

```python
a = 10
b = 20
a, b = b, a    # 先组包 (b, a)，再解包赋值
print(a)       # 20
print(b)       # 10
```

**案例：学生成绩统计**

```python
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
)

# 1. 计算每个学生的总分、平均分 —— 使用元组解包
for id, name, chinese, math, english in students:
    total = chinese + math + english
    avg = total / 3
    print(f"{id} \t {name} \t {chinese} \t {math} \t {english} \t {total} \t {avg:.1f}")

# 2. 统计各科成绩的最低分、最高分、平均分
chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]

print(f"语文最低分: {min(chinese_scores)}, 最高分: {max(chinese_scores)}, 平均分: {sum(chinese_scores)/len(chinese_scores)}")

# 3. 查找成绩优秀（平均分大于90）的学生
for id, name, chinese, math, english in students:
    total = chinese + math + english
    avg = total / 3
    if avg > 90:
        print(f"学号: {id}, 姓名: {name}, 平均分: {avg:.1f}")
```

---

### 3.4 集合（set）

#### 定义与特点

```python
# 定义集合
s1 = {5, 3, 2, 0, 9, 12, 43, 64, 22, 5, 0}
print(s1)   # 自动去重且无序

# 定义空集合（注意：{} 是空字典）
s2 = set()   # ✅ 空集合
# s2 = {}    # ❌ 这是空字典
```

- 集合中的元素**不可重复**（自动去重）
- 集合是**无序**的，不支持索引访问
- 集合是**可变**的

#### 常用方法

| 方法 | 说明 |
| :--- | :--- |
| `add(元素)` | 添加元素 |
| `remove(元素)` | 删除元素（不存在会报错） |
| `discard(元素)` | 删除元素（不存在不报错） |
| `pop()` | 随机删除一个元素 |
| `clear()` | 清空集合 |

#### 集合运算

| 运算 | 方法 | 运算符 |
| :--- | :--- | :--- |
| 交集 | `s2.intersection(s3)` | `s2 & s3` |
| 并集 | `s2.union(s3)` | `s2 \| s3` |
| 差集 | `s2.difference(s3)` | `s2 - s3` |

**案例：选修课统计**

```python
football_set = {"王林", "曾牛", "韩立", "厉飞雨"}
basketball_set = {"张铁", "王林", "曾牛", "韩立", "天运子"}
art_set = {"韩立", "虎咆", "姜老道", "紫灵"}

# 1. 交集 —— 同时选修了足球和篮球的学生
print(football_set & basketball_set)

# 2. 差集 —— 选修了足球但没选篮球的学生
print(football_set - basketball_set)

# 3. 并集 —— 所有选课学生名单
print(football_set | basketball_set | art_set)

# 4. 集合推导式 —— 语法: {要往集合中添加的数据 for s in set1 if 条件}
fb_set = {s for s in football_set if s not in basketball_set}
```

---

### 3.5 字典（dict）

#### 定义与访问

```python
# 定义字典
dict1 = {"王林": 670, "李慕婉": 608, "韩立": 688}

# 访问值
dict1["李慕婉"]            # 获取 → 608
dict1["李慕婉"] = 688      # 修改（key存在就是修改）
dict1["涛哥"] = 550         # 添加（key不存在就是添加）

# 字典的 key 必须是不可变类型（str, int, float, tuple），不能是 list、set、dict
dict2 = {0: 670, 1.5: 608, (1, 2): 580}
```

#### 常用方法

| 方法 | 说明 |
| :--- | :--- |
| `keys()` | 返回所有键 |
| `values()` | 返回所有值 |
| `items()` | 返回所有键值对 |
| `pop(键)` | 删除指定键值对并返回值 |
| `get(键, 默认值)` | 获取值，键不存在时返回默认值 |
| `update(字典)` | 合并字典 |
| `clear()` | 清空字典 |

#### 遍历字典

```python
dict1 = {"王林": 670, "李慕婉": 608, "韩立": 688}

# 方式一：遍历 keys
for k in dict1.keys():
    print(f"{k} : {dict1[k]}")

# 方式二：遍历 items
for k, v in dict1.items():
    print(f"{k} : {v}")
```

#### 字典推导式

```python
# 键值互换
old = {"a": 1, "b": 2}
new = {v: k for k, v in old.items()}  # {1: "a", 2: "b"}
```

**案例：购物车管理系统**

```python
shopping_cart = {}

while True:
    print("1.添加购物车  2.修改购物车  3.删除购物车  4.查询购物车  5.退出")
    choice = input("请选择要执行的操作(1-5): ")

    match choice:
        case "1":  # 添加购物车
            goods_name = input("请输入商品名称: ")
            goods_price = float(input("请输入商品价格: "))
            goods_num = int(input("请输入商品数量: "))
            if goods_name in shopping_cart:
                print("该商品已存在, 请重新选择 ~")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品添加完毕 ~")
        case "2":  # 修改购物车
            goods_name = input("请输入要修改的商品名称: ")
            if goods_name not in shopping_cart:
                print("该商品不存在, 请重新选择 ~")
                continue
            goods_price = float(input("请输入商品最新的价格: "))
            goods_num = int(input("请输入商品最新的数量: "))
            shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
            print("商品修改完毕 ~")
        case "3":  # 删除购物车
            goods_name = input("请输入要删除的商品名称: ")
            if goods_name not in shopping_cart:
                print("该商品不存在, 请重新选择 ~")
            else:
                del shopping_cart[goods_name]
                print("商品删除完毕 ~")
        case "4":  # 查询购物车
            for goods_name in shopping_cart.keys():
                goods_info = shopping_cart[goods_name]
                print(f"商品名称: {goods_name}, 价格: {goods_info['price']}, 数量: {goods_info['num']}")
        case "5":
            print("Bye ~")
            break
        case _:
            print("非法操作, 不支持!!!")
```

---

### 3.6 容器通用操作

| 函数 | 说明 |
| :--- | :--- |
| `len(容器)` | 返回元素个数 |
| `max(容器)` | 返回最大元素 |
| `min(容器)` | 返回最小元素 |
| `sum(容器)` | 求和（数值类型） |
| `sorted(容器)` | 排序，返回列表 |
| `reversed(容器)` | 反转，返回迭代器 |
| `enumerate(容器)` | 返回带索引的枚举对象 |
| `in` / `not in` | 判断元素是否在容器中 |

---

## 第四章 函数

### 4.1 函数基础

#### 函数定义与调用

```python
# 定义函数
def 函数名(参数列表):
    函数体
    return 返回值

# 调用函数
函数名(参数)
```

> **注意事项**：
> - 函数必须**先定义，后调用**
> - 函数定义时不会执行，调用时才执行
> - 通过缩进描述代码的归属关系

#### 参数与返回值

```python
# 计算圆的面积
def circle_area(r):
    area = 3.14 * r ** 2
    return area

area = circle_area(10)
print(area)   # 314.0

# 计算长方形面积（带说明文档）
def rectangle_area(l, w):
    """
    根据长方形的长度和宽度, 计算长方形的面积
    :param l: 长度
    :param w: 宽度
    :return: 长方形的面积
    """
    area = l * w
    return area

print(rectangle_area(20, 10))   # 200

# 多个返回值 —— 封装为元组
def circle_area_len(r):
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)

al = circle_area_len(10)
print(al)          # (314.0, 62.8)
print(type(al))    # <class 'tuple'>

# 元组解包接收多个返回值
area, length = circle_area_len(10)
print(area)        # 314.0
print(length)      # 62.8
```

- **形参**：函数定义时括号里的参数（局部变量）
- **实参**：函数调用时传入的参数
- **return**：返回结果并结束函数，没有 return 则返回 `None`
- 函数可以有**多个返回值**，多个值会封装为元组，可通过解包获取

#### 函数说明文档（Docstring）

```python
def circle_area_len(r):
    """
    该函数用于根据圆的半径, 计算圆的面积和圆的周长
    :param r: 圆的半径
    :return: 圆的面积, 圆的周长
    """
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)
```

> 查看说明文档：`help(函数名)` 或鼠标悬浮在函数上。

#### 函数的嵌套调用

> 在一个函数中调用另一个函数。遵循**栈结构**（LIFO，后进先出）。

```python
def function_a():
    print("a ... before")
    function_b()
    print("a ... after")

def function_b():
    print("b ... before")
    function_c()
    print("b ... after")

def function_c():
    print("c ...")

function_a()
# 输出顺序: a...before → b...before → c... → b...after → a...after
```

#### 函数基础案例

```python
# 案例1: 计算三角形面积
def triangle_area(b, h):
    """
    根据传入的底和高计算三角形面积
    :param b: 底长
    :param h: 高
    :return: 三角形面积
    """
    return b * h / 2

print("底长为 30, 高度为 20 的三角形面积: ", triangle_area(30, 20))

# 案例2: 统计字符串中元音字母的个数
def count_aeiou(s):
    """
    统计字符串中元音字母的个数
    :param s: 字符串
    :return: 元音字母的个数
    """
    num = 0
    for w in s:
        if w in "aeiouAEIOU":
            num += 1
    return num

print(count_aeiou("Hello Python Hello World OK"))   # 7

# 案例3: 计算成绩的最高分、最低分、平均分
def calc_score(score_list):
    max_s = max(score_list)
    min_s = min(score_list)
    avg_s = round(sum(score_list) / len(score_list), 1)
    return max_s, min_s, avg_s

s_list = [589, 609, 605, 643, 677, 455, 477, 489, 503]
max_score, min_score, avg_score = calc_score(s_list)
print("最高分: ", max_score)
print("最低分: ", min_score)
print("平均分: ", avg_score)
```

---

### 4.2 函数进阶

#### 多种参数类型

| 参数类型 | 说明 | 示例 |
| :--- | :--- | :--- |
| 位置参数 | 按位置顺序传递 | `reg_stu("张三", 18, "男", "北京")` |
| 关键字参数 | 按参数名传递 | `reg_stu(name="王林", age=28, gender="男", city="北京")` |
| 混合传参 | 位置参数在前，关键字参数在后 | `reg_stu("李慕婉", 20, gender="女", city="北京")` |
| 默认参数 | 定义时指定默认值 | `def func(a, b=10):` |
| 可变位置参数 `*args` | 接收多余的位置参数，封装为元组 | `def func(*args):` |
| 可变关键字参数 `**kwargs` | 接收多余的关键字参数，封装为字典 | `def func(**kwargs):` |

```python
# 默认参数
def reg_stu(name, age, gender="男", city="北京"):
    print(f"注册成功, 姓名: {name}, 年龄: {age}, 性别: {gender}, 城市: {city}")

reg_stu("王林", 20)                          # 使用默认值
reg_stu("李慕婉", 18, "女")                   # 覆盖 gender 默认值
reg_stu("韩立", 22, city="上海")               # 用关键字参数跳过 gender

# 不定长参数
def calc_data(*args, **kwargs):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    if kwargs.get("round") is not None:
        avg_data = round(avg_data, kwargs.get("round"))
    if kwargs.get("print"):
        print(f"最小值: {min_data}, 最大值: {max_data}, 平均值:{avg_data}")

    return min_data, max_data, avg_data

print(calc_data(2, 7, 9, 10, 45, round=3, print=True))
```

#### 匿名函数（lambda）

```python
# 语法：lambda 参数列表: 表达式
out_line = lambda : print("--------------------------------------")
add = lambda x, y: x + y
print(add(100, 200))   # 300
```

> lambda 只能写单个表达式，不能写复杂的代码块。

**lambda 典型应用场景：排序**

```python
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
data_list.sort(key=lambda item: len(item))   # 按字符串长度排序
print(data_list)
```

#### 递归调用

> 递归：在函数中自己调用自己的情况。一定得有终结点。

```python
# 计算 n 的阶乘
def jc(n):
    if n == 1:        # 终结点
        return 1
    else:
        return n * jc(n - 1)

result = jc(10)
print(result)   # 3628800
```

#### 变量作用域

| 作用域 | 说明 |
| :--- | :--- |
| 局部变量 | 定义在函数内部的变量，只能在函数内部使用 |
| 全局变量 | 定义在函数外部的变量，所有函数都可以访问 |

```python
count = 0  # 全局变量

def increment():
    global count  # 声明使用全局变量
    count += 1
```

> 在函数内修改全局变量，需要使用 `global` 关键字声明。

#### 函数作为参数传递

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calc(x, y, oper):
    return oper(x, y)     # 函数作为参数传递

print(calc(10, 20, multiply))   # 200
```

#### 类型注解

```python
# 变量类型注解
a: int = 695
score: float = 98.5
hobby: str = "Python"
flag: bool = True
pic: None = None

# 容器类型注解
names: list[str | int] = ["A", "C", "E"]          # 联合类型
phones: set[str] = {"13309091111", "15209101902"}
options: dict[str, int] = {"count": 2, "total": 10}
goods: tuple[str, int, int] = ("手机", 6999, 1)

# 函数类型注解
def circle_area_len(r: float) -> tuple[float, float]:
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)

def calc_order_cost(*args: tuple[str, float, int], coupon: int = 0, score: int = 0, express: float = 0.0) -> float:
    """
    根据商品信息、优惠、运费计算订单总金额
    :param args: 商品信息（商品名、价格、数量）
    :param coupon: 优惠券
    :param score: 积分
    :param express: 运费
    :return: 订单的总金额
    """
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)

    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100

    total_cost += express
    return total_cost

total = calc_order_cost(("鼠标", 88.5, 2), ("键盘", 388, 1), ("手机", 6999, 1))
print(total)
```

> **注意**：Python 是动态类型语言，类型注解只是提示，不是强制约束。

---

## 第五章 模块

### 5.1 模块导入

> 模块：一个 `.py` 文件就是一个模块，可以定义变量、函数、类及可执行代码。

| 导入形式 | 代码样例 | 调用方式 |
| :--- | :--- | :--- |
| `import 模块名` | `import random` | `random.randint(10, 100)` |
| `import 模块名 as 别名` | `import random as rd` | `rd.randint(10, 100)` |
| `from 模块名 import 功能名` | `from random import randint` | `randint(10, 100)` |
| `from 模块名 import 功能名 as 别名` | `from random import randint as rint` | `rint(10, 100)` |
| `from 模块名 import *` | `from random import *` | `randint(10, 100)` |

> 导入语句一般写在 `.py` 文件的开头。

---

### 5.2 自定义模块

#### `__name__` 变量

- 当模块**直接运行**时：`__name__` 的值为 `"__main__"`
- 当模块**被导入**时：`__name__` 等于模块的文件名（不含 `.py` 后缀）

```python
if __name__ == "__main__":
    # 仅在直接运行时执行，被导入时不执行
    pass
```

#### `__all__` 变量

- 控制 `from 模块名 import *` 时导入哪些功能
- 不影响直接导入具体功能的语句

```python
__all__ = ["func1", "func2"]  # 只允许导入 func1 和 func2
```

---

### 5.3 包（package）

> 包：本质上就是一个文件夹，包含若干 Python 模块和一个 `__init__.py` 文件。

- `__init__.py` 标识该文件夹是一个包（而非普通文件夹）
- `__init__.py` 中的 `__all__` 控制 `from 包名 import *` 时导入的模块列表

| 导入形式 | 代码样例 |
| :--- | :--- |
| `import 包名.模块名` | `import utils.my_fun` |
| `from 包名 import 模块名` | `from utils import my_fun` |
| `from 包名 import *` | `from utils import *` |
| `from 包名.模块名 import 功能名` | `from utils.my_fun import log_separator1` |
| `from 包名.模块名 import *` | `from utils.my_fun import *` |

**导入示例**：

```python
# 方式一：import 包名.模块名
import utils.my_fun
utils.my_fun.log_separator1()

# 方式二：from 包名 import 模块名
from utils import my_fun
my_fun.log_separator1()

# 方式三：from 包名.模块名 import 功能名
from utils.my_fun import log_separator1, log_separator3
log_separator1()
log_separator3()
```

---

## 第六章 面向对象基础

### 6.1 面向对象编程思想

| 思想 | 核心 | 关注点 |
| :--- | :--- | :--- |
| 面向过程 | 将需求分解为一系列步骤，依次执行 | 流程、步骤 |
| 面向对象 | 将事物抽象为对象，通过对象协作完成任务 | 谁来帮我做这件事 |

> 面向对象编程的基本单元是**对象**，对象包含**属性**（特征）和**方法**（功能/行为）。

---

### 6.2 类与对象

- **类**：描述一组具有相同属性和方法的模板
- **对象**：基于类创建的实例（实例化）

#### 定义类

```python
# 方式一：动态添加属性（不推荐）
class Car:
    pass

c1 = Car()
c1.color = "red"
c1.brand = "BMW"
c1.name = "X5"
c1.price = 500000
print(c1.__dict__)   # 将对象中的所有属性以字典形式输出

# 方式二（推荐）：通过 __init__ 定义实例属性
class Car:
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象初始化完毕, 对象属性已经添加完毕 .")

c1 = Car("红色", "BMW", "X7", 800000)
print(c1.__dict__)
```

> - 类名使用**大驼峰命名法**（如 `UserInfo`、`UserAccount`）
> - `__init__`：初始化方法，创建对象时自动调用
> - `self`：表示当前实例对象本身
> - 定义在类外面的叫**函数**，定义在类中的叫**方法**

---

### 6.3 实例方法

```python
class Car:
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price

    # 定义实例方法
    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶中....")

    def total_cost(self, discount, rate=0.1):
        """
        计算提车的总费用（车价 + 税费）
        :param discount: 折扣
        :param rate: 税率
        :return: 提车的总费用
        """
        total_cost = self.price * discount + rate * self.price
        return total_cost

c1 = Car("红色", "BMW", "X7", 800000)
c1.running()                          # BMW X7 正在高速行驶中....
print(c1.total_cost(0.9, 0.1))        # 提车总费用
print(c1.total_cost(0.9))             # 使用默认税率
```

---

### 6.4 魔法方法

| 方法 | 说明 | 触发时机 |
| :--- | :--- | :--- |
| `__init__(self)` | 初始化方法 | 创建对象时自动调用 |
| `__str__(self)` | 字符串描述 | `print(对象)` 时自动调用 |
| `__eq__(self, other)` | 判断相等 | `对象1 == 对象2` 时调用 |
| `__lt__(self, other)` | 判断小于 | `对象1 < 对象2` 时调用 |
| `__le__(self, other)` | 判断小于等于 | `对象1 <= 对象2` 时调用 |

```python
class Car:
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price

    def __str__(self):
        return f"{self.color} {self.brand} {self.name} {self.price}"

    def __eq__(self, other):
        return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

c1 = Car("白色", "BYD", "汉", 180000)
c2 = Car("白色", "BYD", "汉", 180001)

print(c1)           # 白色 BYD 汉 180000  （自动调用 __str__）
print(c1 == c2)     # False  （自动调用 __eq__）
print(c1 > c2)      # False  （自动调用 __lt__，> 是 __lt__ 取反）
```

---

### 6.5 实例属性与类属性

| 类型 | 归属 | 访问方式 | 特点 |
| :--- | :--- | :--- | :--- |
| 实例属性 | 每个具体对象 | `对象名.属性` | 各对象独立，互不影响 |
| 类属性 | 类本身 | `类名.属性` 或 `对象名.属性` | 所有实例共享 |

```python
class Car:
    wheel = 4       # 类属性：所有车都有 4 个轮子
    tax_rate = 0.1  # 类属性：购置税率

    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color   # 实例属性
        self.name = c_name     # 实例属性
        self.price = c_price   # 实例属性

c1 = Car("白色", "BYD", "汉", 180000)
print(c1.brand)      # 通过实例对象访问实例属性
print(c1.wheel)      # 通过实例对象访问类属性（先查实例属性，不存在再查类属性）
print(Car.wheel)     # 通过类名访问类属性（推荐）
```

> 查找顺序：先查找实例属性，实例属性不存在时再查找类属性。

---

### 6.6 异常处理

#### 什么是异常

> 异常就是程序运行过程中出现的错误，会中断程序的正常执行流程。

常见异常类型：

| 异常类型 | 说明 |
| :--- | :--- |
| `NameError` | 使用未定义的变量 |
| `TypeError` | 类型错误 |
| `IndexError` | 索引越界 |
| `KeyError` | 字典键不存在 |
| `ValueError` | 值错误 |
| `ZeroDivisionError` | 除零错误 |
| `AttributeError` | 属性不存在 |

#### 捕获异常

```python
try:
    # 可能出现异常的代码
    print(my_name)
except NameError as e:
    # 捕获指定类型的异常
    print("名字不存在, 请检查变量或函数名字, 异常信息: ", e)
except ZeroDivisionError as e:
    print("0不能做被除数, 异常信息: ", e)
except IndexError as e:
    print("索引错误, 异常信息: ", e)
except Exception as e:
    # 捕获所有异常
    print("程序运行出错了, 请联系管理员, 错误信息: ", e)
finally:
    # 无论程序是否正常运行, finally代码块中的代码都会运行
    print("资源释放 ~")
```

- `try`：包裹可能出错的代码
- `except`：捕获异常并处理，可指定多个异常类型，`Exception` 可捕获所有异常
- `finally`：可选，无论是否异常都会执行（常用于资源释放）

#### 异常的传递

> 异常在函数调用中会层层上报，直到有人处理它，或者程序崩溃。

```python
def fun1():
    print("fun1 ... running ...")
    fun2()

def fun2():
    print("fun2 ... running ...")
    fun3()

def fun3():
    print("fun3 ... running ...")
    print(my_color)   # 触发 NameError，异常会依次传递 fun3 → fun2 → fun1 → 主程序

if __name__ == '__main__':
    try:
        fun1()
    except Exception as e:
        print("程序运行出错了, 请联系管理员, 错误信息: ", e)
```

---

### 综合案例：教务管理系统（面向对象 + 异常处理）

```python
# 学生类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名: {self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分：{self.chinese + self.math + self.english}"

    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

# 教务管理系统类
class EduManagement:
    system_version = "1.0"       # 类属性
    system_name = "教务管理系统"   # 类属性

    def __init__(self):
        self.student_list = []   # 实例属性

    def add_student(self):
        name = input("请输入学生姓名: ")
        for s in self.student_list:
            if s.name == name:
                print("该学生已经存在, 添加失败!")
                return
        chinese = int(input("请输入学生语文成绩: "))
        math = int(input("请输入学生数学成绩: "))
        english = int(input("请输入学生英语成绩: "))
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name, chinese, math, english)
            self.student_list.append(stu)
            print("学生信息添加成功 ~")
        else:
            print("各科成绩必须得在 0 - 100 之间 !")

    def update_student(self):
        name = input("请输入要修改的学生姓名: ")
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩: {s}")
                chinese = int(input("请输入修改后的语文成绩: "))
                math = int(input("请输入修改后的数学成绩: "))
                english = int(input("请输入修改后的英语成绩: "))
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese, math, english)
                    print("成绩修改成功 ~")
                    return
                else:
                    print("各科成绩必须得在 0 - 100 之间 !")
                    return
        print("未找到该学生, 修改失败 !")

    def delete_student(self):
        name = input("请输入要删除的学生姓名: ")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功~")
                return
        print("未找到该学生, 删除失败 !")

    def query_student(self):
        name = input("请输入要查询的学生姓名: ")
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息: {s}")
                return
        print("未找到该学生 !")

    def list_student(self):
        for s in self.student_list:
            print(s)

    def run(self):
        print(f"欢迎使用教务管理系统 V{EduManagement.system_version}")
        while True:
            print("1.添加学生  2.修改学生  3.删除学生  4.查询指定学生  5.查询所有学生  6.退出系统")
            choice = input("请选择要执行的操作, 输入1-6: ")
            try:
                match choice:
                    case "1": self.add_student()
                    case "2": self.update_student()
                    case "3": self.delete_student()
                    case "4": self.query_student()
                    case "5": self.list_student()
                    case "6":
                        print("Bye ~")
                        break
                    case _:
                        print("输入错误, 请选择1-6之间的菜单功能!")
            except ValueError:
                print("输入的数据有问题, 请检查, 然后重新输入 !!!")
            except Exception:
                print("程序运行出错了, 请重新选择 ~")

if __name__ == '__main__':
    edu_management = EduManagement()
    edu_management.run()
```

---

> 📌 **学习建议**：编程重在实践，每学一个知识点都要动手写代码验证，才能真正掌握！
