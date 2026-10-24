from db import db

"""
Index(['CO_PAIS', 'CO_PAIS_ISON3', 'CO_PAIS_ISOA3', 'NO_PAIS', 'NO_PAIS_ING',
       'NO_PAIS_ESP'],
      dtype='str')
"""

def inserir_ncm_unidade_estatistica(tabela):
    cursor = db.cursor()
    
    cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM pais
        )
    """)
    
    if not cursor.fetchone()[0]:
    
        for i in range(len(tabela)):
            indice_linha = tabela.iloc[i]
    
            insert_tupla = (
                indice_linha["CO_PAIS"],
                indice_linha["CO_PAIS_ISON3"],
                indice_linha["CO_PAIS_ISOA3"],
                indice_linha["NO_PAIS"],
                indice_linha["NO_PAIS_ING"],
                indice_linha["NO_PAIS_ESP"]
            )
    
            cursor.execute(
                """
                INSERT INTO pais (
                    co_pais, co_pais_ison3, co_pais_isoa3, no_pais, no_pais_ing, no_pais_esp
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                insert_tupla
            )
    
        db.commit()
    
    else:
        print("Insert ja existentes")
    
    print(len(tabela))
    
    cursor.close()