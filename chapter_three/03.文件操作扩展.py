# 读文件
"""
    路径写法
        相对路径: 从当前文件所在目录开始查找
        . : 当面目录 ----》 ./resources/静夜思.txt   ./可以省略
        ..: 上一级目录
    绝对路径:
      方式1:  D:\\python_project\\py_project01\\chapter_three\\resources\\静夜思.txt
      方式2：D:/python_project/py_project01/chapter_three/resources/静夜思.txt
      方式3：r"D:\python_project\py_project01\chapter_three\resources\静夜思.txt"
"""

with open(r"D:\python_project\py_project01\chapter_three\resources\静夜思.txt","r",encoding="utf-8") as f:
    content = f.read()
    print(content)