# Reto #6 - “Un elefante se balanceaba…”

"""Escribe un programa que inicie mostrando en pantalla la letra de “Un elefante se balanceaba” iniciando con el número 1, después pregunta al usuario cuantos elefantes más se balancearán y debe responder un número más al mostrado. En caso de ingresar un número diferente pedirle que intente de nuevo y repetir el ciclo hasta tener 10 elefantes.
Tomar en cuenta cuando el texto muestra un solo elefante y varios elefantes.
Ejemplo de inicio:

1 elefante se balanceaba
Sobre la tela de una araña
Como veía que resistía
Fueron a llamar otro elefante"""


elephants = 1
print(elephants, 'elefante se columpiaba\nSobre la tela de una araña\nComo veía que resistía\nFueron a llamar a otro elefante')
while elephants < 10:
    more = int(input('\n¿Cuántos elefantes más se columpian? '))
    if more != elephants + 1:
        print('Número incorrecto, intenta de nuevo')
    else:
        elephants += 1
        print(elephants, 'elefantes se columpiaban\nSobre la tela de una araña\nComo veían que resistía\nFueron a llamar a otro elefante')
        continue
print('\nSe acabarón los elefantes...')
