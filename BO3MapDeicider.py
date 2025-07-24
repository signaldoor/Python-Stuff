import random
import time
import keyboard

random_number = random.randint(0, 10)

maps = ["Shadows of Evil", "Kino der Toten", "Nacht der Untoten", "Origins", "Shi No Numa", "Verrückt", "Ascension", "Moon", "The Giant", "Shangri-La", "Custom Map"]

with open(r"PATH_TO_ASCII_ART", "r") as file:
    ascii_art = file.read()
print(ascii_art)

print("\n\nThe Next Map Will Be: ", end='', flush=True)
time.sleep(2)
print(maps[random_number])

time.sleep(1.5)
print("\n\n\n\nPress any key to exit: ")
keyboard.read_key()
exit()