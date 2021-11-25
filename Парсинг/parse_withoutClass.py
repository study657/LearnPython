from bs4 import BeautifulSoup
import requests

total_page = 5 # Количество страниц для парсинга с указанного сайта

for i in range(1, total_page + 1):
    response = requests.get(f'https://www.ua-football.com/sport?page={i}')
    soup = BeautifulSoup(response.text, 'html.parser')
    news = soup.find_all('li', class_='liga-news-item')

    result = []

    for item in news:
        result.append({
            'title': item.find('span', class_='d-block').get_text(strip=True),
            'decs': item.find('span', class_='name-dop').get_text(strip=True)
        })

    file = open(f'page{i}.txt', 'w', encoding='utf-8')
    page = 1

    for item in result:
        file.write(f'Новость №{page}\nНазвание: {item["title"]}\nОписание: {item["decs"]}\n\n*************************************\n')
        page += 1
    file.close()
else:
    print('Parsing FINISH')