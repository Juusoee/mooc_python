yritykset = 1
 
while True:
    pinkoodi = int(input("PIN-koodi: "))
    if pinkoodi != int(4321):
        yritykset = yritykset +1
        print("Väärin")
 
    if pinkoodi == int(4321):
        break
if yritykset == 1:
    print("Oikein, tarvitsit vain yhden yrityksen!")
else:
    print(f"Oikein, tarvitsit {yritykset} yritystä")     
    