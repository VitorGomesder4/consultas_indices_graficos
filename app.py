
import pandas as pd
import streamlit as st
from selects.select_dinamico import gerar_query_dinamica
from db import db

#CACHE para consulta sql
@st.cache_data(ttl=300)
def executar_reads_query(query):
    return pd.read_sql(query, db, dtype=str)


#Abas da pagina
secao = st.sidebar.radio(
    "Navegação",
    ["Exportações Por Continente", "Exportações Por Bloco Econômico"]
)

if secao == "Exportações Por Continente":
    

    st.title("Exportação por Continente")


    if "pagina" not in st.session_state:
        st.session_state.pagina = 1

    with st.expander("Parâmetros de exportações", expanded=True):
        #Formulario de parametros para realizar consulta sem precisar recarregar codigo toda vez
        with st.form("Parametros_exportações"):
            indice_por_pag = st.number_input(label="Indices por pagina (max 50)", min_value=1 , max_value=50, value=20)

            agrupamento_geografico = st.radio(label="Agrupamento Geografico:", options=["pais", "pais_bloco"])

            agrupamento_ncm = st.radio(label="Agrupar NCM's:", options=["Sim", "Não"])

            aplicar = st.form_submit_button("Aplicar")


        #Guardando os valores como atributos da sessão
        if aplicar:
            st.session_state.indice_por_pag = indice_por_pag
            st.session_state.pagina = 1 #Reseta o valor para 1 se o usuario aplicar

            st.session_state.agrupamento_geografico = agrupamento_geografico

            st.session_state.agrupamento_ncm = agrupamento_ncm


        limite = st.session_state.get("indice_por_pag", 20)

        agrupamento_geografico = st.session_state.get("agrupamento_geografico", "pais")

        agrupamento_ncm = (st.session_state.get("agrupamento_ncm", "Não") == "Sim")

        offset = (st.session_state.get("pagina", 1) - 1) * limite


    x = gerar_query_dinamica(
        agrupamento_geografico=agrupamento_geografico, 
        agrupar_ncm=agrupamento_ncm, 
        somar_exportacao_val=True, 
        tipo_bloco="continente", 
        limite=limite, 
        offset=offset).strip()

    df = executar_reads_query(x)


    #Exibindo Exportações
    st.write("Exportações:")
    st.table(df)


    #Botões para mudar pagina atual
    col1, col2, col3 = st.columns([1, 2, 3])

    with col1:
        if st.button(
            label="Anterior",
            disabled=st.session_state.pagina == 1
        ):
            st.session_state.pagina -= 1
            st.rerun()

    with col2:
        st.write(f"Página {st.session_state.pagina}")

    with col3:
        if st.button("Próxima"):
            st.session_state.pagina += 1
            st.rerun()


#Seção simples para dados por bloco economico
if secao == "Exportações Por Bloco Econômico":

    st.title("Exportação por Bloco Econômico")

    if "pagina" not in st.session_state:
            st.session_state.pagina = 1
    
    with st.expander("Parâmetros de exportações", expanded=True):
        #Formulario de parametros para realizar consulta sem precisar recarregar codigo toda vez
        with st.form("Parametros_exportações"):
            indice_por_pag = st.number_input(label="Indices por pagina (max 50)", min_value=1 , max_value=50, value=20)
        
            agrupamento_geografico = st.radio(label="Agrupamento Geografico:", options=["pais", "pais_bloco"])
        
            agrupamento_ncm = st.radio(label="Agrupar NCM's:", options=["Sim", "Não"])
        
            aplicar = st.form_submit_button("Aplicar")
        
        
            #Guardando os valores como atributos da sessão
            if aplicar:
                st.session_state.indice_por_pag = indice_por_pag
                st.session_state.pagina = 1 #Reseta o valor para 1 se o usuario aplicar
        
                st.session_state.agrupamento_geografico = agrupamento_geografico
        
                st.session_state.agrupamento_ncm = agrupamento_ncm
        
        
            limite = st.session_state.get("indice_por_pag", 20)
        
            agrupamento_geografico = st.session_state.get("agrupamento_geografico", "pais")
        
            agrupamento_ncm = (st.session_state.get("agrupamento_ncm", "Não") == "Sim")
        
            offset = (st.session_state.get("pagina", 1) - 1) * limite


    y = gerar_query_dinamica(agrupamento_geografico=agrupamento_geografico, agrupar_ncm=agrupamento_ncm , somar_exportacao_val=True, tipo_bloco="economico", limite=limite).strip()


    df2 = executar_reads_query(y)


    st.write("Exportações por blocos economico:")
    st.table(df2)

    #Botões para mudar pagina atual
    col1, col2, col3 = st.columns([1, 2, 3])
    
    with col1:
        if st.button(
            label="Anterior",
            disabled=st.session_state.pagina == 1
        ):
            st.session_state.pagina -= 1
            st.rerun()
    
    with col2:
        st.write(f"Página {st.session_state.pagina}")
    
    with col3:
        if st.button("Próxima"):
            st.session_state.pagina += 1
            st.rerun()
