# Documentação

Esse código cria um conversor de moedas com uma interface gráfica usando Tkinter e a API gratuita de conversão de moedas `exchangerate-api.com`. Antes de executar o código, você precisará se inscrever no site `https://www.exchangerate-api.com/` para obter uma chave de API gratuita. Substitua `'SUA_CHAVE_AQUI'` pela chave que você receberá após o registro.

```python
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
```

Certifique-se de instalar a biblioteca forex-python usando o seguinte comando:

```bash
pip install forex-python
```

Substitua `'SUA_CHAVE_AQUI'` pela chave de API fornecida pelo `exchangerate-api.com`. Este código cria uma interface simples onde você pode selecionar a moeda de origem, a moeda de destino, inserir a quantidade e clicar no botão "Converter". O resultado da conversão será exibido na interface. Tenha em mente que a precisão das taxas de câmbio pode variar dependendo da fonte.

<hr>

### Para executar o código do conversor de moedas em Python, você precisará seguir alguns passos:

1. **Instalar Python:**
   Certifique-se de ter o Python instalado em seu sistema. Você pode baixar a versão mais recente do Python em [python.org](https://www.python.org/downloads/).

2. **Instalar Pacotes Necessários:**
   Abra um terminal (ou prompt de comando) e navegue até a pasta onde você salvou o código do conversor de moedas. Em seguida, execute o seguinte comando para instalar a biblioteca `forex-python`:

   ```bash
   pip install forex-python
   ```

3. **Substituir a Chave da API:**
   Vá para o código do conversor de moedas e substitua `'SUA_CHAVE_AQUI'` pela chave de API fornecida pelo `exchangerate-api.com`. Se você ainda não tem uma, pode se inscrever no site [ExchangeRate-API](https://www.exchangerate-api.com/) para obter uma chave gratuita.

4. **Executar o Código:**
   Depois de substituir a chave de API, salve o código em um arquivo com extensão `.py`, por exemplo, `conversor_moedas.py`. Em seguida, abra um terminal, navegue até o diretório onde o arquivo está localizado e execute o seguinte comando:

   ```bash
   python conversor_moedas.py
   ```

   Isso iniciará a aplicação do conversor de moedas com a interface gráfica. A interface aparecerá e você poderá começar a usar o conversor. Certifique-se de que sua conexão com a Internet esteja ativa, pois a aplicação faz chamadas à API para obter as taxas de câmbio em tempo real.