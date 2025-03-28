import random

def gerar_pergunta(operacao):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    if operacao == "adição":
        resposta = num1 + num2
        simbolo = "+"
    elif operacao == "subtração":
        resposta = num1 - num2
        simbolo = "-"
    elif operacao == "multiplicação":
        resposta = num1 * num2
        simbolo = "*"
    elif operacao == "divisão":
        num1 = num1 * num2  # Garantir que a divisão seja exata
        resposta = num1 / num2
        simbolo = "/"
    else:
        return None, None, None

    return num1, num2, resposta, simbolo


def main():
    print("Bem-vindo ao app de operações matemáticas!")
    print("Escolha uma operação para praticar:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    while True:
        escolha = input("Digite o número da operação que você quer praticar: ")

        if escolha == "1":
            operacao = "adição"
        elif escolha == "2":
            operacao = "subtração"
        elif escolha == "3":
            operacao = "multiplicação"
        elif escolha == "4":
            operacao = "divisão"
        elif escolha == "5":
            print("Obrigado por usar o app! Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue

        num1, num2, resposta, simbolo = gerar_pergunta(operacao)
        if num1 is None:
            print("Erro ao gerar pergunta.")
            continue

        print(f"Quanto é {num1} {simbolo} {num2}?")
        tentativa = float(input("Sua resposta: "))

        if tentativa == resposta:
            print("Correto! Muito bem!")
        else:
            print(f"Errado! A resposta correta é {resposta}.")

        print()  # Linha em branco para separar as perguntas


if __name__ == "__main__":
    main()
