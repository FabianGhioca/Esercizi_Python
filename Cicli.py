# Esercizio repository GitHub CICLI

i = 0
while i <= 10:
    print(i)
    i += 1

marche = ["BMW", "Ferrari", "Mazda"]
print("Queste sono le marche presenti: ")
print(marche)
i = input("Inserisci la marca: ")
for x in marche:
    if x == i: 
        print("" +i,"è presente nella lista")
        break