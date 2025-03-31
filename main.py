from crypto_news_scraper.fetch_html import fetch_and_save_pages
from crypto_news_scraper.extract_news import extract_crypto_news
from crypto_news_scraper.save_to_csv import save_news_to_csv

if __name__ == "__main__":
    fetch_and_save_pages()

    crypto_symbol = input("\nEnter cryptocurrency symbol(BTC/ETH/ADA/XRP/DOGE/LTC/BNB/SOL/DOT/AVAX): ").strip().upper()
    keyword_input = input("Enter keywords (comma-separated) or press Enter to skip: ").strip()
    keywords = [kw.strip() for kw in keyword_input.split(",")] if keyword_input else None

    news_list = extract_crypto_news(crypto_symbol, keywords)
    print(news_list)

    if news_list:
        filename = input("Enter filename for CSV (e.g., btc.csv): ").strip()
        save_news_to_csv(news_list, filename)
