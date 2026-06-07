import json

# 写入json数据文件
# user = {
#     "name":"胡歌",
#     "age":18,
#     "gender":"男",
#     "hobbies":["reading","swimming"]
# }

# with open("resources/user.json","w",encoding="utf-8") as f:
#     # ensure_asciiL: 默认True,确保所有输出的数据都是ascii编码（非ascii编码会进行转义）
#     # indent: 会在输出的json数据中添加缩进（格式化）
#     json.dump(user,f,ensure_ascii=False,indent=2)

# 读取json数据文件
with open("resources/user.json","r",encoding="utf-8") as f:
   user = json.load(f)
   print(user)
   print(type(user))

# 读取json文件





   
   