import streamlit as st
from openai import OpenAI
import os
# 设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",  # 页面标题
    page_icon="🤖",  # 页面图标，可以是emoji表情或者图片
    layout="wide",  # 页面布局，centered表示居中，wide表示
    initial_sidebar_state="expanded",  # 侧边栏的初始状态，expanded表示展开，collapsed表示收起
    menu_items={
        "Get Help": "https://docs.streamlit.io/",
        "Report a bug": "https://www.streamlit.io/bug",
        "About": "Streamlit是一个开源的Python库，旨在帮助开发者快速构建和部署交互式数据应用程序。它提供了简单易用的API，使得创建数据可视化、机器学习模型展示和数据分析工具变得非常方便。通过Streamlit，开发者可以专注于数据和逻辑，而不需要担心前端开发的复杂性，从而加速了数据应用的开发过程。"
    }
)

# 大标题
st.title("AI智能伴侣")

# logo
st.logo("./resource/logo.png")

# 输入框
prompt = st.chat_input("请输入你的问题: ", key="chat_input")
if prompt:
    st.chat_message("user").write(prompt)
    print("调用了AI大模型：提示词是：", prompt)