import csv
import requests
from bs4 import BeautifulSoup
import pymongo

def scrape_hockey_data(pages=4):
    base_url = "https://www.scrapethissite.com/pages/forms/?page_num={}&per_page=100"
    all_data = []
    
    for page in range(1, pages+1):
        url = base_url.format(page)
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            table = soup.find('table', class_='table')
            rows = table.find_all('tr')
            
            for row in rows[1:]:
                columns = row.find_all('td')
                team_name = columns[0].text.strip()
                year = columns[1].text.strip()
                wins = columns[2].text.strip()
                losses = columns[3].text.strip()
                ot_losses = columns[4].text.strip()
                win_percentage = columns[5].text.strip()
                goals_for = columns[6].text.strip()
                goals_against = columns[7].text.strip()
                plus_minus = columns[8].text.strip()

                all_data.append([team_name, year, wins, losses, ot_losses, win_percentage, goals_for, goals_against, plus_minus])

    return all_data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Team Name', 'Year', 'Wins', 'Losses', 'OT Losses', 'Win %', 'Goals For (GF)', 'Goals Against (GA)', '+/-'])
        csv_writer.writerows(data)

hockey_data = scrape_hockey_data(pages=4)
save_to_csv(hockey_data, 'hockey_data.csv')



client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hocky_data"]
collection = db["hocky"]


with open('hockey_data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        collection.insert_one(row)









