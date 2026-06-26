import os




# Declaração das Variáveis Globais
usuarios = []
livros = []
emprestimos = []
usuario_livro = []




# Função para Limpar a Tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')




def pressione_enter():
    # CORREÇÃO: Corrigido o erro de digitação em 'Pressione'
    input(' Pressione enter para continuar...')




# Função para exibir logotipo
def show_tittle():
    print('Sistema de Gestão de Biblioteca Comunitária')
    print ('''
    ░█▀▄░▀█▀░█▀▄░█░░░▀█▀░█▀█░▀█▀░█▀▀░█▀▀░█▀█░░░░
    ░█▀▄░░█░░█▀▄░█░░░░█░░█░█░░█░░█▀▀░█░░░█▀█░░░░
    ░▀▀░░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀░▀░░░░
    ''')




def mostrar_usuarios():
    # CORREÇÃO: Se a lista estiver vazia, avisa o usuário
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for c in range(0, len(usuarios)):
            print(f"({c+1}) {usuarios[c]}")




def mostrar_livros():
    # CORREÇÃO: Se a lista estiver vazia, avisa o usuário
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        for c in range(0, len(livros)):
            print(f"({c+1}) {livros[c]} - {usuario_livro[c]}")




def livros_():
    clear_screen()
    show_tittle()
    print("=== MENU DE LIVROS ===")
    print("""
  (1) Listar livros
  (2) Cadastrar livros
  (3) Voltar
    """)




    opcao_livros = input("Digite a opção: ")
    if opcao_livros == "1":
        clear_screen()
        print("=== LIVROS CADASTRADOS ===")# Add os parênteses () para executar a função
        mostrar_livros()
        pressione_enter()
    elif opcao_livros == "2":
        clear_screen()
        print("=== CADASTRAR LIVRO ===")
        add_livros = input("Digite o nome do livro: ")
        livros.append(add_livros)
        usuario_livro.append("Disponivel")
        print("Livro adicionado com sucesso! ")
        pressione_enter()
    elif opcao_livros == "3":
        pass
    else:
        print("Comando nao encontrado!")
        pressione_enter()
   
def usuarios_():
    clear_screen()
    show_tittle()
    print("""
  (1) Listar usuarios
  (2) Cadastrar usuarios
  (3) Voltar
    """)
    opcao_usuarios = input("Digite a opção: ")




    if opcao_usuarios == "1":
        clear_screen()
        print("=== USUÁRIOS CADASTRADOS ===")
        mostrar_usuarios()
        pressione_enter()
    elif opcao_usuarios == "2":
        clear_screen()
        print("=== CADASTRAR USUÁRIO ===")
        add_usuario = input("Digite o nome do usuario: ")
        usuarios.append(add_usuario)
        print("Usuario adicionado com sucesso!")
        pressione_enter()
    elif opcao_usuarios == "3":
        pass
    else:
        print("Comando nao encontrado!")
        pressione_enter()




def emprestimos_():
    clear_screen()
    # CORREÇÃO: Validação para impedir empréstimos sem dados no sistema
    if not usuarios or not livros:
        print("Erro: É necessário ter usuários e livros cadastrados para fazer um empréstimo.")
        pressione_enter()
        return




    mostrar_usuarios()
    esc_nome = int(input("Digite o numero do nome do usuario: "))
   
    mostrar_livros()
    esc_livro = int(input("Digite o numero do livro: "))




    if usuario_livro[esc_livro - 1] == "Disponivel":
      usuario_livro[esc_livro - 1] = usuarios[esc_nome - 1]
      print("Livro reservado com sucesso!")
    else:
      print("Esse livro já está emprestado para:", usuario_livro[esc_livro - 1])




    pressione_enter()
   
def escolha_():
    clear_screen()
    show_tittle() # Adicionado para exibir o título no menu principal
    print("""
(1) Usuarios
(2) Livros
(3) Emprestimos
(4) Sair
""")
    opcoes = input("Digite a opção: ")
    if opcoes == "1":
        clear_screen()
        print("=== MENU DE USUÁRIOS ===")
        usuarios_()
    elif opcoes == "2":
        clear_screen()
        livros_()
    elif opcoes == "3":
        clear_screen()
        print("=== MENU DE EMPRÉSTIMOS ===")
        emprestimos_()
    elif opcoes == "4":
        print("Saindo do sistema...")
        exit() # encerrar o loop infinito do While
    else:
        print("Comando nao encontrado!")
        pressione_enter()




# Execução do programa
while True:
    escolha_()









