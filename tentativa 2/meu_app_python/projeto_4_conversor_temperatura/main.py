# projeto_4_conversor_temperatura/main.py
import tkinter as tk

# Função para converter a temperatura
def converter():
    try:
        temperatura = float(entry.get())  # Pega o valor de entrada e converte para float
        unidade_origem = origem_var.get()
        unidade_destino = destino_var.get()

        if unidade_origem == unidade_destino:
            resultado = temperatura
        elif unidade_origem == "Celsius" and unidade_destino == "Fahrenheit":
            resultado = (temperatura * 9/5) + 32
        elif unidade_origem == "Celsius" and unidade_destino == "Kelvin":
            resultado = temperatura + 273.15
        elif unidade_origem == "Fahrenheit" and unidade_destino == "Celsius":
            resultado = (temperatura - 32) * 5/9
        elif unidade_origem == "Fahrenheit" and unidade_destino == "Kelvin":
            resultado = (temperatura - 32) * 5/9 + 273.15
        elif unidade_origem == "Kelvin" and unidade_destino == "Celsius":
            resultado = temperatura - 273.15
        elif unidade_origem == "Kelvin" and unidade_destino == "Fahrenheit":
            resultado = (temperatura - 273.15) * 9/5 + 32

        result_label.config(text=f"Resultado: {resultado:.2f} {unidade_destino}")
    except ValueError:
        result_label.config(text="Erro! Insira um número válido.")

# Criando a janela
root = tk.Tk()
root.title("Conversor de Temperatura")

# Campo de entrada para a temperatura
entry = tk.Entry(root, width=20, font=("Arial", 14))
entry.pack(pady=10)

# Variáveis para armazenar as unidades de origem e destino
origem_var = tk.StringVar(value="Celsius")
destino_var = tk.StringVar(value="Fahrenheit")

# Dropdown para escolher a unidade de origem
origem_menu = tk.OptionMenu(root, origem_var, "Celsius", "Fahrenheit", "Kelvin")
origem_menu.pack(pady=5)

# Dropdown para escolher a unidade de destino
destino_menu = tk.OptionMenu(root, destino_var, "Celsius", "Fahrenheit", "Kelvin")
destino_menu.pack(pady=5)

# Botão para converter
btn_converter = tk.Button(root, text="Converter", width=20, height=2, command=converter)
btn_converter.pack(pady=10)

# Label para exibir o resultado
result_label = tk.Label(root, text="Resultado: ", font=("Arial", 14))
result_label.pack(pady=10)

# Rodando a interface
root.mainloop()
