# Korjaa ohjelma
luku = int(input("Anna luku: "))
 
if luku > 100:
    luku = luku - 100
    print("Luku oli suurempi kuin sata")
    print("Nyt luvun arvo on pienentynyt sadalla")
    print(f"Arvo on nyt {luku}")
    print(f"{luku} taitaa olla onnenlukuni!")
    print("Hyvää päivänjatkoa!")
elif luku <= 100:
    print(f"{luku} taitaa olla onnenlukuni!")
    print("Hyvää päivänjatkoa!")
 