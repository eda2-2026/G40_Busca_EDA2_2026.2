

def busca_sequencial(jogos, id_procurado):

    comparacoes = 0  # Contador de comparações

    for jogo in jogos: 
        comparacoes += 1  # Incrementa o contador a cada comparação
        if jogo.id == id_procurado:
            return {
                "jogo": jogo,
                "comparacoes": comparacoes
            }
        
    return {
                    "jogo": None,
                    "comparacoes": comparacoes
                }