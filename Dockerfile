# 使用官方 Python 3.8 镜像作为基础镜像
FROM python:3.10

# 更新 pip
RUN pip install --upgrade pip

# 设置工作目录
WORKDIR /app

# 将本地文件复制到容器中
COPY . .

# 安装项目依赖
RUN pip install -r requirements.txt

# 暴露 FastAPI 默认端口
EXPOSE 8090

# 启动 FastAPI 应用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8090"]
