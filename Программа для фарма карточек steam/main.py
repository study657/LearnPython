import steam.webauth as wa
import requests

def OnAppVoteClick(voteid, appid, source):
    post_param=[('sessionid', user.session_id), ('voteid', voteid), ('appid', appid), ('source', source)] # Параметры, которые требует запрос из сайта, посмотреть это можно в браузере через network
    response = requests.post('https://store.steampowered.com/salevote', data=post_param, cookies=user.session.cookies) # POST запрос к сайту с параметрами и т.к. регистрация, то добавляем куки, которые берем из сессии пользователя
    print(response)

lines_fromFile = 25 # Количество строчек из файла аккаунтов

file = open('Аккаунты для карточек.txt', 'r')

for i in range(1, lines_fromFile + 1):
    str = next(file)
    login = str.split(':')[0]
    password = str.split(':')[1].replace('\n', '')

    user = wa.WebAuth(login)
    user.cli_login(password=password)
    user.session.get('https://store.steampowered.com')

    OnAppVoteClick('61', '1091500', '2')
    OnAppVoteClick('62', '1402320', '3')
    OnAppVoteClick('63', '252490', '2')
    OnAppVoteClick('64', '1240440', '2')
    OnAppVoteClick('65', '860510', '2')
    OnAppVoteClick('66', '1195290', '2')
    OnAppVoteClick('67', '1325200', '2')
    OnAppVoteClick('68', '1382330', '2')
    OnAppVoteClick('69', '1196590', '2')
    OnAppVoteClick('70', '1248130', '2')
else:
    print('Все аккаунты получили карточки!')