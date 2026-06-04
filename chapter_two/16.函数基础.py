# 函数定义
def out_line():
    print("函数定义")

# 函数调用
out_line()

"""
2.函数使用注意事项
    1. 函数必须先定义后使用, 否则会报错: NameError: name '函数名' is not defined
    2. 函数定义后i，并不会执行，只有在函数调用时才会执行
    3. 函数中通过缩进来描述归属关系

"""


# 函数的参数与返回值
# # 函数1: 计算圆的面积 -- 半径
# def circle_area(r):
#     area = 3.14 * r ** 2
#     return area
#
# area = circle_area(10)
# print(area)


# 函数2: 计算长方形的面积 -- 长, 宽
# def rectangle_area(l,w):
#     """
#     根据长方形的长度和宽度, 计算长方形的面积
#     :param l: 长度
#     :param w: 宽度
#     :return: 长方形的面积
#     """
#     area = l * w
#     return area
#
# # help(rectangle_area)
# print(rectangle_area(20, 10))
#
#
# # 函数3: 计算圆的面积, 周长 -- 半径 ----> 如果返回值有多个, 多个返回值之间逗号分隔 ---> 多个返回值会封装到元组之中
def circle_area_len(r):
    """"
    根据半径, 计算圆的面积和周长
    :param r: 半径
    :return: 圆的面积和周长
    """
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)

al = circle_area_len(10)
print(al)
print(type(al))
#
# area, length = circle_area_len(10) # 解包
# print(area)
# print(length)


# 函数的嵌套调用
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

print("函数调用完毕 ~")