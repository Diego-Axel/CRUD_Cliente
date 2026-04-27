# 🎯 Migrando o Projeto CRUD de Clientes para SQLAlchemy ORM

## ✅ O que foi modificado

Seu projeto foi convertido para usar **SQLAlchemy ORM** mantendo toda a funcionalidade, mas com uma abordagem mais Pythônica e menos código SQL crua.

### Arquivos novos criados:

1. **`banco/config.py`** - Configuração do SQLAlchemy
   - Conexão com PostgreSQL
   - SessionLocal factory
   - Base para modelos

2. **`banco/models.py`** - Modelo ORM do Cliente
   - Classe `Cliente` mapeando a tabela `clientes`
   - Definição de colunas e tipos

3. **`requirements.txt`** - Dependências do projeto
   - psycopg2-binary (driver PostgreSQL)
   - SQLAlchemy (ORM)

### Arquivos modificados:

- ✅ `cadastrar.py` - Usa `Cliente()` ao invés de SQL INSERT
- ✅ `exibir_dados.py` - Usa `db.query(Cliente)` ao invés de SQL SELECT
- ✅ `alterar_dados.py` - Modifica atributos do objeto ao invés de SQL UPDATE
- ✅ `excluir.py` - Usa `db.delete()` ao invés de SQL DELETE
- ✅ `relatorio.py` - Usa `db.query(Cliente)` para listar todos

## 📦 Instalação das Dependências

```bash
pip install -r requirements.txt
```

Ou instale manualmente:

```bash
pip install SQLAlchemy==2.0.23
pip install psycopg2-binary==2.9.9
```

## 🚀 Como usar

O uso é **exatamente igual** ao anterior! A interface do usuário não mudou, apenas a forma como acessamos o banco de dados nos bastidores:

```bash
python main.py
```

## 📊 Comparação: ODBC vs ORM

### Antes (ODBC puro com psycopg2):
```python
cursor.execute("INSERT INTO clientes (nome, email, celular, cpf, ativo) VALUES (%s, %s, %s, %s, %s)", 
               (nome, email, celular, cpf, True))
connection.commit()
cod_cliente = cursor.fetchone()[0]
```

### Depois (SQLAlchemy ORM):
```python
novo_cliente = Cliente(nome=nome, email=email, celular=celular, cpf=cpf, ativo=True)
db.add(novo_cliente)
db.commit()
db.refresh(novo_cliente)
cod_cliente = novo_cliente.cod_cliente
```

## 🎯 Vantagens da abordagem ORM

✨ **Menos SQL, mais Python**
```python
# Buscar cliente
cliente = db.query(Cliente).filter(Cliente.cod_cliente == 1).first()

# Atualizar
cliente.nome = "Novo Nome"
db.commit()

# Deletar
db.delete(cliente)
db.commit()
```

✨ **Type hints naturais**
```python
cliente.cod_cliente  # IDE sabe que é int
cliente.email        # IDE sabe que é str
```

✨ **Menos vulnerável a SQL Injection**
- O ORM trata automaticamente a parameterização

✨ **Migração de BD mais fácil**
- Se precisar mudar de PostgreSQL para MySQL/SQLite, é só mudar a URL

## 🔄 Estrutura de Diretórios Atualizada

```
CRUD_Cliente/
├── main.py
├── menu.py
├── interfaces.py
├── validarores.py
├── cadastrar.py          ✨ Refatorado para ORM
├── exibir_dados.py       ✨ Refatorado para ORM
├── alterar_dados.py      ✨ Refatorado para ORM
├── excluir.py            ✨ Refatorado para ORM
├── relatorio.py          ✨ Refatorado para ORM
├── encerramento.py
├── requirements.txt      ✨ Novo
├── banco/
│   ├── config.py         ✨ Novo - Configuração SQLAlchemy
│   ├── models.py         ✨ Novo - Modelo ORM Cliente
│   ├── cr_querys.py      ⚠️ Pode ser deletado (legado)
│   ├── insr_query.py     ⚠️ Pode ser deletado (legado)
│   ├── sel_query.py      ⚠️ Pode ser deletado (legado)
│   ├── up_query.py       ⚠️ Pode ser deletado (legado)
│   └── del_query.py      ⚠️ Pode ser deletado (legado)
```

## ⚠️ Arquivos Legados (podem ser deletados)

Os arquivos antigos de queries ainda existem, mas **não são mais usados**:
- `banco/cr_querys.py`
- `banco/insr_query.py`
- `banco/sel_query.py`
- `banco/up_query.py`
- `banco/del_query.py`

Se quiser manter o projeto limpo, você pode deletá-los.

## 🎓 Próximas Melhorias Possíveis

1. **Criar repositório** (`ClienteRepository`) para centralizar queries
2. **Validação com Pydantic** para melhor validação de dados
3. **Usar migrações com Alembic** para versionamento do BD
4. **Adicionar logging** ao invés de apenas print()
5. **Criar testes unitários** com pytest
6. **Implementar relacionamentos** (ex: Cliente → Pedidos)

## ❓ Dúvidas Frequentes

**P: Posso misturar ODBC e ORM?**
R: Sim! Ambos funcionam, mas não é recomendado. Use um ou outro para evitar confusão.

**P: Os dados antigos vão funcionar?**
R: Sim! Sua tabela existente será usada normalmente, apenas a forma de acessar mudou.

**P: E se eu quiser voltar ao ODBC puro?**
R: É fácil - basta reverter os arquivos para as versões anteriores. Mas ORM é melhor! 😉

---

🎉 **Seu projeto está agora moderno com SQLAlchemy ORM!**
