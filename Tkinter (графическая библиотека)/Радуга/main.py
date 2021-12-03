from tkinter import *

window = Tk()
window.title('Радуга')
window.geometry('+700+300')

color_label = Label(window, text='')
color_label.pack(fill=BOTH)

hash_entry = Entry(window, justify=CENTER)
hash_entry.insert(0, '')
hash_entry.pack()

# Не совсем правильный метод подхода, т.е. дублировать функции глупо

# def red():
#     hash_entry.delete(0, END)
#     color_label['text'] = 'Красный'
#     hash_entry.insert(0, btn_red['bg'])

# def orange():
#     hash_entry.delete(0, END)
#     color_label['text'] = 'Оранжевый'
#     hash_entry.insert(0, btn_orange['bg'])

# def yellow():
#     hash_entry.delete(0, END)
#     color_label['text'] = 'Желтый'
#     hash_entry.insert(0, btn_yellow['bg'])

# def green():
#     hash_entry.delete(0, END)
#     color_label['text'] = 'Зеленый'
#     hash_entry.insert(0, btn_green['bg'])

# def cyan():
#     hash_entry.delete(0, END)
#     color_label['text'] = 'Голубой'
#     hash_entry.insert(0, btn_cyan['bg'])

# def blue():
#     hash_entry.delete(0, END)
#     color_label['text'] = 'Синий'
#     hash_entry.insert(0, btn_blue['bg'])

# def purple():
#     hash_entry.delete(0, END)
#     color_label['text'] = 'Фиолетовый'
#     hash_entry.insert(0, btn_purple['bg'])


# btn_red = Button(window, bg='#ff0000', pady=1, command=red)
# btn_red.pack(fill=BOTH)

# btn_orange = Button(window, bg='#ffa500', pady=1, command=orange)
# btn_orange.pack(fill=BOTH)

# btn_yellow = Button(window, bg='#ffff00', pady=1, command=yellow)
# btn_yellow.pack(fill=BOTH)

# btn_green = Button(window, bg='#008000', pady=1, command=green)
# btn_green.pack(fill=BOTH)

# btn_cyan = Button(window, bg='#0000ff', pady=1, command=cyan)
# btn_cyan.pack(fill=BOTH)

# btn_blue = Button(window, bg='#4b0082', pady=1, command=blue)
# btn_blue.pack(fill=BOTH)

# btn_purple = Button(window, bg='#ee82ee', pady=1, command=purple)
# btn_purple.pack(fill=BOTH)




# Более грамотный метод решения данной задачи, однако все равно происходит дублирование кода

# def get_color(color, hex_color):
#     hash_entry.delete(0, END)
#     color_label['text'] = color
#     hash_entry.insert(0, hex_color)


# btn_red = Button(window, bg='#ff0000', pady=1, command=lambda: get_color('Красный', btn_red['bg']))
# btn_red.pack(fill=BOTH)

# btn_orange = Button(window, bg='#ffa500', pady=1, command=lambda: get_color('Оранжевый', btn_orange['bg']))
# btn_orange.pack(fill=BOTH)

# btn_yellow = Button(window, bg='#ffff00', pady=1, command=lambda: get_color('Жёлтый', btn_yellow['bg']))
# btn_yellow.pack(fill=BOTH)

# btn_green = Button(window, bg='#008000', pady=1, command=lambda: get_color('Зелёный', btn_green['bg']))
# btn_green.pack(fill=BOTH)

# btn_cyan = Button(window, bg='#0000ff', pady=1, command=lambda: get_color('Голубой', btn_cyan['bg']))
# btn_cyan.pack(fill=BOTH)

# btn_blue = Button(window, bg='#4b0082', pady=1, command=lambda: get_color('Синий', btn_blue['bg']))
# btn_blue.pack(fill=BOTH)

# btn_purple = Button(window, bg='#ee82ee', pady=1, command=lambda: get_color('Фиолетовый', btn_purple['bg']))
# btn_purple.pack(fill=BOTH)




# Более упрощенный и грамотный подход, а так же значительно короче предыдущих

# colors = {
#     '#ff0000': 'Красный',
#     '#ffa500': 'Оранжевый',
#     '#ffff00': 'Жёлтый',
#     '#008000': 'Зелёный',
#     '#0000ff': 'Голубой',
#     '#4b0082': 'Синий',
#     '#ee82ee': 'Фиолетовый',
# }

# def get_color(color, hex_color):
#     hash_entry.delete(0, END)
#     color_label['text'] = color
#     hash_entry.insert(0, hex_color)

# for key in colors:
#     Button(window, bg=key, pady=1, command=lambda colors=colors[key], hex=key: get_color(colors, hex)).pack(fill=BOTH) # Нужно понимать, что если бы мы не приравняли вновь созданные переменные к lambda функции, то тогда мы бы получали всегда цвета последней кнопки. А по скольку теперь у нас каждая кнопочка ссылается на свою переменную в параметре самой lambda функции, то и присваивается ей соответствующий цвет по порядку из цикла




# ООП подход

colors = {
    '#ff0000': 'Красный',
    '#ffa500': 'Оранжевый',
    '#ffff00': 'Жёлтый',
    '#008000': 'Зелёный',
    '#0000ff': 'Голубой',
    '#4b0082': 'Синий',
    '#ee82ee': 'Фиолетовый',
}

class Button_color:
    def  __init__(self, window, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.button = Button(window, bg=hex_color, pady=1, command=self.set_color)
        self.button.pack(fill=X)

    def set_color(self):
        hash_entry.delete(0, END)
        color_label['text'] = self.text_color
        hash_entry.insert(0, self.hex_color)


for key in colors:
    Button_color(window, colors[key], key)


window.mainloop()