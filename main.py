import requests
import time
from dingtalkchatbot.chatbot import DingtalkChatbot
from datetime import datetime, timedelta, timezone

# WebHook地址
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=01fafa4c3136f5821ae28ad25a54af044d481a9a43dee0cac6bb05f4948a2c26'
secret = 'SEC113bdfe8e1843a8fc863042a0c8ca681049fdb8e2da5b7a36e8e6c2ba3765e14'
xiaoding = DingtalkChatbot(webhook, secret=secret)
#
symbol_m = [
    "BTC",
    "ETH",
    "BNB",
    "ADA",
    "ALGO",
    "ATOM",
    "AVAX",
    "BCH",
    "DOGE",
    "DOT",
    "DYDX",
    "ETC",
    "LINK",
    "LTC",
    "MATIC",
    "NEAR",
    "SOL",
    "TRX",
    "UNI",
    "XRP",

]

# 买入成交量
while True:
    buy_list = []
    for i in symbol_m:
        url = 'https://api3.binance.com/api/v3/klines?symbol=' + i + 'USDT&interval=5m&limit=2'

        data = requests.get(url)
        data_json = data.json()[0]
        print(data_json)
        buy = float(data_json[9])
        vol = float(data_json[5])
        bfb = (buy / vol) * 100
        buy_list.append(round(bfb))

    print(buy_list)
    sz_min = 0
    xd_min = 0
    sz_max = 0
    xd_max = 0
    for i in buy_list:
        if i >= 60:
            sz_min = sz_min + 1
        if i <= 40:
            xd_min = xd_min + 1
        if i >= 70:
            sz_max = sz_max + 1
        if i <= 30:
            xd_max = xd_max + 1

    open_time = int(float(data_json[0]) / 1000)
    td = timedelta(hours=8)
    tz = timezone(td)
    dt = datetime.fromtimestamp(open_time, tz)
    dt = dt.strftime('%m-%d %H:%M')

    if sz_max > 8:
        txt = dt + "---5分钟该位置出现-超级-积极买入---" + str(sz_max)
        xiaoding.send_text(msg=txt, is_at_all=True)
    elif sz_min > 8:
        txt = dt + "---5分钟该位置出现-普通-积极买入---" + str(sz_min)
        xiaoding.send_text(msg=txt, is_at_all=False)
    else:
        print("买入--还未满足条件")

    if xd_max > 8:
        txt = dt + "---5分钟该位置出现-超级-积极卖出---" + str(xd_max)
        xiaoding.send_text(msg=txt, is_at_all=True)

    elif xd_min > 8:
        txt = dt + "---5分钟该位置出现-普通-积极卖出---" + str(xd_min)
        xiaoding.send_text(msg=txt, is_at_all=False)
    else:
        print("卖出--还未满足条件")

    time.sleep(150)

