import requests
from lxml import html


# 读取html文件
with open("resources/仙逆人物志.html", "r", encoding="utf-8") as f:
    html_content = f.read()

    # 解析html文本，将其转换为一个文档对象
    document = html.fromstring(html_content)

    # 解析表头 -xpah 语法
    th_list = document.xpath("//table/thead/tr/th/text()")
    print(th_list)
    #
    # # 解析表内容 -xpah 语法
    # # 获取第一行数据
    # td_list = document.xpath("//table/tbody/tr[1]/td/text()")
    # print(td_list)

    # 获取所有行数据
    tr_list = document.xpath("//table/tbody/tr")
    for tr in tr_list:
        td_list = tr.xpath("./td/text()")
        print(td_list)