# 📦Consultas de exportações
Repositorio de manipulação de bases de dados do MDIC

<details>
<summary><strong> 🛠️Ferramentas/dependencias usadas</strong></summary>

<h2>SQLite</h2>
<h3>Armazenamento das tabelas e queries</h3>

<h2> Python </h2>
<h3>Linguagem mãe do projeto</h3>

<h2> Pandas </h2>
<h3>Tratamento, Inserção dos dados</h3>

<h2> Plotly </h2>
<h3>Criação de gráficos interativos</h3>

<h2> Streamlit </h2>
<h3>Criação da interface e componentes para entrada de parametros</h3>

<h2> sqlite3 </h2>
<h3>Biblioteca nativa do Python para interligar o codigo python 
com o arquivo do banco SQLite</h3>

<h2>Dotenv e OS</h2>
<h3>Usados para carregar arquivo .env (variaveis locais) para definir o arquivo do banco SQLite</h3>

</details>

<details>
<summary><strong>⚙️Como rodar o projeto (clique pra visualizar)</strong></summary>

### 1. Baixe e instale o Python

Instale o Python compatível com o projeto e marque a opção **Add Python to PATH** durante a instalação.

**Vídeo do procedimento:**

[![Vídeo: baixar e instalar o Python](https://img.youtube.com/vi/wwLU-TWkJNM/hqdefault.jpg)](https://youtu.be/wwLU-TWkJNM)

### 2. Como rodar

Após a instalação do python baixe o .zip do repositorio e extraia para o caminho: Downloads/consultas_indices_graficos-main

Abra o cmd e entre no caminho pelos comandos:
cd Downloads
cd consultas_indices_graficos-main

Dentro do caminho no terminal execute os comandos:
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

Dentro do ambiente virtual que voce entrou rode os comandos em sequencia:
python criar_tabelas.py
python preparar_banco.py

E por fim para rodar:
streamlit run app.py

[![Vídeo: Como rodar o projeto](https://img.youtube.com/vi/yyh5gAIad4s/hqdefault.jpg)](https://youtu.be/yyh5gAIad4s)


### 3. Como rodar após instalação/configuração?

voce so precisara entrar no diretorio do projeto rodando:
1. cd Downloads
2. cd consultas_indices_graficos-main
3. .venv\Scripts\activate
4. streamlit run app.py


</details>

<details>
<summary>🤖<strong>Como a IA foi usada nesse projeto</strong></summary>
<h2> 1. Formatação e design do readme<h2>
<h4>Usei a IA para botar o conteudo em um modelo que eu escrevi onde por exemplo na seção de como rodar o projeto so precisei substituir os links de icone e video.</h4>

<h2> 2. Orientações de como fazer uma query dinamica<h2>
<h4>Durante meu desenvolvimento estava pensando como poderia escrever um query dinamica onde sua string era gerada de acordo com os parametros do usuario. Logo usei a IA para me explicar qual o padrao do nos projetos e como eu poderia desenvolver essa query.</h4>

<h2> 3. Tirar dúvidas, funções e métodos de resolução</h2>
<h4>Foram tiradas diversas dúvidas de como usar funções como o .copy() do pandas, como eu poderia importar meus inserts com um header (inserts.py), dúvidas de sintaxe sql, como transformar colunas do dataframe pandas para uma lista com os nomes, etc.</h4>

<h2> 4. Depuração do código</h2>
<h4>Usei a IA para entender erros de lógica, consulta sql, entre outros.

<h2> 5. Recomendações de otimização</h2>
<h4>Perguntei sobre recomendações de otimização e foi recomendado usar o cache_data do streamlit onde a aplicação armazena em um cache as consultas feitas se ter que refaze-las no banco.</h4>

<h2> 6. Entendimento do formato do xlsx<h2>
<h4>Usei a IA para entender o formato do xlsx arquivo excel pois ao tentar tratar e inserir os dados vinham coisas inesperadas na base foi ai que aprendi o conceito de que a tabela possui varios indices de tipos de dados.</h4>
</details>

<details>
<summary><strong>Fontes Usadas:</strong></summary>

<h2>https://docs.plotly.com/</h2>
<h2>https://docs.streamlit.io/</h2>
<h2>https://pandas.pydata.org/docs/</h2>
<h2>https://claude.com/</h2>
<h2>https://www.idtools.com.au/interactive-choropleth-maps-with-plotly-for-python/</h2>
<h2>http://gov.br/inpi</h2>
<h2>http://comexstat.mdic.gov.br/</h2>
</details>