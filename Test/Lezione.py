import tkinter as tk

window = tk.Tk()
window.title("Finestra di prova")
window.geometry("600x600")
window.resizable(True, True)
window.configure(background="black")

# widget

# Stampa
etichetta=tk.Label(window, text="Etichetta di prova", fg="#FF0000", font=("Helvetica", 16))
etichetta.grid(row=0, column=0, sticky="W", padx=10, pady=10)

# Stampa con funzione
def stampa_etichetta():
    text = "Etichetta di prova da funzione"
    text_output = tk.Label(window, text=text, fg="#ff0000", font=("Helvetica", 16))
    text_output.grid(row=1, column=0, sticky="W", padx=10, pady=10)


# Bottone
first_button = tk.Button(text="Clicca!", command=stampa_etichetta) 
first_button.grid(row=0, column=1, sticky="W", padx=10, pady=10)

# Input
input_text = tk.Entry(window)
input_text.grid(row=2, column=0, sticky="W")



# Funzione per stampare un'etichetta con input
def stampa_etichetta_input():
    testo = input_text.get()
    text_output1 = tk.Label(window, text=testo, fg="#FF0000", font=("Helvetica", 16))
    text_output1.grid(row=5, column=0, sticky="W")

from threading import Thread

# Creazione del secondo bottone
second_button = tk.Button(window, text="Clicca!", command=stampa_etichetta_input)
second_button.grid(row=4, column=1, sticky="W", padx=10, pady=10)


if __name__=="__main__":
    window.mainloop()