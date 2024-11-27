lista_libri = ["libro1", "libro3", "libro5"]
libri_prestito = ["libro2", "libro4"]


print("1 - Aggiunta libro")
print("2 - Prestito libro")
print("3 - Riporta libro")
print("4 - Disponibilità libro")
print("5 - Libri disponibili nella libreria")
print("6 - libri dati in prestito")
print("7 - Esci dal programma")

funzione = 0

while funzione <= 6:
    funzione = int(input("Inserisci il numero della funzione desiderata: "))
    if funzione == 1: # Aggiunta libro
        lista_libri.insert(0, input("Inserisci il titolo del nuovo libro: "))
        print(lista_libri)

    elif funzione == 2: # Prestito libro
        print(lista_libri)
        prestito = input("inserisci il libro da prendere in prestito: ")
        lista_libri.remove(prestito)
        libri_prestito.insert(0, prestito)
        print(lista_libri)
        print(libri_prestito)

    elif funzione == 3: # Riporta libro
        print(libri_prestito)
        libro_aggiunta = input("Inserisci il libro riportato: ")
        libri_prestito.remove(libro_aggiunta)
        lista_libri.insert(0, libro_aggiunta)
        print(lista_libri)
        print(libri_prestito)
    elif funzione == 4: # Disponibilita libro
        print(lista_libri)

    elif funzione == 5: # Libri disponibili nella libreria
        lista_libreria = lista_libri + libri_prestito
        print(lista_libreria)

    elif funzione == 6: # Libri dati in prestito
        print(libri_prestito)

    else: # Fine programma
        print("Hai chiuso il programma")
        break
