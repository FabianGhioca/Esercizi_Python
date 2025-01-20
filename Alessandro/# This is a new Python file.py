import csv

programma1 = "C"
programma2 = "C#"
programma3 = "Python"

print("Programmi imparati:" "\n" + programma1 + "\n" + programma2 + "\n"+ programma3)

print("\nInserisci il livello di competenza per ogni programma da 0 a 5:")
conteggio1 = input("Livello del programma C: ")
conteggio2 = input("Livello del programma C#: ")
conteggio3 = input("Livello del programma Python: ")

conteggi = {
    "C": int(conteggio1),
    "C#": int(conteggio2),
    "Python": int(conteggio3)
}

conteggi_ordinati = sorted(conteggi.items(), key=lambda x: x[1], reverse=True)

print("\nConteggi in ordine decrescente:")
for programma, conteggio in conteggi_ordinati:
    print(f"{programma}: {conteggio}")

print("\nMedia dell'esperienza con i programmi è di: {:.2f}".format((int(conteggio1) + int(conteggio2) + int(conteggio3)) / 3))