import ccxt
from config import *
apikey = TEST_API_KEY_BINANCE_SPOT
secret = TEST_API_SECRET_BINANCE_SPOT
testing = True

exchange = ccxt.binance({
    'apiKey':apikey,
    'secret':secret,
    'options':{
        'defaultType':'spot'
    }
})

exchange.set_sandbox_mode(testing)

all_assets = exchange.fetch_balance()["info"]["balances"]
for i in all_assets:
    print(i)

def openLong_spot(sym,amt):
    exchange.create_order(
        symbol=sym,
        type="market",
        side="buy",
        amount = amt
    )

def tpslLong_spot(sym,amt):
    exchange.create_order(
        symbol=sym,
        type="market",
        side="sell",
        amount = amt
    )
