mjono = input("Anna merkkijono: ")
 
numero = 0
osa = mjono[numero]
pituus = len(mjono)
sana = mjono[0]
while True:
    kohta = mjono.find(osa)
    if kohta >= 0:
        print(sana)
        numero += 1
        if numero >= pituus:
            break  
        else:
            sana += mjono[numero]
        