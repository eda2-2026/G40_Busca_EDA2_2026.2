from utils.carregador import carregar_dados
from buscas.sequencial import busca_sequencial
from buscas.hash_estatico import HashEstatico

caminho_planilha = 'dados/Planilha de games.xlsx'

jogos_listados = carregar_dados(caminho_planilha)

hash_table = HashEstatico(tamanho_tabela=100)  # Cria uma tabela hash com X posições

for jogo in jogos_listados:
    hash_table.inserir(jogo)

print(f"Total de jogos carregados: {len(jogos_listados)}")

print("\nPrimeiros 5 jogos:")

for jogo in jogos_listados[:5]:
    print(jogo)


id_desejado = int(input("\nDigite o ID do jogo que deseja buscar: "))

resultado_busca = busca_sequencial(jogos_listados, id_desejado) 
if resultado_busca["jogo"] is not None:
    print("\nJogo encontrado!")
    print(resultado_busca["jogo"])

else: 
    print("\nJogo não encontrado.")

print(f"Total de comparações realizadas: {resultado_busca['comparacoes']}")

resultado_busca_hash = hash_table.buscar_na_tabela(id_desejado)
if resultado_busca_hash["jogo"] is not None:
    print("\nJogo encontrado na tabela hash!")
    print(resultado_busca_hash["jogo"]) 

else:
    print("\nJogo não encontrado na tabela hash.")

print(f"Total de comparações realizadas na tabela hash: {resultado_busca_hash['comparacoes']}")