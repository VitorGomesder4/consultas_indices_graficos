BLOCOS_ECONOMICOS = (  # NOVO: blocos que se sobrepõem aos continentes
    "União Europeia - UE",
    "Associação de Nações do Sudeste Asiático - ASEAN",
    "Mercado Comum do Sul - Mercosul",
)

def gerar_query_dinamica(agrupamento_geografico=None, agrupar_ncm=False, somar_exportacao_val=False, tipo_bloco="continente", limite=20, offset=0,
                         filtro_search=None): 

    selects = []
    groups_by = []
    joins = []
    parametros = [] #lista de parametros a serem incluidos na query


    if agrupamento_geografico == "pais":
        selects.append("pa.no_pais")
        joins.append("""
            JOIN pais as pa
            ON pa.co_pais = ex.CO_PAIS
        """
        )
        groups_by.append("pa.no_pais")


    elif agrupamento_geografico == "pais_bloco":
        selects.append("pb.no_bloco AS bloco")

        lista_blocos = ", ".join(f"'{b}'" for b in BLOCOS_ECONOMICOS)
        operador = "NOT IN" if tipo_bloco == "continente" else "IN"

        joins.append(f"""
            JOIN pais AS pa
                ON pa.co_pais = ex.CO_PAIS
            JOIN pais_bloco AS pb
                ON pb.co_pais = pa.co_pais
                AND pb.no_bloco {operador} ({lista_blocos})
        """)

        groups_by.append("pb.no_bloco")


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
            "SUM(CAST(ex.KG_LIQUIDO AS REAL)) AS Kg_liquido",
            "SUM(CAST(ex.VL_FOB AS REAL)) AS Valor_Fob"
        ])
        # MUDOU: QT_ESTAT só é somada por NCM (a unidade muda de NCM para NCM)
        if agrupar_ncm:
            selects.append("SUM(CAST(ex.QT_ESTAT AS REAL)) AS Quantidade_Exportada")

    else:
        selects.extend([
            "ex.KG_LIQUIDO AS Kg_liquido",
            "ex.VL_FOB AS Valor_Fob",
            "ex.QT_ESTAT AS Quantidade_Exportada"
        ])

    sql = f"""
        SELECT {", ".join(selects)}
        FROM exportacoes AS ex
        {" ".join(joins)}
    """

    if filtro_search and filtro_search.get("tipo") in ["ncm", "pais", "pais_bloco"]:

        valor = filtro_search["valor"]
        
        if filtro_search["tipo"] == "ncm":

            if valor.isdigit():
                sql += "\nWHERE nu.co_ncm = ?"
                parametros.append(valor)
            else:
                sql += "\nWHERE nu.no_ncm_por = ?"
                parametros.append(valor)

        elif filtro_search["tipo"] == "pais":
            sql += "\nWHERE pa.no_pais = ?"
            parametros.append(valor)

        else: #pais_bloco
            sql += "\nWHERE pb.no_bloco = ?"
            parametros.append(valor)

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

        try:
            offset = max(int(offset), 0)
        except (ValueError, TypeError):
            offset = 0

        sql += f"\nLIMIT {limite} OFFSET {offset}"

    return sql, tuple(parametros)