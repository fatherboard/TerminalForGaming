import PySimpleGUI as sg
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from tkinter import messagebox, simpledialog
import subprocess
import binascii
import shutil
import bluetooth

bg_color = "#965fd4"
activebackground = "#734f9a"
# Definimos la lista de elementos
def connect_device(device_address):
    # Obtener el dispositivo seleccionado
    # Vincular la Raspberry Pi con el dispositivo seleccionado
    subprocess.call(["sudo", "hciconfig", "hci0", "piscan"])
    subprocess.call(["sudo", "bluetoothctl", "pair", device_address])
    #subprocess.call(["sudo", "bluetoothctl", "trust", device_address])
    subprocess.call(["sudo", "bluetoothctl", "connect", device_address])
    # Comprobar si la conexión se ha realizado correctamente
    output = subprocess.check_output(["sudo", "bluetoothctl", "info", device_address])
    if b"Connected: yes" in output:
        messagebox.showinfo("","La Raspberry Pi se ha vinculado con el dispositivo seleccionado.")
    else:
        messagebox.showinfo("","La Raspberry Pi no se ha vinculado con el dispositivo seleccionado.")
    subprocess.call(["sudo", "hciconfig", "hci0", "piscan"])

def create_layout(pages_names, pages_device):
# Definimos la estructura de la ventana
    blueIcon = '/home/pi/Downloads/iconoBlue.png'

        
    layout = [
            [sg.Column([[sg.Button(pages_names[0], button_color=('#FFFFFF',bg_color),font=('Helvetica',12, 'bold'),border_width=0,pad=(5,5), size=(17,15), key= lambda: connect_device(pages_device[0])),],
                        [sg.Button(pages_names[1], button_color=('#FFFFFF',bg_color,activebackground),font=('Helvetica',12, 'bold'),border_width=0,pad=(5,5), size=(17,15), key= lambda: connect_device(pages_device[1]))]],
                       background_color="#965fd4"), 
            sg.Column([[sg.Button(pages_names[2], button_color=('#FFFFFF',bg_color),font=('Helvetica',12, 'bold'),border_width=0,pad=(5,5), size=(17,15), key= lambda: connect_device(pages_device[2])),],
                        [sg.Button(pages_names[3], button_color=('#FFFFFF',bg_color),font=('Helvetica',12, 'bold'),border_width=0,pad=(5,5), size=(17,15), key= lambda: connect_device(pages_device[3]))]],
                       background_color="#965fd4"),
            sg.Column([[sg.Button(pages_names[4], button_color=('#FFFFFF',bg_color),font=('Helvetica',12, 'bold'),border_width=0,pad=(5,5), size=(17,15), key= lambda: connect_device(pages_device[4])),],
                        [sg.Button(pages_names[5], button_color=('#FFFFFF',bg_color),font=('Helvetica',12, 'bold'),border_width=0,pad=(5,5), size=(17,15), key= lambda: connect_device(pages_device[5]))]],
                       background_color="#965fd4"),
            sg.Column([[sg.Button(pages_names[6], button_color=('#FFFFFF',bg_color),font=('Helvetica',12, 'bold'),border_width=0,pad=(5,5), size=(17,15), key= lambda: connect_device(pages_device[6])),],
                        [sg.Button(pages_names[7], button_color=('#FFFFFF',bg_color),font=('Helvetica',12, 'bold'),border_width=0,pad=(5,5), size=(17,15), key= lambda: connect_device(pages_device[7]))]],
                       background_color="#965fd4")]]


    #for column in layout:
        #for button in column:
            #print(pages_names[i])
            #if pages_names[i] == "   ":
                #button.update(image_filename ='/home/pi/Downloads/iconoBlue.png')
            #i+=1
                
    return layout

def button_callback(event, nombre_red):
    if event is page_names:
        connect(nombre_red)

def blank_frame():
    return sg.Frame("", [[]], background_color=bg_color, border_width=0,pad=(0,0))

devices = bluetooth.discover_devices()
buttons = []
        
for i, device in enumerate(devices):
    device_name = bluetooth.lookup_name(device)
    if device_name:
        buttons.append(device_name)
        
name_list = devices
num_elem = len(name_list)
module = num_elem % 8
if module != 0:
    add = 8 - module
    name_list += ["   "] * add
    buttons += ["X"] * add

pages_names = [buttons[i:i+8] for i in range(0, len(buttons), 8)]
pages_device= [name_list[i:i+8] for i in range(0, len(name_list), 8)]

global pages
pages = 0

global window
amount_of_frames = 0


def create_layout_num(amount_of_frames):
    layout_frame1 = [[sg.Column([[sg.Button(image_filename='/home/pi/Downloads/prev.png', image_size=(112,600), image_subsample=2,pad=(0, 0), button_color=(activebackground,bg_color), border_width=0, key='-PREV-')]],
                            element_justification='c', vertical_alignment='center',pad=(0,0))]]

    layout_frame3 = [[sg.Column([[sg.Button(image_filename='/home/pi/Downloads/next.png', image_size=(112,600), image_subsample=2,pad=(0, 0), button_color=(activebackground,bg_color), border_width=0,  key='-NEXT-')]],
                            element_justification='right', vertical_alignment='center', pad=(0,0))]]
    
    if amount_of_frames == 5:
        layout_frame2 = create_layout(pages_names[0],pages_device[0])
        layout_frame4 = create_layout(pages_names[1],pages_device[1])
        layout_frame6 = create_layout(pages_names[2],pages_device[2])
        layout_frame8 = create_layout(pages_names[3],pages_device[3])
        layout_frame10 = create_layout(pages_names[4],pages_device[4])
        layout = [
            [blank_frame(), sg.Frame("", layout_frame1, size=(112, 600), border_width=0),
            sg.Frame("", layout_frame2, size=(800, 600),background_color=bg_color,border_width=0, key = "-FRAME2-", visible=True),
            sg.Frame("", layout_frame4, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME4-", visible=False),
            sg.Frame("", layout_frame6, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME6-", visible=False),
            sg.Frame("", layout_frame8, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME8-", visible=False),
            sg.Frame("", layout_frame10, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME10-", visible=False),
            sg.Frame("", layout_frame3, size=(112, 600),border_width=0,key = "-ARROW-"), blank_frame()]]
    elif amount_of_frames == 4:
        layout_frame2 = create_layout(pages_names[0],pages_device[0])
        layout_frame4 = create_layout(pages_names[1],pages_device[1])
        layout_frame6 = create_layout(pages_names[2],pages_device[2])
        layout_frame8 = create_layout(pages_names[3],pages_device[3])
        layout = [
            [blank_frame(), sg.Frame("", layout_frame1, size=(112, 600), background_color=bg_color, border_width=0),
            sg.Frame("", layout_frame2, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME2-", visible=True),
            sg.Frame("", layout_frame4, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME4-", visible=False),
            sg.Frame("", layout_frame6, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME6-", visible=False),
            sg.Frame("", layout_frame8, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME8-", visible=False),
            sg.Frame("", layout_frame3, size=(112, 600),border_width=0,key = "-ARROW-"), blank_frame()]]
    elif amount_of_frames == 3:
        layout_frame2 = create_layout(pages_names[0],pages_device[0])
        layout_frame4 = create_layout(pages_names[1],pages_device[1])
        layout_frame6 = create_layout(pages_names[2],pages_device[2])
        layout = [
            [blank_frame(), sg.Frame("", layout_frame1, size=(112, 600), background_color=bg_color, border_width=0),
            sg.Frame("", layout_frame2, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME2-", visible=True),
            sg.Frame("", layout_frame4, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME4-", visible=False),
            sg.Frame("", layout_frame6, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME6-", visible=False),
            sg.Frame("", layout_frame3, size=(112, 600),border_width=0,key = "-ARROW-"), blank_frame()]]
    elif amount_of_frames == 2:
        layout_frame2 = create_layout(pages_names[0],pages_device[0])
        layout_frame4 = create_layout(pages_names[1],pages_device[1])
        layout = [
            [blank_frame(), sg.Frame("", layout_frame1, size=(112, 600), background_color=bg_color, border_width=0),
            sg.Frame("", layout_frame2, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME2-", visible=True),
            sg.Frame("", layout_frame4, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME4-", visible=False),
            sg.Frame("", layout_frame3, size=(112, 600),border_width=0,key = "-ARROW-"), blank_frame()]]
    elif amount_of_frames == 1:
        layout_frame2 = create_layout(pages_names[0],pages_device[0])

        layout = [
            [blank_frame(), sg.Frame("", layout_frame1, size=(112, 600), background_color=bg_color, border_width=0),
            sg.Frame("", layout_frame2, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME2-", visible=True),
            sg.Frame("", layout_frame3, size=(112, 600),border_width=0,key = "-ARROW-"), blank_frame()]]
    return layout



window = sg.Window("Title", create_layout_num(len(pages_names)), margins=(0, 0),background_color=bg_color,finalize=True)
#window.Maximize()
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == '-NEXT-':
        if pages < len(pages_names)-1:
            pages = pages + 1
            if pages*2 == 2:
                window['-FRAME2-'].Update(visible=False)
                window['-FRAME4-'].Update(visible=True)
            if pages*2 == 4:
                window['-FRAME4-'].Update(visible=False)
                window['-FRAME6-'].Update(visible=True)
            if pages*2 == 6:
                window['-FRAME6-'].Update(visible=False)
                window['-FRAME8-'].Update(visible=True)
            if pages*2 == 8:
                window['-FRAME8-'].Update(visible=False)
                window['-FRAME10-'].Update(visible=True)
                
            window['-ARROW-'].Update(visible=False)
            window['-ARROW-'].Update(visible=True)
            #update_frame2(window, pages_names[pages])

    elif event == '-PREV-':
        if pages == 0:
            window.close()
        elif pages >= 1:
            pages = pages - 1
            if pages*2 == 0:
                window['-FRAME2-'].Update(visible=True)
                window['-FRAME4-'].Update(visible=False)
            if pages*2 == 2:
                window['-FRAME4-'].Update(visible=True)
                window['-FRAME6-'].Update(visible=False)
            if pages*2 == 4:
                window['-FRAME6-'].Update(visible=True)
                window['-FRAME8-'].Update(visible=False)
            if pages*2 == 6:
                window['-FRAME8-'].Update(visible=True)
                window['-FRAME10-'].Update(visible=False)
            window['-ARROW-'].Update(visible=False)
            window['-ARROW-'].Update(visible=True)
            
    elif callable(event):
        event()
                
# Cerramos la ventana
window.close()

