# Reto #2 - Más allá del cuarenta y dos

"""Crea un código que pida al usuario un número y se repita hasta que coloque un número mayor a 42. Cuando se cumpla esta condición muestra el resultado en pantalla indicando esto al usuario y finaliza el ciclo."""

while True:
    number = int(input('Escribe un número: '))
    if number < 42:
        continue
    else:
        print('%d es mayor a 42, excelente!' % number)
        break
