# Kirjoita ratkaisu tähän
ensimmäinen = input("Anna 1. kirjain: ")
toinen = input("Anna 2. kirjain: ")
kolmas = input("Anna 3. kirjain: ")
 
if ensimmäinen > toinen and ensimmäinen < kolmas:
    print(f"Keskimmäinen kirjain on {ensimmäinen}")
elif ensimmäinen < toinen and ensimmäinen > kolmas:
    print(f"Keskimmäinen kirjain on {ensimmäinen}")
elif toinen > ensimmäinen and toinen < kolmas:
    print(f"Keskimmäinen kirjain on {toinen}")
elif toinen < ensimmäinen and toinen > kolmas:
    print(f"Keskimmäinen kirjain on {toinen}")
elif kolmas > toinen and kolmas < ensimmäinen:
    print(f"Keskimmäinen kirjain on {kolmas}")
elif kolmas < toinen and kolmas > ensimmäinen:
    print(f"Keskimmäinen kirjain on {kolmas}")
 