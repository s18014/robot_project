import tkinter as tk
import math


class Robot:
    def __init__(self, canvas, x, y, front, right, back, left):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.front = front
        self.right = right
        self.back = back
        self.left = left

    def draw():
        pass

    def update():
        pass

    def move():
        pass

    def turn():
        pass


class Map:
    def __init__(self, canvas, zoom_rate):
        self.canvas = canvas
        self.wh = canvas.winfo_reqheight()
        self.ww = canvas.winfo_reqwidth()
        self.zoom_rate = zoom_rate
        self.hww = self.ww // 2
        self.hwh = self.wh // 2
        self.cell_x = math.ceil(self.hww / self.zoom_rate)
        self.cell_y = math.ceil(self.hwh / self.zoom_rate)
        self.lineGrid()

    def lineGrid(self):
        self.canvas.delete("grid")
        self.cell_x = math.ceil(self.hww / self.zoom_rate)
        self.cell_y = math.ceil(self.hwh / self.zoom_rate)
        x1 = lambda i: self.hww + i * self.zoom_rate
        x2 = lambda i: self.hww + -(i+1) * self.zoom_rate
        y1 = lambda i: self.hwh + i * self.zoom_rate
        y2 = lambda i: self.hwh + -(i+1) * self.zoom_rate
        for i in range(self.cell_x):
            self.canvas.create_line(x1(i), 0, x1(i), self.wh, tag="grid")
            self.canvas.create_line(x2(i), 0, x2(i), self.wh, tag="grid")
        for i in range(self.cell_y):
            self.canvas.create_line(0, y1(i), self.ww, y1(i), tag="grid")
            self.canvas.create_line(0, y2(i), self.ww, y2(i), tag="grid")
        self.canvas.pack()

    def cellGrid(self):
        pass


class Draw:
    pass


def exit(e):
    root.quit()


def testUpdate(e):
    if e.keysym == "Up" and field.zoom_rate < 50:
        field.zoom_rate += 1
    elif e.keysym == "Down" and field.zoom_rate > 10:
        field.zoom_rate -= 1
    elif e.keysym == "c":
        pass
    field.lineGrid()


root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600, bg="#999")
canvas.pack()
field = Map(canvas, 30)
field.cellGrid()
root.bind_all("q", exit)
root.bind_all("<Up>", testUpdate)
root.bind_all("<Down>", testUpdate)
root.bind_all("c", testUpdate)
# Can not get MouseWheel reactions, why why why why
# root.bind_all("<MouseWheel>", testUpdate)
root.mainloop()
