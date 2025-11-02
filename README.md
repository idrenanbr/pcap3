# Mini-CRM com Orientação a Objetos

Sistema de gerenciamento de leads desenvolvido com **Programação Orientada a Objetos (OOP)** em Python.

## 📋 Requisitos do Projeto

- ✅ **Classes, Métodos e Atributos** (obrigatório)
- ✅ **Herança** (opcional)
- ✅ **Polimorfismo** (opcional)

## 🏗️ Arquitetura OOP

### Estrutura de Classes

```
Contact (classe base)
├── Lead (herança)
└── Customer (herança - demonstra polimorfismo)

LeadRepository (gerenciamento de dados)
CRMApp (interface do usuário)
```

## 📦 Componentes Principais

### 1. **models.py** - Modelos de Dados

#### Classe `Contact` (Base)
- **Atributos:** `name`, `company`, `email`, `created`
- **Métodos:**
  - `to_dict()` - Converte para dicionário (polimórfico)
  - `get_display_info()` - Retorna informação formatada (polimórfico)
  - `validate()` - Valida os dados
  - `__str__()` - Representação em string

#### Classe `Lead` (Herda de Contact)
- **Atributos adicionais:** `stage`
- **Métodos:**
  - `to_dict()` - Override para incluir stage
  - `get_display_info()` - Override para incluir stage
  - `update_stage()` - Atualiza estágio do lead
  - `from_dict()` - Factory method (classmethod)
- **Demonstra:** Herança e polimorfismo

#### Classe `Customer` (Herda de Contact)
- **Atributos adicionais:** `total_purchases`
- **Métodos:**
  - `to_dict()` - Override para incluir compras
  - `get_display_info()` - Override para mostrar compras
  - `add_purchase()` - Adiciona valor de compra
- **Demonstra:** Polimorfismo

### 2. **repository.py** - Persistência de Dados

#### Classe `LeadRepository`
- **Atributos:** `data_dir`, `db_path`
- **Métodos:**
  - `create()` - Adiciona novo lead
  - `read_all()` - Lista todos os leads
  - `search()` - Busca leads
  - `export_to_csv()` - Exporta para CSV
  - `update()` - Atualiza lead
  - `delete()` - Remove lead
  - `count()` - Conta leads
  - `_load()` - Método privado para carregar dados
  - `_save()` - Método privado para salvar dados

### 3. **crm_app.py** - Interface do Usuário

#### Classe `CRMApp`
- **Atributos:** `repository`, `running`
- **Métodos:**
  - `run()` - Loop principal
  - `show_menu()` - Exibe menu
  - `handle_option()` - Processa opções
  - `add_lead()` - Adiciona lead
  - `list_leads()` - Lista leads
  - `search_leads()` - Busca leads
  - `export_csv()` - Exporta CSV
  - `show_statistics()` - Mostra estatísticas
  - `exit_app()` - Encerra aplicação

### 4. **main.py** - Ponto de Entrada
- Função `main()` que instancia `CRMApp` e executa

## 🎯 Conceitos de OOP Aplicados

### 1. **Encapsulamento**
- Atributos privados (`_load`, `_save`)
- Métodos públicos bem definidos
- Controle de acesso aos dados

### 2. **Herança**
- `Lead` herda de `Contact`
- `Customer` herda de `Contact`
- Reutilização de código da classe base

### 3. **Polimorfismo**
- Método `to_dict()` sobrescrito em cada subclasse
- Método `get_display_info()` sobrescrito em cada subclasse
- Comportamento diferente para cada tipo de contato

### 4. **Abstração**
- Classes representam entidades do mundo real
- Interfaces simples escondem complexidade

## 🚀 Como Executar

```bash
python main.py
```

## 📊 Funcionalidades

1. **Adicionar Lead** - Cadastra novo lead no sistema
2. **Listar Leads** - Exibe todos os leads cadastrados
3. **Buscar Lead** - Pesquisa por nome, empresa ou email
4. **Exportar CSV** - Exporta leads para arquivo CSV
5. **Estatísticas** - Mostra estatísticas do sistema

## 💾 Persistência de Dados

- **Formato:** JSON
- **Localização:** `data/leads.json`
- **Exportação:** `data/leads.csv`

## 📝 Exemplo de Uso

```python
from models import Lead
from repository import LeadRepository

# Criar um lead
lead = Lead(
    name="João Silva",
    company="Tech Corp",
    email="joao@techcorp.com"
)

# Salvar no repositório
repo = LeadRepository()
repo.create(lead)

# Buscar leads
results = repo.search("Tech")

# Exportar para CSV
repo.export_to_csv()
```

## 🎓 Autor

**PCP - Alexandre Russi**  
Checkpoint 3 - 2º Semestre  
Entrega: 3 de novembro de 2025

## 📄 Licença

Projeto educacional - FIAP
