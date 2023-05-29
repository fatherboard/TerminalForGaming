import psutil
import csv
import datetime
import time

tiempo = int(input("Ingresa la duración de la recopilación de datos en segundos: "))
carpeta = input("Ingresa el nombre de la carpeta para guardar los datos: ")

with open(f'/home/pi/Desktop/Resultados Benchmarks/{carpeta}/registros.csv', mode='w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(['Fecha', 'Hora', 'CPU %', 'Temperatura CPU', 'Frecuencia CPU', 'Uso Procesador', 'Uso RAM'])

inicio = datetime.datetime.now()  # tiempo de inicio
final = inicio + datetime.timedelta(seconds=tiempo)  # tiempo final

while datetime.datetime.now() < final:
    cpu = psutil.cpu_percent()
    temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
    proc = psutil.Process().cpu_percent()
    freq = psutil.cpu_freq().current
    ram = psutil.virtual_memory().percent
    fecha = datetime.datetime.now().strftime('%m-%d')
    hora = datetime.datetime.now().strftime('%H:%M')
    with open(f'/home/pi/Desktop/Resultados Benchmarks/{carpeta}/registros.csv', mode='a', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([fecha, hora, cpu, temp, freq, proc, ram])
    time.sleep(10)  # esperar 10 segundos antes de obtener el siguiente registro

print('Registros completados.')