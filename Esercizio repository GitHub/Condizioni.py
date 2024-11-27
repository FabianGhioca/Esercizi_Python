# Esercizio repository GitHub CONDIZIONI

numero1 = input("inserisci in primo numero: ")
numero2 = input("inserisci in secondo numero: ")
numero3 = input("inserisci in terzo numero: ")
if numero1 == numero2 == numero3:
    print("Tutti i numeri inseriti sono uguali e il valore è: " + numero1)
elif numero1 == numero2:
    print("Numero 1 e uguale a numero 2 e il valore è: " + numero1)
elif numero1 == numero3:
    print("Numero 1 e uguale a numero 3 e il valore è: " + numero1)
elif numero2 == numero3:
    print("Numero 2 e uguale a numero 3 e il valore è: " + numero2)
else:
    print("non ci sono valori inseriti uguali")