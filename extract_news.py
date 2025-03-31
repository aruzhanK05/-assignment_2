import os
from bs4 import BeautifulSoup
from crypto_news_scraper.fetch_html import crypto_data  
"""
    Extracts cryptocurrency news from saved HTML files.

    :param crypto_symbol: Symbol of the cryptocurrency (BTC, ETH, etc.)
    :param keywords: Optional list of keywords to filter news.
    :return: List of dictionaries with news details (title, link, publication_date, description).
"""
 

def extract_crypto_news(crypto_symbol, keywords=None):
    crypto_symbol = crypto_symbol.upper()

    if crypto_symbol not in crypto_data:
        print(f" Invalid cryptocurrency! Choose from: {list(crypto_data.keys())}")
        return []

    file_path = crypto_data[crypto_symbol]["file"]

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
    except FileNotFoundError:
        print(f" !!!Error: HTML file for {crypto_symbol} not found at {file_path}")
        return []

    
    news_section = soup.find("div", class_="tw-my-6 lg:tw-mb-12")
    if not news_section:
        print(f"!!! Could not find news section for {crypto_symbol}")
        return []

   
    news_items = news_section.find_all(
        "div", class_="tw-border-0 tw-border-b tw-border-solid tw-border-gray-200 dark:tw-border-moon-700 tw-pb-5 tw-flex tw-flex-col", 
        limit=80
    )

    extracted_news = []
    for item in news_items:
        title_tag = item.find("div", class_="tw-mb-4 tw-font-bold tw-text-gray-900 dark:tw-text-moon-50 tw-text-lg md:tw-text-xl tw-leading-7")
        link_tag = item.find("a", href=True)
        description_tag = item.find("div", class_="tw-my-1 tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5")
        date_tag = item.find("time")

        if title_tag and link_tag:
            title = title_tag.text.strip()
            link = link_tag["href"]
            if not link.startswith("http"):
                link = "https://www.coingecko.com" + link  

            description = description_tag.text.strip() if description_tag else "No description available"
            publication_date = date_tag.text.strip() if date_tag else "No date available"

            if keywords:
                if not any(keyword.lower() in title.lower() or keyword.lower() in description.lower() for keyword in keywords):
                    continue

            extracted_news.append({
                "title": title,
                "link": link,
                "publication_date": publication_date,
                "description": description
            })

            if len(extracted_news) >= 8:
                break

    return extracted_news
