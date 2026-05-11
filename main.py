while True:
    print('Sistema de Gestão de Biblioteca Comunitária')
    print ('''
    ░█▀▄░▀█▀░█▀▄░█░░░▀█▀░█▀█░▀█▀░█▀▀░█▀▀░█▀█░░░░
    ░█▀▄░░█░░█▀▄░█░░░░█░░█░█░░█░░█▀▀░█░░░█▀█░░░░
    ░▀▀░░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀░▀░░░░
    ''')
    print('1. Usuários')
    print('2. Livros')
    print('3. Empréstimos')
    print('4. Sair')

    opcao = input('Escolha a opção desejada: ')
    
    if(opcao == '1'):
        print('Usuários')
    elif(opcao == '2'):
        print('Livros')
    elif(opcao == '3'):
        print('Empréstimos')
    elif(opcao == '4'):
        break
    else:
        print('Opção inválida! Digite uma opção do menu...')

