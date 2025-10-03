print("Hallo, wereld!")

name = "Micheal"
age = 20
print(f"Mijn naam is {name} en ik ben {age} jaar oud.")

age = age + 1
print(f"Volgend jaar ben ik {age} jaar oud.")

country = "Nederland"
print(f"Ik kom uit {country}.")

a = 10
b = 3

print(a + b)   # optellen → 13
print(a - b)   # aftrekken → 7
print(a * b)   # vermenigvuldigen → 30
print(a / b)   # delen → 3.333...
print(a // b)  # hele getallen delen → 3
print(a % b)   # restwaarde → 1

voornaam = "Lucas"
achternaam = "Jansen"

volledige_naam = voornaam + " " + achternaam
print(volledige_naam)   # Lucas Jansen
print("ha" * 20)   # hahaha... (20 keer)

x = 5
y = 10

print(x < y)   # True
print(x == y)  # False
print(x != y)  # True

cijfer = 7

if cijfer >= 9:
    print("Uitmuntend!")
elif cijfer >= 6:
    print("Voldoende")
else:
    print("Onvoldoende")
