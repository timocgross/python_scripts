import random
import time

print('Hallo! Wie heiẞt du?')

name = input()

print('Oke ' + name + ', lass uns ein Spiel spielen.')
print('Ich werde mir eine Zahl zwischen 1 und 10 ausdenken und du musst versuchen, sie zu erraten.')
secretNumber = random.randint(1, 10)

time.sleep(3)       # Das Programm pausiert für drei Sekunden.

print('Oke, ich habe eine.')

for guessesTaken in range (1, 4):
    print('Rate.')
    guess = int(input())

    if guess < secretNumber:
        print('Die Zahl ist gröẞer.')
    elif guess > secretNumber:
        print('Die Zahl ist kleiner.')
    else:
        break       # Der Benutzer hat die Zahl erraten.

if guess == secretNumber:
    print('Wow! Du hast es geschafft, meine Zahl in ' + str(guessesTaken) + ' Versuchen zu erraten!')

else:
    print('Leider falsch, meine Zahl war ' + str(secretNumber) + '.')       # Der Benutzer hat verloren.