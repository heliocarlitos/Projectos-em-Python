# Documentação

## Introdução

Este é um pequeno script em Python que utiliza o módulo `calendar` para exibir o calendário de um mês específico. O ano e o mês são definidos como variáveis no início do script, e em seguida, o calendário é impresso na saída padrão.

## Código Fonte

```python
import calendar

# Define o ano e o mês
yy = 2024  # ANO
mm = 12    # MÊS

# Mostra o calendário
print(calendar.month(yy, mm))
```

## Uso

O script imprime o calendário do mês especificado para o ano fornecido. Para personalizar a saída, você pode alterar os valores das variáveis `yy` e `mm` de acordo com suas necessidades.

## Funcionamento

1. **Importação do Módulo `calendar`**: O código começa importando o módulo `calendar`, que fornece funções relacionadas ao calendário.

   ```python
   import calendar
   ```

2. **Definição do Ano e do Mês**: As variáveis `yy` e `mm` são utilizadas para armazenar o ano e o mês para os quais o calendário será exibido.

   ```python
   yy = 2024  # ANO
   mm = 12    # MÊS
   ```

   Você pode modificar essas variáveis para exibir o calendário de um ano ou mês diferente.

3. **Exibição do Calendário**: A função `calendar.month(ano, mês)` é chamada para gerar o calendário do mês especificado. A saída é então impressa na tela usando `print()`.

   ```python
   print(calendar.month(yy, mm))
   ```

## Exemplo de Saída

A saída do script será o calendário do mês especificado, formatado de acordo com as convenções do módulo `calendar`. Por exemplo, ao executar o script com `yy = 2024` e `mm = 12`, a saída pode ser:

```
   December 2024
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
```

## Conclusão

Este script Python simples é útil para exibir o calendário de um mês específico, e você pode personalizar facilmente o ano e o mês para atender às suas necessidades.

<hr>

<span align='center'>
   
   [Licença](https://hcadeveloper.github.io/Licenca-MIT/)
   
</span>
