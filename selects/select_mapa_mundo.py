def gerar_mapa_mundo(ncm):
    query = """
        SELECT
            p.no_pais AS pais,
            e.CO_NCM AS ncm,
            nu.no_ncm_por AS ncm_unidade,
            SUM(CAST(e.VL_FOB AS DECIMAL(20, 2))) AS total_fob,
            SUM(CAST(e.KG_LIQUIDO AS DECIMAL(20, 2))) AS total_kg,
            SUM(CAST(e.QT_ESTAT AS DECIMAL(20, 2))) AS total_quantidade
        FROM exportacoes e
        JOIN pais p ON e.CO_PAIS = p.co_pais
        JOIN ncm_unidade nu ON e.CO_NCM = nu.co_ncm
        WHERE e.CO_NCM LIKE %s
        GROUP BY p.co_pais, p.no_pais, e.CO_NCM
        ORDER BY total_fob DESC
    """

    return query.strip(), (f"{ncm}%",)