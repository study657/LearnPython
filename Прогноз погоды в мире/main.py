from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle
import datetime
import requests

API_KEY = '1e3374e388e5148b3d7f6b9f74949d8e'

def instruction():
    messagebox.showinfo(title='Инструкция использования программы', message='Введите в поле название города или страны, например Москва (moscow). Далее нажмите на кнопку "Запрос погоды" или на клавишу "Enter". Так же после названия города вы можете через запятую (без пробелов) указать код страны, например: odessa,UK\nВ таком случае прогноз будет более детальный')

def about_program():
    messagebox.showinfo(title='О программе', message='Прогноз погоды в мире.\nВерсия программы: v1.0')

def exit():
    window.destroy()

def start_program(event=''):
    input_text = input_person.get()
    if input_text:
        req = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={input_text}&lang=ru&appid={API_KEY}')
        if req.status_code == 200:
            JSON = req.json()
            
            name_country = 'Местоположение: ' + JSON['name'] + ', ' + JSON['sys']['country']
            temperature = 'Температура: ' + str(int(round(1.8 * (JSON['main']['temp'] - 273), 0))) + ' °C'
            pressure = 'Атм. давление: ' + str(JSON['main']['pressure']) + ' гПа'
            humidity = 'Влажность: ' + str(JSON['main']['humidity']) + '%'
            speed = 'Скорость ветра: ' + str(JSON['wind']['speed']) + ' м/с'
            description = 'Погодные условия: ' + str(JSON['weather'][0]['description'])
            sunrise = 'Восход: ' + datetime.datetime.strftime(datetime.datetime.fromtimestamp(JSON['sys']['sunrise']), '%H:%M:%S')
            sunset = 'Закат: ' + datetime.datetime.strftime(datetime.datetime.fromtimestamp(JSON['sys']['sunset']), '%H:%M:%S')
            
            label['text'] = f'{name_country}\n{temperature}\n{pressure}\n{humidity}\n{speed}\n{description}\n{sunrise}\n{sunset}'
        else:
            messagebox.showerror(title='Ошибка получения данных', message='Пожалуйста, проверьте введенный вами город')

window = Tk()
window.title('Прогноз погоды в мире')
window.geometry('600x400+300+300')

style = ThemedStyle()
current_theme = style.theme_use('plastik')

main_menu = Menu()
info_menu = Menu(tearoff=0)
info_menu.add_command(label='Инструкция пользования', command=instruction)
info_menu.add_command(label='О программе', command=about_program)
info_menu.add_separator()
info_menu.add_command(label='Выход', command=exit)
main_menu.add_cascade(label='Справка', menu=info_menu)
window.config(menu=main_menu)


input_person = ttk.Entry(window, font='Arial 13 bold', justify=CENTER)
input_person.place(relheight=0.1, relwidth=0.65, relx=0.06, y=15)
input_person.bind('<Return>', start_program)

button_start = ttk.Button(window, text='Запрос погоды', command=start_program)
button_start.place(relheight=0.1, relwidth=0.2, relx=0.73, y=15)

label = Label(window, bg='#a69a9a', font='Helvetica 15 bold', pady=3, padx=3, anchor=NW, justify=LEFT)
label.place(relheight=0.8, relwidth=0.87, relx=0.06, y=70)

window.mainloop()