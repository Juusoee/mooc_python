saaEnnuste = print("Kerro huominen sääennuste:")
lampotila = int(input("Lämpötila: "))
sataako =  input("Sataako (kyllä/ei): ")
 
 
if lampotila >= 21:
    print("Pue housut ja t-paita")
elif lampotila >= 11:
    print("Pue housut ja t-paita")
    print("Ota myös pitkähihainen paita")
elif lampotila >= 6:
    print("Pue housut ja t-paita")
    print("Ota myös pitkähihainen paita")
    print("Pue päälle takki")
elif lampotila <= 5:
    print("Pue housut ja t-paita")
    print("Ota myös pitkähihainen paita")
    print("Pue päälle takki")
    print("Suosittelen lämmintä takkia")
    print("Kannattaa ottaa myös hanskat")
if sataako == "kyllä":
    print("Muista sateenvarjo!")
    