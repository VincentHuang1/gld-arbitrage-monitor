FROM python:3.10-slim
WORKDIR /app
COPY gld_arbitrage_monitor.py .
RUN pip install --no-cache-dir flask yfinance
CMD ["python", "gld_arbitrage_monitor.py"]
