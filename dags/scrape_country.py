import csv
import requests
from bs4 import BeautifulSoup
import pymongo

def scrape_country_data():
    url = "https://www.scrapethissite.com/pages/simple/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        table = soup.find_all('div', class_='col-md-4 country')
        
        countries = []
        
        for c in table:
            country = c.find('h3', class_='country-name').text.strip()
            capital = c.find('span', class_='country-capital').text.strip()
            population = c.find('span', class_='country-population').text.strip()
            area = c.find('span', class_='country-area').text.strip()
            
            countries.append([country, capital, population, area])
        
        return countries

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Country', 'Capital', 'Population', 'Area'])
        csv_writer.writerows(data)

data = scrape_country_data()
save_to_csv(data, 'countries_data.csv')

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["country_data"]
collection = db["countries"]


with open('countries_data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        collection.insert_one(row)

