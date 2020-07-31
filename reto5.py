# Reto #5 - Adivina el número secreto

"""Crea un programa donde tendrás la variable numero_secreto, la cual toma un valor aleatorio entre 1 y 100. Después pide a tu usuario que indique un número para intentar adivinarlo: en caso de acertar indícale cual era el número secreto y cuantos intentos le tomó; en caso contrario indícale si el número ingresado es mayor o menor al número secreto."""

import random

secretNumber = random.randrange(1, 100)
attempts = 0
while True:
    user = int(input('Intenta adivinar un número entre 1 y 100: '))
    attempts += 1
    if user == secretNumber:
        print('\nExcelente, el número secreto era %d, lograste adivinar en %d intentos' % (
            secretNumber, attempts))
        break
    elif user < secretNumber:
        print('Más!')
        continue
    elif user > secretNumber:
        print('Menos!')
        continue
