from db import db

#Index(['CO_NCM', 'NO_NCM_POR', 'CO_UNID', 'NO_UNID', 'SG_UNID'], dtype='str')

def inserir_ncm_unidade_estatistica(tabela):
    cursor = db.cursor()
    
    cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM ncm_unidade
        )
    """)
    
    if not cursor.fetchone()[0]:
    
        for i in range(len(tabela)):
            indice_linha = tabela.iloc[i]
    
            insert_tupla = (
                indice_linha["CO_NCM"],
                indice_linha["NO_NCM_POR"],
                indice_linha["CO_UNID"],
                indice_linha["NO_UNID"],
                indice_linha["SG_UNID"]
            )
    
            cursor.execute(
                """
                INSERT INTO ncm_unidade (
                    co_ncm, no_ncm_por, co_unid, no_unid, sg_unid
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                insert_tupla
            )
    
        db.commit()
    
    else:
        print("Insert ja existentes")
    
    print(len(tabela))
    
    cursor.close()