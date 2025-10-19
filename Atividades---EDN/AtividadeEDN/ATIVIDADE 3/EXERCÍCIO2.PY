'''2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso" '''


peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura*altura)

if imc <= 18.5:
    print(f'seu é imc é igual a {imc:.2f}. Você está abaixo do peso')
elif imc <= 25:
    print(f'O imc é igual a {imc:.2f}. Seu peso é normal')
elif imc <= 30:
    print(f'seu é imc é igual a {imc:.2f}. Você está sobrepeso')
else:
    print(f'seu é imc é igual a {imc:.2f}. Você está Obeso')
