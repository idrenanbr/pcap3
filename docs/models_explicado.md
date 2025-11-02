# 📘 Explicação Detalhada: models.py

## 🎯 Visão Geral

O arquivo `models.py` define as **classes de domínio** do sistema: `Contact`, `Lead` e `Customer`. Este é o coração da demonstração de OOP, mostrando **herança** e **polimorfismo** em ação.

---

## 📚 Conceitos OOP Demonstrados

### ✅ 1. CLASSES E OBJETOS
### ✅ 2. HERANÇA
### ✅ 3. POLIMORFISMO
### ✅ 4. ATRIBUTOS (instância e classe)
### ✅ 5. MÉTODOS (instância, classe, especiais)

---

## 🏗️ Estrutura de Classes

```
Contact (classe base)
├── Lead (herda de Contact)
└── Customer (herda de Contact)
```

---

## 📖 Classe: Contact (Base)

### O que é?
Classe **PAI** que representa qualquer contato no sistema. Lead e Customer herdam dela.

### Atributos:
- `name` (str) - Nome do contato
- `company` (str) - Empresa do contato
- `email` (str) - E-mail do contato
- `created` (str) - Data de criação (formato ISO: "2025-10-27")

### Métodos:

#### `__init__(self, name, company, email, created=None)`
**Construtor** - Inicializa os atributos do objeto.

```python
# O que acontece:
self.name = name        # Armazena o nome
self.company = company  # Armazena a empresa
self.email = email      # Armazena o email
self.created = created or date.today().isoformat()  # Data de hoje se não fornecida
```

**Por que `self.`?**
- `self` representa o próprio objeto
- `self.name` é um atributo do objeto (não uma variável local)
- Permite acessar o valor depois: `contact.name`

---

#### `to_dict(self) -> dict`
Converte o objeto Contact em dicionário (para salvar em JSON).

**Conceito OOP:** Este método será **SOBRESCRITO** (override) nas classes filhas!

```python
# Retorna:
{
    "name": "João Silva",
    "company": "Empresa X",
    "email": "joao@email.com",
    "created": "2025-10-27"
}
```

**Por que importante?**
- Lead sobrescreve para adicionar `"stage"`
- Customer sobrescreve para adicionar `"total_purchases"`
- Isso é **POLIMORFISMO**!

---

#### `get_display_info(self) -> str`
Retorna string formatada para exibição.

**Conceito OOP:** Também será sobrescrito (override) nas classes filhas!

```python
# Retorna: "João Silva | Empresa X | joao@email.com"
```

**Polimorfismo:**
- Lead adiciona o `stage` ao final
- Customer adiciona `R$ valor` ao final
- Mesmo método, comportamentos diferentes!

---

#### `validate(self) -> bool`
Valida se os dados do contato são válidos.

**Regras:**
1. Nome não pode estar vazio
2. E-mail não pode estar vazio
3. E-mail deve conter "@"

```python
# Retorna True se válido, False se inválido
return bool(self.name and self.email and "@" in self.email)
```

---

#### `__str__(self) -> str`
**Método especial** - chamado quando fazemos `print(contact)` ou `str(contact)`.

```python
# Reutiliza get_display_info() para evitar duplicação
return self.get_display_info()
```

**Por que usar?**
- Facilita debug: `print(lead)` mostra info legível
- Sem isso, mostraria: `<models.Lead object at 0x...>`

---

## 📖 Classe: Lead (Herda de Contact)

### O que é?
Lead **é um** Contact que está no processo de vendas. Tem tudo que Contact tem, **MAIS** o estágio (stage).

### Herança:
```python
class Lead(Contact):  # Lead herda de Contact
```

**Relação:** Lead "é um" Contact (is-a relationship)

### Atributos Extras:
- `stage` (str) - Estágio do lead no funil de vendas

### Atributo de Classe:
```python
STAGES = ["novo", "contatado", "qualificado", "convertido", "perdido"]
```

**O que é atributo de classe?**
- Compartilhado por TODOS os objetos Lead
- Acesso: `Lead.STAGES` ou `self.STAGES`
- Define valores válidos para stage

---

### Métodos:

#### `__init__(self, name, company, email, stage="novo", created=None)`
Construtor - inicializa Lead.

```python
# 1. Chama o construtor do PAI (Contact)
super().__init__(name, company, email, created)
# Isso inicializa: name, company, email, created

# 2. Adiciona o atributo específico de Lead
self.stage = stage if stage in self.STAGES else "novo"
# Valida se stage é válido, senão usa "novo"
```

**O que é `super()`?**
- `super()` retorna referência à classe PAI
- `super().__init__(...)` chama o `__init__` de Contact
- **Reutilização de código** através de herança!

**Por que fazer assim?**
- Evita duplicar código (name, company, email já são tratados em Contact)
- Mantém a lógica centralizada
- Facilita manutenção

---

#### `to_dict(self) -> dict` ⭐ POLIMORFISMO
**SOBRESCREVE** (override) o método de Contact.

```python
def to_dict(self) -> dict:
    # 1. Chama to_dict() do PAI
    data = super().to_dict()  # Retorna: {"name": ..., "company": ..., ...}
    
    # 2. Adiciona campo específico de Lead
    data["stage"] = self.stage
    
    # 3. Retorna dicionário completo
    return data
```

**Resultado:**
```python
{
    "name": "João",
    "company": "X",
    "email": "joao@x.com",
    "created": "2025-10-27",
    "stage": "novo"  # ← Campo extra!
}
```

**Conceito OOP: POLIMORFISMO**
- Mesmo nome de método (`to_dict`)
- Comportamento DIFERENTE (adiciona `stage`)
- Customer também sobrescreve, mas adiciona `total_purchases`

---

#### `get_display_info(self) -> str` ⭐ POLIMORFISMO
**SOBRESCREVE** o método de Contact.

```python
# Formata com colunas de largura fixa + stage
return f"{self.name:<20} | {self.company:<17} | {self.email:<21} | {self.stage}"
```

**Resultado:**
```
João Silva           | Empresa X         | joao@email.com        | novo
```

**Polimorfismo:**
- Contact mostra: nome | empresa | email
- Lead mostra: nome | empresa | email | **stage**
- Customer mostra: nome | empresa | email | **R$ valor**

---

#### `update_stage(self, new_stage: str) -> bool`
Atualiza o estágio do lead (método específico de Lead).

```python
if new_stage in self.STAGES:  # Valida se é válido
    self.stage = new_stage
    return True
return False
```

**Por que validar?**
- Garante que apenas valores válidos sejam aceitos
- Evita erros de digitação
- Mantém consistência dos dados

---

#### `from_dict(cls, data: dict) -> Lead` (classmethod)
**Factory Method** - cria Lead a partir de dicionário.

```python
@classmethod  # Recebe cls (classe) ao invés de self (instância)
def from_dict(cls, data: dict) -> 'Lead':
    return cls(  # cls() = Lead() - chama o construtor
        name=data.get("name", ""),
        company=data.get("company", ""),
        email=data.get("email", ""),
        stage=data.get("stage", "novo"),
        created=data.get("created")
    )
```

**Uso:**
```python
data = {"name": "João", "email": "joao@x.com", "stage": "novo"}
lead = Lead.from_dict(data)  # Cria Lead a partir do dicionário
```

**Por que usar @classmethod?**
- Alternativa ao construtor normal
- Útil para criar objetos a partir de dados do banco/JSON
- `cls` permite que subclasses também funcionem

---

## 📖 Classe: Customer (Herda de Contact)

### O que é?
Customer **é um** Contact que já é cliente (comprou algo). Demonstra polimorfismo de forma diferente de Lead.

### Por que existe?
**Demonstração educacional!** Mostra que:
- Várias classes podem herdar da mesma classe pai
- Cada uma pode sobrescrever métodos de formas diferentes
- Isso é **POLIMORFISMO**!

### Atributos Extras:
- `total_purchases` (float) - Total de compras do cliente

---

### Métodos:

#### `__init__(self, name, company, email, total_purchases=0.0, created=None)`
```python
super().__init__(name, company, email, created)  # Chama Contact.__init__
self.total_purchases = total_purchases  # Atributo específico
```

---

#### `to_dict(self) -> dict` ⭐ POLIMORFISMO
**SOBRESCREVE** de forma DIFERENTE de Lead!

```python
def to_dict(self) -> dict:
    data = super().to_dict()
    data["total_purchases"] = self.total_purchases  # ← Diferente de Lead!
    return data
```

**Comparação:**
- Lead adiciona: `"stage"`
- Customer adiciona: `"total_purchases"`
- **Mesmo método, dados diferentes = POLIMORFISMO!**

---

#### `get_display_info(self) -> str` ⭐ POLIMORFISMO
```python
return f"{self.name:<20} | {self.company:<17} | {self.email:<21} | R$ {self.total_purchases:.2f}"
```

**Resultado:**
```
Maria Santos         | Corp Y            | maria@y.com           | R$ 1500.50
```

---

#### `add_purchase(self, amount: float) -> None`
Adiciona valor ao total de compras.

```python
self.total_purchases += amount  # Equivalente a: self.total_purchases = self.total_purchases + amount
```

---

## 🎓 Resumo dos Conceitos OOP

### 1. **HERANÇA**
```
Contact (PAI)
├── Lead (FILHO) - herda tudo de Contact + adiciona stage
└── Customer (FILHO) - herda tudo de Contact + adiciona total_purchases
```

**Vantagem:** Reutilização de código usando `super()`

---

### 2. **POLIMORFISMO**

| Método | Contact | Lead | Customer |
|--------|---------|------|----------|
| `to_dict()` | 4 campos | 5 campos (+ stage) | 5 campos (+ total_purchases) |
| `get_display_info()` | 3 colunas | 4 colunas (+ stage) | 4 colunas (+ valor) |

**Mesmo método, comportamentos DIFERENTES!**

---

### 3. **ENCAPSULAMENTO**
- Atributos agrupados na classe
- Métodos operam sobre os atributos
- Validação centralizada (`validate()`)

---

### 4. **ABSTRAÇÃO**
- Classes representam conceitos reais (Contato, Lead, Cliente)
- Interface simples esconde complexidade

---

## 💡 Perguntas Frequentes

### Por que Customer não é usado no sistema?
**Resposta:** É apenas para **demonstração de polimorfismo**. Mostra que várias classes podem herdar da mesma classe pai e sobrescrever métodos de formas diferentes.

### Por que usar `super()`?
**Resposta:** Para reutilizar código da classe pai. Sem `super()`, teríamos que duplicar a lógica de inicialização de `name`, `company`, `email`, `created`.

### O que é polimorfismo na prática?
**Resposta:** Mesmo método (`to_dict`, `get_display_info`) tem comportamentos diferentes dependendo do tipo do objeto (Lead vs Customer).

---

## 🚀 Próximo Passo

Leia: **`repository_explicado.md`** para entender persistência de dados e encapsulamento!
