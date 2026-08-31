import pandas as pd 
from modelos.jogos import Jogo

def carregar_dados(caminho_arquivo):
    df = pd.read_excel(caminho_arquivo)
    jogos = []

    for _, row in df.iterrows():   #Percorre cada linha do excel e cria um objeto Jogo com os dados da linha
        jogo = Jogo(
            id_game=row['id_game'],
            name=row['name'],
            year_of_release=row['year_of_release'],
            developer=row['developer'],
            platform=row['platform'],
            critic_score=row['critic_score'],
            user_score=row['user_score']
        )
        jogos.append(jogo) #adiciona o objeto Jogo à lista que vamos utilizar 
    return jogos
