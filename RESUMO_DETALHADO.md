# 📋 Resumo Detalhado do Projeto CRUD de Clientes

## 🎯 Visão Geral do Projeto

Seu projeto é um **CRUD (Create, Read, Update, Delete) simples para gerenciamento de clientes**, desenvolvido em **Python** com banco de dados **PostgreSQL**. É uma aplicação de linha de comando que permite criar, consultar, alterar e excluir registros de clientes, além de gerar relatórios.

---

## 🔌 Abordagem de Acesso ao Banco de Dados: ODBC vs ORM

### O que você está usando AGORA?

Seu projeto foi **convertido para usar SQLAlchemy ORM** (Object-Relational Mapping):

- **SQLAlchemy**: Framework ORM em Python que mapeia tabelas do banco para classes Python
- **Abordagem:** Você trabalha com objetos Python ao invés de escrever SQL crua
- **Driver:** psycopg2 (mantido como adaptador ODBC subjacente)

### Comparação: ODBC Puro vs SQLAlchemy ORM

#### ODBC Puro (Versão Anterior):
```python
# Inserir
cursor.execute("INSERT INTO clientes (nome, email, celular, cpf, ativo) VALUES (%s, %s, %s, %s, %s)", 
               (nome, email, celular, cpf, True))
connection.commit()

# Buscar
cursor.execute("SELECT * FROM clientes WHERE cod_cliente = %s", (1,))
cliente = cursor.fetchone()

# Atualizar
cursor.execute("UPDATE clientes SET nome = %s WHERE cod_cliente = %s", (novo_nome, 1))
connection.commit()

# Deletar
cursor.execute("DELETE FROM clientes WHERE cod_cliente = %s", (1,))
connection.commit()
```

#### SQLAlchemy ORM (Versão Atual):
```python
# Inserir
novo_cliente = Cliente(nome=nome, email=email, celular=celular, cpf=cpf, ativo=True)
db.add(novo_cliente)
db.commit()

# Buscar
cliente = db.query(Cliente).filter(Cliente.cod_cliente == 1).first()

# Atualizar
cliente.nome = novo_nome
db.commit()

# Deletar
db.delete(cliente)
db.commit()
```

**Vantagens do ORM:**
- ✅ Menos código SQL para escrever
- ✅ Mais seguro contra SQL Injection (automático)
- ✅ Type hints funcionam corretamente
- ✅ Código mais Pythônico e legível
- ✅ Fácil migração entre bancos de dados
- ✅ Melhor manutenibilidade

**Quando usar ODBC puro:**
- ❌ Queries muito complexas (JOIN múltiplos, CTEs, etc)
- ❌ Performance crítica em volumes enormes
- ❌ Operações em lote muito grandes

---

## 🏗️ Arquitetura do Projeto

```
CRUD_Cliente/
├── main.py                 # Orquestrador principal
├── menu.py                 # Interface do menu
├── interfaces.py           # Funções de UI (impressão de dados)
├── validarores.py          # Validações (email, telefone)
├── cadastrar.py            # Operação CREATE
├── exibir_dados.py         # Operação READ (um cliente)
├── alterar_dados.py        # Operação UPDATE
├── excluir.py              # Operação DELETE
├── relatorio.py            # READ (todos os clientes)
├── encerramento.py         # Finalização do programa
├── requirements.txt        # Dependências do projeto
├── banco/                  # Camada de Banco de Dados
│   ├── config.py           # Configuração SQLAlchemy ✨ NOVO
│   ├── models.py           # Modelo ORM do Cliente ✨ NOVO
│   ├── cr_querys.py        # CREATE TABLE query (legado)
│   ├── insr_query.py       # INSERT query (legado)
│   ├── sel_query.py        # SELECT queries (legado)
│   ├── up_query.py         # UPDATE queries (legado)
│   └── del_query.py        # DELETE query (legado)
```

---

## 📊 Fluxo Principal (main.py)

```python
while op_cliente != "0":
    op_cliente = menu.menu_cliente()  # Exibe menu
    
    if op_cliente == "1":  cadastrar.cadastro()      # CREATE
    elif op_cliente == "2": exibir.exibir_cliente()  # READ (um)
    elif op_cliente == "3": alterar.alterar_dados()  # UPDATE
    elif op_cliente == "4": excluir.excluir_cliente()  # DELETE
    elif op_cliente == "5": relatorio.relatorio_clientes()  # READ (todos)
    elif op_cliente == "0": break  # Sair
```

---

## 🗄️ Estrutura do Banco de Dados

Sua tabela `clientes` possui essa estrutura:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `cod_cliente` | SERIAL PRIMARY KEY | ID único, auto-incrementado |
| `nome` | VARCHAR(60) | Nome completo do cliente |
| `email` | VARCHAR(40) | Email do cliente |
| `celular` | VARCHAR(25) | Telefone com DDD |
| `cpf` | VARCHAR(20) | CPF do cliente |
| `ativo` | BOOLEAN | Status ativo/inativo |

---

## ⚙️ Configuração do SQLAlchemy (banco/config.py)

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexão PostgreSQL
DATABASE_URL = "postgresql://postgres:palmeiras123@localhost:5432/clientes"

# Engine: gerencia as conexões com o BD
engine = create_engine(DATABASE_URL)

# SessionLocal: factory para criar sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base: classe base para todos os modelos
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

## 🗂️ Modelo ORM do Cliente (banco/models.py)

```python
from sqlalchemy import Column, Integer, String, Boolean
from banco.config import Base

class Cliente(Base):
    """Mapeamento ORM da tabela clientes"""
    
    __tablename__ = "clientes"
    
    cod_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60), nullable=False)
    email = Column(String(40), nullable=False)
    celular = Column(String(25), nullable=False)
    cpf = Column(String(20), nullable=False)
    ativo = Column(Boolean, default=True)
```

**O que significa:**
- Cada `Column` mapeia para um campo da tabela
- `declarative_base()` permite que o SQLAlchemy crie a tabela automaticamente
- Agora `Cliente` é uma classe Python, não apenas um conceito do BD

---

## 🔐 Conexão com PostgreSQL (Agora com ORM)

Todos os módulos agora usam SessionLocal do config:

```python
from banco.config import SessionLocal
from banco.models import Cliente

db = SessionLocal()
try:
    # Operações com ORM
    novo_cliente = Cliente(nome="João", email="joao@email.com", ...)
    db.add(novo_cliente)
    db.commit()
except Exception as error:
    db.rollback()
    print("Erro:", error)
finally:
    db.close()
```

**Diferenças:**
- ❌ Sem `psycopg2.connect()` explícito
- ✅ SessionLocal gerencia a conexão automaticamente
- ✅ Menos código, mais seguro
- ✅ Rollback automático em erros

---

## 📝 Detalhamento das Operações CRUD

### 1️⃣ CREATE (Cadastrar Cliente)

**Arquivo:** `cadastrar.py`

```
FLUXO:
1. Cria SessionLocal
2. Solicita dados (nome, email, celular, cpf)
3. Valida dados (email, celular com regex)
4. Cria objeto Cliente(...)
5. Adiciona com db.add()
6. Confirma com db.commit()
7. Retorna o ID do novo cliente
```

**Código com ORM:**
```python
novo_cliente = Cliente(
    nome=nome_cliente,
    email=email,
    celular=celular,
    cpf=cpf,
    ativo=True
)
db.add(novo_cliente)
db.commit()
db.refresh(novo_cliente)
print(f"ID inserido: {novo_cliente.cod_cliente}")
```

**Antes (ODBC):**
```python
cursor.execute("""
    INSERT INTO clientes (nome, email, celular, cpf, ativo)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING cod_cliente;
""", (nome_cliente, email, celular, cpf, True))
cod_cliente = cursor.fetchone()[0]
```

---

### 2️⃣ READ (Exibir Dados)

**Arquivo:** `exibir_dados.py`

```
FLUXO:
1. Cria SessionLocal
2. Solicita código do cliente
3. Busca com ORM usando filter()
4. Se existir, exibe em formato tabular
5. Se não existir, mostra "Código Inexistente"
```

**Código com ORM:**
```python
cliente = db.query(Cliente).filter(Cliente.cod_cliente == int(cod_cliente)).first()

if cliente:
    print(f"Nome: {cliente.nome}")
    print(f"Email: {cliente.email}")
else:
    print("Código Inexistente")
```

**Antes (ODBC):**
```python
cursor.execute("SELECT cod_cliente, nome, email, celular, cpf FROM clientes WHERE cod_cliente = %s", (cod_cliente,))
records = cursor.fetchall()
if records:
    row = records[0]
    print(f"Nome: {row[1]}")
    print(f"Email: {row[2]}")
```

---

### 3️⃣ READ ALL (Relatório)

**Arquivo:** `relatorio.py`

```
FLUXO:
1. Cria SessionLocal
2. Busca todos os clientes ordenados por cod_cliente
3. Itera e exibe em tabela formatada com pipes
```

**Código com ORM:**
```python
clientes = db.query(Cliente).order_by(Cliente.cod_cliente).all()

for cliente in clientes:
    print(f"| {cliente.cod_cliente} | {cliente.nome} | {cliente.email} |")
```

**Antes (ODBC):**
```python
cursor.execute("SELECT * FROM clientes ORDER BY cod_cliente;")
records = cursor.fetchall()
for row in records:
    print(f"| {row[0]} | {row[1]} | {row[2]} |")
```

---

### 4️⃣ UPDATE (Alterar Dados)

**Arquivo:** `alterar_dados.py`

```
FLUXO:
1. Cria SessionLocal
2. Solicita ID do cliente a alterar
3. Solicita novos dados (com validações)
4. Busca o cliente com ORM
5. Modifica os atributos do objeto
6. Confirma com db.commit()
```

**Código com ORM:**
```python
cliente = db.query(Cliente).filter(Cliente.cod_cliente == int(cod_cliente)).first()

if cliente:
    cliente.nome = nome_cliente
    cliente.email = email
    cliente.celular = celular
    cliente.cpf = cpf
    db.commit()
    print(f"Cliente com ID {cod_cliente} atualizado com sucesso")
```

**Antes (ODBC):**
```python
cursor.execute("""
    UPDATE clientes
    SET nome = %s, email = %s, celular = %s, cpf = %s
    WHERE cod_cliente = %s
""", (nome_cliente, email, celular, cpf, cod_cliente))
connection.commit()
```

---

### 5️⃣ DELETE (Excluir Cliente)

**Arquivo:** `excluir.py`

```
FLUXO:
1. Cria SessionLocal
2. Solicita ID do cliente a excluir
3. Busca o cliente com ORM
4. Deleta com db.delete()
5. Confirma com db.commit()
```

**Código com ORM:**
```python
cliente = db.query(Cliente).filter(Cliente.cod_cliente == int(cod_cliente)).first()

if cliente:
    db.delete(cliente)
    db.commit()
    print(f"Cliente com ID {cod_cliente} excluído com sucesso")
```

**Antes (ODBC):**
```python
cursor.execute("DELETE FROM clientes WHERE cod_cliente = %s", (cod_cliente,))
connection.commit()
```

---

## 🎨 Camadas de Apresentação

### menu.py - Menu Principal
```
- Limpa a tela (cls/clear)
- Exibe opções 1-5 e 0
- Retorna a opção escolhida
```

### interfaces.py - Formatação
```
- dados_cliente()      → Cabeçalho da tabela
- cadastrar_dados()    → Cabeçalho do formulário
- exibir_dados()       → Título da busca
- alterar_dados()      → Título da alteração
- excluir_dados()      → Título da exclusão
```

---

## ✅ Validações (validarores.py)

```python
validar_email(email)      # Verifica padrão de email
validar_numero(numero)    # Verifica padrão (XX) XXXXX-XXXX
```

Ambas usam **regex** para validação.

---

## 🔄 Fluxo de Dados - Exemplo Completo (com ORM)

```
main.py
  ↓
menu.py (exibe opções) → usuário escolhe "1"
  ↓
cadastrar.py
  ├→ SessionLocal() cria conexão
  ├→ Solicita: nome, email, celular, cpf
  ├→ validarores.py (valida email e celular)
  ├→ cliente = Cliente(...)
  ├→ db.add(cliente)
  ├→ db.commit()
  ├→ db.refresh() obtém ID
  └→ db.close()
  ↓
Volta ao menu

✨ Vantagem: Sem SQL crua, tudo em Python!
```

---

## 🚀 Resumo Técnico

| Aspecto | Valor |
|--------|-------|
| **Linguagem** | Python 3 |
| **Banco de Dados** | PostgreSQL |
| **Driver ODBC** | psycopg2 (subjacente) |
| **ORM** | SQLAlchemy 2.0.23 ✨ NOVO |
| **Padrão de Acesso** | ORM (não SQL crua) |
| **Session Management** | SessionLocal (automático) |
| **Validações** | Regex (email, telefone) |
| **Tabela Principal** | clientes (6 campos) |
| **Operações CRUD** | Todas implementadas com ORM |
| **Interface** | CLI (Command Line Interface) |
| **Dependências** | psycopg2-binary, SQLAlchemy |

---

## 📌 Pontos Fortes do Projeto

✅ Estrutura organizada com separação de responsabilidades  
✅ Tratamento de exceções em todas as operações  
✅ Validação de entrada com regex  
✅ Uso de ORM para segurança contra SQL Injection  
✅ Modelo ORM centralizado (banco/models.py)  
✅ Configuração centralizada (banco/config.py)  
✅ SessionLocal gerencia conexões automaticamente  
✅ Fechamento apropriado de sessões  
✅ Interface amigável com menus e formatação  
✅ Code é mais Pythônico e legível  

---

## 💡 Oportunidades de Melhoria

💭 Criar camada de repositório (ClienteRepository) para centralizar queries  
💭 Validação com Pydantic para melhor validação de dados  
💭 Usar migrações com Alembic para versionamento do BD  
💭 Adicionar logging ao invés de apenas prints  
💭 Adicionar testes unitários com pytest  
💭 Implementar relacionamentos (ex: Cliente → Pedidos)  
💭 Usar variáveis de ambiente para credenciais (python-dotenv)  
💭 Adicionar autenticação de usuários  
💭 Criar API REST com FastAPI  

---

## 📚 Conclusão

Seu projeto agora é um excelente exemplo educacional de **CRUD com SQLAlchemy ORM**, demonstrando:
- ✨ Conhecimento de Python avançado
- ✨ Integração com PostgreSQL via ORM
- ✨ Boas práticas de tratamento de erros
- ✨ Validação de entrada
- ✨ Organização modular e reutilizável
- ✨ Evolução de ODBC puro para ORM moderno

**Evolução do Projeto:**
```
Versão 1.0: ODBC puro (psycopg2 com SQL crua)
    ↓
Versão 2.0: SQLAlchemy ORM (código mais Pythônico) ✨ ATUAL
    ↓
Versão 3.0: Possível - Com repositório, logging, e testes
    ↓
Versão 4.0: Possível - API REST com FastAPI
```

É uma abordagem profissional e didática, ideal para aprender arquitetura moderna de aplicações Python! 🎓

---

## 📦 Como Usar

1. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

2. **Executar o projeto:**
```bash
python main.py
```

3. **Estrutura de arquivos criados:**
```
✨ banco/config.py    - Configuração SQLAlchemy
✨ banco/models.py    - Modelo ORM Cliente
📄 requirements.txt   - Dependências
```

---

Para mais detalhes sobre a migração ODBC → ORM, veja [ORM_SETUP.md](ORM_SETUP.md).
