from utils.carregador import carregar_dados
from buscas.sequencial import busca_sequencial

caminho_planilha = 'dados/Planilha de games.xlsx'

jogos_listados = carregar_dados(caminho_planilha)

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

