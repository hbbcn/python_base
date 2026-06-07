import streamlit as st
from openai import OpenAI
import os

print("----------> 重新执行此文件 , 渲染展示页面")

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


# 初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 展示历史消息
for message in st.session_state.messages:
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])
    st.chat_message(message["role"]).write(message["content"])

print({"role": "system", "content": "你是一名非常可爱的AI助理, 你的名字叫小甜甜, 请你使用温柔可爱的语气回答用户的问题。"},
                    *st.session_state.messages)
# 创建OpenAI客户端
client = OpenAI(
    api_key = os.getenv("MOONSHOT_API_KEY"),
    base_url = "https://api.moonshot.cn/v1",
)

history : list[dict] = [
    {"role": "system", "content": "你是一名非常可爱的AI助理, 你的名字叫小甜甜, 请你使用温柔可爱的语气回答用户的问题。"}
]




# logo
st.logo("resources/logo.png")

# 输入框
prompt = st.chat_input("请输入你的问题: ", key="chat_input")
if prompt:
    st.chat_message("user").write(prompt)
    print("------->调用了AI大模型：提示词是：", prompt)
    # 保存输入的消息
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 调用大模型
    # history.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model = "kimi-k2.6",
        messages = [{"role": "system", "content": "你是一名非常可爱的AI助理, 你的名字叫小甜甜, 请你使用温柔可爱的语气回答用户的问题。"},
                    *st.session_state.messages],
        stream = True
    )
    # result = response.choices[0].message.reasoning_content

    # 输出大模型展示结果（非流式）
    # print("<-------大模型返回结果：", result)
    # st.chat_message("assistant").write(result)
    # 输出大模型展示结果（流式）
    response_message = st.empty() # 创建一个空的消息框, 用于展示大模型返回的结果
    full_response =  ""
    for chunk in response:
        # 报错，相应结果中要是是reasoning_content字段，要么是content字段，要么是delta字段，delta字段中要么是content，要么是reasoning_content
        if chunk.choices[0].delta.reasoning_content is not None:
            print("<-------大模型返回结果：", chunk.choices[0].delta.reasoning_content)
            full_response += chunk.choices[0].delta.reasoning_content
            st.chat_message("assistant").write(full_response)
    # 保存大模型返回结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})