import os


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    limpar()
    print("=== CALCULADORA DE MILHAS ===\n")
    tentativa = 0

    while True:
        tentativa += 1
        if tentativa > 3:
            limpar()
            print("Calculadora encerrada devido a quantidade de erros.")
            break

        try:
            valor_dinheiro = float(input("Insira o valor da passagem em R$: "))
            valor_milhas = float(input("Insira o valor da passagem em milhas: "))
            valor_embarque = float(input("Insira o valor de embarque: "))

            if valor_dinheiro <= 0:
                print("\nO valor em dinheiro deve ser maior que zero.")
                continue
            if valor_milhas <= 0:
                print("\nO valor em milhas deve ser maior que zero.")
                continue
            if valor_embarque < 0:
                print("\nA taxa de embarque não pode ser negativa.")
                continue
            if valor_dinheiro <= valor_embarque:
                print(
                    "\nO valor da passagem em dinheiro deve ser maior que a taxa de embarque."
                )
                continue

            calculo_completo = ((valor_dinheiro - valor_embarque) / valor_milhas) * 1000
            print(
                f"\nRealizando as contas, o valor estimado para cada milheiro é R${calculo_completo:.2f}"
            )

            if calculo_completo <= 20:
                print(
                    f"Por esse valor de R${calculo_completo:.2f} está valendo muito a pena usar as milhas!"
                )
            elif calculo_completo < 25:
                print(f"Por esse valor de R${calculo_completo:.2f} está aceitável.")
            elif calculo_completo < 30:
                print(
                    f"Por esse valor de R${calculo_completo:.2f} está bom, porém podia melhorar a situação. Recomendo usar o dinheiro."
                )
            else:
                print(
                    f"Por esse valor de R${calculo_completo:.2f}, opte por usar dinheiro!"
                )
            break

        except ValueError:
            limpar()
            print("=== CALCULADORA DE MILHAS ===\n")
            print("Digite apenas números válidos.\n")
            continue


if __name__ == "__main__":
    main()
