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

### 2. Baixe o projeto

Você pode baixar o projeto em formato ZIP pelo GitHub ou cloná-lo usando o Git.

**Baixar ZIP:** acesse o repositório, clique em `Code` e depois em `Download ZIP`.

**Clonar com Git:**

```bash
git clone URL_DO_REPOSITORIO
```

**Vídeo do procedimento:**

[![Vídeo: baixar o projeto](https://img.youtube.com/vi/bwRj_0GMwI4/hqdefault.jpg)](https://youtu.be/bwRj_0GMwI4)

### 3. Extraia os arquivos do projeto

Se você baixou o ZIP, extraia seu conteúdo para uma pasta de sua preferência.

Se clonou o repositório com Git, os arquivos já estarão disponíveis na pasta criada pelo comando.

**Vídeo do procedimento:**

[![Vídeo: extrair os arquivos do projeto](https://img.youtube.com/vi/TMBYn8fcbnc/hqdefault.jpg)](https://youtu.be/TMBYn8fcbnc)


### 4. Renomeie o arquivo .env

Após extrair o conteúdo do zip abra o diretório e renomeie
`.env.example` para => `.env`.

Depois abra o arquivo com o bloco de notas e, se quiser, altere o nome do
arquivo do banco na variável `DB_DATABASE` e salve o arquivo.

**Vídeo do procedimento:**

[![Vídeo: renomear o arquivo .env](https://img.youtube.com/vi/nt63cdGBhBY/hqdefault.jpg)](https://youtu.be/nt63cdGBhBY)

### 5. Acesse a raiz do projeto pelo terminal

Abra o terminal na pasta principal do projeto, onde estão localizados os arquivos de configuração, o `requirements.txt` e o arquivo principal da aplicação.

**Exemplo no Windows:**

```cmd
cd caminho\para\consultas_indices_graficos
```

**Vídeo do procedimento:**

[![Vídeo: acessar a raiz do projeto pelo terminal](https://img.youtube.com/vi/xAiCeIn6N3Y/hqdefault.jpg)](https://youtu.be/xAiCeIn6N3Y)

### 6. Crie o banco de dados e as tabelas (DDL)

Execute o arquivo SQL responsável por criar o arquivo do banco de dados e as tabelas.

```cmd
python -c "import sqlite3; sqlite3.connect('consultas_indices_graficos.db').executescript(open('ddl/criar_tabelas.sql', encoding='utf-8').read())"
```

**Observação:** o nome do arquivo `.db` deve ser o mesmo definido em `DB_DATABASE` no `.env`. O nome do arquivo SQL também deve corresponder ao arquivo presente no projeto.

**Vídeo do procedimento:**

[![Vídeo: criar o banco de dados e as tabelas](https://img.youtube.com/vi/zgxUm1mbsig/hqdefault.jpg)](https://youtu.be/zgxUm1mbsig)

### 7. Crie o ambiente virtual e execute o projeto

Crie e ative um ambiente virtual Python:

```cmd
python -m venv venv
venv\Scripts\activate
```

Instale as dependências:

```cmd
pip install -r requirements.txt
```

Execute o script responsável por preparar e preencher o banco de dados, caso essa etapa ainda não tenha sido realizada:

```cmd
python preparar_banco.py
```

Por fim, inicie a aplicação:

```cmd
streamlit run app.py
```

Acesse o endereço local apresentado no terminal para utilizar o dashboard.

**Vídeo do procedimento:**

[![Vídeo: criar o ambiente virtual e executar o projeto](https://img.youtube.com/vi/9ldyRRECYrE/hqdefault.jpg)](https://youtu.be/9ldyRRECYrE)
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