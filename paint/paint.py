import tkinter as tk
from tkinter import colorchooser


brush_color = "black"


def draw(event):
    brush_size = 2
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    drawing_area.create_oval(x1, y1, x2, y2, fill=brush_color, outline=brush_color)


def pick_color():
    global brush_color
    new_color = colorchooser.askcolor()[1] 
    if new_color:
        brush_color = new_color 

def setup_window():
    root = tk.Tk()
    root.title("Painter")
    #root.geometry("500x300")
    root.configure(bg="white")


    global drawing_area
    drawing_area = tk.Canvas(root, bg="white", width=600, height=350)
    drawing_area.pack(pady=10)


    drawing_area.bind("<B1-Motion>", draw)

   
    color_button = tk.Button(root, text="Change Color", command=pick_color)
    color_button.pack()

    root.mainloop()

if __name__ == "__main__":
    setup_window()
