import steam.webauth as wa
import requests

def count_lines(filename, chunk_size=1<<13):
    """ Функция, позволяющая получить кол-во строчек в файле с аккаунтами, таким образом мы узнаем кол-во аккаунтов, которые там находятся """
    with open(filename) as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))

quantity_accounts = count_lines('Аккаунты.txt') + 1 # Получили общее кол-во аккаунтов из файла


file = open('Аккаунты.txt', 'r')

for i in range(1, quantity_accounts + 1):
    str = next(file)
    login = str.split(':')[0]
    password = str.split(':')[1].replace('\n', '')

    user = wa.WebAuth(login)
    session = user.cli_login(password)
    session.get('https://store.steampowered.com/points/shop')

    data = requests.get('https://store.steampowered.com/points/shop', cookies=user.session.cookies).text # Получили все содержимое страницы в виде строки по указанному url адресу
    start_pos = data.find("&quot;webapi_token&quot;:&quot;") + 31 # Ищет нам подстроку "&quot;webapi_token&quot;:&quot;" в строке data, а затем мы получаем эту самую подстроку добавляя к ней 31 симвл (длина нашей строки, которую ищем)
    end_post = data.find("&", start_pos) # Ищем докуда нам нужно отрезать
    webapi_token = data[start_pos:end_post] # Далее вырезаем из нашей строки нужный нам access_token

    response = requests.post('https://api.steampowered.com/ISaleItemRewardsService/ClaimItem/v1?access_token=' + webapi_token, data={'input_protobuf_encoded' : ''}, cookies=user.session.cookies) # Параметр data={'input_protobuf_encoded' : ''} является не обязательным, т.к. возвращает пустоту, но все же желательно его оставить
    
    if response.status_code == 200:
        print(f'Аккаунт {login} успешно получил стикер!')
    else:
        print(f'У аккаунта {login} возникла ошибка при получении стикера!')
else:
    print('Все аккаунты из файла получили стикер!')

file.close()