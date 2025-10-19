#4 - Criar um código que serve para analisar números digitados pelo usuário, 
# classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

# 1. Inicia os contadores
pares = 0
impares = 0

while True:

    num = int(input("Digite um número (ou 0 para sair): "))

    if num == 0:
        break  # Encerra o laço

    # 5. Verifica se é par ou ímpar e atualiza o contador
    if num % 2 == 0:
        pares += 1  # Adiciona 1 à contagem de pares
    else:
        impares += 1  # Adiciona 1 à contagem de ímpares

print("\n--- Resultado ---")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")