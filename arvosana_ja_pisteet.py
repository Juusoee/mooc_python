# Kirjoita ratkaisu tähän
pisteet = int(input("Anna pisteet [0-100]: "))
 
if pisteet > 100:
    print("Arvosana: mahdotonta!")
elif pisteet >= 90 <= 100:
    print("Arvosana: 5")
elif pisteet >=80 <= 89:
    print("Arvosana: 4")
elif pisteet >=70 <= 79:
    print("Arvosana: 3")
elif pisteet >=60 <=69:
    print("Arvosana: 2")
elif pisteet >= 50 <= 59:
    print("Arvosana: 1")
elif pisteet > 0 <= 49:
    print("Arvosana: hylätty")
elif pisteet < 0:
    print("Arvosana: mahdotonta!")