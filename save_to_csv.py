import os
import csv

"""
    Saves extracted cryptocurrency news to a CSV file.

    Parameters:
    - news_list (list of dict): A list of dictionaries containing news articles as was asked 
     in  additional functions criteria.
      Each dictionary should have the keys: 'publication_date', 'title', 'link', and 'description'.
    - filename (str): Name of the CSV file (e.g., 'btc_news.csv').

    Actions:
    - Creates a "news_data" directory if it doesn't exist.
    - Writes the news data to a CSV file in "news_data".
    - Uses UTF-8-SIG encoding for proper character support.
    - Prints a confirmation message upon successful save.

    Example:
        save_news_to_csv(news_list, "btc_news.csv")
    """


def save_news_to_csv(news_list, filename):
    os.makedirs("news_data", exist_ok=True)  
    filepath = os.path.join("news_data", filename)

    with open(filepath, "w", newline="", encoding="utf-8-sig") as csvfile:
        fieldnames = ["Publication Date", "Title", "Link", "Description"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for news in news_list:
            writer.writerow({
                "Publication Date": news["publication_date"],
                "Title": news["title"],
                "Link": news["link"],
                "Description": news["description"]
            })

    print(f"! News saved successfully to {filepath}")
