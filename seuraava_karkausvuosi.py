def find_leap(year, first):
    if not first and ((year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)):
        return year
    else:
        return find_leap(year+1, False)
 
year = int(input("Vuosi: "))
print("Vuotta", year, "seuraava karkausvuosi on", find_leap(year, True))
 