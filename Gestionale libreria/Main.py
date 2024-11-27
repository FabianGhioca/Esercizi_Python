lista_libri = ["libro1", "libro3", "libro5"]
libri_prestito = ["libro2", "libro4"]




funzione = 0

while funzione <= 6:
    print("1 - Aggiunta libro")
    print("2 - Prestito libro")
    print("3 - Riporta libro")
    print("4 - Disponibilità libro")
    print("5 - Libri disponibili nella libreria")
    print("6 - libri dati in prestito")
    print("7 - Esci dal programma")
    funzione = int(input("Inserisci il numero della funzione desiderata: "))

    if funzione == 1: # Aggiunta libro
        libro_aggiunta = input("Inserisci il titolo del nuovo libro: ")
        lista_libri.insert(0, libro_aggiunta)
        print("Hai aggiunto questo libro: " +libro_aggiunta)
        print("Ecco la lista aggiornata:")
        for item in lista_libri:
            print(item)

    elif funzione == 2: # Prestito libro
        for item in lista_libri:
            print(item)
        prestito = input("inserisci il libro da prendere in prestito: ")
        lista_libri.remove(prestito)
        libri_prestito.insert(0, prestito)
        print("Hai preso in prestito questo libro: " +prestito)

    elif funzione == 3: # Riporta libro
        print("Quali di questi libri devi riportare?")
        print(libri_prestito)
        libro_riportato = input("Inserisci il libro riportato: ")
        libri_prestito.remove(libro_riportato)
        lista_libri.insert(0, libro_riportato)
        print("Hai riporato questo libro: " +libro_riportato)

    elif funzione == 4: # Disponibilita libro
        for item in lista_libri:
            print(item)

    elif funzione == 5: # Libri disponibili nella libreria
        lista_libreria = lista_libri + libri_prestito
        for item in lista_libreria:
            print(item)

    elif funzione == 6: # Libri dati in prestito
        for item in libri_prestito:
            print(item)

    else: # Fine programma
        print("Hai chiuso il programma")
        break