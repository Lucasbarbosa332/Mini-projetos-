# projeto_8_maior_menor_numero/main.py
import tkinter as tk

def calcular_maior_menor():
    try:
        numeros = list(map(int, entry.get().split(',')))
        maior = max(numeros)
        menor = min(numeros)
        result_label.config(text=f"Maior: {maior} | Menor: {menor}")
    except ValueError:
        result_label.config(text="Erro! Insira números válidos separados por vírgula.")

root = tk.Tk()
root.title("Maior e Menor Número")

entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.pack(pady=10)

btn_calcular = tk.Button(root, text="Calcular Maior e Menor", width=20, height=2, command=calcular_maior_menor)
btn_calcular.pack(pady=10)

result_label = tk.Label(root, text="Maior e Menor: ", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
