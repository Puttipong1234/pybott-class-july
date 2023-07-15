import requests
import json

url = 'http://127.0.0.1:5000/signals/crypto-spot'
heroku_url = "https://xxxxxxx.com/signals" # webhook
ข้อมูลตัวอย่าง = {
            'ACTION': 'OPEN LONG', # << USE
            'AMOUNT_COIN' : '0.01', # << USE
            'AMOUNT_USDT' : '30.00',
            'LEV' : '[PB-BTC-06]', 
            'SYMBOL' : 'BTCUSDT', # << USE
            'PASSWORD': "xxxxx", # << USE
            'FACTOR' : "10" # << USE....
            }

ข้อมูลตัวอย่าง = json.dumps(ข้อมูลตัวอย่าง)

x = requests.post(url, data = ข้อมูลตัวอย่าง)
# x = requests.post(heroku_url, data = ข้อมูลตัวอย่าง)

print(x.text)