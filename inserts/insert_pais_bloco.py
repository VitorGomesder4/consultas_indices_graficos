from db import db

"""
Index(['CO_PAIS', 'CO_BLOCO', 'NO_BLOCO', 'NO_BLOCO_ING', 'NO_BLOCO_ESP'],
      dtype='str')
"""

def inserir_ncm_unidade_estatistica(tabela):
    cursor = db.cursor()
    
    cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM pais_bloco
        )
    """)
    
    if not cursor.fetchone()[0]:
    
        for i in range(len(tabela)):
            indice_linha = tabela.iloc[i]
    
            insert_tupla = (
                indice_linha["CO_PAIS"],
                indice_linha["CO_BLOCO"],
                indice_linha["NO_BLOCO"],
                indice_linha["NO_BLOCO_ING"],
                indice_linha["NO_BLOCO_ESP"]
            )
    
            cursor.execute(
                """
                INSERT INTO pais_bloco (
                    co_pais, co_pais_ison3, co_pais_isoa3, no_pais, no_pais_ing, no_pais_esp
                )
                VALUES (%s, %s, %s, %s, %s)
                """,
                insert_tupla
            )
    
        db.commit()
    
    else:
        print("Insert ja existentes")
    
    print(len(tabela))
    
    cursor.close()