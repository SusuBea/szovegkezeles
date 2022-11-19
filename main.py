
#Kérj be a felhasználótól egy szöveget
szoveg = input("Írj be valamit: ")
#Alakítsd át nagybetűssé
print(szoveg.upper())

#Az előző szövegről döntsd el, hogy 10 karakternél hosszabb-e?
# Ha igen, írd ki a hosszát!
if len(szoveg) >= 10:
    print(f"A szöveg hossza: {len(szoveg)}")
print("")


szoveg = input("Adj meg egy szövegt ami 3 betűnál hosszabb: ")
while len(szoveg) <3:
    print("Ez kevesebb volt, mint 3 betű!")
    szoveg = input("Adj meg újra egy több mint 3 betűs szöveget:  ")
else:
    print(szoveg)
print("")

szoveg = input("Adj meg egy szöveget: ")
i=0
while i < len(szoveg) and szoveg[i].upper() != "A":
    i += 1

if i < len(szoveg):
    print(f" Van a betű 'a' szövegben a {i+1}. karakteren. ")
else:
    print("Nincs a szövegben a betű.")
print("")

szoveg = input("Írj be egy szöveget: ")
i=0
a_sum = 0
while i < len(szoveg):
    if szoveg[i].upper() == "A":
        a_sum += 1
    i+= 1
print(f"{a_sum} darab a betű van a szövegben.")











