
---
<img src="https://github.com/user-attachments/assets/6279cd0c-d692-4c5e-bd89-b6d2d5d230f0" alt="Captura de Tela" width="200">

Estou realizando o estudo do SQLAlchemy para que seja mais uma ferramenta a ser usada em prol da educação básica, pois o objetivo é captar o máximo de dados possíveis do universo da sala de aula.

---
---

# 📚 **Estudos sobre SQLAlchemy**

![sqlalchemy-img](https://github.com/user-attachments/assets/de60eb02-425b-4df9-8de8-6d52d431ca76)


Este repositório contém exemplos e explicações práticas sobre o uso do **SQLAlchemy**, uma biblioteca Python poderosa para trabalhar com bancos de dados relacionais. Os estudos incluem desde os conceitos básicos até o uso avançado do ORM (Object Relational Mapping).

---

## 🔖 **Roteiro de Estudos**

### 1️⃣ **Conceitos Básicos do SQLAlchemy**  
✅ **Core vs. ORM**: Diferenças entre as duas abordagens principais do SQLAlchemy.  
✅ **Instalação**: Como instalar a biblioteca.  
✅ **Engine**: Configuração e criação do mecanismo de conexão.  
✅ **Pools**: Gerenciamento de conexões com o banco de dados.  
✅ **Dialetos**: Como o SQLAlchemy suporta diferentes bancos de dados.  

### 2️⃣ **Conexões e Transações**  
🔗 Como se conectar ao banco de dados utilizando a **Engine**.  
♻️ Gerenciamento de transações com `commit`, `rollback` e `savepoints`.  

### 3️⃣ **Schemas e Tipos**  
🛠️ Definição de **metadados** (tabelas e colunas).  
📋 Uso de tipos de dados suportados pelo SQLAlchemy.  
📦 Criação e manipulação de tabelas no banco de dados.  

### 4️⃣ **Query Builder**  
🔍 Construção de consultas SQL de forma programática.  
⚙️ Uso de operadores (`select`, `where`, `join`, etc.).  
📊 Execução e manipulação de resultados.  

### 5️⃣ **ORM (Object Relational Mapping)**  
🏗️ Diferenças entre os modelos **declarativos** e **imperativos**.  
🌀 Configuração de **Session** para gerenciamento de objetos.  
🤝 Criação de relacionamentos entre objetos, como **One-to-Many** e **Many-to-Many**.  

---

## 🗂️ **Estrutura do Repositório**

A estrutura do repositório está organizada em subpastas, cada uma correspondendo a uma etapa do roteiro de estudos:

```
/sqlalchemy-studies
├── 1-conceitos-basicos       // Exemplos básicos de Core vs. ORM, Engine, Pools e Dialetos
├── 2-conexoes-transacoes     // Conexões com o banco e controle de transações
├── 3-schemas-tipos           // Definição de tabelas e tipos de dados
├── 4-query-builder           // Exemplos de consultas complexas utilizando o Core
├── 5-orm                     // Estudo detalhado do ORM com modelos e relacionamentos
```

---

## 🚀 **Como Executar os Exemplos**

### **Pré-Requisitos**  
🟢 **Python 3.8+**  
🟢 Um banco de dados suportado pelo SQLAlchemy (como SQLite, MySQL ou PostgreSQL).  
🟢 Instale o SQLAlchemy com:  
```bash
pip install sqlalchemy
```

---

## ✨ **Exemplos**

### 🔗 **Conectando-se ao Banco de Dados**
```python
from sqlalchemy import create_engine

# Conectar ao banco SQLite (dialeto usado como exemplo)
engine = create_engine("sqlite:///meu_banco.db", echo=True)
connection = engine.connect()

# Fechar a conexão
connection.close()
```

---

### 🛠️ **Criando uma Tabela**
```python
from sqlalchemy import MetaData, Table, Column, Integer, String

# Metadados e definição da tabela
metadata = MetaData()
users_table = Table(
    "users", 
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("email", String, unique=True)
)

# Criar a tabela no banco
metadata.create_all(engine)
```

---

### 🌐 **Usando o ORM**
```python
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

# Base declarativa para o ORM
Base = declarative_base()

# Modelo da tabela
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)

# Criar a tabela no banco
Base.metadata.create_all(engine)

# Criar uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Adicionar um novo usuário
new_user = User(name="João Silva", email="joao@example.com")
session.add(new_user)
session.commit()
```

---

## 📚 **Referências**

- 🌐 [Documentação Oficial do SQLAlchemy](https://docs.sqlalchemy.org/)  
- 🔗 [Exemplos no GitHub](https://github.com/sqlalchemy/sqlalchemy)  

---

---
## Recursos Úteis

- <a href="https://www.youtube.com/watch?v=t4C1c62Z4Ag&t=4076s&ab_channel=EduardoMendes">
  <img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" alt="YouTube Logo" style="width:20px; vertical-align:middle;"> Curso de SQLAlchemy por Eduardo Mendes (Dunossauro)
</a>

> Esse é um curso introdutório ao SQLAlchemy, ministrado por Eduardo Mendes, também conhecido como Dunossauro. Ele aborda conceitos fundamentais e exemplos práticos.

---

## 🎨 **Visualizações**


![image](https://github.com/user-attachments/assets/e0da3040-97f4-4692-86a3-5b97ebdd8157)


---
