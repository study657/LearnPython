from tkinter import *
from tkinter import messagebox
import requests

def create_label(text, font, bg, row, column, columnspan=1, sticky=''):
    elem = Label(window, text=text, font=font, bg=bg, padx=20)
    elem.grid(row=row, column=column, columnspan=columnspan, sticky=sticky)

    return elem

def start_change():
        try:
            input_value = float(input_forValue.get())
            input_forValueUSD.delete(0, END)
            input_forValueUSD.insert(0, round(input_value * float(label_usd_buy['text']), 2))

            input_forValueEUR.delete(0, END)
            input_forValueEUR.insert(0, round(input_value * float(label_eur_buy['text']), 2))

            input_forValueUAN.delete(0, END)
            input_forValueUAN.insert(0, round(input_value * float(label_uan_buy['text']), 2))
        except:
            messagebox.showerror(title='Ошибка обмена', message='Проверьте правильность ввода данных')

URL_ADRESS = 'https://www.cbr-xml-daily.ru/latest.js'
response = requests.get(URL_ADRESS)
JSON = response.json()

window = Tk()
window.title('Конвертер валют')
window.geometry('335x250+300+300')
window.resizable(0, 0)

create_label('Валюта', 'Arial 12 bold', '#d9cece', 0, 0)
create_label('Покупка', 'Arial 12 bold', '#d9cece', 0, 1)
create_label('Продажа', 'Arial 12 bold', '#d9cece', 0, 2)

create_label('USD', 'Arial 11', '#f7dfdf', 1, 0, 1, EW)
label_usd_buy = create_label(JSON['rates']['USD'], 'Arial 11', '#f7dfdf', 1, 1, 1, EW)
label_usd_sale = create_label(round(JSON['rates']['USD'] - (JSON['rates']['USD'] * 1.5 / 100), 6), 'Arial 11', '#f7dfdf', 1, 2, 1, EW)

create_label('EUR', 'Arial 11', '#d9cece', 2, 0, 1, EW)
label_eur_buy = create_label(JSON['rates']['EUR'], 'Arial 11', '#d9cece', 2, 1, 1, EW)
label_eur_sale = create_label(round(JSON['rates']['EUR'] - (JSON['rates']['EUR'] * 1.5 / 100), 6), 'Arial 11', '#d9cece', 2, 2, 1, EW)

create_label('UAN', 'Arial 11', '#f7dfdf', 3, 0, 1, EW)
label_uan_buy = create_label(JSON['rates']['UAH'], 'Arial 11', '#f7dfdf', 3, 1, 1, EW)
label_uan_sale = create_label(round(JSON['rates']['UAH'] - (JSON['rates']['UAH'] * 1.5 / 100), 6), 'Arial 11', '#f7dfdf', 3, 2, 1, EW)

current_valute = Label(window, text='Рубль:', font='Arial 11 bold', pady=5)
current_valute.grid(row=4, column=0, columnspan=1, sticky=EW)

input_forValue = Entry(window, justify=CENTER)
input_forValue.grid(row=4, column=1, columnspan=2, sticky=EW)


button_change = Button(window, text='Обмен', font='Arial 12 bold', command=start_change)
button_change.grid(row=5, column=1, columnspan=2, sticky=EW)


current_usd = Label(window, text='USD:', font='Arial 11 bold', pady=1)
current_usd.grid(row=7, column=0, columnspan=1, sticky=EW)

input_forValueUSD = Entry(window, justify=CENTER)
input_forValueUSD.grid(row=7, column=1, columnspan=2, sticky=EW)

current_eur = Label(window, text='EUR:', font='Arial 11 bold', pady=1)
current_eur.grid(row=8, column=0, columnspan=1, sticky=EW)

input_forValueEUR = Entry(window, justify=CENTER)
input_forValueEUR.grid(row=8, column=1, columnspan=2, sticky=EW)

current_uan = Label(window, text='UAN:', font='Arial 11 bold', pady=1)
current_uan.grid(row=9, column=0, columnspan=1, sticky=EW)

input_forValueUAN = Entry(window, justify=CENTER)
input_forValueUAN.grid(row=9, column=1, columnspan=2, sticky=EW)

window.mainloop()