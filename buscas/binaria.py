def busca_binaria(jogos, id_procurado):

    comparacoes = 0  # Contador de comparações
    inicio = 0
    fim = len(jogos) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        comparacoes += 1  # Incrementa o contador a cada comparação

        if jogos[meio].id == id_procurado:
            return {
                "jogo": jogos[meio],
                "comparacoes": comparacoes
            }

        if jogos[meio].id < id_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1

    return {
        "jogo": None,
        "comparacoes": comparacoes
    }
