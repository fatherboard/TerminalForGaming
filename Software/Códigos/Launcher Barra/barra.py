import tkinter as tk
import subprocess
import time

bg_color = "#965fd4"
activebackground = "#734f9a"
fg = "#8bd450"
hover = "#d3290f"
unnable = "#d8d8d8"
unnable_fg = "black"

class Taskbar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack_propagate(False)
        self.pack(side=tk.TOP, fill=tk.X)
        self.configure(bg=bg_color)
        self.wifi_button = tk.Button(self, text='', bg=bg_color,borderwidth = 0,highlightthickness=0, fg=fg,activebackground=activebackground,activeforeground = hover, font=('Roboto', 10, 'bold'),width = 20, anchor= 'w', command=self.open_wifi_manager)
        self.wifi_button.pack(side=tk.LEFT, padx=10)
        self.time_label = tk.Label(self, text='', bg=bg_color, fg=fg, font=('Roboto', 16, 'bold'), width = 10, anchor= 'center')
        self.time_label.pack(side=tk.LEFT, padx=220)
        self.bluetooth_button = tk.Button(self, text='', bg=bg_color,borderwidth = 0,highlightthickness=0, fg=fg,activebackground=activebackground,activeforeground = hover, font=('Roboto', 10, 'bold'),width = 18, anchor= 'w', command=self.open_bluetooth_config)
        self.bluetooth_button.pack(side=tk.LEFT, padx=10)
        self.mouse_active = False
        self.bind('<Enter>', self.handle_mouse_enter)
        self.bind('<Leave>', self.handle_mouse_leave)
        self.update_taskbar()

    def update_taskbar(self):
        # Update time label
        self.time_label.config(text=time.strftime('%H:%M:%S'))

        # Get wifi info
        wifi_info = subprocess.check_output(['iwgetid']).decode('utf-8')
        if 'ESSID' in wifi_info:
            wifi_name = wifi_info.split('"')[1]
            self.wifi_button.config(text=f'WiFi: {wifi_name}')
        else:
            self.wifi_button.config(text='WiFi: Not Connected')

        # Get bluetooth info
        bluetooth_info = subprocess.check_output(['hciconfig']).decode('utf-8')
        if 'BD Address' in bluetooth_info:
            bluetooth_name = bluetooth_info.split('\n')[1].split()[1]
            self.bluetooth_button.config(text=f'Bluetooth: {bluetooth_name}')
        else:
            self.bluetooth_button.config(text='Bluetooth: Not Connected')

        # Schedule next update
        self.after(1000, self.update_taskbar)

    def handle_mouse_enter(self, event):
        self.mouse_active = True
        self.configure_root_size()
        self.show_taskbar()
        

    def handle_mouse_leave(self, event):
        self.mouse_active = False
        self.after(4000, self.hide_taskbar)

    def show_taskbar(self):
        if self.mouse_active:
            self.configure(height=40)
            self.pack(side=tk.TOP, fill=tk.X)

    def hide_taskbar(self):
        if not self.mouse_active:
            self.configure(height=1)
            self.configure_root_transparent()
            
    def configure_root_size(self):
        root.geometry('1024x40+0+0')
        root.configure(bg='')
        
    def configure_root_transparent(self):
        root.geometry('1024x1+0+0')
        root.configure(bg='')
        
    def open_wifi_manager(self):
        output = subprocess.Popen(['iwgetid'], stdout=subprocess.PIPE).communicate()[0]
        wifi_info = output.decode('utf-8')
        if 'ESSID' in wifi_info:
            subprocess.run(["nmcli", "radio", "wifi", "off"])
        else:
            subprocess.run(["nmcli", "radio", "wifi", "on"])
            
    def open_bluetooth_config(self):
        import subprocess

        try:
            output = subprocess.Popen(['iwgetid'], stdout=subprocess.PIPE).communicate()[0]
            wifi_info = output.decode('utf-8')
            if 'ESSID' in wifi_info:
                subprocess.run(["nmcli", "radio", "wifi", "on"])
            else:
                print('Not connected to WiFi')
        except subprocess.CalledProcessError:
            print('Error getting WiFi information')

root = tk.Tk()
root.geometry('1024x40+0+0')
root.configure(bg='')
root.overrideredirect(True)
taskbar = Taskbar(root)
root.mainloop()