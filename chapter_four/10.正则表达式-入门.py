import re


# 一串字符，包含手机号和QQ号
msg = "13888867888我的手机号是: , 另一个手机号是13888857888 QQ号是: 123456789"
msg2 = "我的手机号是: 13888887888, 另一个手机号是13888857888 QQ号是: 123456789"

#1. match -> 从字符串的开头匹配
result = re.match(r"1[3-9]\d{9}", msg)
# result 不为 None
if result:
    print(result.group()) # 返回匹配的字符串
    print(result.span()) # 返回匹配的起始位置和结束位置
    print(result.start()) # 返回匹配的起始位置
    print(result.end()) # 返回匹配的结束位置
# result 为 None
else:
    print("没有匹配到手机号")

# 2. search -> 从字符串的任意位置匹配
result2 = re.search(r"1[3-9]\d{9}", msg2)
if result2:
    print(result2.group()) # 匹配到的字符串
    print(result2.span()) # 匹配到的起始位置和结束位置
    print(result2.start()) # 匹配到的起始位置
    print(result2.end()) # 匹配到的结束位置
else:
    print("没有匹配到手机号")

# 3. findall -> 返回所有匹配的字符串(列表)
result3 = re.findall(r"1[3-9]\d{9}", msg2)
if result3:
    print(result3) # 所有匹配的字符串
    for item in result3:
        print(item)
else:
    print("没有匹配到手机号")

movie_duration = "1h 32m"
h_ref  = re.search(r"(\d+)h",movie_duration)
print(h_ref.group())
print(h_ref.group(1))