import pandas as pd
from db import db

print("Lendo exportações...")
tabela_exportacoes = pd.read_csv("bases_csv/EXP_2026.csv", sep=";")


os_5_produtos_escolhidos_co_ncm = {
    "vinhos": "2204",
    "queijos": "0406",
    "carne": "0200",
    "bebidas espirituosas": "2208",
    "cervejas": "2203"
    }


for coluna in tabela_exportacoes:
    tabela_exportacoes[coluna] = tabela_exportacoes[coluna].astype(str)

    #print(coluna, type(tabela_exportacoes[coluna].iloc[0]))

tabela_5_produtos_ig = tabela_exportacoes[tabela_exportacoes["CO_NCM"].str.startswith(tuple(os_5_produtos_escolhidos_co_ncm.values()))].copy()



print(tabela_5_produtos_ig.iloc[0])