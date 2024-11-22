# projeto_10_invertendo_string/main.py
import tkinter as tk

def inverter_string():
    texto = entry.get()
    resultado = texto[::-1]
    result_label.config(text=f"String Invertida: {resultado}")

root = tk.Tk()
root.title("Inverter String")

entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.pack(pady=10)

btn_inverter = tk.Button(root, text="Inverter String", width=20, height=2, command=inverter_string)
btn_inverter.pack(pady=10)

result_label = tk.Label(root, text="String Invertida: ", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
