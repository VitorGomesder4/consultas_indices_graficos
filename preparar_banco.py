import pandas as pd
from inserts.inserts import inserir_exportacoes, inserir_ncm_unidade_estatistica, inserir_pais, inserir_pais_bloco
from db import db

# =========Tabela de exportacoes e seu tratamento===============
print("Lendo exportações...")
tabela_exportacoes = pd.read_csv("bases_csv/EXP_2026.csv", sep=";", dtype=str)


os_5_produtos_escolhidos_co_ncm = {
    "vinhos": ["2204"],
    "cervejas": ["22030000"],
    "carne_bovina": ["0201"],
    "café": ["0901"],
    "bebidas_espirituosas": ["2208"]
}


prefixos = tuple(p for lista in os_5_produtos_escolhidos_co_ncm.values() for p in lista)

tabela_5_produtos_ig = tabela_exportacoes[
    tabela_exportacoes["CO_NCM"].str.startswith(prefixos)
].copy()

inserir_exportacoes(tabela_5_produtos_ig)




# =========Tabela de paises e seu tratamento===============

print("Lendo correlacoes...")
tabela_correlacoes = pd.read_excel("bases_csv/TABELAS_AUXILIARES.xlsx", sheet_name=None, dtype=str)

"""
print(tabela_correlacoes["6"]) #ncm unidades
print(tabela_correlacoes["10"]) #paises
print(tabela_correlacoes["11"]) #blocos/continentes paises
"""
#===============================================================#
#Tratando para tabela ncm_unidade_estatistica
tabela_ncm_unidade = tabela_correlacoes["6"].copy()

for coluna in tabela_ncm_unidade:
    tabela_ncm_unidade[coluna] = tabela_ncm_unidade[coluna].astype(str)

inserir_ncm_unidade_estatistica(tabela_ncm_unidade)
#===============================================================#

#===============================================================#
#Tratando para tabela paises
tabela_paises = tabela_correlacoes["10"].copy()

for coluna in tabela_paises:
    tabela_paises[coluna] = tabela_paises[coluna].astype(str)

inserir_pais(tabela_paises)
#===============================================================#

#===============================================================#
#Tratando para tabela paises_blocos
tabela_pais_bloco = tabela_correlacoes["11"].copy()

for coluna in tabela_pais_bloco:
    tabela_pais_bloco[coluna] = tabela_pais_bloco[coluna].astype(str)

inserir_pais_bloco(tabela_pais_bloco)
#===============================================================#