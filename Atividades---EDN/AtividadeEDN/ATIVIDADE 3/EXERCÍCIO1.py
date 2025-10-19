'''1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais).
'''

idade_usuario = int(input('Digite sua idade: '))

if idade_usuario <= 13:
    print('Você é uma criança')
elif idade_usuario <= 17:
    print('Você é adolescente')
elif idade_usuario <= 59:
    print('Você é adulto')
else:
    print('Você é idoso')
