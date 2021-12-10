from tkinter import *
from datetime import datetime

window = Tk()
window.title('Часы')
window.geometry('200x60+100+100')
window.resizable(0, 0)

def set_time():
    """ Функция, которая будет устанавливать время в наше окно виджета """
    window.after(200, set_time)
    time = datetime.today().strftime("%H:%M:%S")
    label['text'] = time

label = Label(window, text='', bg='#baaa59', font=('Arial Bold', 20), padx=10, pady=10)
label.pack(fill=BOTH)
set_time()

window.mainloop()