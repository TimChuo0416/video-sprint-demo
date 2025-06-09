# Dockerfile
FROM python:3.9-slim

# 安裝 OpenCV 所需的系統依賴函式庫
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# 安裝 Python 套件
RUN pip install numpy opencv-python-headless

# 設定容器內的工作目錄
WORKDIR /app

# 複製腳本到容器中
COPY step_a.py .
COPY step_b.py .