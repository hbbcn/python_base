from openai import OpenAI
import os

import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

client = OpenAI(
    api_key = os.getenv("MOONSHOT_API_KEY"),
    base_url = "https://api.moonshot.cn/v1",
)

history = [
    {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"}
]

def chat(query, history):
    history.append({
        "role": "user",
        "content": query
    })
    completion = client.chat.completions.create(
        model="kimi-k2.6",
        messages=history
    )
    result = completion.choices[0].message.content
    history.append({
        "role": "assistant",
        "content": result
    })
    return result

print(chat("地球的自转周期是多少？", history), flush=True)
print(chat("月球呢？", history), flush=True)
