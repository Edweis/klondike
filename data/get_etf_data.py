''"""Scrap Yahoo Finance API to get ETFs data.

We can loop over a bash's `curl` command because yahoo blocks it by adding a session id.
The goal is to first go on the downloading page, find the download button, then download it.
"""
# Part 1. Import Python Modules

from selenium import webdriver
from time import sleep
from urllib.parse import urlparse, parse_qs
import csv
from urllib.request import urlopen
import shutil
import os.path
import datetime

period_end = datetime.datetime(2017, 10, 4)


def unix_time_millis(dt):
    dt += datetime.timedelta(days=1)
    return str(int((dt - datetime.datetime.utcfromtimestamp(0)).total_seconds()))

period_end = unix_time_millis(period_end)


# Part 2. Download ETFs name
# TODO find a way to get an ETF list to make sure we have them all

# url = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download"
file_name = "etf_names.txt" # Where tickers are stored
download_folder = 'etfs'
error_file = "scraping_errors.csv"
# with urlopen(url) as response, open(file_name, 'wb') as out_file:
#     shutil.copyfileobj(response, out_file)

# Part 3. Set up Chromedriver for scraping

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": download_folder,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
driver = webdriver.Chrome(chrome_options=options)

# Part 4. Get Crumb Value

def get_crumb():
    driver.get("https://finance.yahoo.com/quote/AAPL/"
               "history?period1=0&period2=2000000000&interval=1d&filter=history&frequency=1d")
    sleep(10)
    el = driver.find_element_by_xpath("// a[. // span[text() = 'Download Data']]")
    link = el.get_attribute("href")
    a = urlparse(link)
    crumb = parse_qs(a.query)["crumb"][0]
    return crumb

crumb = None
for i in range(10): # we run it 10 times
    crumb = get_crumb()
    if not crumb:
        sleep(100)
    else:
        break

if not crumb:
    raise ValueError("Crumb Not Set")


# Part 5. Download Yahoo ETFs Quotes

for file in os.listdir(download_folder): # we remove all files in directory
    file_path = os.path.join(download_folder, file)
    os.unlink(file_path)


def download_etfs_quotes(ticker):
    driver.get("https://query1.finance.yahoo.com/v7/finance/download/"
               "{0}?period1=0&period2={1}&interval=1d&events=history&crumb={2}".format(ticker, period_end, crumb))
    sleep(1)

for t in range(3): # We try to get it 3 times
    with open(file_name) as tickers_file:
        tickers_reader = csv.reader(tickers_file)
        next(tickers_reader)
        for line in tickers_reader:
            ticker = line[0].strip()
            if not os.path.isfile(f".{download_folder}/{ticker}.csv"):
                download_etfs_quotes(ticker)

# Part 6. Identify Missing Data

errors = {}
with open(file_name) as tickers_file:
    tickers_reader = csv.reader(tickers_file)
    next(tickers_reader)
    for line in tickers_reader:
        ticker = line[0].strip()
        if not os.path.isfile("./{download_folder}/{ticker}.csv"):
            errors[ticker] = "Quotes not downloaded."

with open(error_file, "w+") as errors_file:
    errors_writer = csv.writer(errors_file)
    errors_writer.writerow(["ticker", "error"])
    for ticker in errors:
        errors_writer.writerow([ticker, errors[ticker]])
