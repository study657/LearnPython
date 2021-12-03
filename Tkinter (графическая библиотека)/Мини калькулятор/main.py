from tkinter import *

window = Tk()
window.title('Мини калькулятор')
window.iconbitmap('1486504349-calculate-calculation-education-business-calculator-math_81324.ico')
window.geometry('500x300+500+300')

num1 = 10
num2 = 5

def pluse():
    print(num1 + num2)

def minus():
    print(num1 - num2)

def multiply():
    print(num1 * num2)

def divide():
    print(int(num1 / num2))

btn_plus = Button(window, text='+', bg='#eb3838', padx=10, pady=5, command=pluse)
btn_plus.pack(fill=BOTH)

btn_minus = Button(window, text='-', bg='#4771c4', padx=10, pady=5, command=minus)
btn_minus.pack(fill=BOTH)

btn_multiply = Button(window, text='*', bg='#20bd5f', padx=10, pady=5, command=multiply)
btn_multiply.pack(fill=BOTH)

btn_divide = Button(window, text='/', bg='#ebc50c', padx=10, pady=5, command=divide)
btn_divide.pack(fill=BOTH)


window.mainloop()