from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests

def createElem(window, text, font, padx, row, column, ipadx, pady=0):
    elem = Label(window, text=text, font=font, padx=padx, pady=pady)
    elem.grid(row=row, column=column, ipadx=ipadx)

    return elem

def about_program():
    messagebox.showinfo(title='О программе', message='Конвертер разные валютных пар.\nВерсия программы: v1.0')

def exite():
    window.destroy()

def exchange():
    try:
        exchangeCalculation()
    except:
        messagebox.showerror(title='Произошла ошибка', message='Проверьте введенные вами данные в поле')

def choose_select(event):
    clearInputFields()

    response = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    if response.status_code == 200:
        JSON = response.json()

        if сombo.get() == 'Рубль':
            usd_buy['text'] = JSON['rates']['USD']
            usd_sale['text'] = round(JSON['rates']['USD'] - (JSON['rates']['USD'] * 1.5 / 100), 6)

            eur_buy['text'] = JSON['rates']['EUR']
            eur_sale['text'] = round(JSON['rates']['EUR'] - (JSON['rates']['EUR'] * 1.5 / 100), 6)

            uah_buy['text'] = JSON['rates']['UAH']
            uah_sale['text'] = round(JSON['rates']['UAH'] - (JSON['rates']['UAH'] * 1.5 / 100), 6)

            rub_buy['text'] = 1
            rub_sale['text'] = 1
        elif сombo.get() == 'Доллар':
            usd_buy['text'] = 1
            usd_sale['text'] = 1

            eur_buy['text'] = round((1 / JSON['rates']['USD']) / (1 / JSON['rates']['EUR']), 6)
            eur_sale['text'] = round(float(eur_buy['text']) - (float(eur_buy['text']) * 1.5 / 100), 6)

            uah_buy['text'] = round((1 / JSON['rates']['USD']) / (1 / JSON['rates']['UAH']), 6)
            uah_sale['text'] = round(float(uah_buy['text']) - (float(uah_buy['text']) * 1.5 / 100), 6)

            rub_buy['text'] = round(1 / JSON['rates']['USD'], 6)
            rub_sale['text'] = round(float(rub_buy['text']) - (float(rub_buy['text']) * 1.5 / 100), 6)
        elif сombo.get() == 'Евро':
            usd_buy['text'] = round((1 / JSON['rates']['EUR']) / (1 / JSON['rates']['USD']), 6)
            usd_sale['text'] = round(float(usd_buy['text']) - (float(usd_buy['text']) * 1.5 / 100), 6)

            eur_buy['text'] = 1
            eur_sale['text'] = 1

            uah_buy['text'] = round((1 / JSON['rates']['EUR']) / (1 / JSON['rates']['UAH']), 6)
            uah_sale['text'] = round(float(uah_buy['text']) - (float(uah_buy['text']) * 1.5 / 100), 6)

            rub_buy['text'] = round(1 / JSON['rates']['EUR'], 6)
            rub_sale['text'] = round(float(rub_buy['text']) - (float(rub_buy['text']) * 1.5 / 100), 6)
        elif сombo.get() == 'Гривна':
            usd_buy['text'] = round((1 / JSON['rates']['UAH']) / (1 / JSON['rates']['USD']), 6)
            usd_sale['text'] = round(float(usd_buy['text']) - (float(usd_buy['text']) * 1.5 / 100), 6)

            eur_buy['text'] = round((1 / JSON['rates']['UAH']) / (1 / JSON['rates']['EUR']), 6)
            eur_sale['text'] = round(float(eur_buy['text']) - (float(eur_buy['text']) * 1.5 / 100), 6)

            uah_buy['text'] = 1
            uah_sale['text'] = 1

            rub_buy['text'] = round(1 / JSON['rates']['UAH'], 6)
            rub_sale['text'] = round(float(rub_buy['text']) - (float(rub_buy['text']) * 1.5 / 100), 6)
    elif response.status_code == 404:
        messagebox.showwarning('Проблемы с соединением по курсам валют!')

def clearInputFields():
    entry_USD_promo.delete(0, END)
    entry_EUR_promo.delete(0, END)
    entry_UAH_promo.delete(0, END)
    entry_RUB_promo.delete(0, END)

def exchangeCalculation():
    entry_USD_promo.insert(0, round(float(entry_forValue.get()) * float(usd_buy['text']), 2))
    entry_EUR_promo.insert(0, round(float(entry_forValue.get()) * float(eur_buy['text']), 2))
    entry_UAH_promo.insert(0, round(float(entry_forValue.get()) * float(uah_buy['text']), 2))
    entry_RUB_promo.insert(0, round(float(entry_forValue.get()) * float(rub_buy['text']), 2))

    if сombo.get() == 'Рубль':
        entry_RUB_promo.delete(0, END)
        entry_RUB_promo.insert(0, float(entry_forValue.get()))
    elif сombo.get() == 'Доллар':
        entry_USD_promo.delete(0, END)
        entry_USD_promo.insert(0, float(entry_forValue.get()))
    elif сombo.get() == 'Евро':
        entry_EUR_promo.delete(0, END)
        entry_EUR_promo.insert(0, float(entry_forValue.get()))
    elif сombo.get() == 'Гривна':
        entry_UAH_promo.delete(0, END)
        entry_UAH_promo.insert(0, float(entry_forValue.get()))


currencys = ["Рубль", "Доллар", "Евро", "Гривна"]

window = Tk()
window.title('Конвертер разных валют')
window.geometry('490x385+300+300')
window.resizable(0, 0)

main_menu = Menu()
info_menu = Menu(tearoff=0)
info_menu.add_command(label="О программе", command=about_program)
info_menu.add_separator()
info_menu.add_command(label="Выход", command=exite)
main_menu.add_cascade(label="Справка", menu=info_menu)
window.config(menu=main_menu)


# Шапка таблицы
createElem(window, 'Валюта', 'Arial 14 bold', 30, 0, 0, 10)
createElem(window, 'Покупка', 'Arial 14 bold', 30, 0, 1, 10)
createElem(window, 'Продажа', 'Arial 14 bold', 30, 0, 2, 10)


# Ячейки таблицы
createElem(window, 'USD', 'Arial 12', 30, 1, 0, 10, pady=5)
usd_buy = createElem(window, '0', 'Arial 12', 30, 1, 1, 10, pady=5)
usd_sale = createElem(window, '0', 'Arial 12', 30, 1, 2, 10, pady=5)

createElem(window, 'EUR', 'Arial 12', 30, 2, 0, 10, pady=5)
eur_buy = createElem(window, '0', 'Arial 12', 30, 2, 1, 10, pady=5)
eur_sale = createElem(window, '0', 'Arial 12', 30, 2, 2, 10, pady=5)

createElem(window, 'UAH', 'Arial 12', 30, 3, 0, 10, pady=5)
uah_buy = createElem(window, '0', 'Arial 12', 30, 3, 1, 10, pady=5)
uah_sale = createElem(window, '0', 'Arial 12', 30, 3, 2, 10, pady=5)

createElem(window, 'RUB', 'Arial 12', 30, 4, 0, 10, pady=5)
rub_buy = createElem(window, '0', 'Arial 12', 30, 4, 1, 10, pady=5)
rub_sale = createElem(window, '0', 'Arial 12', 30, 4, 2, 10, pady=5)


# Создаем селект для выбора валютных пар
frame = Frame(window, pady=20)
frame.grid(row=5, column=0, ipadx=10)
 
сombo = ttk.Combobox(frame, values=currencys)
сombo.set("Выберите валюту")
сombo.pack()
сombo.bind('<<ComboboxSelected>>', choose_select)


# Создаем поле для ввода единиц для обмена
entry_forValue = Entry(window, font='Arial 12', justify=CENTER)
entry_forValue.grid(row=5, column=1, columnspan=3, ipadx=60)

# Создаем кнопку для обмена средств
button_forExchange = Button(window, text='Обмен', bg='#006363', highlightcolor='#1D7373', font='Arial 14 bold', command=exchange)
button_forExchange.grid(row=6, column=1, columnspan=3, ipadx=110)


# Создаем таблицу вывода данных
createElem(window, 'USD:', 'Arial 12', 30, 7, 0, 10, pady=5)
entry_USD_promo = Entry(window, justify=CENTER, font='Arial 12')
entry_USD_promo.grid(row=7, column=1, columnspan=3, ipadx=58)

createElem(window, 'EUR:', 'Arial 12', 30, 8, 0, 10, pady=5)
entry_EUR_promo = Entry(window, justify=CENTER, font='Arial 12')
entry_EUR_promo.grid(row=8, column=1, columnspan=3, ipadx=58)

createElem(window, 'UAH:', 'Arial 12', 30, 9, 0, 10, pady=5)
entry_UAH_promo = Entry(window, justify=CENTER, font='Arial 12')
entry_UAH_promo.grid(row=9, column=1, columnspan=3, ipadx=58)

createElem(window, 'RUB:', 'Arial 12', 30, 10, 0, 10, pady=5)
entry_RUB_promo = Entry(window, justify=CENTER, font='Arial 12')
entry_RUB_promo.grid(row=10, column=1, columnspan=3, ipadx=58)




window.mainloop()