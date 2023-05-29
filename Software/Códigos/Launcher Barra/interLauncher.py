import PySimpleGUI as sg
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from glob import glob
import subprocess
import os

bg_color = "#965fd4"
activebackground = "#734f9a"
# Definimos la lista de elementos
def get_apps():
    app_list = []
    sites = glob("sites.site")
    if sites != []:
        with open(sites[0]) as file:
            file = file.readlines()
            count = 0
            for line in file:
                x = line.strip()
                x = [f.strip() for f in x.split("#")]
                count+=1
                title, address, image = x
                app_list.append(address)
                       
    return app_list

def get_icons():
    image_list = []
    sites = glob("sites.site")
    if sites != []:
        with open(sites[0]) as file:
            file = file.readlines()
            count = 0
            for line in file:
                x = line.strip()
                x = [f.strip() for f in x.split("#")]
                count+=1
                title, address, image = x
                img_link= "/home/pi/Downloads/" + image
                image_list.append(img_link)
                       
    return image_list

def create_layout(pages_names, icon_list):
# Definimos la estructura de la ventana
    i = 0
    for icon_list[i] in icon_list:
        if icon_list[i] == "   ":
            icon_list[i] = "/home/pi/Downloads/iconoSettings2.png"
        i+=1
            
    layout = [
            [sg.Column([[sg.Button('   ', button_color=(activebackground,bg_color),border_width=0,pad=(5,10), image_filename=icon_list[0], key=lambda: os.system(pages_names[0]))],
                        [sg.Button('   ', button_color=(activebackground,bg_color),border_width=0,pad=(5,10), image_filename=icon_list[1], key= lambda: os.system(pages_names[1]))]],
                       background_color="#965fd4"), 
            sg.Column([[sg.Button('   ', button_color=(activebackground,bg_color),border_width=0,pad=(5,10), image_filename=icon_list[2], key= lambda: os.system(pages_names[2]))],
                        [sg.Button('   ', button_color=(activebackground,bg_color),border_width=0,pad=(5,10), image_filename=icon_list[3], key= lambda: os.system(pages_names[3]))]],
                       background_color="#965fd4"),
            sg.Column([[sg.Button('   ', button_color=(activebackground,bg_color),border_width=0,pad=(5,10), image_filename=icon_list[4], key= lambda: os.system(pages_names[4]))],
                        [sg.Button('   ', button_color=(activebackground,bg_color),border_width=0,pad=(5,10), image_filename=icon_list[5], key= lambda: os.system(pages_names[5]))]],
                       background_color="#965fd4"),
            sg.Column([[sg.Button('   ', button_color=(activebackground,bg_color),border_width=0,pad=(5,10), image_filename=icon_list[6], key= lambda: os.system(pages_names[6]))],
                        [sg.Button('   ', button_color=(activebackground,bg_color),border_width=0,pad=(5,10), image_filename=icon_list[7], key= lambda: os.system(pages_names[7]))]],
                       background_color="#965fd4")]]
    
    return layout


def blank_frame():
    return sg.Frame("", [[]], background_color=bg_color, border_width=0,pad=(0,0))


name_list = get_apps()
icon_list = get_icons()
        
num_elem = len(name_list)
module = num_elem % 8
if module != 0:
    add = 8 - module
    name_list += ["   "] * add
    icon_list += ["   "] * add

pages_names = [name_list[i:i+8] for i in range(0, len(name_list), 8)]
icons_names = [icon_list[i:i+8] for i in range(0, len(icon_list), 8)]

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
        layout_frame2 = create_layout(pages_names[0],icons_names[0])
        layout_frame4 = create_layout(pages_names[1],icons_names[1])
        layout_frame6 = create_layout(pages_names[2],icons_names[2])
        layout_frame8 = create_layout(pages_names[3],icons_names[3])
        layout_frame10 = create_layout(pages_names[4],icons_names[4])
        layout = [
            [blank_frame(), sg.Frame("", layout_frame1, size=(112, 600), border_width=0),
            sg.Frame("", layout_frame2, size=(800, 600),background_color=bg_color,border_width=0, key = "-FRAME2-", visible=True),
            sg.Frame("", layout_frame4, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME4-", visible=False),
            sg.Frame("", layout_frame6, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME6-", visible=False),
            sg.Frame("", layout_frame8, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME8-", visible=False),
            sg.Frame("", layout_frame10, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME10-", visible=False),
            sg.Frame("", layout_frame3, size=(112, 600),border_width=0,key = "-ARROW-"), blank_frame()]]
    elif amount_of_frames == 4:
        layout_frame2 = create_layout(pages_names[0],icons_names[0])
        layout_frame4 = create_layout(pages_names[1],icons_names[1])
        layout_frame6 = create_layout(pages_names[2],icons_names[2])
        layout_frame8 = create_layout(pages_names[3],icons_names[3])
        layout = [
            [blank_frame(), sg.Frame("", layout_frame1, size=(112, 600), background_color=bg_color, border_width=0),
            sg.Frame("", layout_frame2, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME2-", visible=True),
            sg.Frame("", layout_frame4, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME4-", visible=False),
            sg.Frame("", layout_frame6, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME6-", visible=False),
            sg.Frame("", layout_frame8, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME8-", visible=False),
            sg.Frame("", layout_frame3, size=(112, 600),border_width=0,key = "-ARROW-"), blank_frame()]]
    elif amount_of_frames == 3:
        layout_frame2 = create_layout(pages_names[0],icons_names[0])
        layout_frame4 = create_layout(pages_names[1],icons_names[1])
        layout_frame6 = create_layout(pages_names[2],icons_names[2])
        layout = [
            [blank_frame(), sg.Frame("", layout_frame1, size=(112, 600), background_color=bg_color, border_width=0),
            sg.Frame("", layout_frame2, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME2-", visible=True),
            sg.Frame("", layout_frame4, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME4-", visible=False),
            sg.Frame("", layout_frame6, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME6-", visible=False),
            sg.Frame("", layout_frame3, size=(112, 600),border_width=0,key = "-ARROW-"), blank_frame()]]
    elif amount_of_frames == 2:
        layout_frame2 = create_layout(pages_names[0],icons_names[0])
        layout_frame4 = create_layout(pages_names[1],icons_names[1])
        layout = [
            [blank_frame(), sg.Frame("", layout_frame1, size=(112, 600), background_color=bg_color, border_width=0),
            sg.Frame("", layout_frame2, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME2-", visible=True),
            sg.Frame("", layout_frame4, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME4-", visible=False),
            sg.Frame("", layout_frame3, size=(112, 600),border_width=0,key = "-ARROW-"), blank_frame()]]
    elif amount_of_frames == 1:
        layout_frame2 = create_layout(pages_names[0],icons_names[0])

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
        if pages >= 1:
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



