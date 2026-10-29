import pandas as pd
import streamlit as st
from selects.select_dinamico import gerar_query_dinamica
from selects.select_padrao import gerar_query_padrao
from selects.select_descricao_ncm import gerar_descricao_ncm
from selects.select_mapa_mundo import gerar_mapa_mundo
from db import db
import plotly.express as px

#CACHE para consulta sql
@st.cache_data(ttl=300)
def executar_reads_query(query, parametros=None):
    return pd.read_sql(query, db, params=parametros, dtype=str)


#Abas da pagina
secao = st.sidebar.radio(
    "Navegação",
    ["Exportações Por Continente", "Exportações Por Bloco Econômico", "Gráficos"]
)

#Se a seção for exportação por continente vamos exibir tabela para tal
if secao == "Exportações Por Continente":
    

    st.title("Exportação por Continente")

    #Criando atributo de paginação
    if "pagina" not in st.session_state:
        st.session_state.pagina = 1


    with st.expander("Parâmetros de exportações", expanded=False):
        #Formulario de parametros para realizar consulta sem precisar recarregar codigo toda vez
        with st.form("Parametros_exportações"):
            indice_por_pag = st.number_input(label="Indices por pagina (max 50)", min_value=1 , max_value=50, value=20)

            agrupamento_geografico = st.radio(label="Agrupamento Geografico:", options=["pais", "pais_bloco"], index=None)

            agrupamento_ncm = st.radio(label="Agrupar NCM's:", options=["Sim", "Não"], index=None)

            tipo_filtro = st.selectbox(
                label="Filtrar por:",
                options=["Sem filtro", "ncm", "pais", "pais_bloco"],
            )

            valor_filtro = st.text_input(label="Valor do filtro (código ou nome):")

            aplicar = st.form_submit_button("Aplicar")


        #Guardando os valores como atributos da sessão
        if aplicar:
            st.session_state.indice_por_pag = indice_por_pag
            st.session_state.pagina = 1 #Reseta o valor para 1 se o usuario aplicar

            st.session_state.agrupamento_geografico = agrupamento_geografico
            st.session_state.agrupamento_ncm = agrupamento_ncm

            st.session_state.usar_query_dinamica = True #atributo que define se visualiza exportacoes individuais padroes ou agrupadas

            st.session_state.tipo_filtro = tipo_filtro
            st.session_state.valor_filtro = valor_filtro.strip()


        limite = st.session_state.get("indice_por_pag", 20)

        agrupamento_geografico = st.session_state.get("agrupamento_geografico", "pais")

        agrupamento_ncm = (st.session_state.get("agrupamento_ncm", "Não") == "Sim")

        offset = (st.session_state.get("pagina", 1) - 1) * limite


    tipo = st.session_state.get("tipo_filtro", "Sem filtro")
    valor = st.session_state.get("valor_filtro", "")

    filtro_search = {"tipo": tipo, "valor": valor} if tipo != "Sem filtro" and valor else None

    if st.session_state.get("usar_query_dinamica", False):
        try:
            x, x_params = gerar_query_dinamica(
                agrupamento_geografico=agrupamento_geografico, 
                agrupar_ncm=agrupamento_ncm, 
                somar_exportacao_val=True, 
                tipo_bloco="continente", 
                limite=limite, 
                offset=offset,
                filtro_search=filtro_search)
        except ValueError as e:
            st.error(str(e))
            st.stop()

        x = x.strip()

        df = executar_reads_query(x, x_params)
        
    else:
        x = gerar_query_padrao(limite=limite, offset=offset)

        df = executar_reads_query(x)


    #Container referente a seção da tabela exibida
    with st.container(border=True):

        #Botao para resetar estado de exibição
        resetar_tabela = st.button(label="Resetar Tabela para padrão")

        if resetar_tabela:
            for i in ("indice_por_pag", "agrupamento_geografico", "agrupamento_ncm", "usar_query_dinamica", "tipo_filtro", "valor_filtro"):
                st.session_state.pop(i, None)
            st.session_state.pagina = 1
            st.rerun()

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

    
    with st.expander("Parâmetros de exportações", expanded=False):
        #Formulario de parametros para realizar consulta sem precisar recarregar codigo toda vez
        with st.form("form_bloco"):
            indice_por_pag = st.number_input(label="Indices por pagina (max 50)", min_value=1, max_value=50, value=20)
            agrupamento_geografico = st.radio(label="Agrupamento Geografico:", options=["pais", "pais_bloco"], index=None)
            agrupamento_ncm = st.radio(label="Agrupar NCM's:", options=["Sim", "Não"], index=None)
            tipo_filtro = st.selectbox(label="Filtrar por:", options=["Sem filtro", "ncm", "pais", "pais_bloco"])
            valor_filtro = st.text_input(label="Valor do filtro (código ou nome):")
            aplicar = st.form_submit_button("Aplicar")

        if aplicar:
            st.session_state.indice_por_pag = indice_por_pag
            st.session_state.pagina = 1
            st.session_state.agrupamento_geografico = agrupamento_geografico
            st.session_state.agrupamento_ncm = agrupamento_ncm
            st.session_state.usar_query_dinamica = True
            st.session_state.tipo_filtro = tipo_filtro
            st.session_state.valor_filtro = valor_filtro.strip()

        limite = st.session_state.get("indice_por_pag", 20)
        agrupamento_geografico = st.session_state.get("agrupamento_geografico", "pais")
        agrupamento_ncm = (st.session_state.get("agrupamento_ncm", "Não") == "Sim")
        offset = (st.session_state.get("pagina", 1) - 1) * limite


    tipo = st.session_state.get("tipo_filtro", "Sem filtro")
    valor = st.session_state.get("valor_filtro", "")

    filtro_search = {"tipo": tipo, "valor": valor} if tipo != "Sem filtro" and valor else None

    if st.session_state.get("usar_query_dinamica", False):
        try:
            y, y_params = gerar_query_dinamica(agrupamento_geografico=agrupamento_geografico, 
                                            agrupar_ncm=agrupamento_ncm , 
                                            somar_exportacao_val=True, 
                                            tipo_bloco="economico", 
                                            limite=limite, 
                                            offset=offset,
                                            filtro_search=filtro_search)
        except ValueError as e:
            st.error(str(e))
            st.stop()

        y = y.strip()

        df2 = executar_reads_query(y, y_params)

    else:
        y = gerar_query_padrao(limite=limite, offset=offset)
        df2 = executar_reads_query(y)


    #Container referente a seção da tabela exibida
    with st.container(border=True):

        #Botao para resetar estado de exibição
        resetar_tabela = st.button(label="Resetar Tabela para padrão")
        
        if resetar_tabela:
            for i in ("indice_por_pag", "agrupamento_geografico", "agrupamento_ncm", "usar_query_dinamica", "tipo_filtro", "valor_filtro"):
                st.session_state.pop(i, None)
            st.session_state.pagina = 1
            st.rerun()

        #EXIBINDO exportações por bloco_economico
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



# ABA de visualização de graficos de visualização
if secao == "Gráficos":
    st.title("Gráficos")


    # Geração de tabela para descrição dos ncm que o usuario ira escolher
    query = gerar_descricao_ncm()
    df_para_descricao_ncm = executar_reads_query(query)

    st.text("Descrição dos Produtos disponíveis: ")
    st.dataframe(df_para_descricao_ncm)


    #Geração de tabela para exibir grafico de mapa do mundo


    st.text("Mapa exportações: ")

    produto = st.selectbox(label="Produto", options=df_para_descricao_ncm["CO_NCM"].sort_values().tolist())

    query, parametros = gerar_mapa_mundo(produto)
    df_para_mapa_mundo = executar_reads_query(query, parametros)

    descricao_produto = df_para_descricao_ncm.loc[
        df_para_descricao_ncm["CO_NCM"] == produto,
        "no_ncm_por"
    ].iloc[0]

    grafico_mapa_mundo = px.choropleth(
        data_frame=df_para_mapa_mundo,
        locations="pais",
        locationmode="country names",
        color="total_quantidade",
        hover_name="pais",
        hover_data=["total_fob", "total_kg"],
        projection="equirectangular",
        title=f"Exportações de {descricao_produto}"
        )

    st.plotly_chart(grafico_mapa_mundo, use_container_width=True)

    st.dataframe(df_para_mapa_mundo)