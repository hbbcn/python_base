import streamlit as st

# 设置页面的配置项
st.set_page_config(
    page_title="Streamlit入门",  # 页面标题
    page_icon=":cat:",  # 页面图标，可以是emoji表情或者图片
    layout="wide",  # 页面布局，centered表示居中，wide表示
    initial_sidebar_state="expanded",  # 侧边栏的初始状态，expanded表示展开，collapsed表示收起
    menu_items={
        "Get Help": "https://docs.streamlit.io/",
        "Report a bug": "https://www.streamlit.io/bug",
        "About": "Streamlit是一个开源的Python库，旨在帮助开发者快速构建和部署交互式数据应用程序。它提供了简单易用的API，使得创建数据可视化、机器学习模型展示和数据分析工具变得非常方便。通过Streamlit，开发者可以专注于数据和逻辑，而不需要担心前端开发的复杂性，从而加速了数据应用的开发过程。"
    }
)

#大标题
st.title("Streamlit入门")
#小标题
st.header("streamlit一级标题")
st.subheader("streamlit二级标题")
#文本
st.text("这是一个文本")
# 段落文字
st.write("布偶猫，被誉为“猫中仙女”，以其优雅的外表和温顺的性格成为最受欢迎的宠物猫之一。")
st.write("它们体型较大，成年后可达10-20斤，拥有深邃的蓝色眼眸和柔顺的中长毛，毛色多为双色、手套色或重点色，宛如戴着一副可爱的面具。最迷人的是其松弛柔软的体态，当你抱起它时，它会像布偶一样全身放松，信赖地偎依在主人怀中，“布偶”之名便由此而来。")
st.write("性格是布偶猫最大的魅力。它们极度温顺、安静且粘人，被称为“小狗猫”，喜欢跟随主人走动，享受陪伴。它们通常脾气极好，忍耐力强，能与儿童和其他宠物友好相处，是理想的家庭伴侣。其轻柔的叫声和爱撒娇的天性，能带给主人无尽的温暖与治愈。")
st.write("养护方面，需要定期梳理其丰厚毛发以防止打结，并提供足够的关注与互动。拥有一只布偶猫，就如同拥有了一位温柔优雅、终生依恋的毛茸茸家人。")

# 图片
st.image("./resource/cat.jpg")

# 音频
st.audio("./resource/news.mp3")

# 视频
st.video("./resource/news.mp4")

# logo
st.logo("./resource/logo.png")

# 表格
student_data = {
    "姓名": ["张三", "李四", "王五"],
    "语文成绩": [90, 80, 85],
    "数学成绩": [95, 88, 92],
    "英语成绩": [88, 90, 91]
}
st.table(student_data)

# 输入框
name = st.text_input("请输入你的名字: ")
st.write(f"你好, {name}!")

password = st.text_input("请输入你的密码: ", type="password")
st.write(f"你输入的密码是: {password}")

# 单选按钮，默认选中“女”
gender = st.radio("请选择你的性别: ", ["男", "女", "其他"], index=1)
st.write(f"你选择的性别是: {gender}")