import tkinter as tk
from tkinter import messagebox
import bluetooth
import subprocess
import os
import shutil

bg_color = "#965fd4"
activebackground = "#734f9a"

class AcceptWindow(tk.Toplevel):
	def __init__(self, master, message, callback):
		super().__init__(master)
		self.title("Accept Window")
		self.message = message
		self.callback = callback
		self.init()

	def init(self):
		tag_message = tk.Label(self, text=self.message)
		tag_message.pack(padx=20, pady=20)
		btn_accept = tk.Button(self, text="Accept", command=self.accept)
		btn_accept.pack(padx=10, pady=10)
		self.grab_set()

	def accept(self):
		self.callback()
		self.destroy()

def modify_config_file():
	# Ruta del archivo config.txt
	config_file = "/boot/config.txt"

	# Ruta del archivo temporal para modificar
	temp_file = "/tmp/temp_config.txt"

	# Copiar el archivo config.txt al archivo temporal
	shutil.copyfile(config_file, temp_file)

	# Abrir el archivo temporal para lectura y escritura
	with open(temp_file, "r+") as file:
		# Leer todo el contenido del archivo
		content = file.read()

		# Buscar la sección delimitada por [OVERCLOCK]
		start = content.find("[OVERCLOCK]\n")
		end = content.find("\n\n", start)
		if end == -1:
			end = len(content)

		# Reemplazar la sección existente con la nueva sección
		new_config = "[OVERCLOCK]\nforce_turbo=0\nover_voltage=0\narm_freq=1800\ngpu_freq=750"
		content = content[:start] + new_config + content[end:]

		# Regresar al inicio del archivo y escribir los cambios
		file.seek(0)
		file.write(content)
		file.truncate()

	# Sobreescribir el archivo config.txt con el contenido del archivo temporal
	shutil.copyfile(temp_file, config_file)

	# Eliminar el archivo temporal
	os.remove(temp_file)
	#os.system('sudo reboot')
	
# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de dos frames")
ventana.attributes("-fullscreen", True)

# Crea un frame principal para contener los dos frames secundarios
frame_principal = tk.Frame(ventana,bg=bg_color,highlightthickness=0,borderwidth=0)
frame_principal.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Divide el frame principal en dos frames secundarios
frame_izquierdo = tk.Frame(frame_principal,bg=bg_color,highlightthickness=0,borderwidth=0)
frame_izquierdo.pack(side=tk.LEFT, expand=True)

# Crea la lista de redes
frame_derecho = tk.Frame(frame_principal,bg=bg_color)
frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Obtener una lista de todos los dispositivos Bluetooth disponibles

# Crear etiqueta para la lista de dispositivos
texto=tk.Label(frame_derecho, text="Overclock SetUp\n\nGpuFreq=750\n\nArmFreq=1800\n\nTURBO= NO\n\nOVER Voltage = NO\n",bg=bg_color,font=('Roboto', 25,'bold'),fg='white', anchor='center')
texto.pack(side=tk.TOP, padx=50, pady=40)
# Crear lista de dispositivos como botones
   
frame_boton = tk.Frame(frame_principal,bg=bg_color,highlightthickness=0,borderwidth=0)
frame_boton.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
frame= tk.Frame(frame_derecho,bg=bg_color,highlightthickness=0,borderwidth=0)
frame.pack(side=tk.LEFT, expand=True)

imagen = tk.PhotoImage(file="/home/pi/Downloads/iconoRelax.png")
etiqueta_imagen = tk.Label(frame_izquierdo, image=imagen,borderwidth=0,bg=bg_color,activebackground="#C090FF",highlightthickness=0, padx=10, pady=10, anchor="center")
etiqueta_imagen.pack(side=tk.TOP, padx=100, pady=50)

btn_ret = tk.Button(frame_izquierdo, text="CLOSE",borderwidth=0,bg=bg_color,highlightthickness=0,activebackground="#C090FF",fg='white',font=('Roboto', 32,'bold'), command = ventana.destroy)
btn_ret.pack(side=tk.TOP)

btn_ret = tk.Button(frame_derecho, text="REBOOT",borderwidth=0,bg=bg_color,highlightthickness=0,activebackground="#C090FF",fg='white',font=('Roboto', 32,'bold'), command = modify_config_file)
btn_ret.place(x=160, y=460)

ventana.mainloop()

