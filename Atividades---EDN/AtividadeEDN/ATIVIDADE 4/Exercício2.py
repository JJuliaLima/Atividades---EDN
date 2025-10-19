'''
2 - Criar um código que registre as notas de alunos e calcular a média da turma.
'''

notas = []

while True:
    entrada_usuario = input("Digite uma nota ou escreva 'PARE' para encerrar: ")
    if entrada_usuario.upper() == 'PARE':
        break 

    nota = float(entrada_usuario)
    notas.append(nota) # .append() é o método que adiciona um item ao final da lista.

print("Notas registradas:", notas)


def calculo_media (notas):
    qtd_notas = len(notas)
    soma = sum(notas) 
    media= soma / qtd_notas
    return media
        
media_da_turma = calculo_media(notas)

print(f"A média calculada da turma é: {media_da_turma}")