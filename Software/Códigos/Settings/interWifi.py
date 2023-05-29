import PySimpleGUI as sg
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from tkinter import messagebox, simpledialog
import subprocess
import binascii
import shutil

bg_color = "#965fd4"
activebackground = "#734f9a"
# Definimos la lista de elementos
def connect(nombre_red):
    password = simpledialog.askstring("Contraseña", f"Ingrese la contraseña para la red '{nombre_red}':", show='*')
    if password:
            # Convierte la contraseña a formato hexadecimal
            #password_hex = binascii.hexlify(password.encode('utf-8')).decode('utf-8')  
        subprocess.call(['sudo','systemctl', 'stop', 'NetworkManager'])
        subprocess.call(['sudo','killall', 'wpa_supplicant'])
        subprocess.call(['sudo','ifconfig', 'wlan0', 'up'])
        
            # Intenta agregar la nueva red al archivo wpa_supplicant.conf
        try:
            # Copia el archivo wpa_supplicant.conf a un archivo auxiliar
            shutil.copy('/etc/wpa_supplicant/wpa_supplicant.conf', '/etc/wpa_supplicant/wpa_supplicant.conf.bak')
            
            # Abre el archivo auxiliar en modo de escritura
            network_clean = nombre_red.replace('"',"")
            with open('/etc/wpa_supplicant/wpa_supplicant.conf.bak', 'a') as f:
                f.write(f'network={{\n\tssid="{network_clean}"\n\tpsk="{password}"\n\tkey_mgmt=WPA-PSK\n\tpriority=1\n}}\n')
         
                # Sobreescribe el archivo original con el archivo auxiliar
            shutil.move('/etc/wpa_supplicant/wpa_supplicant.conf.bak', '/etc/wpa_supplicant/wpa_supplicant.conf')
         
                # Muestra un mensaje de éxito
            messagebox.showinfo("Red agregada", f"Se ha agregado la red '{network_clean}' al archivo wpa_supplicant.conf.")
            subprocess.call(['sudo','ifconfig', 'wlan0', 'down'])
            subprocess.call(['sudo','ifconfig', 'wlan0', 'up'])
            #wlan0 up
            subprocess.call(['sudo', 'wpa_supplicant', '-B', '-i', 'wlan0', '-c', '/etc/wpa_supplicant/wpa_supplicant.conf', '-D', 'wext'])
            #ejecutar wpa_supplicant con el comando sudo wpa_supplicant -B -i wlan0 -c <wpa_passphrase red password>
            subprocess.call(['sudo','dhclient', 'wlan0'])
        except Exception as e:
            messagebox.showerror("Error al agregar la red", f"No se pudo agregar la red '{nombre_red}' al archivo wpa_supplicant.conf. Error: {e}")
    else:
        messagebox.showerror("Error de conexión", "Debe ingresar una contraseña para conectar a la red.")
 
def scan_names():
    # Ejecuta el comando iwlist y captura la salida
    output = subprocess.check_output(['iwlist', 'wlan0', 'scan']).decode('utf-8')
    # Busca los nombres de las redes WiFi en la salida
    networks = [line.split(':')[1].strip() for line in output.split('\n') if 'ESSID' in line]
    
    networks = [network for network in networks if 20 > len(network) >= 4]
    redes = []
    for network in networks:
        network_clean = network.replace('"',"")
        if network_clean not in redes:
            redes.append(network_clean)
            
    return redes


def create_layout(pages_names, pages_quality):
# Definimos la estructura de la ventana
    i = 0
    list_buttons = []
    for quality in pages_quality:
        if quality > 50:
            list_buttons.append('/home/pi/Downloads/iconoMaxQuality.png')
        elif 30 < quality < 50:
            list_buttons.append('/home/pi/Downloads/iconoMediumQuality.png')
        elif 0 < quality < 30:
            list_buttons.append('/home/pi/Downloads/iconoLowQuality.png')
        else:
            list_buttons.append('/home/pi/Downloads/iconoNoQuality.png')
        
    layout = [
            [sg.Column([[sg.Button('   ', button_color=(activebackground,bg_color),border_width=0,pad=(0,0), image_filename=list_buttons[0], key= lambda: connect(pages_names[0])),]
                       ,[sg.Text(pages_names[0], font=('Helvetica',10, 'bold'), justification = 'center', size=(25,0),background_color="#965fd4")],
                        [sg.Button('   ', button_color=(activebackground,bg_color),border_width=0,pad=(5,0), image_filename=list_buttons[1], key= lambda: connect(pages_names[1]))]
                        ,[sg.Text(pages_names[1], font=('Helvetica',10, 'bold'), justification = 'center', size=(25,0),background_color="#965fd4")]],
                       background_color="#965fd4"), 
            sg.Column([[sg.Button('   ', button_color=(activebackground,bg_color),border_width=0,pad=(0,0), image_filename=list_buttons[2], key= lambda: connect(pages_names[2])),]
                       ,[sg.Text(pages_names[2], font=('Helvetica',10, 'bold'), justification = 'center', size=(25,0),background_color="#965fd4")],
                       [sg.Button('   ', button_color=(activebackground,bg_color),border_width=0,pad=(5,0), image_filename=list_buttons[3], key= lambda: connect(pages_names[3]))]
                      ,[sg.Text(pages_names[3], font=('Helvetica',10, 'bold'), justification = 'center', size=(25,0),background_color="#965fd4")]],
                       background_color="#965fd4"),
            sg.Column([[sg.Button('   ', button_color=(activebackground,bg_color),border_width=0,pad=(0,0), image_filename=list_buttons[4], key= lambda: connect(pages_names[4])),]
                       ,[sg.Text(pages_names[4], font=('Helvetica',10, 'bold'), justification = 'center', size=(25,0),background_color="#965fd4")],
                       [sg.Button('   ', button_color=(activebackground,bg_color),border_width=0,pad=(5,0), image_filename=list_buttons[5], key= lambda: connect(pages_names[5]))]
                       ,[sg.Text(pages_names[5], font=('Helvetica',10, 'bold'), justification = 'center', size=(25,0),background_color="#965fd4")]],
                       background_color="#965fd4", element_justification='right'),
            sg.Column([[sg.Button('   ', button_color=(activebackground,bg_color),border_width=0,pad=(0,0), image_filename=list_buttons[6], key= lambda: connect(pages_names[6])),]
                       ,[sg.Text(pages_names[6], font=('Helvetica',10, 'bold'), justification = 'center', size=(25,0),background_color="#965fd4")],
                       [sg.Button('   ', button_color=(activebackground,bg_color),border_width=0,pad=(5,0), image_filename=list_buttons[7], key= lambda: connect(pages_names[7]))]
                       ,[sg.Text(pages_names[7], font=('Helvetica',10, 'bold'), justification = 'center', size=(25,0),background_color="#965fd4")]],
                       background_color="#965fd4", element_justification='right')]]
    
    return layout
def button_callback(event, nombre_red):
    if event is page_names:
        connect(nombre_red)

def scan_qualities(num_elementos):
       # Ejecuta el comando iwlist y captura la salida
    output = subprocess.check_output(['iwlist', 'wlan0', 'scan']).decode('utf-8')
    lista_calidades = output
            
    lista_calidades = subprocess.check_output(['iwlist', 'wlan0', 'scan']).decode('utf-8')
    calidades = [line.split('Quality=')[1].strip() for line in output.split('\n') if 'Quality' in line]
    calidades_lista = []
    for calidad in calidades:
        if(len(calidades_lista)< num_elementos):
            calidad_clean = calidad.replace('"',"")
            calidades_lista.append(int(calidad[0:2]))
    return calidades_lista

def blank_frame():
    return sg.Frame("", [[]], background_color=bg_color, border_width=0,pad=(0,0))


name_list = scan_names()
num_elem = len(name_list)
module = num_elem % 8
quality_list = scan_qualities(num_elem)
if module != 0:
    add = 8 - module
    name_list += ["   "] * add
    quality_list += [0] * add

pages_names = [name_list[i:i+8] for i in range(0, len(name_list), 8)]
pages_quality= [quality_list[i:i+8] for i in range(0, len(quality_list), 8)]

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
        layout_frame2 = create_layout(pages_names[0],pages_quality[0])
        layout_frame4 = create_layout(pages_names[1],pages_quality[1])
        layout_frame6 = create_layout(pages_names[2],pages_quality[2])
        layout_frame8 = create_layout(pages_names[3],pages_quality[3])
        layout_frame10 = create_layout(pages_names[4],pages_quality[4])
        layout = [
            [blank_frame(), sg.Frame("", layout_frame1, size=(112, 600), border_width=0),
            sg.Frame("", layout_frame2, size=(800, 600),background_color=bg_color,border_width=0, key = "-FRAME2-", visible=True),
            sg.Frame("", layout_frame4, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME4-", visible=False),
            sg.Frame("", layout_frame6, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME6-", visible=False),
            sg.Frame("", layout_frame8, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME8-", visible=False),
            sg.Frame("", layout_frame10, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME10-", visible=False),
            sg.Frame("", layout_frame3, size=(112, 600),border_width=0,key = "-ARROW-"), blank_frame()]]
    elif amount_of_frames == 4:
        layout_frame2 = create_layout(pages_names[0],pages_quality[0])
        layout_frame4 = create_layout(pages_names[1],pages_quality[1])
        layout_frame6 = create_layout(pages_names[2],pages_quality[2])
        layout_frame8 = create_layout(pages_names[3],pages_quality[3])
        layout = [
            [blank_frame(), sg.Frame("", layout_frame1, size=(112, 600), background_color=bg_color, border_width=0),
            sg.Frame("", layout_frame2, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME2-", visible=True),
            sg.Frame("", layout_frame4, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME4-", visible=False),
            sg.Frame("", layout_frame6, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME6-", visible=False),
            sg.Frame("", layout_frame8, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME8-", visible=False),
            sg.Frame("", layout_frame3, size=(112, 600),border_width=0,key = "-ARROW-"), blank_frame()]]
    elif amount_of_frames == 3:
        layout_frame2 = create_layout(pages_names[0],pages_quality[0])
        layout_frame4 = create_layout(pages_names[1],pages_quality[1])
        layout_frame6 = create_layout(pages_names[2],pages_quality[2])
        layout = [
            [blank_frame(), sg.Frame("", layout_frame1, size=(112, 600), background_color=bg_color, border_width=0),
            sg.Frame("", layout_frame2, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME2-", visible=True),
            sg.Frame("", layout_frame4, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME4-", visible=False),
            sg.Frame("", layout_frame6, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME6-", visible=False),
            sg.Frame("", layout_frame3, size=(112, 600),border_width=0,key = "-ARROW-"), blank_frame()]]
    elif amount_of_frames == 2:
        layout_frame2 = create_layout(pages_names[0],pages_quality[0])
        layout_frame4 = create_layout(pages_names[1],pages_quality[1])
        layout = [
            [blank_frame(), sg.Frame("", layout_frame1, size=(112, 600), background_color=bg_color, border_width=0),
            sg.Frame("", layout_frame2, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME2-", visible=True),
            sg.Frame("", layout_frame4, size=(800, 600),background_color=bg_color,border_width=0,key = "-FRAME4-", visible=False),
            sg.Frame("", layout_frame3, size=(112, 600),border_width=0,key = "-ARROW-"), blank_frame()]]
    elif amount_of_frames == 1:
        layout_frame2 = create_layout(pages_names[0],pages_quality[0])

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

