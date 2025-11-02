# 📘 Explicação Detalhada: repository.py

## 🎯 Visão Geral

O arquivo `repository.py` implementa o **padrão Repository** para gerenciar a persistência de dados. É responsável por salvar e carregar leads do arquivo JSON.

---

## 📚 Conceitos OOP Demonstrados

### ✅ 1. ENCAPSULAMENTO (métodos privados)
### ✅ 2. SEPARAÇÃO DE RESPONSABILIDADES
### ✅ 3. ABSTRAÇÃO
### ✅ 4. PADRÃO REPOSITORY

---

## 🏗️ O que é o Padrão Repository?

**Repository Pattern** = Padrão que centraliza o acesso aos dados.

### Vantagens:
- ✅ Abstrai como os dados são salvos (JSON, banco, etc)
- ✅ Interface simples: create, read, update, delete (CRUD)
- ✅ Facilita mudanças futuras (trocar JSON por PostgreSQL)
- ✅ Separa persistência da lógica de negócio

### Analogia:
Repository é como um **bibliotecário**:
- Você pede um livro (lead)
- Não precisa saber onde/como ele está guardado
- O bibliotecário cuida disso (métodos `_load`, `_save`)

---

## 📖 Classe: LeadRepository

### Responsabilidade:
Gerenciar APENAS a persistência de leads (salvar/carregar arquivo JSON).

### Atributos:
- `data_dir` (Path) - Caminho do diretório de dados
- `db_path` (Path) - Caminho do arquivo JSON

---

## 🔧 Métodos

### `__init__(self, data_dir="data")`
Construtor - configura caminhos e cria diretório.

```python
# Constrói caminho completo do diretório
# __file__ = caminho de repository.py
# .resolve() = caminho absoluto
# .parent = diretório pai
# / data_dir = adiciona "data"
self.data_dir = Path(__file__).resolve().parent / data_dir

# Cria diretório se não existir
self.data_dir.mkdir(exist_ok=True)

# Define caminho do arquivo JSON
self.db_path = self.data_dir / "leads.json"
```

**Resultado:** `/caminho/do/projeto/data/leads.json`

---

### `_load(self) -> List[dict]` 🔒 PRIVADO

**Método PRIVADO** - indicado pelo prefixo `_`

#### O que faz?
Carrega leads do arquivo JSON.

#### Por que privado?
- **ENCAPSULAMENTO**: Detalhe de implementação
- Outras classes não precisam saber COMO os dados são carregados
- Apenas métodos públicos da classe devem usar

```python
def _load(self) -> List[dict]:
    # 1. Verifica se arquivo existe
    if not self.db_path.exists():
        return []  # Retorna lista vazia se não existe
    
    # 2. Tenta carregar JSON
    try:
        return json.loads(self.db_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []  # Retorna lista vazia se JSON corrompido
```

**Tratamento de erros:**
- Arquivo não existe → `[]`
- JSON inválido → `[]`
- **Nunca quebra o sistema!**

---

### `_save(self, leads: List[dict]) -> None` 🔒 PRIVADO

**Método PRIVADO**

#### O que faz?
Salva lista de leads no arquivo JSON.

```python
def _save(self, leads: List[dict]) -> None:
    self.db_path.write_text(
        json.dumps(leads, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
```

**Parâmetros do JSON:**
- `ensure_ascii=False` → Permite acentos (á, ç, ã)
- `indent=2` → Formata com indentação (JSON legível)
- `encoding="utf-8"` → Suporta caracteres especiais

---

### `create(self, lead: Lead) -> None` 🌍 PÚBLICO

**CRUD: CREATE**

#### O que faz?
Adiciona novo lead ao repositório.

```python
def create(self, lead: Lead) -> None:
    leads = self._load()           # 1. Carrega leads existentes
    leads.append(lead.to_dict())   # 2. Adiciona novo (como dicionário)
    self._save(leads)              # 3. Salva tudo de volta
```

**Fluxo:**
1. Lê arquivo JSON
2. Converte Lead em dicionário (polimorfismo!)
3. Adiciona à lista
4. Salva arquivo atualizado

---

### `read_all(self) -> List[Lead]` 🌍 PÚBLICO

**CRUD: READ**

#### O que faz?
Retorna todos os leads como **objetos Lead** (não dicionários).

```python
def read_all(self) -> List[Lead]:
    data = self._load()  # 1. Carrega dicionários
    return [Lead.from_dict(item) for item in data]  # 2. Converte em objetos
```

**Por que retornar objetos?**
- Objetos têm **métodos** (`validate()`, `update_stage()`)
- Dicionários são apenas dados
- Objetos são mais fáceis de trabalhar em OOP

**List Comprehension:**
```python
# Equivalente a:
result = []
for item in data:
    result.append(Lead.from_dict(item))
return result
```

---

### `search(self, query: str) -> List[tuple[int, Lead]]` 🌍 PÚBLICO

#### O que faz?
Busca leads por nome, empresa ou email.

#### Retorno:
Lista de **tuplas** `(índice, lead)`:
- `índice` → Posição na lista (útil para editar/deletar)
- `lead` → Objeto Lead encontrado

```python
def search(self, query: str) -> List[tuple[int, Lead]]:
    leads = self.read_all()
    results = []
    query_lower = query.lower()  # Case-insensitive
    
    for index, lead in enumerate(leads):
        # Concatena nome + empresa + email
        search_text = f"{lead.name} {lead.company} {lead.email}".lower()
        
        # Verifica se query está contido no texto
        if query_lower in search_text:
            results.append((index, lead))
    
    return results
```

**Algoritmo:**
- Busca linear simples O(n)
- Case-insensitive (ignora maiúsculas)
- Busca em nome, empresa e email

**Exemplo:**
```python
results = repo.search("João")
# Retorna: [(0, Lead("João Silva", ...)), (5, Lead("João Pedro", ...))]
```

---

### `export_to_csv(self, path=None) -> Optional[Path]` 🌍 PÚBLICO

#### O que faz?
Exporta leads para arquivo CSV (planilha).

```python
def export_to_csv(self, path: Optional[str] = None) -> Optional[Path]:
    # 1. Define caminho (usa path fornecido ou padrão data/leads.csv)
    csv_path = Path(path) if path else (self.data_dir / "leads.csv")
    
    # 2. Carrega dados
    leads_data = self._load()
    
    # 3. Escreve CSV
    try:
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            if leads_data:
                fieldnames = ["name", "company", "email", "stage", "created"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()  # Cabeçalho
                for row in leads_data:
                    writer.writerow(row)  # Cada lead
        return csv_path  # Sucesso
    except PermissionError:
        return None  # Erro (arquivo aberto em outro programa)
```

**Resultado CSV:**
```csv
name,company,email,stage,created
João Silva,Empresa X,joao@x.com,novo,2025-10-27
Maria Santos,Corp Y,maria@y.com,contatado,2025-10-27
```

---

### `update(self, index: int, lead: Lead) -> bool` 🌍 PÚBLICO

**CRUD: UPDATE**

#### O que faz?
Atualiza lead específico pela posição.

```python
def update(self, index: int, lead: Lead) -> bool:
    leads = self._load()
    
    # Valida se índice existe
    if 0 <= index < len(leads):
        leads[index] = lead.to_dict()  # Substitui
        self._save(leads)
        return True  # Sucesso
    
    return False  # Índice inválido
```

**Uso:**
```python
lead = Lead("João Silva", "X", "joao@x.com", "convertido")
sucesso = repo.update(0, lead)  # Atualiza lead na posição 0
```

---

### `delete(self, index: int) -> bool` 🌍 PÚBLICO

**CRUD: DELETE**

#### O que faz?
Remove lead específico pela posição.

```python
def delete(self, index: int) -> bool:
    leads = self._load()
    
    if 0 <= index < len(leads):
        leads.pop(index)  # Remove da posição
        self._save(leads)
        return True
    
    return False
```

---

### `count(self) -> int` 🌍 PÚBLICO

#### O que faz?
Retorna número total de leads.

```python
def count(self) -> int:
    return len(self._load())
```

**Simples e direto!**

---

## 🎓 Conceitos OOP em Ação

### 1. **ENCAPSULAMENTO** 🔒

```
MÉTODOS PRIVADOS (internos):
├── _load()  → Carrega JSON
└── _save()  → Salva JSON

MÉTODOS PÚBLICOS (interface):
├── create()
├── read_all()
├── search()
├── update()
├── delete()
└── count()
```

**Vantagem:**
- Outras classes não precisam saber COMO os dados são salvos
- Pode mudar de JSON para PostgreSQL alterando apenas `_load` e `_save`
- Interface pública permanece a mesma!

---

### 2. **SEPARAÇÃO DE RESPONSABILIDADES**

**LeadRepository:**
- ✅ SÓ cuida de persistência
- ❌ NÃO sabe de interface do usuário
- ❌ NÃO sabe de regras de negócio

**CRMApp:**
- ✅ SÓ cuida de interface
- ❌ NÃO sabe como dados são salvos

**Lead:**
- ✅ SÓ representa um lead
- ❌ NÃO sabe como é salvo

---

### 3. **ABSTRAÇÃO**

**Interface simples:**
```python
repo = LeadRepository()
repo.create(lead)        # Adiciona
leads = repo.read_all()  # Lista
repo.delete(0)           # Remove
```

**Complexidade escondida:**
- Leitura/escrita de arquivo
- Conversão JSON
- Tratamento de erros
- Validação de índices

---

## 💡 Perguntas Frequentes

### Por que usar métodos privados (_load, _save)?
**Resposta:** ENCAPSULAMENTO. São detalhes de implementação que outras classes não precisam conhecer. Se mudarmos de JSON para banco de dados, apenas esses métodos mudam.

### Por que read_all() retorna objetos Lead?
**Resposta:** Objetos têm métodos (validate, update_stage). Dicionários são só dados. Objetos são mais úteis em OOP.

### O que acontece se o JSON estiver corrompido?
**Resposta:** `_load()` captura a exceção e retorna lista vazia `[]`. O sistema continua funcionando.

---

## 🚀 Próximo Passo

Leia: **`crm_app_explicado.md`** para entender a interface e composição!
