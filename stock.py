import pandas as pd
import requests

# 設定目標日期
target_date = '20240913'

# 把 csv 檔抓下來
url = f'https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date={target_date}&type=ALL&response=csv'
res = requests.get(url)
data = res.text 

# 把爬下來的資料整理成需要的格式
# 股價欄位的長度為16, 開頭沒有"="
s_data = data.split('\n')
output = []
for d in s_data:
    _d = d.split('","')
    length = len(_d)
    symbol = _d[0]
  
    if length == 16 and not symbol.startswith('='):
        output.append([
          ele.replace('",\r','').replace('"','') 
          for ele in _d
        ])
 
# 轉成 DataFrame 並存成 csv 檔
df = pd.DataFrame(output[1:], columns=output[0])
df.set_index('證券代號', inplace=True)
df.to_csv('all_stock_price_a_day/stock_price_'+target_date+'.csv')
