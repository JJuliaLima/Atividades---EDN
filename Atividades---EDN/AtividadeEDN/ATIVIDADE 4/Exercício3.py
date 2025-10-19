'''3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.'''


while True:
    senha = input('Digite sua senha: ')

    comprimento_minimo = len(senha) >= 8

    contem_numero = any(c.isdigit() for c in senha)

    if len(senha) >= 8 and contem_numero == True :
        print('Critério de comprimento atendido!')
        break
    else:
        print('Senha inválida. Verifique os critérios:')
        if not comprimento_minimo:
            print(f'Sua senha tem apenas {len(senha)} caracteres. Precisa ter no mínimo 8. Tente novamente: ')
        if not contem_numero:
            print('Sua senha não contém nenhum número. Tente novamente: ')