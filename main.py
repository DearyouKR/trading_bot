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
    buy_list_5 = []
    for i in symbol_m:
        url_5 = 'https://api3.binance.com/api/v3/klines?symbol=' + i + 'USDT&interval=5m&limit=2'

        data_5 = requests.get(url_5)
        data_json_5 = data_5.json()[0]
        # print(data_json_5)
        buy_5 = float(data_json_5[9])
        vol_5 = float(data_json_5[5])
        bfb_5 = (buy_5 / vol_5) * 100
        buy_list_5.append(round(bfb_5))

    print(buy_list_5)
    sz_min_5 = 0
    xd_min_5 = 0
    sz_max_5 = 0
    xd_max_5 = 0
    for i in buy_list_5:
        if i >= 60:
            sz_min_5 = sz_min_5 + 1
        if i <= 40:
            xd_min_5 = xd_min_5 + 1
        if i >= 70:
            sz_max_5 = sz_max_5 + 1
        if i <= 30:
            xd_max_5 = xd_max_5 + 1

    open_time_5 = int(float(data_json_5[0]) / 1000)
    td_5 = timedelta(hours=8)
    tz_5 = timezone(td_5)
    dt_5 = datetime.fromtimestamp(open_time_5, tz_5)
    dt_5 = dt_5.strftime('%m-%d %H:%M')

    if sz_max_5 > 8:
        txt_5 = dt_5 + "---5分钟前20出现-超级-积极买入---" + str(sz_max_5)
        xiaoding.send_text(msg=txt_5, is_at_all=True)
    elif sz_min_5 > 8:
        txt_5 = dt_5 + "---5分钟前20出现-普通-积极买入---" + str(sz_min_5)
        xiaoding.send_text(msg=txt_5, is_at_all=False)
    else:
        print("5分买入--还未满足条件")

    if xd_max_5 > 8:
        txt_5 = dt_5 + "---5分钟前20出现-超级-积极卖出---" + str(xd_max_5)
        xiaoding.send_text(msg=txt_5, is_at_all=True)

    elif xd_min_5 > 8:
        txt_5 = dt_5 + "---5分钟前20出现-普通-积极卖出---" + str(xd_min_5)
        xiaoding.send_text(msg=txt_5, is_at_all=False)
    else:
        print(i + "--还未满足条件")
        # xiaoding.send_text(msg="还未满足条件", is_at_all=False)

    buy_list_15 = []
    for i in symbol_m:
        url_15 = 'https://api3.binance.com/api/v3/klines?symbol=' + i + 'USDT&interval=15m&limit=2'

        data_15 = requests.get(url_15)
        data_json_15 = data_15.json()[0]
        # print(data_json_15)
        buy_15 = float(data_json_15[9])
        vol_15 = float(data_json_15[5])
        bfb_15 = (buy_15 / vol_15) * 100
        buy_list_15.append(round(bfb_15))

    print(buy_list_15)
    sz_min_15 = 0
    xd_min_15 = 0
    sz_max_15 = 0
    xd_max_15 = 0
    for i in buy_list_15:
        if i >= 60:
            sz_min_15 = sz_min_15 + 1
        if i <= 40:
            xd_min_15 = xd_min_15 + 1
        if i >= 70:
            sz_max_15 = sz_max_15 + 1
        if i <= 30:
            xd_max_15 = xd_max_15 + 1

    open_time_15 = int(float(data_json_15[0]) / 1000)
    td_15 = timedelta(hours=8)
    tz_15 = timezone(td_15)
    dt_15 = datetime.fromtimestamp(open_time_15, tz_15)
    dt_15 = dt_15.strftime('%m-%d %H:%M')

    if sz_max_15 > 8:
        txt_15 = dt_15 + "---15分钟前20出现-超级-积极买入---" + str(sz_max_15)
        xiaoding.send_text(msg=txt_15, is_at_all=True)
    elif sz_min_15 > 8:
        txt_15 = dt_15 + "---15分钟前20出现-普通-积极买入---" + str(sz_min_15)
        xiaoding.send_text(msg=txt_15, is_at_all=False)
    else:
        print("15分买入--还未满足条件")

    if xd_max_15 > 8:
        txt_15 = dt_15 + "---15分钟前20出现-超级-积极卖出---" + str(xd_max_15)
        xiaoding.send_text(msg=txt_15, is_at_all=True)

    elif xd_min_15 > 8:
        txt_15 = dt_15 + "---15分钟前20出现-普通-积极卖出---" + str(xd_min_15)
        xiaoding.send_text(msg=txt_15, is_at_all=False)
    else:
        print(i + "--还未满足条件")

    time.sleep(300)
