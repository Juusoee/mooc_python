lukumaara = -1
summa = 0
pos = 0
neg = 0
 
print("Syötä kokonaislukuja, 0 lopettaa:")
 
while True:
    luku = int(input("Luku: "))
    summa += luku
    lukumaara = lukumaara +1
    if luku == 0:
        break
    if luku < 0:
        neg = neg +1
    if luku > 0:
        pos = pos +1
print(f"Lukuja yhteensä {int(lukumaara)}")
print(f"Lukujen summa {summa}")
print(f"Lukujen keskiarvo {float(summa/lukumaara)}")
print(f"Positiivisia {pos}")
print(f"Negatiivisia {neg}")