import pandas as pd

class Carregador:
    @staticmethod
    def carregar_dados(url: str):
        return pd.read_csv(url)
