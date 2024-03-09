from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import pymongo

def scrape_job_details(url):
    driver = webdriver.Chrome()
    driver.get(url)

  
    jobs_category = driver.find_element(By.XPATH, "//a[contains(@href,'/en/jobs')]")
    jobs_category.click()

   
    chef_category = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/en/ads/bangladesh/chef-jobs')]"))
    )
    chef_category.click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'normal--2QYVk.gtm-normal-ad')))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, 'html.parser')
    job_postings = soup.find_all('li', class_='normal--2QYVk gtm-normal-ad')

    job_details = []
    for job in job_postings:
        try:
            title = job.find('h2', class_='heading--2eONR heading-2--1OnX8 title--3yncE block--3v-Ow').text.strip()
        except AttributeError:
            title = None

        try:
            salary = job.find('div', class_='price--3SnqI color--t0tGX').text.strip()
        except AttributeError:
            salary = None

        try:
            location = job.find('div', class_='description--2-ez3').text.strip()
        except AttributeError:
            location = None

        try:
            posted_date = job.find('div', class_='updated-time--1DbCk').text.strip()
        except AttributeError:
            posted_date = None

        try:
            link = job.find('a', class_='card-link--3ssYv gtm-ad-item')['href']
        except (AttributeError, KeyError):
            link = None

        job_details.append({
            'Title': title,
            'Salary': salary,
            'Location': location,
            'Posted Date': posted_date,
            'Link': link
        })

    return job_details


def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Salary', 'Location', 'Posted Date', 'Link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for job in data:
            writer.writerow(job)



url = "https://bikroy.com/"
job_details = scrape_job_details(url)


save_to_csv(job_details, 'job_details.csv')

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["bikroy_jobs"]
collection = db["job_details"]
with open('job_details.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        collection.insert_one(row)
