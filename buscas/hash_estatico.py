class HashEstatico:

    def __init__(self, tamanho_tabela):
        self.tamanho_tabela = tamanho_tabela
        self.tabela = [[] for _ in range(tamanho_tabela)] # Inicializa a tabela com listas vazias
        #O objetivo de criar uma lista com várias listas dentro é permitir que cada posição da tabela possa armazenar múltiplos elementos, caso haja colisões. 
        #Cada posição da tabela é uma lista que pode conter vários elementos que compartilham o mesmo índice de hash.

    def funcao_hash(self, id_game):
        return id_game % self.tamanho_tabela

    def inserir(self, jogo):
        indice = self.funcao_hash(jogo.id)
        self.tabela[indice].append(jogo)  # Adiciona o jogo à lista na posição do índice calculado

    def buscar_na_tabela(self, id_desejado):
        comparacoes = 0  # Contador de comparações
        indice = self.funcao_hash(id_desejado)
        for jogo in self.tabela[indice]:
            comparacoes += 1  # Incrementa o contador a cada comparação
            if jogo.id == id_desejado:
                return {
                    "jogo": jogo,
                    "comparacoes": comparacoes
                }
        return {
            "jogo": None,
            "comparacoes": comparacoes
        }