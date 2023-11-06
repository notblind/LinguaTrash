from multiprocessing import Pool

import psycopg2
import requests
from bs4 import BeautifulSoup


class Db:
    __slots__ = ["conn", "cursor"]

    # def __init__(self):
    # 	self.connect()

    def connect(self):
        self.conn = psycopg2.connect(
            host="127.0.0.1",
            database="loco",
            user="younior",
            password="d2513111",
            port="5432",
        )
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

    def insert(self, text):
        self.connect()
        self.cursor.execute(text)
        self.conn.commit()
        self.cursor.close()

    def execute(self, text):
        self.connect()
        self.cursor.execute(text)

        res = self.cursor.fetchall()

        self.cursor.close()

        return res


db = Db()
month = {
    "Января": "01",
    "Февраля": "02",
    "Марта": "03",
    "Апреля": "04",
    "Мая": "05",
    "Июня": "06",
    "Июля": "07",
    "Августа": "08",
    "Сентября": "09",
    "Октября": "10",
    "Ноября": "11",
    "Декабря": "12",
}


def get_html(html):
    return requests.get(html).text


def get_list_tasks(html):
    soup = BeautifulSoup(html, "html.parser")
    lists = soup.find_all("div", class_="list")

    res = []
    for item in lists:
        for i in item.find_all("li"):
            res.append(i.find("a").get("href"))

    return res


def parsing(html):
    soup = BeautifulSoup(html, "html.parser")
    day = soup.find("h1", class_="entry-title").get_text().split("– ")[1]

    d = (day[0] + day[1]).strip()
    if len(d) == 1:
        d = "0" + d
    day_numbers = d + "." + month[day[2:].strip()]

    holidays_list = []
    holidays = soup.find("ul", class_="praznikk").find_all("li")

    for h in holidays:
        holidays_list.append(h.get_text())

    return {"day": day_numbers, "holidays": holidays_list}


def write_in_database(data, db):
    q = "INSERT INTO dayofweek(day_text) VALUES ('" + data["day"] + "');"
    db.insert(q)

    q = "select * from dayofweek where day_text='{}';".format(data["day"])
    day_id = db.execute(q)[0][0]

    for holiday in data["holidays"]:
        q = "INSERT INTO holiday(day_id, description) VALUES ({}, '{}');".format(
            day_id, holiday
        )
        print(q)
        db.insert(q)


def work(task):
    res = parsing(get_html(task))
    write_in_database(res, db)


if __name__ == "__main__":
    list_tasks = get_list_tasks(get_html("https://calendaronline.ru/prazdniki-goda/"))

    # for task in list_tasks:
    # 	res = parsing(get_html(task))
    # 	write_in_database(res, db)

    with Pool(10) as p:
        p.map(work, list_tasks)

    db.disconnect()
