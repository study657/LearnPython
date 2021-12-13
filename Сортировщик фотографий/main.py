from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import datetime
import os

def instruction_info():
    messagebox.showinfo(title='Инструкция пользования', message='Нажмите на кнопку "указать путь", затем выберите папку, в которой находятся фотографии, которые нуждаются в сортировке.\nЗатем нажмите кнопку "Произвести сортировку"')

def about_program():
    messagebox.showinfo(title='О программе', message='Программа для сортировки изображений по папкам.\nТекущая версия программы v1.0')

def exite():
    window.destroy()

def get_path():
    folder_path = filedialog.askdirectory()
    input_path.insert(0, folder_path)

def sort_start():
    folder_path = input_path.get() # Получаем содержимое в нашем инпуте
    if folder_path:
        try:
            for folder, subfolder, files in os.walk(folder_path):
                for file in files:
                    path = os.path.join(folder, file) # Получаем полный путь к каждому нашему файлу
                    mtime = os.path.getmtime(path) # Получаем время последнего изменения файла, в секундах
                    date = datetime.datetime.fromtimestamp(mtime) # С помощью модуля datetime получаем адекватную дату в нормальном формате
                    date = date.strftime(f'%Y-%m-%d') # Получили дату в таком формате: Год-месяц-число
                    date_folder = os.path.join(folder_path, date) # Получаем полные склеенные пути к нашим папкам
                    if not os.path.exists(date_folder): # Если такой папки в нашем каталоге нет, тогда
                        os.mkdir(date_folder) # Создаем дирректорию под названием нашей папки, т.е. создаем папку там, где работает
                    os.rename(path, os.path.join(date_folder, file)) # Переносим наш файл из дирректории текущей в папку, которую мы только что создали. Однако нужно понимать, что любой файл имеет название не просто файл.расширение, а это ПОЛНЫЙ ПУТЬ К ФАЙЛУ
            else:
                messagebox.showinfo(title='Предупреждение', message='Сортировка прошла успешно!')
        except:
            messagebox.showinfo(title='Предупреждение', message='Вы ввели некорректный путь к папке!')


window = Tk()
window.title('Photo Sort')
window.geometry('600x400+100+100')

main_menu = Menu()
main_menu.add_cascade(label='Справка')

main_menu = Menu(window)
info_menu = Menu(tearoff=0)
info_menu.add_command(label='Инструкция пользования', command=instruction_info)
info_menu.add_command(label='О программе', command=about_program)
info_menu.add_separator()
info_menu.add_command(label='Выход', command=exite)
main_menu.add_cascade(label='Справка', menu=info_menu)
window.config(menu=main_menu)


style = ttk.Style()
style.configure('btn_start.TButton', font=('Helvetica', 15))

frame = Frame(window, bg='#a36767', bd=5)
frame.pack(padx=10, fill=X)

input_path = Entry(frame)
input_path.pack(side=LEFT, expand=TRUE, fill=X, ipady=3)

btn_path = ttk.Button(frame, text='Указать путь', command=get_path)
btn_path.pack(side=LEFT, padx=5)

btn_start = ttk.Button(window, text='Произвести сортировку', style='btn_start.TButton', command=sort_start)
btn_start.pack(pady=10)

window.mainloop()