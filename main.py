import perfil


def trocar_senha(usuario):
    nova_senha = input("Digite sua nova senha: ")
    confirmar_senha = input("Confirme sua nova senha: ")

    while nova_senha != confirmar_senha:
        print("As senhas não correspondem. Tente novamente.")
        nova_senha = input("Digite sua nova senha: ")
        confirmar_senha = input("Confirme sua nova senha: ")

    # Atualizando o arquivo de usuários
    with open("usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("usuarios.txt", "w") as arquivo:
        for linha in linhas:
            dados = linha.strip().split(',')
            if dados[0] == usuario:
                dados[1] = nova_senha  # Atualiza a senha
                arquivo.write(','.join(dados) + '\n')
            else:
                arquivo.write(linha)

    print("Senha alterada com sucesso!\n")


def realizar_login():
    tentativas = 3
    while tentativas > 0:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
                if dados[0] == usuario and dados[1] == senha:
                    print(f"Login bem-sucedido! Bem-vindo, {dados[3]}")
                    return True

        tentativas -= 1
        print(f"Credenciais incorretas. Tentativas restantes: {tentativas}")

    # Se o usuário errar três vezes, oferece a opção de troca de senha
    esqueci = input("Você esqueceu sua senha? (s/n): ").lower()
    if esqueci == 's':
        deseja_trocar = input("Você deseja trocar a senha? (s/n): ").lower()
        if deseja_trocar == 's':
            trocar_senha(usuario)
        else:
            return False  # Volta ao menu principal


def menu():
    while True:
        print("Menu de Login:")
        print("1. Login")
        print("2. Cadastro")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            if realizar_login():
                break
        elif opcao == '2':
            perfil.cadastrar_usuario()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu()
