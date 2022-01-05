"""
Разработайте скрипт на Python, который будет выводить в консоль 
(STDOUT) информацию о предстоящих событиях анонсированных на главной 
странице python.org (Upcoming Events). Вывод информации оформите по 
своему усмотрению. Выбор библиотек на ваше усмотрение.
"""

import requests
from bs4 import BeautifulSoup as bs
from prettytable import PrettyTable

def python_upcoming_events():
    # Подготовим таблицу, в которую будем выводить данные в консоли
    events_table = PrettyTable()
    events_table.field_names = ["№", "Name", "Date", "Location", "More info"]
    
    # Спарсим страницу с предстоящими событиями
    url = "https://www.python.org/events/python-events"
    page = requests.get(url)
    soup = bs(page.text, "html.parser")
    body = soup.find('div', class_ = "shrubbery")
    events_names = body.find_all('li')
    
    # Подготовим данные для таблицы
    for row, event in enumerate(events_names, start = 1):
        name = event.h3.text
        date = event.time.text
        location = event.find('span', class_ = 'event-location').text
        info = 'https://www.python.org' + event.h3.a.get('href')
        events_table.add_row([row, name, date, location, info])

    print(events_table)

python_upcoming_events()
