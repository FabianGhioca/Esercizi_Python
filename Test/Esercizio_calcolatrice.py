import tkinter as tk

# Creazione della finestra
window = tk.Tk()
window.title("Calcolatrice")
window.geometry("600x600")
window.resizable(False, False)
window.configure(background="black")

# Input primo valore
input_text = tk.Entry(window)
input_text.grid(row=0, column=0, sticky="W")

# Input secondo valore 
input_text2 = tk.Entry(window)
input_text2.grid(row=2, column=0, sticky="W")

# Operazione della moltiplicazione
def Operazione_Moltiplicazione():
    int_input_text = int(input_text.get())
    int_input_text2 = int(input_text2.get())
    risultato = int_input_text * int_input_text2
    output_risultato = tk.Label(window, text=risultato, fg="#ff0000", font=("Helvetica", 16))
    output_risultato.grid(row=4, column=0, sticky="W", padx=10, pady=10)

# Operazione della divisione
def Operazione_Divisione():
    int_input_text = int(input_text.get())
    int_input_text2 = int(input_text2.get())
    if int_input_text >= int_input_text2:
        risultato = int_input_text / int_input_text2
        output_risultato = tk.Label(window, text=risultato, fg="#ff0000", font=("Helvetica", 16))
        output_risultato.grid(row=4, column=0, sticky="W", padx=10, pady=10)
    else:
        testo = "I valori emmessi non sono validi"
        output_errore = tk.Label(window, text=testo, fg="#ff0000", font=("Helvetica", 16))
        output_errore.grid(row=4, column=0, sticky="W", padx=10, pady=10)

moltiplicazione = tk.Button(text="*", command = Operazione_Moltiplicazione)
moltiplicazione.grid(row=1, column=0, sticky="W", padx=10, pady=10)

divisione = tk.Button(text="/", command = Operazione_Divisione)
divisione.grid(row=1, column=1, sticky="W", padx=10, pady=10)





if __name__=="__main__":
    window.mainloop()