"""
investigar random.choice() de la librería random
python juego.py piedra

Tu jugaste Piedra
Computador jugó tijera
Ganaste!!

Argumento inválido: Debe ser piedra, papel o tijera.
"""

import sys
import random   

jugador = sys.argv[1].lower()

computador = ["piedra", "papel", "tijera"]
computador = random.choice(computador)

#mylist = ["apple", "banana", "cherry"]
#print(random.choice(mylist))

if jugador == "piedra" or jugador == "papel" or jugador == "tijera":
    if jugador == "piedra" and computador == "piedra" or jugador == "papel" and computador == "papel" or jugador == "tijera" and computador == "tijera":
        print(f"Tu jugaste {jugador}\nComputador jugó {computador}\nEmpataste!!")
    elif jugador == "piedra" and computador == "tijera" or jugador == "papel" and computador == "piedra" or jugador == "tijera" and computador == "papel":
        print(f"Tu jugaste {jugador}\nComputador jugó {computador}\nGanaste!!")
    else:
        print(f"Tu jugaste {jugador}\nComputador jugó {computador}\nPerdiste!!")
else:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")



