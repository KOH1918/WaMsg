import pywhatkit
from datetime import datetime
import time
import csv

mensaje = input('ingrese el mensaje ')

with open('clientes.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        seconds = time.time() + 60
        date = datetime.fromtimestamp(seconds)
        telefono = row[0]
        pywhatkit.sendwhatmsg(telefono, mensaje, date.hour, date.minute)