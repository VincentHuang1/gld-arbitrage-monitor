
from flask import Flask, render_template_string
import yfinance as yf
import datetime

app = Flask(__name__)

# 每股GLD代表的黄金盎司（根据你提供的0.09219142）
GLD_PER_SHARE_OUNCE = 0.09219142

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>GLD Arbitrage Monitor</title>
    <meta http-equiv="refresh" content="300">
    <style>
        body { font-family: Arial; background-color: #f8f9fa; margin: 40px; }
        h1 { color: #2b7bba; }
        table { width: 90%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 12px 16px; border: 1px solid #ccc; text-align: right; }
        th { background-color: #2b7bba; color: white; }
        tr:nth-child(even) { background-color: #eef2f5; }
        .signal { background-color: #ffd6d6; font-weight: bold; }
    </style>
</head>
<body>
    <h1>GLD 实时套利监控仪表盘</h1>
    <p>数据更新时间：{{ time }}</p>
    <table>
        <tr>
            <th>GOLD 现货价（USD/oz）</th>
            <th>GLD 市场价（USD）</th>
            <th>GLD 理论价</th>
            <th>价差 (%)</th>
            <th>套利信号</th>
        </tr>
        <tr class="{{ row_class }}">
            <td>{{ gold_price }}</td>
            <td>{{ gld_price }}</td>
            <td>{{ theoretical_price }}</td>
            <td>{{ diff_pct }}%</td>
            <td>{{ signal }}</td>
        </tr>
    </table>
</body>
</html>
'''

@app.route("/")
def index():
    # 获取实时价格
    gold_data = yf.download("GC=F", period="1d", interval="1m")
    gld_data = yf.download("GLD", period="1d", interval="1m")

    gold_price = round(gold_data["Close"].dropna().iloc[-1], 2)
    gld_price = round(gld_data["Close"].dropna().iloc[-1], 2)

    theoretical_price = round(gold_price * GLD_PER_SHARE_OUNCE, 2)
    diff_pct = round((gld_price - theoretical_price) / theoretical_price * 100, 2)

    signal = "-"
    row_class = ""
    if abs(diff_pct) > 1:
        signal = "套利机会"
        row_class = "signal"

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template_string(
        HTML_TEMPLATE,
        time=current_time,
        gold_price=gold_price,
        gld_price=gld_price,
        theoretical_price=theoretical_price,
        diff_pct=diff_pct,
        signal=signal,
        row_class=row_class
    )

import os

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

