# etl-pipeline-medallion-architecture

# Projeto de Ingestão de Dados - ETL Pipeline

Este é um projeto de ingestão de dados utilizando a arquitetura de pipeline ETL (Extract, Transform, Load). O sistema é projetado para extrair dados de arquivos .csv e .json, transformá-los em arquivos Parquet e carregá-los em um banco de dados Postgres. O sistema utiliza Docker para orquestrar o ambiente de banco de dados e SQLTools/DBeaver para gestão de banco de dados.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para o desenvolvimento do pipeline ETL.
- **PostgreSQL**: Banco de dados relacional utilizado para armazenar os dados processados.
- **Docker**: Containerização do ambiente de banco de dados.
- **SQLTools (VSCode) e DBeaver** : Para gerenciar e consultar o banco de dados.
- **Pandas**: Manipulação e transformação de dados.
- **pyarrows**: Manipulação de dados para trabalhar com Parquet
- **requests**: Biblioteca para fazer requisições HTTP em Pyhton

## Como Instalar

1. Clone o repositório:

   ```bash
   git clone https://github.com/Mariana-RDS/etl-pipeline-medallion-architecture.git
   cd etl-pipeline-medallion-architecture
   ```
2. Crie um ambiente virtual para o projeto:

   ```bash
   python3 -m venv .venv
   ```

3. Ative o ambiente virtual:

   ```bash
   source .venv/bin/activate
   ```

4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

5. Conecte-se ao Docker para rodar o Postgres:

   ```bash
   docker compose up -d
   docker compose down #para parar o ambiente do Docker

   ```

6. Abra o VS Code e configure a conexão com o banco de dados usando a extensão SQLTools ou o DBeaver
   - Host: 127.0.0.1
   - Porta: 5432 (ou a porta que você configurou no Docker)
   - Banco: bd_etl
   - Usuário: postgres
   - Senha: postgres

## Como executar

1. Execute os scripts do ETL:

   ```bash
   python3 get_data.py #01-bronze-raw: etapa de extração
   python3 normalize_data.py #02-silver-validated: etapa de tratamento, normalização dos dados
   python3 db.py #conexão com o banco de dados
   python3 populate_db.py #03-gold-enriched: populando o banco com os dados tratados para consumo
   ```