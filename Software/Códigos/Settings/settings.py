import tkinter as tk
import tkinter.ttk as ttk
import os

root = tk.Tk()
root.title("My launcher")
#root.attributes("-fullscreen", True)
bg_color = "#965fd4"
activebackground = "#734f9a"
fg = "#8bd450"
hover = "#d3290f"
unnable = "#d8d8d8"
unnable_fg = "black"


class Button:

    row = 0
    column = 0

    def __init__(self, text, func, arg, image=""):
        if image != "":
            image = tk.PhotoImage(file=image)
        root.rowconfigure(Button.row, weight=1, minsize=40)
        root.columnconfigure(Button.column, weight=1, minsize=40)
        self.button = tk.Button(
            root,
            text=text,
            image=image,
            borderwidth=0,
            bd=0,  # Eliminar borde gris
            bg=bg_color,
            highlightthickness=0,
            activebackground=activebackground,
            compound=tk.LEFT,
            command=lambda: func(arg))

        self.button.grid(
            row=Button.row,
            column=Button.column,
            sticky="nsew", padx=0)
        self.button.image = image
        if Button.column < 3:
            Button.column += 1
        else:
            Button.column = 0
            Button.row += 1


with open("settings.site") as file:
    file = file.readlines()
for line in file:
    x = line.strip()
    x = [f.strip() for f in x.split("#")]
    title, address, image = x
    Button(title, os.system, address, image="/home/pi/Downloads/" + image)
    
icon= tk.PhotoImage(file = "/home/pi/Downloads/prev.png")
btn_ret = tk.Button(root, image = icon,borderwidth=0,bg=bg_color,highlightthickness=0,activebackground=hover, command = root.destroy)
btn_ret.grid(row=0, column=0, sticky="nw", padx=(0, 0), pady=(0, 0))

root.mainloop()



