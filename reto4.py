# Reto #4 - Lista de invitados

"""Estás organizando un banquete al que quieres invitar a tus amigos. Crea un programa que pida el nombre de uno de tus amigos, al hacerlo aumenta en uno una variable contadora, después pregunta si quieres invitar a alguien más: si la respuesta es afirmativa entonces pregunta por una persona más; en caso contrario cierra el ciclo y muestra en pantalla cuantos invitados son."""

name = str(input('Ingresa el nombre de tu amigo: '))
counter = 1
question = 'y'
while question == 'y':
    question = str(input('¿Invitarás a alguien más? (y/n) '))
    if question == 'y':
        name = str(input('Ingresa el nombre de tu amigo: '))
        counter += 1
        continue
print('Tienes %d invitados a la fiesta' % counter)
