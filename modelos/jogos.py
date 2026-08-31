class Jogo:
    def __init__(self, id_game, name, year_of_release, developer, platform, critic_score,user_score):
        self.id = id_game
        self.name = name
        self.year_of_release = year_of_release
        self.developer = developer
        self.platform = platform
        self.critic_score = critic_score
        self.user_score = user_score

    def __str__(self):
        return (
            f"ID: {self.id} | "
            f"Nome: {self.name} | "
            f"Plataforma: {self.platform} | "
            f"Ano: {self.year_of_release} | "
            f"Desenvolvedor: {self.developer} | "
            f"Nota Crítica: {self.critic_score} | "
            f"Nota Usuário: {self.user_score}"
        )