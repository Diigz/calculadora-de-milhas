import os


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


limpar()
print("=== CALCULADORA DE MILHAS ===\n")

while True:
    try:
        valor_em_dinheiro = float(input("Me diga o valor da passagem: "))
        valor_em_milhas = float(input("Muito bem, agora me diga o valor em milhas: "))

        if valor_em_milhas <= 0:
            limpar()
            print("O valor em milhas deve ser maior que zero!")
            continue

        taxa_de_embarque = float(
            input("Por fim, me diga a taxa de embarque com as milhas: ")
        )
        break
    except ValueError:
        limpar()
        print("Responda corretamente!")

calculo = valor_em_dinheiro - taxa_de_embarque
calculo = (calculo / valor_em_milhas) * 1000

print(f"\nRealizando o cálculo, o valor de cada milha está R${calculo:.2f}")

if calculo <= 20:
    print(
        f"Por esse valor de R${calculo:.2f} está valendo muito a pena usar as milhas!"
    )
elif calculo > 20 and calculo < 25:
    print(f"Por esse valor de R${calculo:.2f} está aceitável.")
elif calculo >= 25 and calculo < 30:
    print(
        f"Por esse valor de R${calculo:.2f} está bom, porém podia melhorar a situação. Recomendo usar o dinheiro."
    )
else:
    print(f"Por esse valor de R${calculo:.2f}, opte por usar dinheiro!")
