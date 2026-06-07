import streamlit as st
from openai import OpenAI
from datetime import datetime
import os

import json


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
# 生成会话名称函数
def generate_session_name():
   return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


# 保存会话信息函数
def  save_session():
    if st.session_state.current_session:
        # 构建新的会话对象
        session_data = {
            "nick_name": st.session_state.nick_name,
            "personality": st.session_state.personality,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }
        # 如果当前目录下没有 sessions 目录，则创建
        if not os.path.exists("sessions"):
            os.mkdir("sessions")

        # 保存会话数据
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)
        print(f"保存会话成功: {st.session_state.current_session}: {session_data}")

# 加载所有的会话信息列表
def load_sessions():
    session_list = []
    # 加载sessions目录下的文件
    if os.path.exists("sessions"):
        for file in os.listdir("sessions"):
            if file.endswith(".json"):
                session_list.append(file[:-5])

    return session_list

# 获取指定session信息
def load_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            # 读取会话数据
            with open(f"sessions/{session_name}.json", "r", encoding="utf -8") as f:
                session_data = json.load(f)
                st.session_state.messages = session_data["messages"]
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.personality = session_data["personality"]
                st.session_state.current_session = session_name
    except Exception as e:
        st.error(f"加载会话失败: {e}")

# 大标题
st.title("AI智能伴侣")

system_prompt = """
        你叫 %s，现在是用户的真实伴侣，请完全代入伴侣角色。
        规则：
            1. 每次只回1条消息
            2. 禁止任何场景或状态描述性文字
            3. 匹配用户的语言
            4. 回复简短，像微信聊天一样
            5. 有需要的话可以用❤️🌸等emoji表情
            6. 用符合伴侣性格的方式对话
            7. 回复的内容, 要充分体现伴侣的性格特征
        伴侣性格：
            - %s
        你必须严格遵守上述规则来回复用户。
    """

# 初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []
# 昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小甜甜"
# 个性
if "personality" not in st.session_state:
    st.session_state.personality = "活泼开朗的东北姑娘"
# 会话标识
if "current_session" not in st.session_state:
    # 当前系统时间 %Y-%m-%d_%H-%M-%S Y:年，M:月，d:日，H:时，m:分，s:秒
    current_time = generate_session_name()
    st.session_state.current_session = current_time

# 展示历史消息
for message in st.session_state.messages:
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])
    st.chat_message(message["role"]).write(message["content"])

print(
    {"role": "system", "content": system_prompt % ("小甜甜", "温柔可爱")},
    *st.session_state.messages)
# 创建OpenAI客户端
client = OpenAI(
    api_key=os.getenv("MOONSHOT_API_KEY"),
    base_url="https://api.moonshot.cn/v1",
)


# logo
st.logo("resources/logo.png")

# 左侧侧边栏
with st.sidebar:
    # 会话信息
    st.subheader("AI控制面板")

    # 新建会话
    if st.button("新建会话",width="stretch",icon="✏️"):
        # 1.保存当前会话信息
        save_session()
        # 2.创建新的会话
        if st.session_state.messages: # 如果聊天信息非空,则新建会话
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()
            save_session()
            # 重新执行此文件
            st.rerun()

    # 会话历史
    st.text("会话历史")
    session_list = load_sessions()
    for session in session_list:
        # st.columns([4,1])  占 80% 宽度 (coll1) 占 20% (coll2)
        coll1,coll2 = st.columns([4,1])
        with coll1:
            # 加载会话信息
            # st.button() 点击按钮后,会返回True，key参数指定了按钮的唯一标识符
            # 三元表达式语法: 值1 if 条件 else 值2
            if st.button(session, width="stretch", icon="📝",key=f"load_{session}",type="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()
        # 删除会话
        with coll2:
            st.button("",width="stretch",icon="❌️",key=f"delete_{session}")
            pass


    # 伴侣信息
    st.subheader("伴侣信息")
    nick_name = st.text_input("伴侣昵称",placeholder="请输入昵称",value=st.session_state.nick_name)
    # 昵称输入框
    if nick_name:
        st.session_state.nick_name = nick_name
    # 性格输入框
    personality = st.text_area("伴侣性格", placeholder="请输入伴侣性格",value=st.session_state.personality)
    if personality:
        st.session_state.personality = personality

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
        model="kimi-k2.6",
        messages=[{"role": "system",
                   "content": system_prompt % (st.session_state.nick_name, st.session_state.personality)},
                  *st.session_state.messages],
        stream=True
    )
    # result = response.choices[0].message.reasoning_content

    # 输出大模型展示结果（非流式）
    # print("<-------大模型返回结果：", result)
    # st.chat_message("assistant").write(result)
    # 输出大模型展示结果(流式)
    response_message = st.empty()  # 创建一个空的消息框, 用于展示大模型返回的结果
    full_response = ""
    for chunk in response:
        # 使用 getattr 安全地获取 reasoning_content 属性
        delta = chunk.choices[0].delta
        reasoning_content = getattr(delta, 'reasoning_content', None)
        content = getattr(delta, 'content', None)

        # 优先使用 reasoning_content，如果不存在则使用 content
        # if reasoning_content is not None:
        #     print("<-------大模型返回结果 reasoning_content:", reasoning_content)
        #     full_response += reasoning_content
        #     response_message.chat_message("assistant").write(full_response)
        if content is not None:
            print("<-------大模型返回结果 content:", content)
            full_response += content
            response_message.chat_message("assistant").write(full_response)
    # 保存大模型返回结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    save_session()