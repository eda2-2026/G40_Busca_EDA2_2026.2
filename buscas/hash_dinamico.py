class HashDinamico:

    def __init__(self, tamanho_inicial=10):
        self.tamanho = tamanho_inicial
        self.tabela = [[] for _ in range(self.tamanho)]
        self.quantidade = 0

    def _hash(self, id_jogo):
        return id_jogo % self.tamanho

    def inserir(self, jogo):
        indice = self._hash(jogo.id)
        self.tabela[indice].append(jogo)
        self.quantidade += 1

        # Aumenta a tabela quando ela fica muito cheia
        if self.quantidade / self.tamanho > 0.70:
            self._redimensionar(self.tamanho * 2)

    def buscar(self, id_procurado):
        comparacoes = 0
        indice = self._hash(id_procurado)

        for jogo in self.tabela[indice]:
            comparacoes += 1  # Incrementa a cada comparação

            if jogo.id == id_procurado:
                return {
                    "jogo": jogo,
                    "comparacoes": comparacoes
                }

        return {
            "jogo": None,
            "comparacoes": comparacoes
        }

    def remover(self, id_procurado):
        indice = self._hash(id_procurado)

        for posicao, jogo in enumerate(self.tabela[indice]):
            if jogo.id == id_procurado:
                del self.tabela[indice][posicao]
                self.quantidade -= 1

                # Diminui a tabela quando ela fica muito vazia
                if self.tamanho > 10 and self.quantidade / self.tamanho < 0.25:
                    self._redimensionar(self.tamanho // 2)

                return True

        return False

    def _redimensionar(self, novo_tamanho):
        jogos = []

        for lista in self.tabela:
            for jogo in lista:
                jogos.append(jogo)

        self.tamanho = novo_tamanho
        self.tabela = [[] for _ in range(self.tamanho)]

        for jogo in jogos:
            indice = self._hash(jogo.id)
            self.tabela[indice].append(jogo)
