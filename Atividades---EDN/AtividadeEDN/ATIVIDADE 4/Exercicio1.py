# 1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).


print('Bem vindo a calculadora ;)')

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
operador = input("Digite a operação desejada (+, -, *, /): ")

def soma(numero1, numero2):
    return  numero1 + numero2

def subtracao(numero1, numero2):
    return  numero1 - numero2

def multiplicacao(numero1, numero2):
    return  numero1 * numero2

def divisao(numero1, numero2):
    if numero2 == 0:
        return "Erro: Divisão por zero"
    return  numero1 / numero2

if operador == '+':
    print(f"O resultado é: {soma(numero1, numero2)}") # Chama a função dentro do print
elif operador == '-':
    print(f'O resultado é: {subtracao(numero1, numero2)}')
elif operador == '*':
    print(f'O resultado é: {multiplicacao(numero1, numero2)}')
elif operador == '/':
    print(f'O resultado é: {divisao(numero1, numero2)}')
else:
    print('operador não é reconhecido')