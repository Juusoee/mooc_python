# Kirjoita ratkaisu tähän
vuosi = int(input("Anna vuosi: "))
 
 
if vuosi % 4 != 0:
    print("Vuosi ei ole karkausvuosi.")
elif vuosi % 100 == 0 and vuosi % 400 != 0:
    print("Vuosi ei ole karkausvuosi.")
else:
    print("Vuosi on karkausvuosi.")