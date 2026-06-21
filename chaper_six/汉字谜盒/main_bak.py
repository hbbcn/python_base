import os
import json
import uuid
from datetime import datetime
from typing import Any, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import logging

# 配置日志的基本信息
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
)

# 创建FastAPI实例
app = FastAPI(title="汉字谜盒")

# 会话存储目录
SESSIONS_DIR = "sessions"
if not os.path.exists(SESSIONS_DIR):
    os.makedirs(SESSIONS_DIR)

# 数据模型
class ChatRequest(BaseModel):
    session_id: str
    message: str

class SessionData(BaseModel):
    messages: List[dict] = []

@app.get("/")
def root():
    """
    根路由，返回前端页面
    """
    return FileResponse("static/index.html")

@app.get("/api/sessions")
def get_sessions():
    """
    获取所有会话列表（从文件名提取）
    """
    try:
        sessions = []
        for filename in os.listdir(SESSIONS_DIR):
            if filename.endswith('.json'):
                sessions.append(filename[:-5])  # 去掉 .json 后缀
        return {"code": 200, "data": sorted(sessions, reverse=True)}
    except Exception as e:
        logging.error(f"获取会话列表失败: {e}")
        return {"code": 500, "message": "获取会话列表失败"}

@app.post("/api/sessions")
def create_session():
    """
    创建新会话
    """
    try:
        session_id = str(uuid.uuid4())[:8]
        session_file = os.path.join(SESSIONS_DIR, f"{session_id}.json")
        
        # 初始化空会话文件
        with open(session_file, 'w', encoding='utf-8') as f:
            json.dump({"messages": []}, f)
        
        return {"code": 200, "data": session_id}
    except Exception as e:
        logging.error(f"创建会话失败: {e}")
        return {"code": 500, "message": "创建会话失败"}

@app.get("/api/sessions/{session_id}")
def get_session(session_id: str):
    """
    获取指定会话的聊天记录
    """
    session_file = os.path.join(SESSIONS_DIR, f"{session_id}.json")
    if not os.path.exists(session_file):
        raise HTTPException(status_code=404, detail="会话不存在")
    
    try:
        with open(session_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return {"code": 200, "data": data}
    except Exception as e:
        logging.error(f"读取会话失败: {e}")
        raise HTTPException(status_code=500, detail="读取会话失败")

@app.delete("/api/sessions/{session_id}")
def delete_session(session_id: str):
    """
    删除指定会话
    """
    session_file = os.path.join(SESSIONS_DIR, f"{session_id}.json")
    if not os.path.exists(session_file):
        raise HTTPException(status_code=404, detail="会话不存在")
    
    try:
        os.remove(session_file)
        return {"code": 200, "message": "删除成功"}
    except Exception as e:
        logging.error(f"删除会话失败: {e}")
        raise HTTPException(status_code=500, detail="删除会话失败")

@app.post("/api/chat")
def chat(request: ChatRequest):
    """
    聊天接口（模拟AI回复）
    """
    session_file = os.path.join(SESSIONS_DIR, f"{request.session_id}.json")
    if not os.path.exists(session_file):
        raise HTTPException(status_code=404, detail="会话不存在")
    
    try:
        # 1. 读取历史消息
        with open(session_file, 'r', encoding='utf-8') as f:
            session_data = json.load(f)
        
        # 2. 添加用户消息
        session_data["messages"].append({"role": "user", "content": request.message})
        
        # 3. 模拟AI回复（实际项目中这里应调用 OpenAI API）
        ai_response = f"你问的是：{request.message}。这是一个模拟的AI回复。"
        session_data["messages"].append({"role": "assistant", "content": ai_response})
        
        # 4. 保存回文件
        with open(session_file, 'w', encoding='utf-8') as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)
        
        return {"code": 200, "data": ai_response}
    except Exception as e:
        logging.error(f"聊天处理失败: {e}")
        raise HTTPException(status_code=500, detail="聊天处理失败")

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")

# 启动项目
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)