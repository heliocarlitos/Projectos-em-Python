import tkinter as tk
from tkinter import messagebox

class MinhaInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Minha Interface")

        # Criar e posicionar widgets
        self.criar_widgets()

    def criar_widgets(self):
        # Rótulo de boas-vindas
        tk.Label(self.root, text="Bem-vindo à Minha Interface", font=("Arial", 16)).pack(pady=10)

        # Botão com evento associado
        tk.Button(self.root, text="Clique-me", command=self.exemplo_funcao).pack(pady=10)

        # Entrada de texto
        self.entrada_texto = tk.Entry(self.root)
        self.entrada_texto.pack(pady=10)

    def exemplo_funcao(self):
        texto_entrada = self.entrada_texto.get()
        messagebox.showinfo("Mensagem", f"Você digitou: {texto_entrada}")

if __name__ == "__main__":
    root = tk.Tk()
    minha_interface = MinhaInterface(root)
    root.mainloop()
