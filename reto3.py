# Reto #3 - Sumas consecutivas

"""Pide al usuario que ingrese dos números y los sume. Después pregunta si quiere añadir otro número: si la respuesta es afirmativa añádelo al total; en caso contrario finaliza el ciclo y muestra el resultado total en pantalla."""

while True:
    num1 = int(input('Ingresa un número: '))
    num2 = int(input('Ahora otro: '))
    res = num1 + num2
    question = str(input('¿Quíeres sumar otro número? (y/n) ').lower())
    if question == 'y':
        num3 = int(input('Ingresa el número: '))
        res = num1 + num2 + num3
        print('El resultado de la suma es: {}'.format(res))
        break
    else:
        print('El resultado de la suma es: {}'.format(res))
        break
