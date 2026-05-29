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
def show_tittle()

# Função para exibir os menus
def show_menu(menu):
    clear_screen
    if(menu == 'usuários')
    clear_screen()
        print('Usuários')
        print('1. Novo usuário')
        print('2. Ver usuários')
        print('3. Voltar')
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
    
    if(opcao == '1'): # Opção  'Usuários' do menu principal
        show_menu(menu)
        opcao=input('Escolha uma opção: ')
        if opcao == 1: 
            #cadastra um novo usuário
            pass
        elif opcao==2:
            #listar os usuários
            pass
        else:
            print('opção inválida')
    elif(opcao == '2'):
        print('Livros')
    elif(opcao == '3'):
        print('Empréstimos')
    elif(opcao == '4'):
        break
    else:
        print('Opção inválida! Digite uma opção do menu...')

