# Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# * Valor em reais: R$ 100.00
# * Taxa do dólar: R$ 5.20
# * Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

real = float(100)
dolar = float(5.20)
euro = float(6.15)

conversao_euro = real / euro
print(f"O valor de R${real:.2f} convertido para euro na cotação de {euro:.2f}, é igual a {conversao_euro:.2f}")

conversao_dolar = real / dolar
print(f"O valor de R${real:.2f} convertido para dolar na cotação de {dolar:.2f}, é igual a {conversao_dolar:.2f}")
