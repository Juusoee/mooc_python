# Kirjoita ratkaisu tähän
print("Henkilö 1:")
henkilo1 = input("Nimi: ")
ika1 = int(input("Ikä: "))
print("Henkilö 2:")
henkilo2 = input("Nimi: ")
ika2 = int(input("Ikä: "))
 
if ika1 < ika2:
    print(f"Vahnempi on {henkilo2}")
elif ika1 > ika2:
    print(f"Vanhempi on {henkilo1}")
elif ika1 == ika2:
    print(f"{henkilo1} ja {henkilo2} ovat yhtä vanhoja")
