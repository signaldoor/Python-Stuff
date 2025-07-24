import random

random_number = random.randint(0, 4)

headwear = ["Freeman Glasses", "Valve", "Ludens Sunglasses", "V's headware", "Bridges Cap"]

print(f"The number is: {str(random_number)}")
print(f"The next headwear you have to wear is: {headwear[random_number]}")