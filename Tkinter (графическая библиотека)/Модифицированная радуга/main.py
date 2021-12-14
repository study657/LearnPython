from tkinter import *

window = Tk()
window.title('Радуга')
window.geometry('370x100+300+300')
window.resizable(0, 0)

lable_color = Label(window, bg='#000', height=2)
lable_color.pack(fill=X, pady=5)

def change_color(event):
    lable_color['bg'] = event.widget['bg']

def white_color(event):
    lable_color['bg'] = '#fff'

def create_elem(color):
    elem = Label(window, bg=color, height=3, width=6)
    elem.pack(side=LEFT, padx=2)
    elem.bind('<Button-1>', lambda event: change_color(event))
    elem.bind('<Button-3>', white_color)

create_elem('#FF0000')
create_elem('#FF7F00')
create_elem('#FFFF00')
create_elem('#00FF00')
create_elem('#0000FF')
create_elem('#4B0082')
create_elem('#9400D3')

window.mainloop()