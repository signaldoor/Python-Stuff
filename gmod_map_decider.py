import random
import time
import keyboard

random_number = random.randint(0, 10)

maps = ["Construct", "Shambles", "Gmall", "Normal Mall", "Shambles Night", "Dollar General", "", "Ultrabox", "", "Neon Construct", "Theatre", "Tornado Alley", "Halfway Park", "7 Eleven", "Granli", "Moon Surface"]

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