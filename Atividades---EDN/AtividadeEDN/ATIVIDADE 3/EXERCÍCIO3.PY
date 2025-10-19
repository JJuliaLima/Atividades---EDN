'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual ''' 


valor = float(input("Digite a temperatura: "))
origem = input("Qual a unidade de origem (C, F, K)? ").upper()
destino = input("Para qual unidade deseja converter (C, F, K)? ").upper()


# Converter a temperatura de origem Celsius
temp_em_celsius = 0 #declarando variável com valor padrão

if origem == 'C':
    temp_em_celsius = valor
elif origem == 'F':
    # Fórmula: (F - 32) * 5/9
    temp_em_celsius = (valor - 32) * 5 / 9
elif origem == 'K':
    # Fórmula: K - 273.15
    temp_em_celsius = valor - 273.15


resultado = 0

if destino == 'C':
    resultado = temp_em_celsius
elif destino == 'F':
    # Fórmula: (C * 9/5) + 32
    resultado = (temp_em_celsius * 9 / 5) + 32
elif destino == 'K':
    # Fórmula: C + 273.1550
    resultado = temp_em_celsius + 273.15


print(f"\nResultado: {valor}°{origem} é igual a {resultado:.2f}°{destino}")