from db import db

def inserir_exportacoes(tabela):
    cursor = db.cursor()

    cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM exportacoes
        )
    """)

    if not cursor.fetchone()[0]:

        for i in range(len(tabela)):
            indice_linha = tabela.iloc[i]

            insert_tupla = (
                indice_linha["CO_ANO"],
                indice_linha["CO_MES"],
                indice_linha["CO_NCM"],
                indice_linha["CO_UNID"],
                indice_linha["CO_PAIS"],
                indice_linha["SG_UF_NCM"],
                indice_linha["CO_VIA"],
                indice_linha["CO_URF"],
                indice_linha["QT_ESTAT"],
                indice_linha["KG_LIQUIDO"],
                indice_linha["VL_FOB"]
            )

            cursor.execute(
                """
                INSERT INTO exportacoes (
                    CO_ANO, CO_MES, CO_NCM, CO_UNID, CO_PAIS,
                    SG_UF_NCM, CO_VIA, CO_URF, QT_ESTAT,
                    KG_LIQUIDO, VL_FOB
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                insert_tupla
            )

        db.commit()

    else:
        print("Insert ja existentes")

    print(len(tabela))

    cursor.close()