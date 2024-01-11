import tkinter as tk
from forex_python.converter import CurrencyRates

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Moedas")
        
        # Adquira sua chave gratuita de API em https://www.exchangerate-api.com/
        self.api_key = 'SUA_CHAVE_AQUI'
        self.currency_rates = CurrencyRates(api_key=self.api_key)

        # Variáveis
        self.from_currency = tk.StringVar()
        self.to_currency = tk.StringVar()
        self.amount = tk.DoubleVar()

        # Layout
        tk.Label(root, text="De Moeda:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(root, text="Para Moeda:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(root, text="Quantidade:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(root, text="Resultado:").grid(row=3, column=0, padx=10, pady=10)

        # Listas de Moedas
        currencies = self.currency_rates.get_currencies()
        currency_list = list(currencies.keys())
        
        # Dropdowns
        tk.OptionMenu(root, self.from_currency, *currency_list).grid(row=0, column=1, padx=10, pady=10)
        tk.OptionMenu(root, self.to_currency, *currency_list).grid(row=1, column=1, padx=10, pady=10)

        # Entradas
        tk.Entry(root, textvariable=self.amount).grid(row=2, column=1, padx=10, pady=10)
        tk.Entry(root, state='readonly', textvariable=tk.StringVar()).grid(row=3, column=1, padx=10, pady=10)

        # Botão de Conversão
        tk.Button(root, text="Converter", command=self.convert).grid(row=4, column=0, columnspan=2, pady=10)

    def convert(self):
        try:
            amount = float(self.amount.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()

            # Obter a taxa de câmbio
            rate = self.currency_rates.get_rate(from_curr, to_curr)

            # Calcular e exibir o resultado
            result = round(amount * rate, 2)
            result_str = f"{amount} {from_curr} = {result} {to_curr}"
            tk.StringVar().set(result_str)

        except Exception as e:
            tk.StringVar().set("Erro ao converter. Verifique suas entradas.")

if __name__ == "__main__":
    root = tk.Tk()
    converter = CurrencyConverter(root)
    root.mainloop()
