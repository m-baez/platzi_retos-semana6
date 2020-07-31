# Reto #1 - Suma hasta cincuenta

"""Crea una variable que se llame total, después pide a tu usuario que ingrese un número y lo sume al valor de total. Haz que esto se repita hasta que el valor de total sea mayor a 50 y muestra el resultado en pantalla."""

total = 0
limit = 50

while total <= limit:
    number = int(input('Ingresa un número: '))
    total += number
print('%d es mayor que 50' % total)
