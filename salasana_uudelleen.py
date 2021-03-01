# Kirjoita ratkaisu tähän
salasana1 = input("Salasana:")
salasana2 = input("Toista salasana:")
while True:
    if salasana1 == salasana2:
        break
    print("Ei ollut sama!")
    salasana2 = input("Toista salasana:")
print("Käyttäjätunnus luotu!")