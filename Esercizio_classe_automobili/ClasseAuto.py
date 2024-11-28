class Auto:
    def __init__(self, marca, modello, anno, velocita = 0):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.velocita = velocita

    def Descrizione(self):
        print(f"La marca del veicolo è {self.marca}")
        print(f"Il modello del veicolo è {self.modello}")
        print(f"L' anno del veicolo è {self.anno}")

    def AumentoVelocita(self, velocita):
        self.velocita += velocita
        print(f"La velocita attuale è di {self.velocita}km/h")