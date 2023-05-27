import requests
from bs4 import BeautifulSoup
import json


url = 'https://quotes.toscrape.com/'

def get_quotes_json():
    response = requests.get(url)
    all_for_quotes_ = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('span', attrs={'class':'text'})
        authors = soup.find_all('small', class_='author')
        alltags = soup.find_all('div', class_='tags')
        for i in range(0, len(quotes)):
            tagsforquote = alltags[i].find_all('a', class_='tag')
            tags=[]
            for tagforquote in tagsforquote:
                tags.append(tagforquote.text)
            all_for_quotes_.append({
                    "tags": tags,
                    "author": authors[i].text,
                    "quote": authors[i].text
                })
    return(all_for_quotes_)


def get_authors_json():
    response = requests.get(url)
    all_for_authors_ = []
    authors_urls=[]
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', attrs={'class':'quote'})
        for quote in quotes:
            authors_url=url+quote.find('a')['href']
            fullname = quote.find('small', attrs={'class': 'author'}).string
            new_response = requests.get(authors_url)
            new_soup = BeautifulSoup(new_response.text, 'html.parser')
            new_quotes = new_soup.find_all('div', attrs={'class':'author-details'})
            dates = new_soup.find_all('span', attrs={'class':'author-born-date'})
            locations = new_soup.find_all('span', attrs={'class':'author-born-location'})
            descriptions = new_soup.find_all('div', attrs={'class':'author-description'})
            for i in range(0, len(new_quotes)):
                all_for_authors_.append({
                    "fullname": fullname,
                    "born_date": dates[i].text,
                    "born_location": locations[i].text,
                    "description": descriptions[i].text})
    print(all_for_authors_)
    return(all_for_authors_)


if __name__ == '__main__':
    quotes=get_quotes_json()
    with open('quotes.json', 'w') as f:
        json.dump(quotes, f)
    authors=get_authors_json()
    with open('authors.json', 'w') as f:
        json.dump(authors, f)
