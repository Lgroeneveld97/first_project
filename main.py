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

temperatuur = 25
if temperatuur > 30:
    print("Het is heet buiten.")

for i in range(2, 14, 2):  # van 2 t/m 10, steeds +2
    print(i)

dieren = ["hond", "kat", "konijn"]

for pil in dieren:
    print("Ik zie een", pil)

getallen = [10, 20, 30, 40]
dieren = ["hond", "kat", "konijn"]

print(getallen)
print(dieren)

print(dieren[0])   # hond
print(dieren[2])   # konijn
print(dieren[-3])  # hond

dieren.append("olifant")   # toevoegen aan het einde
print(dieren)

dieren.remove("hond")      # eerste 'hond' verwijderen
print(dieren)

laatste = dieren.pop()     # haalt laatste element weg
print("Weggehaald:", laatste)

for dier in dieren:
    print("Ik zie een", dier)

getallen = [5, 2, 9, 1]

print(len(getallen))   # lengte → 4
print(min(getallen))   # kleinste → 1
print(max(getallen))   # grootste → 9
print(sorted(getallen)) # gesorteerde lijst → [1,2,5,9]
print(sum(getallen))   # som → 17

def begroet():
    print("Hallo!")
    print("Welkom bij Python.")
begroet()