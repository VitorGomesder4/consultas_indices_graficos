# 📦Consultas de exportações
Repositorio de manipulação de bases de dados do MDIC


## 🛠️Processo de como rodar o projeto

### 1. Baixe e instale o Python

Instale o Python compatível com o projeto e marque a opção **Add Python to PATH** durante a instalação.

**Vídeo do procedimento:**

[![Vídeo: baixar e instalar o Python](https://img.youtube.com/vi/wwLU-TWkJNM/hqdefault.jpg)](https://youtu.be/wwLU-TWkJNM)

### 2. Baixe e instale o MariaDB

Baixe e instale o MariaDB Server. Durante a instalação, configure a senha do usuário `root`.

**Vídeo do procedimento:**

[![Vídeo: baixar e instalar o MariaDB](https://img.youtube.com/vi/myQ3a4l78D4/hqdefault.jpg)](https://youtu.be/myQ3a4l78D4)

### 3. Inicie o serviço do MariaDB

Inicie o serviço do MariaDB pelo aplicativo de serviços do Windows (`services.msc`) ou pelo terminal, caso necessário.

**Vídeo do procedimento:**

[![Vídeo: iniciar o serviço do MariaDB](https://img.youtube.com/vi/pw8RDVaZUqU/hqdefault.jpg)](https://youtu.be/pw8RDVaZUqU)

### 4. Baixe o projeto

Você pode baixar o projeto em formato ZIP pelo GitHub ou cloná-lo usando o Git.

**Baixar ZIP:** acesse o repositório, clique em `Code` e depois em `Download ZIP`.

**Clonar com Git:**

```bash
git clone URL_DO_REPOSITORIO
```

**Vídeo do procedimento:**

[![Vídeo: baixar o projeto](https://img.youtube.com/vi/bwRj_0GMwI4/hqdefault.jpg)](https://youtu.be/bwRj_0GMwI4)

### 5. Extraia os arquivos do projeto

Se você baixou o ZIP, extraia seu conteúdo para uma pasta de sua preferência.

Se clonou o repositório com Git, os arquivos já estarão disponíveis na pasta criada pelo comando.

**Vídeo do procedimento:**

[![Vídeo: extrair os arquivos do projeto](https://img.youtube.com/vi/TMBYn8fcbnc/hqdefault.jpg)](https://youtu.be/TMBYn8fcbnc)


### 6. Renomeie o arquivo .env

Após extrair o conteúdo do zip abra o diretório e renomeie
`.env.example` para => `.env`.

Depois abra o arquivo com o bloco de notas, escreva sua senha na
variável `DB_PASSWORD` e salve o arquivo.

**Vídeo do procedimento:**

[![Vídeo: renomear o arquivo .env](https://img.youtube.com/vi/nt63cdGBhBY/hqdefault.jpg)](https://youtu.be/nt63cdGBhBY)

### 7. Acesse a raiz do projeto pelo terminal

Abra o terminal na pasta principal do projeto, onde estão localizados os arquivos de configuração, o `requirements.txt` e o arquivo principal da aplicação.

**Exemplo no Windows:**

```cmd
cd caminho\para\consultas_indices_graficos
```

**Vídeo do procedimento:**

[![Vídeo: acessar a raiz do projeto pelo terminal](https://img.youtube.com/vi/xAiCeIn6N3Y/hqdefault.jpg)](https://youtu.be/xAiCeIn6N3Y)

### 8. Crie o banco de dados e as tabelas (DDL)

Execute o arquivo SQL responsável por criar o banco de dados e as tabelas.

```cmd
"C:\Program Files\MariaDB 13.0\bin\mariadb.exe" -u root -p < criar_tabelas.sql
```

**Observação:** se o MariaDB estiver instalado em outro diretório, ajuste o caminho do executável. O nome do arquivo SQL também deve corresponder ao arquivo presente no projeto.

**Vídeo do procedimento:**

[![Vídeo: criar o banco de dados e as tabelas](https://img.youtube.com/vi/zgxUm1mbsig/hqdefault.jpg)](https://youtu.be/zgxUm1mbsig)

### 9. Crie o ambiente virtual e execute o projeto

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
