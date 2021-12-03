from tkinter import *

window = Tk()
window.title('Размещение кнопок калькулятора')
window.geometry('300x500+700+300')

wrapper = Frame(window)
wrapper.pack()

# btn1 = Button(wrapper, text='7', padx=20, pady=20).grid(row=0, column=0)
# btn2 = Button(wrapper, text='8', padx=20, pady=20).grid(row=0, column=1)
# btn3 = Button(wrapper, text='9', padx=20, pady=20).grid(row=0, column=2)

# btn4 = Button(wrapper, text='4', padx=20, pady=20).grid(row=1, column=0)
# btn5 = Button(wrapper, text='5', padx=20, pady=20).grid(row=1, column=1)
# btn6 = Button(wrapper, text='6', padx=20, pady=20).grid(row=1, column=2)

# btn7 = Button(wrapper, text='1', padx=20, pady=20).grid(row=2, column=0)
# btn8 = Button(wrapper, text='2', padx=20, pady=20).grid(row=2, column=1)
# btn9 = Button(wrapper, text='3', padx=20, pady=20).grid(row=2, column=2)

# btn10 = Button(wrapper, text='0', padx=20, pady=20).grid(row=3, column=1)

row = 0
column = 0

buttons = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0',
]

for btn in buttons:
    if btn == '0':
        Button(wrapper, text=btn, padx=20, pady=20).grid(row=3, column=1)
    else:
        Button(wrapper, text=btn, padx=20, pady=20).grid(row=row, column=column)
        column += 1
        if column == 3:
            column = 0
            row += 1

window.mainloop()