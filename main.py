import  os

# Declaração das Variáveis Globais
opcao = '0'
usuarios = []
livros = []
emprestimos = []

# Função para Limpar a Tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pressione_enter():
    input (' Precione enter para continuar...')

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
    show_tittle()
    
    if(menu == 'principal'):
        print('1. Usuários')
        print('2. Livros')
        print('3. Empréstimos')
        print('0. Sair')
    elif(menu == 'usuarios'):    
        print('Usuários')
        print('1. Novo usuário')
        print('2. Ver usuários')
        print('0. Voltar')
    elif (menu == 'novo_usuario'):
        print('NOVO USUÁRIO')
    elif(menu == 'listar_usuarios'):
        print('VER USUÁRIOS')
    elif(menu == 'livros'):
        print('1. Livros')
        print('2. Cadastrar livros')
        print('0. Voltar')
    elif(menu == 'livros'):
        print('VER LIVROS')
    elif(menu == 'emprestimos'):    
        print('Empréstimos')
        print('1. Novo empréstimos')
        print('2. Devolução')
        print('0. Voltar')
    elif(menu == 'novo_emprestimo'):
        print ('NOVO EMPRÉSTIMO')
    elif(menu == 'devolucao'):
        print ('DEVOLUÇÃO')
    elif(menu == 'emprestimos'):
        if(opcao == '1'):
            menu= 'novo_emprestimo'
        elif(opcao == '2'):
            menu = 'devolucao'
        elif(opcao == '0'):
            menu = 'principal'
    opcao = input('Digite a poção desejada: ')

def cadastrar(tipo):
    if(tipo == 'usuarios'):
        codigo = len(usuarios) + 1
        nome = input('Digite o nome do usuário: ')
        email = input('Digite o e-mail do usuário: ')
        # Adicionar o usuário à matriz caso não exista
        usuarios.append([codigo, nome, email])
    elif(tipo == 'produtos'):
        codigo = len(produtos) + 1
        nome = input('Digite o nome do produto: ')
        quantidade = float(input('Digite a quantidade do produto: '))
        valor = float(input('Digite o valor do produto: '))
        # Adicionar o produto à matriz
        produtos.append([codigo, nome, quantidade, valor])
    elif(tipo == 'pedidos'):
        numero = len(pedidos) + 1
        usuario = int(input('Digite o código do usuário: '))
        produto = int(input('Digite o código do produto: '))
        quantidade = float(input('Digite a quantidade do pedido: '))
        # Adicionar o pedido à matriz
        empréstimos.append([usuários, livros, empréstimos])

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
    show_menu('principal')

    if(opcao == '1'): # Opção "Usuário" do menu principal
        show_menu('usuarios')
        if(opcao == '1'): # Opção "Novo Usuário" do menu "Usuário"
            show_menu('novo_usuario', False)
            cadastrar('usuarios') 
        elif(opcao == '2'): # Opção "Listar Usuários" do menu "Usuário"
            show_menu('listar_usuarios', False)
            listar('usuarios')
            pressione_enter()
        elif(opcao == '0'): # Opção "Voltar" do menu "Usuário"
            print('VOLTAR')
        else:
            print('Opção inválida...')
    elif(opcao == '2'): # Opção "Produto" do menu principal
        show_menu('produto')
        if(opcao == '1'): # Opção "Novo Produto" do menu "Produto"
            show_menu('novo_produto', False)
            cadastrar('produtos') 
        elif(opcao == '2'): # Opção "Listar Usuários" do menu "Produto"
            show_menu('listar_produtos', False)
            listar('produtos')
            pressione_enter()
        elif(opcao == '0'): # Opção "Voltar" do menu "Produto"
            print('VOLTAR')
        else:
            print('Opção inválida...')
    elif(opcao == '3'): # Opção "Pedido" do menu principal
        show_menu('pedido')
        if(opcao == '1'): # Opção "Novo Pedido" do menu "Pedido"
            show_menu('novo_pedido', False)
            cadastrar('pedidos') 
        elif(opcao == '2'): # Opção "Listar Pedidos" do menu "Pedido"
            show_menu('listar_pedidos', False)
            listar('pedidos')
            pressione_enter()
        elif(opcao == '0'): # Opção "Voltar" do menu "Pedido"
            print('VOLTAR')
        else:
            print('Opção inválida...')
    elif(opcao == '0'): # Opção "Sair" do menu principal
        break
    else:
        print('Opção inválida! Digite uma opção do menu...')

clear_screen()
print('O programa foi encerrado.')
 nova parte borgenssss
import  os

# Declaração das Variáveis Globais
opcao = '0'
usuarios = []
livros = []
emprestimos = []

# Função para Limpar a Tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pressione_enter():
    input (' Precione enter para continuar...')

# Função para exibir logotipo
def show_tittle():
    print('Sistema de Gestão de Biblioteca Comunitária')
    print ('''
    ░█▀▄░▀█▀░█▀▄░█░░░▀█▀░█▀█░▀█▀░█▀▀░█▀▀░█▀█░░░░
    ░█▀▄░░█░░█▀▄░█░░░░█░░█░█░░█░░█▀▀░█░░░█▀█░░░░
    ░▀▀░░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀░▀░░░░
    ''')

# Função para exibir os menus
def show_menu(menu, opcoes = True):
    global opcao
    clear_screen
    show_tittle()
    
    if(menu == 'principal'):
        print('1. Usuários')
        print('2. Livros')
        print('3. Empréstimos')
        print('0. Sair')
    elif(menu == 'usuarios'):
        print('Usuários')
        print('1. Novo usuário')
        print('2. Ver usuários')
        print('0. Voltar')
    elif (menu == 'novo_usuario'):
        print('NOVO USUÁRIO')
    elif(menu == 'listar_usuarios'):
        print('VER USUÁRIOS')
    elif(menu == 'livros'):
        print('1. gLivros')
        print('2. Cadastrar livros')
        print('0. Voltar')
    elif(menu == 'livros'):
        print('VER LIVROS')
    elif(menu == 'emprestimos'):
        print('Empréstimos')
        print('1. Novo empréstimos')
        print('2. Devolução')
        print('0. Voltar')
    elif(menu == 'novo_emprestimo'):
        print ('NOVO EMPRÉSTIMO')
    elif(menu == 'devolucao'):
        print ('DEVOLUÇÃO')
    elif(menu == 'emprestimos'):
        if(opcao == '1'):
            menu= 'novo_emprestimo'
        elif(opcao == '2'):
            menu = 'devolucao'
        elif(opcao == '0'):
            menu = 'principal'
    
    if opcoes:
        opcao = input('Digite a poção desejada: ')

def cadastrar(tipo):
    if(tipo == 'usuarios'):
        codigo = len(usuarios) + 1
        nome = input('Digite o nome do usuário: ')
        email = input('Digite o e-mail do usuário: ')
        # Adicionar o usuário à matriz caso não exista
        usuarios.append([codigo, nome, email])
    elif(tipo == 'livros'):
        codigo = len(livros) + 1
        nome = input('Digite o nome do produto: ')
        quantidade = float(input('Digite a quantidade de livros: '))
        valor = float(input('Digite o valor do livro: '))
        # Adicionar o produto à matriz
        livros.append([codigo, nome, quantidade, valor])
    elif(tipo == 'emprestimos'):
        numero = len(livros) + 1
        usuario = int(input('Digite o código do usuário: '))
        livro = int(input('Digite o código do livro: '))
        quantidade = float(input('Digite a quantidade do pedido: '))
        # Adicionar o pedido à matriz
        emprestimos.append([numero ,usuarios, livros, emprestimos])

def listar(tipo):
    if(tipo == 'usuarios'):
        for usuario in usuarios:
            print(f'código {usuario[0]} - {usuario[1]} - {usuario[2]}')
    elif(tipo == 'livro'):
        for livro in livros:
            print(f'código {livros[0]} - {livros[1]} - {livros[2]}')
    elif(tipo == 'emprestimos'):
        for emprestimo in emprestimos:
            print(f'emprestimos {emprestimos[0]} - usuário {usuario[emprestimos[1]-1][1]} - livros {livros [emprestimos[2]-1][1]} - qtd = {emprestimos[3]}')
    else:
        print('Não há valores a exibir...')
        pressione_enter()

while True:
    show_menu('principal')

    if(opcao == '1'): # Opção "Usuário" do menu principal
        show_menu('usuarios')
        if(opcao == '1'): # Opção "Novo Usuário" do menu "Usuário"
            show_menu('listar_usuarios', False)
            cadastrar('usuarios')
        elif(opcao == '2'): # Opção "Listar Usuários" do menu "Usuário"
            show_menu('listar_usuarios', False)
            listar('usuarios')
            pressione_enter()
        elif(opcao == '0'): # Opção "Voltar" do menu "Usuário"
            print('VOLTAR')
        else:
            print('Opção inválida...')
    elif(opcao == '2'): # Opção "Produto" do menu principal
        show_menu('produto')
        if(opcao == '1'): # Opção "Novo Produto" do menu "Produto"
            show_menu('novo_produto', False)
            cadastrar('produtos')
        elif(opcao == '2'): # Opção "Listar Usuários" do menu "Produto"
            show_menu('listar_produtos', False)
            listar('produtos')
            pressione_enter()
        elif(opcao == '0'): # Opção "Voltar" do menu "Produto"
            print('VOLTAR')
        else:
            print('Opção inválida...')
    elif(opcao == '3'): # Opção "Pedido" do menu principal
        show_menu('pedido')
        if(opcao == '1'): # Opção "Novo Pedido" do menu "Pedido"
            show_menu('novo_pedido', False)
            cadastrar('pedidos')
        elif(opcao == '2'): # Opção "Listar Pedidos" do menu "Pedido"
            show_menu('listar_pedidos', False)
            listar('pedidos')
            pressione_enter()
        elif(opcao == '0'): # Opção "Voltar" do menu "Pedido"
            print('VOLTAR')
        else:
            print('Opção inválida...')
    elif(opcao == '0'): # Opção "Sair" do menu principal
        break
    else:
        print('Opção inválida! Digite uma opção do menu...')

clear_screen()
print('O programa foi encerrado.')

