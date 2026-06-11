#csv操作 - 方式1--原始操作

# with open('csv_data/data.csv', 'w', encoding='utf-8', newline='') as f:
#     f.write("name,age,sex\n")
#     f.write("小王,18,男,女\n")
#     f.write("小张,19,女\n")
#     f.write("小李,20,男\n")
#

# 读
with open('csv_data/data.csv', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())

# Python 在写入文件时会将 \n 转换为操作系统默认的换行符：
# Windows: \r\n
# Linux/Mac: \n
# 当设置 newline='' 时，Python 不会进行任何转换，写入什么就保存什么。
# csv操作 - 方式2--csv
import csv
with open('csv_data/data02.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f,fieldnames=["name", "age", "sex"])
    writer.writeheader()
    writer.writerow({"name": "小王", "age": 18, "sex": "男"})
    writer.writerow({"name": "小张", "age": 19, "sex": "女"})
    writer.writerow({"name": "小李", "age": 20, "sex": "男"})
    writer.writerow({"name": "小王", "age": 18, "sex": "男"})

# 读
with open('csv_data/data02.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)