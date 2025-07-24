import time
import keyboard

# Logging in le' Terminal

time.sleep(1)
print("Connecting...")
time.sleep(2)
print("\nCONNECTION SUCCESSFUL!\n\n\nWelcome To The UCA Porting Service Terminal. Please Log In With Your UCA Credentials.")
with open(r"PATH_TO_ASCII_ART", "r") as file:
    ascii_art = file.read()
print(ascii_art)
time.sleep(2)
print("\n\n\nLogging In...")
time.sleep(2.3)
print("\nWelcome, Sam Porter Bridges.")
time.sleep(2)

# Max Carry Capacity

while True:
    try:
        carry_capacity = float(input("\n\nEnter Your Max Carry Capacity (kg): "))
        break
    except ValueError:
        print("Invalid Input. Please Enter A Valid Number (e.g., 50 or 80.5)")

# Total Orders

cargo_total_weight = input("\nInput Number of Orders: ")
total_weight = float(cargo_total_weight)

# Cargo Weight & Carry Capacity Comparison

if total_weight == 1:
    cargo_1 = float(input("\nInput Weight For First Order (kg): "))
    total_cargo = cargo_1
    print(f"\n\nTotal Cargo Weight: {round(total_cargo)} Kilos.")
    if carry_capacity > cargo_1:
        print(f"Cargo Weight Is {round(carry_capacity - cargo_1)}kg Under Max Carry Capacity.")
    elif carry_capacity < cargo_1:
        print(f"Cargo Weight Is {round(cargo_1 - carry_capacity)}kg Over Max Carry Capacity.")
    else:
        print("Cargo Weight Exactly Matches Cargo Capacity.")
            
elif total_weight == 2:
    cargo_1 = float(input("Input Weight for First Order (kg): "))
    cargo_2 = float(input("Input Weight For Second Order (kg): "))
    total_cargo = cargo_1 + cargo_2
    print(f"\n\nTotal Cargo Weight: {round(total_cargo)} Kilos.")
    if carry_capacity > total_cargo:
        print(f"Cargo Weight Is {round(carry_capacity - total_cargo)}kg Under Max Carry Capacity.")
    elif carry_capacity < total_cargo:
        print(f"Cargo Weight Is {round(total_cargo - carry_capacity)}kg Over Max Carry Capacity.")
    else:
        print("Cargo Weight Exactly Matches Max Carry Capacity.")

elif total_weight == 3:
    cargo_1 = float(input("Input Weight For First Order (kg): "))
    cargo_2 = float(input("Input Weight For Second Order (kg): "))
    cargo_3 = float(input("Input Weight For Third Order (kg): "))
    total_cargo = cargo_1 + cargo_2 + cargo_3
    print(f"\n\nTotal Cargo Weight: {round(total_cargo)} Kilos.")
    if carry_capacity > total_cargo:
        print(f"Cargo Weight Is {round(carry_capacity - total_cargo)}kg Under Max Carry Capacity.")
    elif carry_capacity < total_cargo:
        print(f"Cargo Weight Is {round(total_cargo - carry_capacity)}kg Over Max Carry Capacity.")
    else:
        print("Cargo Weight Exactly Matches Max Carry Capacity.")

elif total_weight == 4:
    cargo_1 = float(input("Input Weight For First Order (kg): "))
    cargo_2 = float(input("Input Weight For Second Order (kg): "))
    cargo_3 = float(input("Input Weight For Third Order (kg): "))
    cargo_4 = float(input("Input Weight For Fourth Order (kg): "))
    total_cargo = cargo_1 + cargo_2 + cargo_3 + cargo_4
    print(f"\n\nTotal Cargo Weight: {round(total_cargo)} Kilos.")
    if carry_capacity > total_cargo:
        print(f"Cargo Weight Is {round(carry_capacity - total_cargo)}kg Under Max Carry Capacity.")
    elif carry_capacity < total_cargo:
        print(f"Cargo Weight Is {round(total_cargo - carry_capacity)}kg Over Max Carry Capacity.")
    else:
        print("Cargo Weight Exactly Matches Max Carry Capacity.")

elif total_weight == 5:
    cargo_1 = float(input("Input Weight For First Order (kg): "))
    cargo_2 = float(input("Input Weight For Second Order (kg): "))
    cargo_3 = float(input("Input Weight For Third Order (kg): "))
    cargo_4 = float(input("Input Weight For Fourth Order (kg): "))
    cargo_5 = float(input("Input Weight For Fifth Order (kg): "))
    total_cargo = cargo_1 + cargo_2 + cargo_3 + cargo_4 + cargo_5
    print(f"\n\nTotal Cargo Weight: {round(total_cargo)} Kilos.")
    if carry_capacity > total_cargo:
        print(f"Cargo Weight Is {round(carry_capacity - total_cargo)}kg Under Max Carry Capacity.")
    elif carry_capacity < total_cargo:
        print(f"Cargo Weight Is {round(total_cargo - carry_capacity)}kg Over Max Carry Capacity.")
            
    else:
        print("Cargo Weight Exactly Matches Max Carry Capacity.")

else:
    print("(Invalid Numbers. Max Number of 5 Orders At Once.)")

# Exit

time.sleep(0.5)
print("\n\n\nPress Any Key To Exit UCA Porting Terminal...")
keyboard.read_key()
exit()