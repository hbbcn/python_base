from fastapi import FastAPI

# 创建 FastAPI 对象
app = FastAPI()
# 定义API接口 ---》 该函数的返回表示API接口
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "张三"},
        {"id": 2, "name": "李四"},
        {"id": 3, "name": "王五"},
    ]

# 启动服务 ---》 uvicorn 启动服务:python中轻量级Web服务器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)