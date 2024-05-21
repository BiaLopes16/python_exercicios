# Função para verificar a senha do correntista
def verificar_senha(senha_digitada, senha_correta, tentativas_restantes, nome):
    if senha_digitada == senha_correta:
        print(f"Olá, {nome}, Seja bem-vindo ao nosso banco.")
        return True, tentativas_restantes
    else:
        tentativas_restantes -= 1
        if tentativas_restantes > 0:
            print(f"Senha incorreta. Você ainda tem {tentativas_restantes} {'tentativa' if tentativas_restantes == 1 else 'tentativas'}.")
        else:
            print(f"Senha incorreta. {nome}, Sua conta foi bloqueada. Por favor, dirija-se a um de  nossos caixas.")
        return False, tentativas_restantes

def main():
    senha_correta = "123456"
    tentativas_restantes = 3

    # Solicita o nome do correntista
    nome = input("Digite seu nome: ")

    while tentativas_restantes > 0:
        senha_digitada = input("Digite sua senha: ")
        acesso, tentativas_restantes = verificar_senha(senha_digitada, senha_correta, tentativas_restantes, nome)
        if acesso:
            break

if __name__ == "__main__":
    main()