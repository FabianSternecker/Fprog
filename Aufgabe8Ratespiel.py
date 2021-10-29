import random
z = random.randint(0,9);
print("Willkommen zum Ratespiel! Du hast drei Versuche!")

for x in range(3):
    guess = z - int(input("Rate die Zahl!"))
    if guess == 0:
        print("Du lagst richtig!")
        break
    elif guess<0:
        print("Die gesuchte Zahl ist kleiner!")
    elif guess>0:
        print("Die gesuchte Zahl ist größer!")
if guess != 0:
    print("Verloren!")
