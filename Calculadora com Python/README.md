# Documentação

## Código

```python
import tkinter as tk

def press(key):
    """
    Atualiza a entrada da calculadora quando um botão é pressionado.

    Parâmetros:
    - key (str): O valor do botão pressionado.
    """
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(key))

def calculate():
    """
    Avalia a expressão na entrada e exibe o resultado.

    Em caso de erro, exibe "Erro" na entrada.
    """
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")

def clear():
    """Limpa a entrada da calculadora."""
    entry.delete(0, tk.END)

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora")

# Adicionar uma entrada para a calculadora
entry = tk.Entry(root, width=20, font=('Arial', 14), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Adicionar os botões
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda key=button: press(key) if key != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Adicionar o botão de limpar
tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 14), command=clear).grid(row=row_val, column=col_val)

# Iniciar o loop da interface gráfica
root.mainloop()
```

Esses comentários fornecem uma explicação para as funções `press`, `calculate` e `clear`, bem como para as diferentes partes do código, como a criação da janela principal, a adição da entrada e dos botões. Isso deve ajudar a entender o propósito e o funcionamento de cada parte do código.