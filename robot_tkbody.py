from tkinter import *

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
b1 = Button(f1, bg='SteelBlue1', text='turn right')
b1.grid(row=2, column=0)
b2 = Button(f1, bg='SteelBlue1', text='turn left')
b2.grid(row=2, column=2)
b3 = Button(f1, bg='SteelBlue1', text='turn back')
b3.grid(row=2, column=4)
b4 = Button(f1, bg='SteelBlue1', text='move forward')
b4.grid(row=3, column=0)
b5 = Button(f1, bg='SteelBlue1', text='move right')
b5.grid(row=3, column=2)
b6 = Button(f1, bg='SteelBlue1', text='move left')
b6.grid(row=3, column=4)
b7 = Button(f1, bg='SteelBlue1', text='move back')
b7.grid(row=4, column=2)

l3 = Label(f1, text='direction now')
l3.grid(row=6, column=0)
e3 = Entry(f1)
e3.grid(row=6, column=2)
l4 = Label(f1, text='x position now')
l4.grid(row=7, column=0)
e4 = Entry(f1)
e4.grid(row=7, column=2)
l5 = Label(f1, text='y position now')
l5.grid(row=8, column=0)
e5 = Entry(f1)
e5.grid(row=8, column=2)
button = Button(f1, bg='IndianRed2', text='Exit', command=mado.destroy)
button.grid(row=11, column=2)
mainloop()
