def gerar_descricao_ncm():
    query = f"""
        SELECT DISTINCT
            exportacoes.CO_NCM,
            ncm_unidade.no_ncm_por
        FROM exportacoes
        JOIN ncm_unidade
            ON exportacoes.CO_NCM = ncm_unidade.co_ncm
        GROUP BY
            exportacoes.CO_NCM
    """

    return query.strip()