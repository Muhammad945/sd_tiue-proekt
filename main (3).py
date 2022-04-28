from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('450x330')

canvas = Canvas(root, width=800, height=600)
canvas.pack()


def load_image(name):
    img = Image.open(name)
    img.thumbnail((200, 200), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)


def set_image(image):
    canvas.delete("all")
    canvas.create_image(100, 115, image=image)


image = load_image("room.png")
image2 = load_image("Gone_Home_-_Bedroom.png")
image3 = load_image("images.jpg")
image4 = load_image("лг.jpg")

set_image(image)


def naz():
    t1['text'] = "room"
    set_image(image)


def mag():
    t2['text'] = "gone home"
    set_image(image2)


def kar():
    t3['text'] = "vip"
    set_image(image3)


def mal():
    t4['text'] = "5 stars"
    set_image(image4)



t1 = Label(root, text="Цена: 1 000 000сум")
t1.place(x=200, y=50)

t2 = Label(root, text="Цена: 1 500 000сум")
t2.place(x=200, y=100)

t3 = Label(root, text="Цена: 2 000 000сум")
t3.place(x=200, y=150)

t4 = Label(root, text="Цена: 3 000 000сум")
t4.place(x=200, y=150)

btn1 = Button(root, text="booking", width=25, command=naz)
btn1.place(x=25, y=240)

btn2 = Button(root, text="booking", width=25, command=mag)
btn2.place(x=240, y=240)

btn3 = Button(root, text="booking", width=25, command=kar)
btn3.place(x=25, y=280)

btn4 = Button(root, text="booking", width=25, command=mal)
btn4.place(x=240, y=280)

root.mainloop()