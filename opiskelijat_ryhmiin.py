howMany = int(input("Montakoha opiskelijaa? "))
groupSize = int(input("Mikä on ryhmä koko? "))
 
summa = howMany / groupSize
 
 
if summa < groupSize:
    print(f"Ryhmien määrä: {int(summa)}")
if summa >= groupSize:
    print(f"Ryhmien määrä: {int(summa+1)}")
elif summa <= groupSize:
    print(f"Ryhmien määrä: {int(summa+1)}")
 