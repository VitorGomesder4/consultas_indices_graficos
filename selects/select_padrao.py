#Query que sera tabela padrao de exibição ao entrar na pagina
def gerar_query_padrao(limite=20, offset=0):
    query = f"""
        SELECT
            ex.CO_ANO,
            ex.CO_MES,
            ex.CO_NCM,
            nu.no_ncm_por,
            pa.no_pais,
            pb.no_bloco AS bloco,
            ex.QT_ESTAT AS Quantidade_Exportada,
            ex.KG_LIQUIDO AS Kg_liquido,
            ex.VL_FOB AS Valor_Fob
        FROM exportacoes AS ex
        LEFT JOIN pais AS pa
            ON pa.co_pais = ex.CO_PAIS
        LEFT JOIN pais_bloco AS pb
            ON pb.co_pais = pa.co_pais
        LEFT JOIN ncm_unidade AS nu
            ON nu.co_ncm = ex.CO_NCM
        ORDER BY ex.CO_ANO DESC, ex.CO_MES DESC
        LIMIT {int(limite)} OFFSET {int(offset)}
    """
    return query.strip()