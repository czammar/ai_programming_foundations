"""
A dummy game to guess a random number between 1 and 10
"""

import random

# Create a random number from 1 to 10
secret_number = random.randint(1, 10)
intents = 0

# Begin message
print("Por favor elige un número entre 1 y 10. Solo tienes 3 intentos ;)")

while True:
    try:
        if intents >= 3:
            print("Quemaste tus 3 intentos, Perdiste :(!!!")
            break

        user_input = int(input("Tu Respuesta: "))

        if user_input < 1 or user_input > 10:
            print("Intenta de nueva, con un número entre 1 y 10.")
            continue

        # Comparision between goal and objetive
        if user_input == secret_number:
            print("¡Correcto! Adivinaste el número.")
            break
        elif abs(user_input - secret_number) <= 2:
            intents = intents+1
            print("Caliente!! 🔥 🔥 🔥 ")
        else:
            intents = intents+1
            print("Frío!! ❄️ ❄️ ❄️ ")
    except ValueError:
        print("Por favor ingresa un número válido.")
