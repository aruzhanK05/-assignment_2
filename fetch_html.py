import os
import time
import urllib.request
"""
    Fetches the latest CoinGecko web pages for cryptocurrencies and saves them as HTML files.

    Iterates through `crypto_data` to fetch web pages.
    Saves each page in the "web" directory and creates the "web" folder automatically.
    Introduces a delay to prevent request blocking.
    Handles HTTP errors and and bypasses the restrictions (e.g., 403, 500) 
    
    """

crypto_data = {
    "BTC": {"url": "https://www.coingecko.com/en/coins/bitcoin", "file": "web/bitcoin.html"},
    "ETH": {"url": "https://www.coingecko.com/en/coins/ethereum", "file": "web/eu.html"},
    "ADA": {"url": "https://www.coingecko.com/en/coins/cardano", "file": "web/cardano.html"},
    "XRP": {"url": "https://www.coingecko.com/en/coins/xrp", "file": "web/xrp.html"},
    "DOGE": {"url": "https://www.coingecko.com/en/coins/dogecoin", "file": "web/doge.html"},
    "LTC": {"url": "https://www.coingecko.com/en/coins/litecoin", "file": "web/lite.html"},
    "BNB": {"url": "https://www.coingecko.com/en/coins/binancecoin", "file": "web/bnb.html"},
    "SOL": {"url": "https://www.coingecko.com/en/coins/solana", "file": "web/sol.html"},
    "DOT": {"url": "https://www.coingecko.com/en/coins/polkadot", "file": "web/dot.html"},
    "AVAX": {"url": "https://www.coingecko.com/en/coins/avalanche", "file": "web/avax.html"},
}


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def fetch_and_save_pages():
    os.makedirs("web", exist_ok=True)  

    for symbol, data in crypto_data.items():
        url, file_path = data["url"], data["file"]
        request = urllib.request.Request(url, headers=headers)

        try:
            with urllib.request.urlopen(request) as response:
                page_content = response.read()

            with open(file_path, "wb") as file:
                file.write(page_content)

            print(f" Successfully saved {symbol} page!")

         
            time.sleep(2)

        except urllib.error.HTTPError as e:
            print(f" HTTP Error for {symbol}: {e.code} - {e.reason}")
        except urllib.error.URLError as e:
            print(f" URL Error for {symbol}: {e.reason}")
