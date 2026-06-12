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

def cadastrar(tipo):
        empréstimos.append([numero, usuários, livros, quantidade])

def listar(tipo):
    if(tipo == 'usuarios'):
        for usuario in usuario:
            print(f'código {usuario[0]} - {usuario[1]} - {usuario[2]}')
    elif(tipo == 'livro'):
        for livros in livros:
            print(f'código {livros[0]} - {livros[1]} - {livros[2]}')
    elif(tipo == 'emprestimos'):
        for emprestimos in emprestimos:
            print(f'emprestimos {emprestimos[0]} - usuário {usuario[emprestimos[1]-1][1]} - livros {livros [emprestimos[2]-1][1]} - qtd = {emprestimos[3]}')
    else:
        print('Não há valores a exibir...')
        pressione_enter()

while True:
    show_tittle()
    show_menu('principal')
    
    opcao = input('Escolha a opção desejada: ')
    
    if(opcao == '1'): # Opção  'Usuários' do menu principal
        show_menu('novo_usuarios', False)
        cadastrar('usuarios')
        pressione_enter()
        opcao=input('Escolha uma opção: ')
        if opcao == 1: 
            #adicionar
            pass
        elif opcao == 2:
            #listar os usuários
            pass
        else:
            print('opção inválida')
    elif(opcao == '2'):: # Opção "Livros" do menu principal
    show_menu('livro')
        print('Livros')
    elif(opcao == '3'):
        print('Empréstimos')
    elif(opcao == '0'):
        break
    else:
        print('Opção inválida! Digite uma opção do menu...')

clear_screen()

