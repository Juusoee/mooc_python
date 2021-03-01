sana = input("Sana: ")
pituus = len(sana)
vali1 = ""
vali2 = ""
 
print(30 * "*")
 
if pituus % 2 != 0:
    vali2 += " "
if pituus == 28:
    print("*"+sana+"*")
    
while len("*") + len(vali1) + len(sana) + len(vali2) +  len("*") < 30:    
    vali1 += " "
    vali2 += " "
 
 
 
print("*" + vali1 + sana + vali2 + "*")
 
print(30 * "*")