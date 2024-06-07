import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.bbc.com/news";

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

headlines = soup.find_all('h2')
print(headlines)

with open('headlines.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline', 'URL'])

    for headline in headlines:
        headline_text = headline.text.strip()
        print(headline_text)
        parent_a_tag = headline.find_parent('a')
        if parent_a_tag:
            headline_url = parent_a_tag['href']
            if not headline_url.startswith('http'):
                headline_url = f"https://www.bbc.com{headline_url}"
            writer.writerow([headline_text, headline_url])

print("Data scraping complete and saved to headlines",csv)