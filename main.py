'''
La La ruina del apostador (Gambler's Ruin) dice que una persona que juegue algún juego con un valor esperado
negativo llegará a perder todo su dinero tarde o temprano, sin importar el sistema que use para apostar.

Podemos hacer una simulación de este concepto en Python, usando la librería random.

1 - Supongamos que comenzamos con 50 fichas (todas del mismo valor) y apostamos una ficha cada vez que jugamos.

2 - Tenemos una probabilidad de 0.4 de ganar cada vez que jugamos (cómo podemos simular esto?). Si ganamos,
tenemos una ficha más. Caso contrario, perdemos la ficha que apostamos.

3 - En una noche se estima que podemos jugar este juego hasta 300 veces, pero si llegamos a tener 0 fichas ya 
no vamos a poder apostar en toda la noche.

Crear un programa que simule nuestra noche de apuestas, que imprima en pantalla cuántas apuestas pudimos hacer
antes de perder todo el dinero o si pudimos sobrevivir a las 300 apuestas.

Para resolver el problema, crear una función que tenga como entradas la cantidad de fichas inicial, la 
probabilidad de victoria de cada juego y la cantidad máxima de veces que podemos jugar, que devuelva la cantidad
de fichas con la que terminamos al final de la noche y la cantidad de apuestas que pudimos hacer.

Correr esta función 20 veces y obtener el valor medio de la cantidad de apuestas final.
Cuánto tiempo tarda cada simulación en ejecutarse? Imprimir en pantalla este tiempo cada vez que se corre la 
función.
'''

import random
import time

comienzo = time.time()

fichas = 50
probabilidad = 0.4
cant_maxima = 300


def simulador_apuestas(Fichas, Prob, C_Max):
    fichas_final = 0
    fichas_final += Fichas
    cant_apuestas = 0
    while cant_apuestas < C_Max and fichas_final > 0:
        a = random.randint(1, 10)
        if a > (10 - Prob*10):
            fichas_final += 1
            cant_apuestas += 1
        else:
            fichas_final -= 1
            cant_apuestas += 1
    return fichas_final, cant_apuestas


prueba = simulador_apuestas(fichas, probabilidad, cant_maxima)
print(f"Cantidad de fichas al final de la noche es: {prueba [0]}")
print(
    f"La cantidad de apuestas antes de perder todas las fichas fue de: {prueba[1]}")
#print (prueba)


def simulador_prom(Fichas, Prob, C_Max):
    cont = 20
    total_apuestas = 0
    for i in range(cont):
        prueba = simulador_apuestas(Fichas, Prob, C_Max)
        total_apuestas += prueba[1]
        #print (total_apuestas)

    return print('El promedio total de apuestas es:', round(total_apuestas/20))


simulador_prom(fichas, probabilidad, cant_maxima)

fin = time.time()
tiempo_total = (fin - comienzo) * 1000
print("El tiempo de ejecucion del programa fue: %.4f milisegundos" % tiempo_total)
