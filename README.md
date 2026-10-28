# 📦Consultas de exportações
Repositorio de manipulação de bases de dados do MDIC


## 🛠️Processo de como rodar o projeto

### 1. Baixe e instale o Python

Instale o Python compatível com o projeto e marque a opção **Add Python to PATH** durante a instalação.

**Vídeo do procedimento:**

<!-- Adicione o vídeo aqui -->

### 2. Baixe e instale o MariaDB

Baixe e instale o MariaDB Server. Durante a instalação, configure a senha do usuário `root`.

**Vídeo do procedimento:**

<!-- Adicione o vídeo aqui -->

### 3. Inicie o serviço do MariaDB

Inicie o serviço do MariaDB pelo aplicativo de serviços do Windows (`services.msc`) ou pelo terminal, caso necessário.

**Vídeo do procedimento:**

<!-- Adicione o vídeo aqui -->

### 4. Baixe o projeto

Você pode baixar o projeto em formato ZIP pelo GitHub ou cloná-lo usando o Git.

**Baixar ZIP:** acesse o repositório, clique em `Code` e depois em `Download ZIP`.

**Clonar com Git:**

```bash
git clone URL_DO_REPOSITORIO
```

**Vídeo do procedimento:**

<!-- Adicione o vídeo aqui -->

### 5. Extraia os arquivos do projeto

Se você baixou o ZIP, extraia seu conteúdo para uma pasta de sua preferência.

Se clonou o repositório com Git, os arquivos já estarão disponíveis na pasta criada pelo comando.

**Vídeo do procedimento:**

<!-- Adicione o vídeo aqui -->

### 6. Acesse a raiz do projeto pelo terminal

Abra o terminal na pasta principal do projeto, onde estão localizados os arquivos de configuração, o `requirements.txt` e o arquivo principal da aplicação.

**Exemplo no Windows:**

```cmd
cd caminho\para\consultas_indices_graficos
```

**Vídeo do procedimento:**

<!-- Adicione o vídeo aqui -->

### 7. Crie o banco de dados e as tabelas (DDL)

Execute o arquivo SQL responsável por criar o banco de dados e as tabelas.

```cmd
"C:\Program Files\MariaDB 13.0\bin\mariadb.exe" -u root -p < criar_tabelas.sql
```

**Observação:** se o MariaDB estiver instalado em outro diretório, ajuste o caminho do executável. O nome do arquivo SQL também deve corresponder ao arquivo presente no projeto.

**Vídeo do procedimento:**

<!-- Adicione o vídeo aqui -->

### 8. Crie o ambiente virtual e execute o projeto

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

<!-- Adicione o vídeo aqui -->
