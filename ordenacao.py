def quick_sort (valores):
    if len(valores) <= 1:
        return valores
    pivo = valores[len(valores) // 2]

    menores = []
    iguais = []
    maiores = []

    for valor in valores:
        if valor < pivo:
            menores.append(valor)
        if valor == pivo:
            iguais.append(valor)
        if valor > pivo:
            maiores.append(valor)

    return quick_sort(menores) + iguais + quick_sort(maiores)

print(quick_sort([7, 3, 9, 1, 5]))