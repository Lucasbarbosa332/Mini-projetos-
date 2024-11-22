# projeto_9_tabuada/main.py
import tkinter as tk

def gerar_tabuada():
    try:
        numero = int(entry.get())
        tabuada = [f"{numero} x {i} = {numero * i}" for i in range(1, 11)]
        result_label.config(text="\n".join(tabuada))
    except ValueError:
        result_label.config(text="Erro! Insira um número válido.")

root = tk.Tk()
root.title("Tabuada")

entry = tk.Entry(root, width=20, font=("Arial", 14))
entry.pack(pady=10)

btn_calcular = tk.Button(root, text="Gerar Tabuada", width=20, height=2, command=gerar_tabuada)
btn_calcular.pack(pady=10)

result_label = tk.Label(root, text="Tabuada: ", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()

