from tkinter import messagebox
from tkinter import *

def exite():
    window.destroy()

def info_program():
    messagebox.showinfo(title='Информация о программе', message='Простенький калькулятор для рассчета не сложных выражений')

def ver_program():
    messagebox.showinfo(title='Версия программы', message='Текущая версия программы: v1.0')

def createButton(text, fg, x, y, func1='', func2=''):
    button = Button(window, text=text, font='Arial 18 bold', fg=fg, bg='#3b3636', height=2, width=5, command=func2)
    button.place(relheight=0.12, relwidth=0.25, x=x, y=y)
    button.bind('<Button-1>', func1)
    entry.bind('<Return>', result_expression)

    return button

def button_mission(event):
    entry.insert(END, event.widget['text'])

def delete_input():
    entry.delete(0, END)
    label['text'] = ''

def result_expression(event=''):
    try:
        expression = entry.get()
        if entry.get().find('÷') != -1:
            expression = entry.get().replace('÷', '/')
        elif entry.get().find('×') != -1:
            expression = entry.get().replace('×', '*')

        label['text'] = eval(expression)
        entry.delete(0, END)
        entry.insert(END, label['text'])
    except:
        entry.delete(0, END)
        label['text'] = ''
        messagebox.showerror(title='Ошибка', message='Вы допустили ошибку')

def result_percent():
    try:
        label['text'] = float(entry.get().replace('%', '')) / 100
        entry.delete(0, END)
        entry.insert(END, label['text'])
    except:
        entry.delete(0, END)
        label['text'] = ''
        messagebox.showinfo(title='Предупреждение', message='Для того, чтобы рассчитать процент от числа, пожалуйста введите сначала число процента, а затем действие над ним.\nНапример: 5%×100')


def test():
    print('sdfsdfsd')

window = Tk()
window.title('Калькулятор')
window.geometry('307x480+700+100')
window.resizable(0, 0)
window.config(bg='#383030')

main_menu = Menu()
info_menu = Menu(tearoff=0)
info_menu.add_command(label="Информация о программе", command=info_program)
info_menu.add_command(label="Версия программы", command=ver_program)
info_menu.add_separator()
info_menu.add_command(label="Выход", command=exite)
main_menu.add_cascade(label="Справка", menu=info_menu)
window.config(menu=main_menu)

entry = Entry(window, bg='#1c1a1a', fg='#fff', font='Helvetica 25 bold', insertbackground='#fff')
entry.place(relheight=0.2, relwidth=1)

label = Label(window, text='', bg='#1c1a1a', fg='#fff', font='Arial 16 bold', justify=LEFT)
label.place(relheight=0.1, relwidth=1, y=102)

createButton('C', 'red', 0, 165, func2=delete_input)
createButton('(', '#fff', 77, 165, button_mission)
createButton(')', '#fff', 154, 165, button_mission)
createButton('÷', '#3e2bba', 231, 165, button_mission)

createButton('7', '#fff', 0, 226, button_mission)
createButton('8', '#fff', 77, 226, button_mission)
createButton('9', '#fff', 154, 226, button_mission)
createButton('×', '#3e2bba', 231, 226, button_mission)

createButton('4', '#fff', 0, 287, button_mission)
createButton('5', '#fff', 77, 287, button_mission)
createButton('6', '#fff', 154, 287, button_mission)
createButton('-', '#3e2bba', 231, 287, button_mission)

createButton('1', '#fff', 0, 348, button_mission)
createButton('2', '#fff', 77, 348, button_mission)
createButton('3', '#fff', 154, 348, button_mission)
createButton('+', '#3e2bba', 231, 348, button_mission)

createButton('0', '#fff', 0, 409, button_mission)
createButton('.', '#fff', 77, 409, button_mission)
createButton('%', '#fff', 154, 409, func2=result_percent)
createButton('=', '#3e2bba', 231, 409, func2=result_expression)


window.mainloop()