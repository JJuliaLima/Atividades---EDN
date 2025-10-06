# Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

# * Nota 1: 7.5
# * Nota 2: 8.0
# * Nota 3: 6.5
# O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
    
Nota1 = float(7.5)
Nota2 = float(8.0)
Nota3 = float(6.5)

soma = Nota1+Nota2+Nota3
media = soma / 3

print(f'{Nota1}')
print(f'{Nota2}')
print(f'{Nota3}')
print(f'a média final é igual a {media:.2f}')

if media:
    media <= 5.9
    print('O aluno está aprovado')
else: 
    print('O aluno está reprovado')
