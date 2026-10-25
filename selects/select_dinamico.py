BLOCOS_ECONOMICOS = ("União Europeia - UE",
                     "Associação de Nações do Sudeste Asiático - ASEAN",
                     "Mercado Comum do Sul - Mercosul")
# os demais blocos (Europa, África, Ásia, Oceania...) são continentes/regiões: 1 por país

def gerar_query_dinamica(agrupamento_geografico=None, agrupar_ncm=False,
                         somar_exportacao_val=False, tipo_bloco="continente", limite=20):
    selects, groups_by, joins = [], [], []
    lista_blocos = ", ".join(f"'{b}'" for b in BLOCOS_ECONOMICOS)

    if agrupamento_geografico == "pais":
        selects.append("pa.no_pais")
        joins.append("JOIN pais AS pa ON pa.co_pais = ex.CO_PAIS")
        groups_by.append("pa.no_pais")

    elif agrupamento_geografico == "pais_bloco":
        # (3) um tipo de bloco por vez: cada país cai em NO MÁXIMO 1 linha -> sem soma duplicada
        # (4) LEFT JOIN, com o filtro dentro do ON: países sem bloco (Brasil, "Não Declarados") não somem
        operador = "NOT IN" if tipo_bloco == "continente" else "IN"
        selects.append("COALESCE(pb.no_bloco, 'Sem bloco') AS bloco")
        joins.append(f"""LEFT JOIN pais_bloco AS pb
            ON pb.co_pais = ex.CO_PAIS AND pb.no_bloco {operador} ({lista_blocos})""")
        groups_by.append("COALESCE(pb.no_bloco, 'Sem bloco')")

    if agrupar_ncm:
        selects += ["nu.co_ncm", "nu.no_ncm_por"]
        joins.append("JOIN ncm_unidade AS nu ON nu.co_ncm = ex.CO_NCM")
        groups_by += ["nu.co_ncm", "nu.no_ncm_por"]

    if somar_exportacao_val:
        selects += ["SUM(CAST(ex.KG_LIQUIDO AS DECIMAL(20,2))) AS kg_liquido",
                    "SUM(CAST(ex.VL_FOB AS DECIMAL(20,2))) AS valor_fob"]
        # (5) QT_ESTAT está em unidades diferentes por NCM: só soma se agrupar por NCM
        if agrupar_ncm:
            selects.append("SUM(CAST(ex.QT_ESTAT AS DECIMAL(20,2))) AS quantidade_estatistica")

    sql = f"SELECT {', '.join(selects)}\nFROM exportacoes AS ex\n" + "\n".join(joins)

    if groups_by and somar_exportacao_val:
        sql += "\nGROUP BY " + ", ".join(groups_by)
        sql += "\nORDER BY valor_fob DESC"   # (2) alias existente

    try:
        limite = int(limite)
        if limite < 1: raise ValueError
    except (ValueError, TypeError):
        limite = 20
    return sql + f"\nLIMIT {limite}"


if __name__ == "__main__":
    print(gerar_query_dinamica("pais_bloco", True, True, "continente", 25))
