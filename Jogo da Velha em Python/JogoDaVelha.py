import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.turno = 'X'
        self.tabuleiro = [' '] * 9

        # Botão para iniciar um novo jogo
        tk.Button(root, text="Novo Jogo", command=self.novo_jogo).grid(row=0, column=0, columnspan=3, pady=10)

        # Botões para as células do tabuleiro
        self.botoes = []
        for i in range(3):
            for j in range(3):
                btn = tk.Button(root, text='', width=10, height=3, command=lambda row=i, col=j: self.celula_clique(row, col))
                btn.grid(row=i+1, column=j, padx=5, pady=5)
                self.botoes.append(btn)

        # Botão para sair do jogo
        tk.Button(root, text="Sair", command=self.root.destroy).grid(row=4, column=0, columnspan=3, pady=10)

    def novo_jogo(self):
        self.turno = 'X'
        self.tabuleiro = [' '] * 9
        for btn in self.botoes:
            btn.config(text='')
        messagebox.showinfo("Novo Jogo", "Novo jogo iniciado!")

    def celula_clique(self, row, col):
        index = 3 * row + col
        if self.tabuleiro[index] == ' ':
            self.tabuleiro[index] = self.turno
            self.botoes[index].config(text=self.turno)
            
            if self.verificar_vitoria():
                messagebox.showinfo("Vitória", f"O jogador {self.turno} venceu!")
                self.novo_jogo()
            elif ' ' not in self.tabuleiro:
                messagebox.showinfo("Empate", "O jogo terminou em empate!")
                self.novo_jogo()
            else:
                self.turno = 'O' if self.turno == 'X' else 'X'

    def verificar_vitoria(self):
        # Verifica as linhas, colunas e diagonais para determinar se houve vitória
        for i in range(3):
            if self.tabuleiro[i] == self.tabuleiro[i + 3] == self.tabuleiro[i + 6] != ' ':
                return True
            if self.tabuleiro[3 * i] == self.tabuleiro[3 * i + 1] == self.tabuleiro[3 * i + 2] != ' ':
                return True
        if self.tabuleiro[0] == self.tabuleiro[4] == self.tabuleiro[8] != ' ':
            return True
        if self.tabuleiro[2] == self.tabuleiro[4] == self.tabuleiro[6] != ' ':
            return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    jogo_da_velha = JogoDaVelha(root)
    root.mainloop()
