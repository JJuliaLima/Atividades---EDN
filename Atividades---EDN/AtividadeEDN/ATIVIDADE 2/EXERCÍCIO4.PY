# 4- Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

# * Distância percorrida: 300 km
# * Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

D_percorrida = 300
Combustivel_gasto = 25

consumo_medio = D_percorrida / Combustivel_gasto

print(f'Tendo percorrido cerca de {D_percorrida}km, e com gasto de {Combustivel_gasto}L de combstível. O consumo médio é igual {consumo_medio:.2f} km\L')