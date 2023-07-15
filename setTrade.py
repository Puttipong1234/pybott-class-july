import settrade_v2
from config import *

exchange = settrade_v2.Investor(
    app_id=TEST_API_KEY_SET,
    app_secret = TEST_API_SECRET_SET,
    app_code="SANDBOX",
    broker_id="SANDBOX",
)

# my_wallet_E = exchange.Equity(account_no="pyybott-E")
# print(my_wallet_E.get_account_info())

# my_wallet_D = exchange.Derivatives(account_no="pyybott-D")
# print(my_wallet_D.get_account_info())

# openLong

def openLong_set(sym,amt):
    print("open long SET")
    try:
        my_wallet_E.place_order(
            pin="000000",
            side="Buy",
            symbol=sym,
            volume=amt,
            price=0,
            price_type="MP-MKT"
        )
    except Exception as e:
        print(e)
    # create order code

def tpslLong_set(sym,amt):
    print("tpsl long SET")
    # create order code
    try:
        my_wallet_E.place_order(
            pin="000000",
            side="Sell",
            symbol=sym,
            volume=amt,
            price=0,
            price_type="MP-MKT"
        )
    except Exception as e:
        print(e)

# closeLong
# openShort
# closeShort

