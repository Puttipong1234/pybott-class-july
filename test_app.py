from flask import Flask , request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/buyBTC")
def buybtc():
    return "BTC to the moon"

if __name__ == '__main__':
    app.run()
    