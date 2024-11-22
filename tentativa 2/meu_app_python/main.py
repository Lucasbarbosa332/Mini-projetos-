import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import subprocess
import os

# Função para chamar o projeto
def abrir_projeto(projeto):
    try:
        # Caminho do diretório principal (onde o arquivo main.py da interface gráfica está)
        caminho_principal = os.path.dirname(os.path.abspath(__file__))
        
        # Caminho completo do script do projeto
        caminho_projeto = os.path.join(caminho_principal, projeto, "main.py")
        
        # Verificar se o arquivo existe
        if os.path.exists(caminho_projeto):
            # Usando subprocess para rodar o script do projeto
            subprocess.run(["python", caminho_projeto])
        else:
            messagebox.showerror("Erro", f"Projeto {projeto} não encontrado!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

# Função de animação de fundo (mudando a cor do fundo)
def animar_fundo():
    cores = ["#f4f4f4", "#e3e3e3", "#d1d1d1", "#f4f4f4"]
    cor_atual = cor_index[0]
    cor_index[0] = (cor_atual + 1) % len(cores)
    root.config(bg=cores[cor_atual])
    root.after(500, animar_fundo)

# Função de animação no título da janela (fazendo piscar)
def animar_titulo():
    if root.title() == "Aplicativo Python - Projetos Básicos":
        root.title("Projetos Python - Explore Agora!")
    else:
        root.title("Aplicativo Python - Projetos Básicos")
    root.after(500, animar_titulo)

# Função para estilizar os botões com efeitos de hover e borda arredondada
def estilo_botao(btn):
    btn.config(
        font=("Arial", 12, "bold"),
        bg="#4CAF50",  # Cor de fundo do botão
        fg="white",  # Cor do texto
        relief="flat",  # Sem bordas
        height=2,
        width=25,
        bd=0,
        activebackground="#45a049",  # Cor de fundo quando o botão é pressionado
        activeforeground="white",  # Cor do texto quando o botão é pressionado
        pady=5,
        padx=10
    )

    def on_enter(event):
        btn.config(bg="#45a049")  # Cor ao passar o mouse sobre o botão
    
    def on_leave(event):
        btn.config(bg="#4CAF50")  # Cor normal

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Criando a janela principal
root = tk.Tk()
root.title("Aplicativo Python - Projetos Básicos")
root.geometry("450x650")  # Tamanho da janela ajustado para mais botões

# Estilizando a janela
root.config(bg="#f4f4f4")
root.resizable(False, False)

# Lista de botões
projetos = [
    ("Projeto 1: Hello World", "projeto_1_hello_world"),
    ("Projeto 2: Calculadora", "projeto_2_calculadora"),
    ("Projeto 3: Lista de Tarefas", "projeto_3_lista_tarefas"),
    ("Projeto 4: Conversor de Temperatura", "projeto_4_conversor_temperatura"),
    ("Projeto 5: Fibonacci", "projeto_5_fibonacci"),
    ("Projeto 6: Par ou Ímpar", "projeto_6_par_impar"),
    ("Projeto 7: Contador de Caracteres", "projeto_7_contador_caracteres"),
    ("Projeto 8: Maior e Menor Número", "projeto_8_maior_menor_numero"),
    ("Projeto 9: Tabuada", "projeto_9_tabuada"),
    ("Projeto 10: Invertendo String", "projeto_10_invertendo_string")
]

# Adicionando os botões
for nome, projeto in projetos:
    btn = tk.Button(root, text=nome, command=lambda p=projeto: abrir_projeto(p))
    estilo_botao(btn)
    btn.pack(pady=10)

# Adicionando um título estilizado no topo da janela
titulo_label = tk.Label(root, text="Aplicativo Python - Projetos Básicos", font=("Arial", 16, "bold"), bg="#f4f4f4", fg="#333")
titulo_label.pack(pady=20)

# Rodando a animação de fundo e título
cor_index = [0]  # Índice para as cores de fundo
animar_fundo()
animar_titulo()

# Rodando a interface gráfica
root.mainloop()
