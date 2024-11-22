# projeto_3_lista_tarefas/main.py
import tkinter as tk

# Funções para manipular a lista de tarefas
def adicionar_tarefa():
    tarefa = entry.get()
    if tarefa != "":
        listbox.insert(tk.END, tarefa)  # Adiciona a tarefa à lista
        entry.delete(0, tk.END)  # Limpa o campo de entrada

def remover_tarefa():
    try:
        tarefa_selecionada = listbox.curselection()  # Pega a tarefa selecionada
        listbox.delete(tarefa_selecionada)  # Remove a tarefa da lista
    except IndexError:
        pass

# Criando a janela
root = tk.Tk()
root.title("Lista de Tarefas")

# Campo de entrada para adicionar tarefas
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

# Botão para adicionar tarefas
btn_adicionar = tk.Button(root, text="Adicionar Tarefa", width=20, height=2, command=adicionar_tarefa)
btn_adicionar.pack(pady=5)

# Lista para exibir as tarefas
listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 14))
listbox.pack(pady=10)

# Botão para remover tarefas
btn_remover = tk.Button(root, text="Remover Tarefa", width=20, height=2, command=remover_tarefa)
btn_remover.pack(pady=5)

# Rodando a interface
root.mainloop()
