import csv

enlaces = open('enlaces.txt', 'w')
mensaje = input('ingrese el mensaje ')

with open('clientes.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        nombre = row[0]
        telefono = row[1]
        mensaje_f = mensaje.replace(' ', '%20')
        mensaje_f_name = mensaje_f.replace('asd', f'{nombre}')
        enlaces.write(f'https://wa.me/{telefono}?text={mensaje_f_name}\n')