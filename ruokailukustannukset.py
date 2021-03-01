timesPerWeek = int(input("Montako kertaa viikossa syöt Unicafessa? "))
uniCafePrice = float(input("Unicafe-lounaan hinta? "))
perWeekShop = float(input("Paljonko käytät viikossa ruokaostoksiin? "))
print("")
 
uniCafeTotal = uniCafePrice * timesPerWeek
weekly = uniCafeTotal + perWeekShop
daily = weekly / 7
 
print("Kustannukset keskimäärin: ")
print(f"Päivässä {daily} euroa")
print(f"Viikossa {weekly} euroa")