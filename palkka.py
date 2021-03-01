tuntipalkka = float(input("Tuntipalkka: "))
tyotunnit = int(float(input("Työtunnit: ")))
viikonpaiva = input("Viikonpäivä: ")
 
if viikonpaiva == "sunnuntai":
    tuntipalkka = tuntipalkka*2.0
    print(f"Palkka {float(tyotunnit*tuntipalkka)} euroa")
if viikonpaiva == "maanantai":
    summa = tuntipalkka*tyotunnit
    print(f"Palkka {float(summa)} euroa")
if viikonpaiva == "tiistai":
    summa = tuntipalkka*tyotunnit
    print(f"Palkka {float(summa)} euroa")
if viikonpaiva == "keskiviikko":
    summa = tuntipalkka*tyotunnit
    print(f"Palkka {float(summa)} euroa")
if viikonpaiva == "torstai":
    summa = tuntipalkka*tyotunnit
    print(f"Palkka {float(summa)} euroa")
if viikonpaiva == "perjantai":
    summa = tuntipalkka*tyotunnit
    print(f"Palkka {float(summa)} euroa")
if viikonpaiva == "lauantai":
    summa = tuntipalkka*tyotunnit
    print(f"Palkka {float(summa)} euroa")
 
