from bs4 import BeautifulSoup
import requests
import sqlite3
import db

index_url = 'https://in.investing.com/indices/major-indices'
INDEX_DATA_SELECTOR = "#js-main-container > section.main-container.container > div > section.instrument.js-section-content > section > div.common-table-wrapper > div > table"


def fetch_response(url):
    response = requests.get(url)
    return response.text


def index_data():
    file = open("C:/Users/jaind/PycharmProjects/MYPROJECT1/index.text", mode='r', encoding='utf-8')
    data = file.read()
    INDEX_DATA_SELECTOR = "#js-main-container > section.main-container.container > div > section.instrument.js-section-content > section > div.common-table-wrapper > div > table > tbody"
    content = fetch_response(index_url)
    soup = BeautifulSoup(str(data), "html.parser")
    # print(soup)
    index_update_all = soup.select(INDEX_DATA_SELECTOR)
    tr = soup.findAll("tr")
    data_to_send = []
    count = 0
    for i in tr:
        if count < 3:
            count = count + 1
            continue
        count = count + 1
        data = i.text.split("\n")
        if len(data) <= 18:
            continue
        if len(data[6]) < 1:
            continue
        data_to_send.append({'index': data[6],
                             'open': data[8],
                             'high': data[10],
                             'low': data[12],
                             'change': data[14],
                             'change percent': data[16],
                             'date': data[18]
                             })
    save_date_to_db(data_to_send)
    return data_to_send


def save_date_to_db(news_data):
    query = "INSERT INTO `index_data` (`id`, `index_number`, `open`, `high`, `low`, `day_change`, `change percent`, `date`) VALUES"
    for news in news_data:
        print(news)
        query = query + " (NULL,'" + news['index'] + "','" + news['open'] + "','" + news['high'] + "','" + news[
            'low'] + "','" + news['change'] + "','" + news['change percent'] + "','" + news['date'] + "'),"
    query = query[:len(query) - 1]
    db_curser = db.mycursor
    db_curser.execute(query)
    db.mydb.commit()


print(index_data())
