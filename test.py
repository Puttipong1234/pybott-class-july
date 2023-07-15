# int float
เรามีเงิน = 30000
btc = 70000
เราซื้อBTCได้ = เรามีเงิน/btc
print(เราซื้อBTCได้)

# string
สัญญาณ = "OPEN LONG"
side = สัญญาณ.split(" ")[1]
action = สัญญาณ.split(" ")[0]
print(side)
print(action)

# list dictionary
list_a = [0,1,2,3,4,5,6]
list_of_symbol = ["BTC","ETH","BNB"]

for symbol in list_of_symbol:
    print(symbol)

# json -- dictionary

dict_a = {"dog":"สุนัข"}
print(dict_a["dog"])

# payload เวลาผมส่งข้อมูลซื้อขายมาจาก tradingview

sample_payload = {
    "ACTION" : "OPEN LONG",
    "AMOUNT" : "0.1",
    "LEVERAGE" : 10
}

print("ได้รับสัญญาณ : " + sample_payload["ACTION"])
print("จำนวน : " + sample_payload["AMOUNT"])

#function

x = 0
y = 2
result = x + y # 2

x1 = 1
y1 = 3

x2 = 2
y2 = 5

def plus(num1,num2):
    result = num1 + num2
    return result

print(plus(1,2))

def calculate_btc_amount(จำนวนเงิน):
    result = จำนวนเงิน/70000
    return result

แดง = 10000
เขียว = 20000

print(calculate_btc_amount(แดง))
print(calculate_btc_amount(เขียว))

