from tkinter import *
import os

os.system('xset r off')


class Ball:
    def __init__(self, canvas, x, y, size, v):
        self.canvas = canvas
        self.wh = canvas.winfo_reqheight() - size
        self.ww = canvas.winfo_reqwidth() - size
        self.x = x
        self.y = y
        self.size = size
        self.v = v
        self.leftKey = False
        self.rightKey = False
        self.canJump = True
        self.ball = canvas.create_oval(self.x - self.size, self.y - self.size, self.x + self.size, self.y + self.size, fill="red")

    def fall(self):
        self.canvas.delete(self.ball)
        self.g = 0.3
        self.v += self.g
        if self.y > self.wh:
            self.v = 0
            self.y = self.wh
        if self.y < self.size:
            self.v = 0
            self.y = self.size
        self.y += self.v

        self.ball = canvas.create_oval(self.x - self.size, self.y - self.size, self.x + self.size, self.y + self.size, fill="red")
        self.canvas.after(16, self.fall)

    def jump(self):
        if self.canJump:
            if self.y > self.wh:
                self.y = self.wh - 1
            self.v = -10
            self.canJump = False

    def move(self):
        if self.leftKey:
            self.x += 10
        if self.rightKey:
            self.x -= 10
        if self.x > self.ww:
            self.x = self.ww
        if self.x < self.size:
            self.x = self.size
        self.canvas.after(16, self.move)


class Discription:
    def __init__(self, canvas, x, y, text):
        self.canvas = canvas
        self.wh = canvas.winfo_reqheight()
        self.ww = canvas.winfo_reqwidth()
        self.x = x
        self.y = y
        self.text = text
        self.exist = False
        self.textBox = self.canvas.create_text(self.x, self.y, text=self.text)
        self.canvas.delete(self.textBox)

    def help(self):
        self.canvas.delete(self.textBox)
        if self.exist:
            self.textBox = self.canvas.create_text(self.x, self.y, text=self.text, font=("", 12))
        self.canvas.after(16, self.help)

    def init(self):
        self.canvas.create_text(self.ww - 70, 30, text="HELP:   h", font=("", 12))


def pressKey(event):
    if event.keysym == "a":
        ball1.rightKey = True
    if event.keysym == "d":
        ball1.leftKey = True
    if event.keysym == "space":
        ball1.jump()
    if event.keysym == "h":
        text1.exist = not text1.exist
        text1.x = ball1.x
        text1.y = ball1.y - ball1.size - 50


def releaseKey(event):
    if event.keysym == "a":
        ball1.rightKey = False
    if event.keysym == "d":
        ball1.leftKey = False
    if event.keysym == "space":
        ball1.canJump = True


def exit():
    global root
    root.quit()


root = Tk()

text = """
MoveLeft :   a
MoveRight:   d
Jump     :   space
"""

canvas = Canvas(root, width=800, height=600, bg="#0f0")
canvas.pack()

ball1 = Ball(canvas, 100, 100, 50, 0)
ball1.fall()
ball1.move()

text1 = Discription(canvas, 0, 0, text)
text1.init()
text1.help()

root.bind("<KeyPress-space>", pressKey)
root.bind("<KeyRelease-space>", releaseKey)
root.bind("<KeyPress-a>", pressKey)
root.bind("<KeyRelease-a>", releaseKey)
root.bind("<KeyPress-d>", pressKey)
root.bind("<KeyRelease-d>", releaseKey)
root.bind("<KeyPress-h>", pressKey)
Button(root, text="EXIT", bg="red", command=exit).pack()
root.mainloop()

os.system('xset r on')
