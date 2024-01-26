peso = float(input("Qual o seu peso? "))
unidade = input("(K)g ou (L)bs: ")
if unidade == "K" or unidade == "k":
    conversão = peso / 0.45
    print(f"O peso em Lbs é: {peso}")
else:
    conversão = peso * 0.45
    print(f"O peso em Kg é: {peso}")