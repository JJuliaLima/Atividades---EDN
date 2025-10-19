# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes

produto = 'Camiseta'
preco = float(50.00)
desconto = preco * (20 / 100) 

preco_final = preco - desconto
print(f'Considerando o desconto de 20% da {produto} o valor final é de R${preco_final:.2f}')
