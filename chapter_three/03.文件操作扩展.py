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

# with open(r"D:\python_project\py_project01\chapter_three\resources\静夜思.txt","r",encoding="utf-8") as f:
#     content = f.read()
#     print(content)


# a: 追加
with open("resources/静夜思.txt", "a", encoding="utf-8") as f:
    # 2. 写入文件内容
    f.write("静夜思(李白)\n\n")
    f.write("窗前明月光，\n")
    f.write("疑是地上霜。\n")
    f.write("举头望明月，\n")
    f.write("低头思故乡。\n")
    f.write("程序结束")