from tkinter import *

def setting():
    if e4.get() == "":
        x = 0
    if e4.get() != "":
        D = e4.get()
        if D == "Forward":
            x = 0
        if D == "Right":
            x = 1
        if D == "Back":
            x = 2
        if D == "Left":
            x = 3
    return x

def changeD(x):
    if x == 0:
        D = 'Forward'
    if x == 1:
        D = 'Right'
    if x == 2:
        D = 'Back'
    if x == 3:
        D = 'Left'
    return D

def turn_right():
    x = (setting() + 1) % 4
    e3.delete(0,END)
    e3.insert(0,"Right")
    D = changeD(x)
    e4.delete(0,END)
    e4.insert(0,D)


def turn_left():
    x = (setting() + 3) % 4
    e3.delete(0,END)
    e3.insert(0,"Left")
    D = changeD(x)
    e4.delete(0,END)
    e4.insert(0,D)


def turn_back():
    x = (setting() + 2) % 4
    e3.delete(0,END)
    e3.insert(0,"Back")
    D = changeD(x)
    e4.delete(0,END)
    e4.insert(0,D)

def move_setting():
    if e1.get() != "" and e2.get() !="":
        px, py = int(e1.get()), int(e2.get())
    if e1.get() == "" and e2.get() =="":
        if e5.get() == "" and e6.get() =="":
            px, py = 0, 0
        else:
            px, py = int(e5.get()), int(e6.get())
    e1.delete(0,END)
    e2.delete(0,END)
    return px, py

def move_forward():
    px, py = move_setting()
    if e4.get() == 'Forward':
        py +=1
    if e4.get() == 'Right':
        px += 1
    if e4.get() == 'Back':
        py -= 1
    if e4.get() == 'Left':
        px -= 1
    e5.delete(0,END)
    e5.insert(0,px)
    e6.delete(0,END)
    e6.insert(0,py)

def move_right():
    px, py = move_setting()
    if e4.get() == 'Forward':
        px +=1
    if e4.get() == 'Right':
        py -= 1
    if e4.get() == 'Back':
        px -= 1
    if e4.get() == 'Left':
        py += 1
    e5.delete(0,END)
    e5.insert(0,px)
    e6.delete(0,END)
    e6.insert(0,py)

def move_back():
    px, py = move_setting()
    if e4.get() == 'Forward':
        py -=1
    if e4.get() == 'Right':
        px -= 1
    if e4.get() == 'Back':
        py += 1
    if e4.get() == 'Left':
        px += 1
    e5.delete(0,END)
    e5.insert(0,px)
    e6.delete(0,END)
    e6.insert(0,py)

def move_left():
    px, py = move_setting()
    if e4.get() == 'Forward':
        px -=1
    if e4.get() == 'Right':
        py += 1
    if e4.get() == 'Back':
        px += 1
    if e4.get() == 'Left':
        py -= 1
    e5.delete(0,END)
    e5.insert(0,px)
    e6.delete(0,END)
    e6.insert(0,py)


mado = Tk()
c1 = Canvas(mado, bg='white', width=500, height=500)
c1.pack(side=LEFT)
f1 = Frame(mado, width=300, height=500)
f1.pack(side=LEFT)
l1= Label(f1, text='start pos of x')
l1.grid(row=0, column=0)
e1 = Entry(f1)
e1.grid(row=0, column=2)
l2= Label(f1, text='start pos of y')
l2.grid(row=1, column=0)
e2 = Entry(f1)
e2.grid(row=1, column=2)
b0 = Button(f1, bg='SteelBlue1', text='enter the data')
b1 = Button(f1, bg='SteelBlue1', text='turn right', command=turn_right)
b1.grid(row=2, column=0)
b2 = Button(f1, bg='SteelBlue1', text='turn left', command=turn_left)
b2.grid(row=2, column=2)
b3 = Button(f1, bg='SteelBlue1', text='turn back', command=turn_back)
b3.grid(row=2, column=4)
b4 = Button(f1, bg='SteelBlue1', text='move forward', command=move_forward)
b4.grid(row=3, column=0)
b5 = Button(f1, bg='SteelBlue1', text='move right', command=move_right)
b5.grid(row=3, column=2)
b6 = Button(f1, bg='SteelBlue1', text='move left', command=move_left)
b6.grid(row=3, column=4)
b7 = Button(f1, bg='SteelBlue1', text='move back', command=move_back)
b7.grid(row=4, column=2)
l3 = Label(f1, text='last turn').grid(row=6, column=0)
e3 = Entry(f1)
e3.grid(row=6, column=2)
l4 = Label(f1, text='direction now')
l4.grid(row=7, column=0)
e4 = Entry(f1)
e4.grid(row=7, column=2)
l5 = Label(f1, text='x position now')
l5.grid(row=8, column=0)
e5 = Entry(f1)
e5.grid(row=8, column=2)
l7 = Label(f1, text='y position now')
l7.grid(row=9, column=0)
e6 = Entry(f1)
e6.grid(row=9, column=2)
button = Button(f1, bg='IndianRed2', text='Exit', command=mado.destroy)
button.grid(row=11, column=2)

mainloop()
