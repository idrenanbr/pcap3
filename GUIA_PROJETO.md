# 📚 Guia Completo do Projeto Mini-CRM

## 📁 O que cada arquivo faz?

### 🔵 **Arquivos Principais (Código Python)**

#### 1. `models.py` - MODELOS DE DADOS
**O que faz:** Define as classes dos objetos (Contact, Lead, Customer)

**Conceitos OOP demonstrados:**
- ✅ **Herança**: Lead e Customer herdam de Contact
- ✅ **Polimorfismo**: Métodos sobrescritos
- ✅ **Atributos**: name, company, email, stage, created

**Como verificar:**
```python
# Execute no terminal:
python -c "from models import Contact, Lead, Customer; print('✅ Classes funcionam!')"
```

---

#### 2. `repository.py` - GERENCIAMENTO DE DADOS
**O que faz:** Salva e carrega leads do arquivo JSON

**Conceitos OOP demonstrados:**
- ✅ **Encapsulamento**: Métodos privados _load() e _save()
- ✅ **Métodos**: create(), read_all(), search(), export_to_csv()
- ✅ **Atributos**: data_dir, db_path

**Como verificar:**
```python
# Execute no terminal:
python -c "from repository import LeadRepository; repo = LeadRepository(); print(f'✅ Repositório OK - Total leads: {repo.count()}')"
```

---

#### 3. `crm_app.py` - INTERFACE DO USUÁRIO
**O que faz:** Controla o menu e interações com o usuário

**Conceitos OOP demonstrados:**
- ✅ **Classe**: CRMApp
- ✅ **Métodos**: run(), add_lead(), list_leads(), search_leads()
- ✅ **Composição**: Usa LeadRepository internamente

**Como verificar:**
Quando você roda `python main.py`, este arquivo é executado!

---

#### 4. `main.py` - PONTO DE ENTRADA
**O que faz:** Inicia o programa (arquivo principal)

**Conteúdo:**
```python
from crm_app import CRMApp

def main():
    app = CRMApp()
    app.run()

if __name__ == "__main__":
    main()
```

**Como verificar:**
```bash
python main.py
# Deve mostrar o menu do CRM
```

---

### 📘 **Arquivos de Documentação**

#### 5. `README.md` - DOCUMENTAÇÃO DO PROJETO
**O que faz:** Explica o projeto para quem ver no GitHub

**Conteúdo:**
- Descrição do sistema
- Arquitetura OOP
- Como usar
- Conceitos demonstrados

**Como verificar:**
- Abra o arquivo e veja se está bem escrito
- É o primeiro arquivo que aparece no GitHub

---

#### 6. `GITHUB.md` - GUIA DE PUBLICAÇÃO
**O que faz:** Ensina como publicar no GitHub passo a passo

**Conteúdo:**
- Como criar repositório
- Como fazer push do código
- Como entregar no Canvas

**Como verificar:**
- Siga os passos deste arquivo para publicar

---

#### 7. `replit.md` - MEMÓRIA DO PROJETO
**O que faz:** Armazena informações técnicas e decisões do projeto

**Para:** Uso interno do Replit
**Não precisa:** Entregar no GitHub (mas pode deixar)

---

### 📂 **Pasta de Dados**

#### 8. `data/leads.json` - BANCO DE DADOS
**O que faz:** Armazena os leads em formato JSON

**Como verificar:**
```bash
cat data/leads.json
# Mostra os leads cadastrados
```

---

#### 9. `data/leads.csv` - EXPORTAÇÃO
**O que faz:** Arquivo CSV gerado quando você exporta

**Como verificar:**
- Use a opção [4] no menu
- Abre o arquivo no Excel ou editor

---

## ✅ Como Verificar se Está Tudo Correto?

### 🔍 **Teste 1: Verificar Classes OOP**

```bash
python -c "
from models import Contact, Lead, Customer
from repository import LeadRepository
from crm_app import CRMApp

print('✅ Contact (classe base)')
print('✅ Lead (herda de Contact)')
print('✅ Customer (herda de Contact)')
print('✅ LeadRepository')
print('✅ CRMApp')
print('\n🎉 Todas as classes foram criadas!')
"
```

---

### 🔍 **Teste 2: Testar Herança**

```bash
python -c "
from models import Lead, Customer

lead = Lead('João', 'Empresa X', 'joao@email.com')
customer = Customer('Maria', 'Empresa Y', 'maria@email.com', 1500.00)

print(f'Lead: {lead.name} - Stage: {lead.stage}')
print(f'Customer: {customer.name} - Compras: R$ {customer.total_purchases}')
print('\n✅ Herança funciona!')
"
```

---

### 🔍 **Teste 3: Testar Polimorfismo**

```bash
python -c "
from models import Lead, Customer

lead = Lead('João', 'Tech', 'joao@tech.com')
customer = Customer('Maria', 'Corp', 'maria@corp.com', 2000.00)

print('Método to_dict() com polimorfismo:')
print(f'Lead: {lead.to_dict()}')
print(f'Customer: {customer.to_dict()}')
print('\n✅ Polimorfismo funciona!')
"
```

---

### 🔍 **Teste 4: Usar o Sistema Completo**

```bash
python main.py
```

**Teste as opções:**
1. ✅ [1] Adicionar Lead - Cadastre um lead
2. ✅ [2] Listar Leads - Veja os leads
3. ✅ [3] Buscar Lead - Busque por nome
4. ✅ [4] Exportar CSV - Gere o CSV
5. ✅ [5] Estatísticas - Veja estatísticas
6. ✅ [0] Sair - Encerre

---

## 🎯 Checklist Final

Antes de entregar, verifique:

### Código OOP
- [ ] `models.py` existe e tem 3 classes (Contact, Lead, Customer)
- [ ] `repository.py` existe e tem LeadRepository
- [ ] `crm_app.py` existe e tem CRMApp
- [ ] `main.py` existe e inicia o sistema

### Conceitos OOP
- [ ] **Herança**: Lead e Customer herdam de Contact ✅
- [ ] **Polimorfismo**: Métodos to_dict() sobrescritos ✅
- [ ] **Encapsulamento**: Métodos privados _load() e _save() ✅
- [ ] **Classes e Atributos**: Todas as classes têm atributos ✅

### Funcionalidades
- [ ] Sistema roda sem erros
- [ ] Consegue adicionar leads
- [ ] Consegue listar leads
- [ ] Consegue buscar leads
- [ ] Consegue exportar CSV

### Documentação
- [ ] README.md está completo
- [ ] Código tem comentários

### GitHub
- [ ] Código publicado no GitHub
- [ ] Repositório é PÚBLICO
- [ ] Link copiado para entregar

---

## 🚀 Resumo Visual

```
┌─────────────────────────────────────────────┐
│         Mini-CRM (Projeto Completo)         │
└─────────────────────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
    MODELOS     REPOSITÓRIO    INTERFACE
   (models.py) (repository.py) (crm_app.py)
        │            │            │
        │            │            │
    Contact      LeadRepo      CRMApp
    ├─ Lead         │            │
    └─ Customer     │            │
                    │            │
        └───────────┴────────────┘
                    │
                    ▼
                main.py
             (Inicia tudo)
```

---

## 🎓 Entrega no Canvas

**Último passo:** Publique no GitHub e entregue APENAS o link!

**Exemplo de link correto:**
```
https://github.com/seu-usuario/mini-crm-oop
```

**BOA SORTE! 🚀**
