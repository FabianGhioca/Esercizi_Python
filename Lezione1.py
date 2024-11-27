# Inserimento di dati e stamparli

#nomeinput = input("Inserisci nome: ")
#cognomeinput = input("Inserisci cognome: ")
#data = input("Inserisci la data di nascita: ")
#print("Questo è il tuo nome e cognome: " +nomeinput, "" +cognomeinput, "e sei nato il " + data)


# Operazione somma

#numero1 = int(input("inserisci numero 1:"))
#numero2 = int(input("inserisci numero 2:"))
#print("La somma è = ",numero1+numero2)


# Operazione moltiplicazione

#numero1 = int(input("inserisci numero 1:"))
#numero2 = int(input("inserisci numero 2:"))
#print("La moltiplicazione è = ",numero1*numero2)


# Operazione divisione

#numero1 = int(input("inserisci numero 1:"))
#numero2 = int(input("inserisci numero 2:"))
#print("La moltiplicazione è = ",numero1/numero2)


# Esercizio1
# Cocatenazione delle stringhe, stampare le stringhe, ricevere un input da tastiera, 
# operazioni sulle variabili (somma, moltiplicazione, divisione ecc.)

# nome = input("Inserisci nome: ")
# cognome = input("Inserisci cognome: ")
# data = input("Inserisci la data di nascita: ")
# print("Questo è il tuo nome e cognome: " +nome, "" +cognome, "e sei nato il " + data)
# 
# numero1 = int(input("inserisci numero 1:"))
# numero2 = int(input("inserisci numero 2:"))
# print("La somma è = ",numero1+numero2)
# print("La moltiplicazione è = ",numero1*numero2)
# 
# if numero1 >= numero2:
#     print("La Divisione è = ",numero1/numero2)
#     print("La sottrazzione è = ",numero1-numero2)
# else:
#     print("Non è possibile effettuare la divisione e la sottrazzione")



# Esercizio 2

# cognomeinput = input("Inserisci cognome: ")
# nomeinput = input("Inserisci nome: ")
# datainput = input("Inserisci la data di nascita: ")
# print("La tua data e il tuo nome è " +cognomeinput, "" +nomeinput, "" +datainput)


# IF

# x = 4
# if x > 3:
#     print("x maggiore di 3")



# Esercizio 3

# numero1 = input("inserisci in primo numero: ")
# numero2 = input("inserisci in secondo numero: ")
# numero3 = input("inserisci in terzo numero: ")
# if numero1 == numero2 == numero3:
#     print("Tutti i numeri inseriti sono uguali e il valore è: " + numero1)
# elif numero1 == numero2:
#     print("Numero 1 e uguale a numero 2 e il valore è: " + numero1)
# elif numero1 == numero3:
#     print("Numero 1 e uguale a numero 3 e il valore è: " + numero1)
# elif numero2 == numero3:
#     print("Numero 2 e uguale a numero 3 e il valore è: " + numero2)
# else:
#     print("non ci sono valori inseriti uguali")


# eta = int(input("Inserisci l'eta: "))
# if eta < 13:
#     print("Bambino")
# elif 13 <= eta < 18:
#     print("Adolescente")
# else:
#     print("Adulto")



# Lista

# frutta = ["mela", "banana", "uva"]
# if "mela" in frutta:
#     print("La mela è nella lista della frutta")
# else:
#     print("La mela è finita")



# FOR

# for i in range (5,10):
#     print(i)



# Funzione

def saluto(nome):
    print("Ciao " +nome + "!")

print("inserisci nome: ")
nomeinput = input()
saluto(nomeinput)