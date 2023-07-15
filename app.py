from flask import Flask , request
from cryptotrade import *
from setTrade import *
from cryptoTradeSpot import *
import json
from config import LINE_NOTIFY_API
from line_notify import LineNotify

app = Flask(__name__)

notify = LineNotify(LINE_NOTIFY_API)
notify.send("Start Server")

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/buyBTC")
def buybtc():
    return "BTC to the moon"

@app.route("/check")
def check_amt():
    from test import calculate_btc_amount
    return str(calculate_btc_amount(30000))

@app.route("/signals/crypto-future",methods = ["GET","POST"])
def trade_signal_future():
    if request.method == "POST":
        print("ได้รับคำสั่งซื้อขายจาก tradingview")
        notify.send("crypto-future ได้รับคำสั่งซื้อขายจาก tradingview")
        signal = json.loads(request.data)
        notify.send(signal)
        act = signal["ACTION"]
        amt = signal["AMOUNT_COIN"]
        sym = signal["SYMBOL"]
        
        if "OPEN LONG" in act:
            print("ทำการเปิดสัญญา LONG")
            openLong(sym,amt)
        
        elif "OPEN SHORT" in act:
            print("ทำการเปิดสัญญา SHORT")
            openShort(sym,amt)
        
        elif "TPSL LONG" in act:
            tpslLong(sym,amt)
        
        elif "TPSL SHORT" in act:
            tpslShort(sym,amt)
            
        
        return "200"
    
    else :
        return "This is route for receive Crypto signal"

@app.route("/signals/crypto-spot",methods = ["GET","POST"])
def trade_signal_spot():
    if request.method == "POST":
        notify.send("crypto-spot ได้รับคำสั่งซื้อขายจาก tradingview")
        signal = json.loads(request.data)
        notify.send(signal)
        
        act = signal["ACTION"]
        amt = signal["AMOUNT_COIN"]
        sym = signal["SYMBOL"]
        
        if "OPEN LONG" in act:
            print("ทำการเปิดสัญญา LONG")
            openLong_spot(sym,amt)
        
        elif "TPSL LONG" in act:
            tpslLong_spot(sym,amt)
        return "200"
    
    else :
        return "This is route for receive Crypto signal"

@app.route("/signals/Settrade",methods = ["GET","POST"])
def trade_signal_settrade():
    if request.method == "POST":
        notify.send("Settrade-spot ได้รับคำสั่งซื้อขายจาก tradingview")
        signal = json.loads(request.data)
        notify.send(signal)
        act = signal["ACTION"]
        amt = signal["AMOUNT_COIN"]
        sym = signal["SYMBOL"]
        
        if "OPEN LONG" in act:
            print("ทำการซื้อหุ้น")
            openLong_set(sym,amt)
        
        elif "TPSL LONG" in act:
            tpslLong_set(sym,amt)
            
        return "200"
    
    else :
        return "This is route for receive Settrade signal"



if __name__ == '__main__':
    app.run(debug=True)
    