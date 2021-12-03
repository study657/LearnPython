from tkinter import *

window = Tk()
window.title('Радуга')
window.geometry('600x600+700+300')


wrapper = Label(window, bg='black')
wrapper.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)


window.mainloop()