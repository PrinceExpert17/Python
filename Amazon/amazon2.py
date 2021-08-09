from requests_html import HTMLSession
import csv
import datetime
import sqlite3

# Connect to SQL Database/create database
conn = sqlite3.connect('amztracker.db')
c = conn.cursor()
#c.execute('''CREATE TABLE prices(date DATE, asin TEXT, price FLOAT, title TEXT)''')


# Start a session and create a list
headers = {"User-Agents": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
s = HTMLSession()
asins = []

# Read the csv file
with open('asins.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        asins.append(row[0])

# Scrape the data
for asin in asins:
    r = s.get(f'https://www.amazon.com/dp/{asin}', headers=headers)
    try:
        price = r.html.find('#price_inside_buybox')[0].text.replace('$', '').strip()
    except:
        price = r.html.find('#priceblock_ourprice')[0].text.replace('$', '').strip()
    title = r.html.find('#productTitle')[0].text.strip()
    asin = asin
    date = datetime.datetime.today()

    c.execute('''INSERT INTO prices VALUES(?,?,?,?)''', (date, asin, price, title))
    print(f'Added data for {asin}, {price}')

conn.commit()
print('Database committed new entries')