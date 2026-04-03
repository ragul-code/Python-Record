import requests
import pandas as pd

# Sample stocks
stocks = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]

def get_data(symbol):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
    data = requests.get(url).json()
    
    close_prices = data['chart']['result'][0]['indicators']['quote'][0]['close']
    return pd.Series(close_prices).dropna()

def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi.iloc[-1]

def scan():
    print("Scanning stocks...\n")
    for stock in stocks:
        try:
            prices = get_data(stock)
            rsi = calculate_rsi(prices)

            if rsi < 30:
                signal = "BUY"
            elif rsi > 70:
                signal = "SELL"
            else:
                signal = "HOLD"

            print(f"{stock} | RSI: {round(rsi,2)} → {signal}")

        except Exception as e:
            print(f"{stock} error")

if __name__ == "__main__":
    scan()