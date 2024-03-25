from tkinter import *


def calculate():
    mile = float(entry.get())
    km = round(mile * 1.6, 2)
    km_result_label.config(text=f'{km}')


window = Tk()
window.title('mile to km converter')
window.config(width=350, height=200)

is_equal_to_label = Label(text='is equal to')
is_equal_to_label.place(x=20, y=70)

entry = Entry(width=10)
entry.focus()
entry.place(x=100, y=40)

miles_label = Label(text='Miles')
miles_label.place(x=210, y=40)

km_label = Label(text='Km')
km_label.place(x=210, y=70)

km_result_label = Label(text='0')
km_result_label.place(x=140, y=70)

button = Button(text='Calculate', command=calculate)
button.place(x=100, y=100)

window.mainloop()

