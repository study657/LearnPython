from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests


def create_trio_elems(label_text, row, column, label_padx, entry_row, entry_column, infoButton_row, infoButton_column, message, entry_width=40):
    label = Label(window, text=label_text, font='Arial 12 bold')
    label.grid(row=row, column=column, padx=label_padx)

    entry = Entry(window, font='Arial 12 bold', bg='#413b45', fg='#7fe016', justify=CENTER, width=entry_width)
    entry.grid(row=entry_row, column=entry_column)

    infoButton = Button(window, text='?', font='Arial 10 bold', bg='#413b45', fg='#fc0000', justify=CENTER, width=2, bd=0, pady=0, command=lambda: info_button(message))
    infoButton.grid(row=infoButton_row, column=infoButton_column, padx=5)

    return entry

def info_button(message):
    messagebox.showinfo(title='Информация о данном поле', message=message)

def about_program():
    messagebox.showinfo(title='О программе', message='Программа, которая позволяет пользователю парсить любые сайты, если вы хоть немного знакомы с HTML версткой')

def exite():
    window.destroy()

def start_parsing():
    button_start['state'] = DISABLED
    if general_elem.get() != '':
        general_elems = general_elem.get().split(',')

        response = requests.get(f'{link_page.get()}')
        soup = BeautifulSoup(response.text, 'html.parser')
        general_elems = general_elem.get().split(',')
        elems = soup.find_all(general_elems[0].lstrip(), class_=general_elems[1].lstrip())

        result = []
        curr = 0

        if auxiliary_elem1.get() != '':
            auxiliary_elems1 = auxiliary_elem1.get().split(',')
            auxiliary_elems2 = auxiliary_elem2.get().split(',')
            auxiliary_elems3 = auxiliary_elem3.get().split(',')
            auxiliary_elems4 = auxiliary_elem4.get().split(',')
            auxiliary_elems5 = auxiliary_elem5.get().split(',')

            for item in elems:
                result.append({
                    'title1': item.find(auxiliary_elems1[0].lstrip(), class_=auxiliary_elems1[1].lstrip()).get_text(strip=True),
                    'title2': '',
                    'title3': '',
                    'title4': '',
                    'title5': ''
                })
                if auxiliary_elem2.get() != '':
                    result[curr]['title2'] = item.find(auxiliary_elems2[0].lstrip(), class_=auxiliary_elems2[1].lstrip()).get_text(strip=True)
                if auxiliary_elem3.get() != '':
                    result[curr]['title3'] = item.find(auxiliary_elems3[0].lstrip(), class_=auxiliary_elems3[1].lstrip()).get_text(strip=True)
                if auxiliary_elem4.get() != '':
                    result[curr]['title4'] = item.find(auxiliary_elems4[0].lstrip(), class_=auxiliary_elems4[1].lstrip()).get_text(strip=True)
                if auxiliary_elem5.get() != '':
                    result[curr]['title5'] = item.find(auxiliary_elems5[0].lstrip(), class_=auxiliary_elems5[1].lstrip()).get_text(strip=True)

                curr += 1

            file = open(f'page.txt', 'w', encoding='utf-8')

            pref1 = ''
            pref2 = ''
            pref3 = ''
            pref4 = ''
            pref5 = ''

            if testFor_general_auxiliary_elem.get() != '':
                pref1 = '\n'
            if testFor_auxiliary_elem2.get() != '':
                pref2 = '\n'
            if testFor_auxiliary_elem3.get() != '':
                pref3 = '\n'
            if testFor_auxiliary_elem4.get() != '':
                pref4 = '\n'
            if testFor_auxiliary_elem5.get() != '':
                pref5 = '\n'

            for item in result:
                file.write(f'''{testFor_general_auxiliary_elem.get()}{pref1}{testFor_auxiliary_elem1.get()} {item["title1"]}\n{testFor_auxiliary_elem2.get()} {item["title2"]}{pref2}{testFor_auxiliary_elem3.get()} {item["title3"]}{pref3}{testFor_auxiliary_elem4.get()} {item["title4"]}{pref4}{testFor_auxiliary_elem5.get()} {item["title5"]}{pref5}\n{separator_elems.get()}\n''')
            file.close()
        else:
            button_start['state'] = NORMAL
            messagebox.showwarning(title='Предупреждение', message='Поле 1.Вложенные элементы для поиска в основном теге(тег, класс) не может быть пустым!')
        button_start['state'] = NORMAL
        messagebox.showinfo(title='Оповещение', message='Парсинг прошел успешно, ищите в папке файлик с данными!')
    else:
        button_start['state'] = NORMAL
        messagebox.showwarning(title='Предупреждение', message='Поле основной элемент для поиска на странице (тег, класс) не может быть пустым!')


window = Tk()
window.title('Универсальный парсер сайтов')
window.geometry('1000x500+500+300')
window.resizable(0, 0)


main_menu = Menu()
info_menu = Menu(tearoff=0)
info_menu.add_command(label="О программе", command=about_program)
info_menu.add_separator()
info_menu.add_command(label="Выход", command=exite)
 
main_menu.add_cascade(label="Справка", menu=info_menu)
window.config(menu=main_menu)


link_page = create_trio_elems('Ссылка на сайт:', 0, 0, 30, 0, 1, 0, 2, 'Поле для ввода ссылки на сайт, например:\nhttps://www.ua-football.com/sport')
general_elem = create_trio_elems('Основной элемент для поиска на странице (тег, класс)', 2, 0, 30, 2, 1, 2, 2, 'Введите сюда тег и класс (через запятую) основного элемента, с которого вы желаете получить информацию, например:\ndiv, show_info')
auxiliary_elem1 = create_trio_elems('1.Вложенные элементы для поиска в основном теге(тег, класс)', 3, 0, 30, 3, 1, 3, 2, 'Введите сюда вложенные теги и класс (через запятую) элементов, которые вы бы хотели получать с сайта, например:\nspan, price_info')
auxiliary_elem2 = create_trio_elems('2.Вложенные элементы для поиска в основном теге(тег, класс)', 4, 0, 30, 4, 1, 4, 2, 'Введите сюда вложенные теги и класс (через запятую) элементов, которые вы бы хотели получать с сайта, например:\nspan, price_info')
auxiliary_elem3 = create_trio_elems('3.Вложенные элементы для поиска в основном теге(тег, класс)', 5, 0, 30, 5, 1, 5, 2, 'Введите сюда вложенные теги и класс (через запятую) элементов, которые вы бы хотели получать с сайта, например:\nspan, price_info')
auxiliary_elem4 = create_trio_elems('4.Вложенные элементы для поиска в основном теге(тег, класс)', 6, 0, 30, 6, 1, 6, 2, 'Введите сюда вложенные теги и класс (через запятую) элементов, которые вы бы хотели получать с сайта, например:\nspan, price_info')
auxiliary_elem5 = create_trio_elems('5.Вложенные элементы для поиска в основном теге(тег, класс)', 7, 0, 30, 7, 1, 7, 2, 'Введите сюда вложенные теги и класс (через запятую) элементов, которые вы бы хотели получать с сайта, например:\nspan, price_info')

label = Label(window, text='Вывод данных с парсинга:', font='Arial 15 bold', fg='#823b8a', pady=10)
label.grid(row=8, column=0, columnspan=3)

testFor_general_auxiliary_elem = create_trio_elems('Основной заголовок', 9, 0, 30, 9, 1, 9, 2, 'Здесь вам нужно написать текст для того, чтобы понимать, что вы получили с вложенного элемента под номером 1')
testFor_auxiliary_elem1 = create_trio_elems('1.Заголовок для вложенного элемента', 10, 0, 30, 10, 1, 10, 2, 'Здесь вам нужно написать текст для того, чтобы понимать, что вы получили с вложенного элемента под номером 1')
testFor_auxiliary_elem2 = create_trio_elems('2.Заголовок для вложенного элемента', 11, 0, 30, 11, 1, 11, 2, 'Здесь вам нужно написать текст для того, чтобы понимать, что вы получили с вложенного элемента под номером 2')
testFor_auxiliary_elem3 = create_trio_elems('3.Заголовок для вложенного элемента', 12, 0, 30, 12, 1, 12, 2, 'Здесь вам нужно написать текст для того, чтобы понимать, что вы получили с вложенного элемента под номером 3')
testFor_auxiliary_elem4 = create_trio_elems('4.Заголовок для вложенного элемента', 13, 0, 30, 13, 1, 13, 2, 'Здесь вам нужно написать текст для того, чтобы понимать, что вы получили с вложенного элемента под номером 4')
testFor_auxiliary_elem5 = create_trio_elems('5.Заголовок для вложенного элемента', 14, 0, 30, 14, 1, 14, 2, 'Здесь вам нужно написать текст для того, чтобы понимать, что вы получили с вложенного элемента под номером 5')
separator_elems = create_trio_elems('Разделитель, между спаршенными данными', 15, 0, 30, 15, 1, 15, 2, 'Здесь вам нужно поставить разделитель между спаршенными даннымми, например вот такой:\n*****************************')

button_start = Button(window, text='Запустить парсинг', font='Arial 12 bold', bg='#413b45', fg='#ffa929', padx=50, command=start_parsing)
button_start.grid(row=16, column=0, columnspan=3, pady=20)


window.mainloop()