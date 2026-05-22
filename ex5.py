idade = int(input("Sua idade: "))
if idade >= 18:
    print("Maior de idade.")
    print("Acesso liberado!")
    else:
        print("Menor de idade.")
        faltam = 18 - idade
        print(f"Faltam {faltam} ano(s).")