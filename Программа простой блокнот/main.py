from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pyperclip


window = Tk()
window.title('Простой блокнот')
# window.iconbitmap('Notepad_22522.ico')
window.geometry('1000x800+100+100')


def open_file():
    """ Функция, которая позволяет открыть нужный нам файл через проводник и вставить его данные в текстовое поле """
    file_path = filedialog.askopenfilename()
    if file_path:
        text_wrap.delete('1.0', END)
        text_file = open(file_path, encoding='utf-8').read()
        text_wrap.insert('1.0', text_file)

def save_file():
    """ Функция, которая позволяет сохранить наш файл в нужное место """
    file_path = filedialog.asksaveasfilename(filetypes=(("Текстовые документы (*.txt)", "*.txt"), ("Все файлы", "*.*")))
    file = open(f'{file_path}.txt', mode='w', encoding='utf-8')
    file.write(text_wrap.get('1.0', END))
    file.close()

def exite_program():
    """ Функция, которая позволяет выйти из программы """
    window.destroy()

def choose_theme(bg, fg, selectbackground, insertbackground):
    """ Функция, которая позволяет изменить цвет темы на указанный """
    text_wrap['bg'] = bg
    text_wrap['fg'] = fg
    text_wrap['selectbackground'] = selectbackground
    text_wrap['insertbackground'] = insertbackground

def info_program():
    """ Функция, позволяющая узнать информацию о программе """
    messagebox.showinfo(title='Информация о программе', message='Текущая версия программы: v1.0')

def show_menu(event):
    """ Функция, которая показывает меню, при клике на правую клавишу мыши """
    click_menu.post(event.x_root, event.y_root)

def copy_text():
    """ Функция, которая позволяет добавить текст в буфер обмена для сохранения """
    pyperclip.copy(text_wrap.selection_get())

def paste_text():
    """ Функция, которая позволяет вставить ранее скопированный текст из буфера """
    text_wrap.insert(INSERT, pyperclip.paste())


# Создание текстового виджета
text_wrap = Text(window, bg='#fff', fg='#000', selectbackground='#ebdae9', insertbackground='#000', font='Arial 14', padx=5, pady=5, wrap=WORD)
text_wrap.place(relheight=1, relwidth=0.99)

# Создание возможности скролить текст, если он не помещается
scroll = Scrollbar(command=text_wrap.yview)
scroll.pack(side=RIGHT, fill=Y)
text_wrap.config(yscrollcommand=scroll.set)

# Создание главного меню
main_menu = Menu(window, tearoff=0)
window.config(menu=main_menu)

# Создание подменю Файл
file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exite_program)

# Создание подменю Разное
different_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Разное', menu=different_menu)
decoration_menu = Menu(different_menu, tearoff=0)
decoration_menu.add_command(label='Светлая', command=lambda: choose_theme('#fff', '#000', '#ebdae9', '#000'))
decoration_menu.add_command(label='Тёмная', command=lambda: choose_theme('#362f35', '#fff', '#cfa7cb', '#665f65'))
decoration_menu.add_command(label='Голубая', command=lambda: choose_theme('#17c4eb', '#17eb53', '#32d1bf', '#308548'))

different_menu.add_cascade(label='Оформление', menu=decoration_menu)
different_menu.add_cascade(label='О программе', command=info_program)


# Создание меню по клику на правую клавишу мыши
text_wrap.bind('<Button-3>', show_menu)
click_menu = Menu(tearoff=0)
click_menu.add_command(label='Копировать', command=copy_text)
click_menu.add_command(label='Вставить', command=paste_text)


window.mainloop()