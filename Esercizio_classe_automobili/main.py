from ClasseAuto import Auto
a = Auto("Nissan", "GTR R5", "2005")


while True:
    print("1 - Descrizione del veicolo")
    print("2 - Aumenta la velocita")
    print("3 - Diminuisci la velocita")
    print("4 - Fine Programma")
    scelta = int(input("Seleziona cosa vuoi fare:"))

    if scelta == 1:
        a.Descrizione()

    elif scelta == 2:
        velocita = int(input("inserisci la velocita da aumentare: "))
        a.AumentoVelocita(velocita)

    # elif scelta == 3:



    # elif scelta == 4:
    #     print("Il veicolo si è fermato in sicurezza e si è chiuso il programma!")
    #     break