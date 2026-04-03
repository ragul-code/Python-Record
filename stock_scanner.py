import random

stocks = ["RELIANCE", "TCS", "INFY", "HDFCBANK", "ITC"]

def scan_stocks():
    print("Scanning stocks...\n")
    for stock in stocks:
        signal = random.choice(["BUY", "SELL", "HOLD"])
        print(f"{stock}: {signal}")

if __name__ == "__main__":
    scan_stocks()