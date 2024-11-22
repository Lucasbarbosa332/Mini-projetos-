# projeto_6_par_impar/main.py
import tkinter as tk

def verificar_par_impar():
    try:
        numero = int(entry.get())
        if numero % 2 == 0:
            result_label.config(text=f"O número {numero} é PAR.")
        else:
            result_label.config(text=f"O número {numero} é ÍMPAR.")
    except ValueError:
        result_label.config(text="Erro! Insira um número válido.")

root = tk.Tk()
root.title("Verificador de Par/Ímpar")

entry = tk.Entry(root, width=20, font=("Arial", 14))
entry.pack(pady=10)

btn_verificar = tk.Button(root, text="Verificar", width=20, height=2, command=verificar_par_impar)
btn_verificar.pack(pady=10)

result_label = tk.Label(root, text="Resultado: ", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
