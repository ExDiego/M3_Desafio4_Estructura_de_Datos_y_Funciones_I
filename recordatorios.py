import sys


recordatorios = [
    ['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-01', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]
]

recordatorios.append(["2021-02-01", "06:00", "Empezar el año"])
recordatorios[2]=['2021-07-16', "13:00", "No hacer nada es feriado"]
recordatorios.pop(1) #se borra el 01-05
recordatorios.append(['2021-12-24', "22:00", "Cena de Navidad"]) #se añade
recordatorios.append(['2021-12-31', "22:00", "Cena de Año Nuevo"]) #se añade cena

#for recordatorio in recordatorios:
#    print(recordatorio)

print('''
        ''')

for fechas in sorted(recordatorios):
    print(fechas)
    
