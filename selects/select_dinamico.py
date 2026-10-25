BLOCOS_ECONOMICOS = (  # NOVO: blocos que se sobrepõem aos continentes
    "União Europeia - UE",
    "Associação de Nações do Sudeste Asiático - ASEAN",
    "Mercado Comum do Sul - Mercosul",
)

def gerar_query_dinamica(agrupamento_geografico=None, agrupar_ncm=False, somar_exportacao_val=False, tipo_bloco="continente", limite=20, offset=0):  # NOVO: parâmetro tipo_bloco

    selects = []
    groups_by = []
    joins = []


    if agrupamento_geografico == "pais":
        selects.append("pa.no_pais")
        joins.append("""
            JOIN pais as pa
            ON pa.co_pais = ex.CO_PAIS
        """
        )
        groups_by.append("pa.no_pais")


    elif agrupamento_geografico == "pais_bloco":
        # MUDOU: COALESCE mostra "Sem bloco" para países sem bloco (antes sumiam do resultado)
        selects.append("COALESCE(pb.no_bloco, 'Sem bloco') AS bloco")

        # NOVO: um tipo de bloco por vez (continente OU econômico); senão o mesmo país
        # entra em 2 blocos e o valor é somado duas vezes
        lista_blocos = ", ".join(f"'{b}'" for b in BLOCOS_ECONOMICOS)
        operador = "NOT IN" if tipo_bloco == "continente" else "IN"

        # MUDOU: LEFT JOIN no pais_bloco (antes JOIN) para não perder países sem bloco,
        # e o filtro de tipo fica no ON (no WHERE o LEFT JOIN voltaria a descartar linhas)
        joins.append(f"""
            JOIN pais as pa
            ON pa.co_pais = ex.CO_PAIS
            LEFT JOIN pais_bloco as pb
            ON pb.co_pais = pa.co_pais
            AND pb.no_bloco {operador} ({lista_blocos})
        """)
        groups_by.append("COALESCE(pb.no_bloco, 'Sem bloco')")  # MUDOU: mesmo COALESCE do select


    selects.append("nu.co_ncm")
    selects.append("nu.no_ncm_por")
    
    joins.append("""
        JOIN ncm_unidade as nu
        ON nu.co_ncm = ex.CO_NCM
    """)
    if agrupar_ncm:
        groups_by.append("nu.co_ncm")
        groups_by.append("nu.no_ncm_por")

    if somar_exportacao_val:
        selects.extend([
            "SUM(CAST(ex.KG_LIQUIDO AS DECIMAL(15, 2))) AS Kg_liquido",
            "SUM(CAST(ex.VL_FOB AS DECIMAL(15, 2))) AS Valor_Fob"
        ])
        # MUDOU: QT_ESTAT só é somada por NCM (a unidade muda de NCM para NCM)
        if agrupar_ncm:
            selects.append("SUM(CAST(ex.QT_ESTAT AS DECIMAL(15, 2))) AS Quantidade_Exportada")

    sql = f"""
        SELECT {", ".join(selects)}
        FROM exportacoes AS ex
        {" ".join(joins)}
    """

    if groups_by and somar_exportacao_val:
        sql += "\nGROUP BY " + ", ".join(groups_by)

    if somar_exportacao_val:
        # MUDOU: sem agrupar por NCM não existe Quantidade_Exportada, então ordena por Valor_Fob
        sql += "\nORDER BY " + ("Quantidade_Exportada" if agrupar_ncm else "Valor_Fob") + " DESC"

    if limite:
        try:
            limite = int(limite)

            if limite < 1:
                raise ValueError

        except (ValueError, TypeError):
            limite = 20

    sql += f"\nLIMIT {limite} OFFSET {offset}"

    return sql

x = gerar_query_dinamica("pais_bloco", agrupar_ncm=True, somar_exportacao_val=True, tipo_bloco="continente")
y = gerar_query_dinamica("pais_bloco", somar_exportacao_val=True, tipo_bloco="economico")

print(x.strip())