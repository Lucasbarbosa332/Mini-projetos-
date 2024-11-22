# projeto_5_fibonacci/main.py
import tkinter as tk

def fibonacci():
    try:
        n = int(entry.get())
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        result_label.config(text="Sequência: " + ", ".join(map(str, fib[:n])))
    except ValueError:
        result_label.config(text="Erro! Insira um número válido.")

root = tk.Tk()
root.title("Sequência de Fibonacci")

entry = tk.Entry(root, width=20, font=("Arial", 14))
entry.pack(pady=10)

btn_calcular = tk.Button(root, text="Calcular Fibonacci", width=20, height=2, command=fibonacci)
btn_calcular.pack(pady=10)

result_label = tk.Label(root, text="Sequência: ", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()

