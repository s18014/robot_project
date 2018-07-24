import tkinter as tk
import math


class RobotStatus:
    def __init__(self, canvas, x, y, front, right, back, left):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.front = front
        self.right = right
        self.back = back
        self.left = left


class Map:
    def __init__(self, canvas, zoom_rate):
        self.canvas = canvas
        self.wh = canvas.winfo_reqheight()
        self.ww = canvas.winfo_reqwidth()
        self.zoom_rate = zoom_rate

    def grid(self):
        self.canvas.delete("grid")
        square_x = math.ceil(self.ww / self.zoom_rate)
        square_y = math.ceil(self.wh / self.zoom_rate)
        for i in range(square_x):
            self.canvas.create_line(i*self.zoom_rate, 0, i*self.zoom_rate, self.wh, tag="grid")
            self.canvas.pack()
        for i in range(square_y):
            self.canvas.create_line(0, i*self.zoom_rate, self.ww, i*self.zoom_rate, tag="grid")
            self.canvas.pack()

        self.canvas.pack()


class Draw:
    pass


def exit(e):
    root.quit()


def testUpdate(e):
    if e.keysym == "Up" and field.zoom_rate < 50:
        field.zoom_rate += 1
    elif e.keysym == "Down" and field.zoom_rate > 10:
        field.zoom_rate -= 1
    print(field.zoom_rate)
    field.grid()


root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600, bg="#999")
canvas.pack()
field = Map(canvas, 30)
field.grid()
root.bind_all("q", exit)
root.bind_all("<Up>", testUpdate)
root.bind_all("<Down>", testUpdate)
# Can not get MouseWheel reactions, why why why why
# root.bind_all("<MouseWheel>", testUpdate)
root.mainloop()
