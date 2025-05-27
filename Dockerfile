
# 使用官方 Python 基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 拷贝 Flask 应用程序文件
COPY gld_arbitrage_monitor.py .

# 安装所需依赖
RUN pip install --no-cache-dir flask yfinance

# 设置默认执行命令
CMD ["python", "gld_arbitrage_monitor.py"]
