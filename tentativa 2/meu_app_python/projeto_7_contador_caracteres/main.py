# projeto_7_contador_caracteres/main.py
import tkinter as tk

def contar_caracteres():
    texto = entry.get()
    count = len(texto)
    result_label.config(text=f"Caracteres: {count}")

root = tk.Tk()
root.title("Contador de Caracteres")

entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.pack(pady=10)

btn_contar = tk.Button(root, text="Contar Caracteres", width=20, height=2, command=contar_caracteres)
btn_contar.pack(pady=10)

result_label = tk.Label(root, text="Caracteres: 0", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
