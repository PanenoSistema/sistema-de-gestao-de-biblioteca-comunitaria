import  os

# Declaração das Variáveis Globais
opcao = 0
usuários = []
livros = []
empréstimos = []

# Função para Limpar a Tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir logotipo
def show_tittle():
    print('Sistema de Gestão de Biblioteca Comunitária')
    print ('''
    ░█▀▄░▀█▀░█▀▄░█░░░▀█▀░█▀█░▀█▀░█▀▀░█▀▀░█▀█░░░░
    ░█▀▄░░█░░█▀▄░█░░░░█░░█░█░░█░░█▀▀░█░░░█▀█░░░░
    ░▀▀░░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀░▀░░░░
    ''')

# Função para exibir os menus
def show_menu(menu):
    global opcao
    clear_screen


    if(menu == 'principal'):
        print('1. Usuários')
        print('2. Livros')
        print('3. Empréstimos')
        print('0. Sair')

    if(menu == 'usuarios'):    
        print('Usuários')
        print('1. Novo usuário')
        print('2. Ver usuários')
        print('0. Voltar')

    if(menu == 'novo_usuario'):
        print('NOVO USUÁRIO')
    elif(menu == 'listar_usuarios'):
        print('VER USUÁRIOS')

    if(menu == 'livros'):
        print('1. Livros')
        print('2. Livros indisponíveis')
        print('0. Voltar')

    if(menu == 'livros'):
        print('VER LIVROS')

    if(menu == 'emprestimos'):    
        print('Empréstimos')
        print('1. Novo empréstimos')
        print('2. Devolução')
        print('0. Voltar')


while True:
    show_tittle()
    show_menu('principal')
    
    opcao = input('Escolha a opção desejada: ')
    
    if(opcao == '1'): # Opção  'Usuários' do menu principal
        show_menu('usuarios')
        opcao=input('Escolha uma opção: ')
        if opcao == 1: 
            #adicionar
            pass
        elif opcao == 2:
            #listar os usuários
            pass
        else:
            print('opção inválida')
    elif(opcao == '2'):
        print('Livros')
    elif(opcao == '3'):
        print('Empréstimos')
    elif(opcao == '0'):
        break
    else:
        print('Opção inválida! Digite uma opção do menu...')


