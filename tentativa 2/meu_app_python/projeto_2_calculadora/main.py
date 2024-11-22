# projeto_2_calculadora/main.py
import tkinter as tk

# Função que realiza as operações matemáticas
def calcular():
    try:
        result = eval(entry.get())  # eval para calcular a expressão matemática
        result_label.config(text="Resultado: " + str(result))
    except Exception as e:
        result_label.config(text="Erro na expressão!")

# Criando a janela
root = tk.Tk()
root.title("Calculadora Simples")

# Caixa de entrada para o usuário digitar a expressão
entry = tk.Entry(root, width=20, font=("Arial", 14))
entry.pack(pady=10)

# Botão de cálculo
btn_calcular = tk.Button(root, text="Calcular", width=20, height=2, command=calcular)
btn_calcular.pack(pady=10)

# Label para mostrar o resultado
result_label = tk.Label(root, text="Resultado: ", font=("Arial", 14))
result_label.pack(pady=10)

# Rodando a interface
root.mainloop()
