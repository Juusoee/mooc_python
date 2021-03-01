tarina = ""
edellinen_sana = ""
 
while True:
    sana = input("Anna sana: ")
    if sana == "loppu":
        break
    elif sana == edellinen_sana:
        break
    edellinen_sana = sana
    tarina += sana + " "
 
print(tarina)