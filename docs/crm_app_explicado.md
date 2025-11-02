# 📘 Explicação Detalhada: crm_app.py

## 🎯 Visão Geral

O arquivo `crm_app.py` implementa a **interface do usuário** da aplicação. É responsável por exibir menus, capturar entrada do usuário e processar as opções escolhidas.

---

## 📚 Conceitos OOP Demonstrados

### ✅ 1. COMPOSIÇÃO (has-a)
### ✅ 2. ENCAPSULAMENTO
### ✅ 3. SEPARAÇÃO DE RESPONSABILIDADES
### ✅ 4. EVENT LOOP (loop de eventos)
### ✅ 5. COMMAND PATTERN

---

## 🏗️ Classe: CRMApp

### Responsabilidade:
Gerenciar APENAS a interface com o usuário (menus, inputs, outputs).

### Atributos:
- `repository` (LeadRepository) - **COMPOSIÇÃO**: CRMApp "tem um" repositório
- `running` (bool) - Controla se a aplicação está rodando

---

## 🔄 COMPOSIÇÃO vs HERANÇA

### Composição (has-a) ✅
```python
class CRMApp:
    def __init__(self):
        self.repository = LeadRepository()  # CRMApp "TEM UM" repositório
```

### Herança (is-a) ❌
```python
class CRMApp(LeadRepository):  # ERRADO!
    # CRMApp "É UM" repositório? NÃO!
```

**Por que Composição?**
- CRMApp **usa** LeadRepository
- CRMApp **não é** um LeadRepository
- Composição é mais flexível e apropriada aqui

---

## 🔧 Métodos

### `__init__(self)`
Construtor - inicializa atributos.

```python
def __init__(self):
    self.repository = LeadRepository()  # COMPOSIÇÃO
    self.running = True  # Estado inicial
```

**Conceitos:**
- **COMPOSIÇÃO**: Cria e armazena um LeadRepository
- **ESTADO**: `running` controla o loop principal

---

### `run(self) -> None`
Loop principal da aplicação (Event Loop).

```python
def run(self) -> None:
    print("=" * 60)
    print("Mini-CRM com Orientação a Objetos")
    print("=" * 60)
    
    while self.running:  # Loop infinito até running = False
        self.show_menu()
        option = input("\nEscolha uma opção: ").strip()
        self.handle_option(option)
```

**Event Loop:**
1. Mostra menu
2. Espera input do usuário
3. Processa opção
4. Repete

**Como parar?**
- Usuário escolhe opção "0"
- `exit_app()` define `self.running = False`
- Loop termina

---

### `show_menu(self) -> None`
Exibe o menu principal.

```python
def show_menu(self) -> None:
    print("\n" + "=" * 60)
    print("MENU PRINCIPAL")
    print("=" * 60)
    print("[1] Adicionar Lead")
    print("[2] Listar Leads")
    print("[3] Buscar Lead")
    print("[4] Exportar para CSV")
    print("[5] Estatísticas")
    print("[0] Sair")
    print("=" * 60)
```

**Por que um método separado?**
- **Separação de responsabilidades**
- Facilita manutenção (alterar menu em um só lugar)
- Código mais organizado

---

### `handle_option(self, option: str) -> None`
Processa a opção escolhida - **COMMAND PATTERN**.

```python
def handle_option(self, option: str) -> None:
    # Dicionário mapeia opções para métodos
    options = {
        "1": self.add_lead,
        "2": self.list_leads,
        "3": self.search_leads,
        "4": self.export_csv,
        "5": self.show_statistics,
        "0": self.exit_app
    }
    
    action = options.get(option)  # Busca método
    if action:
        action()  # Executa método
    else:
        print("\n❌ Opção inválida!")
```

**Command Pattern:**
- Dicionário mapeia opções → métodos
- Mais elegante que múltiplos `if/elif`
- Fácil adicionar novas opções

**Alternativa (menos elegante):**
```python
if option == "1":
    self.add_lead()
elif option == "2":
    self.list_leads()
elif option == "3":
    ...
```

---

### `add_lead(self) -> None`
Adiciona novo lead ao sistema.

```python
def add_lead(self) -> None:
    print("\n" + "-" * 60)
    print("ADICIONAR NOVO LEAD")
    print("-" * 60)
    
    # 1. Captura dados
    name = input("Nome: ").strip()
    company = input("Empresa: ").strip()
    email = input("E-mail: ").strip()
    
    # 2. Cria objeto Lead
    lead = Lead(name=name, company=company, email=email)
    
    # 3. Valida
    if not lead.validate():
        print("\n❌ Erro: Nome e e-mail válido são obrigatórios!")
        return
    
    # 4. Salva usando repositório (COMPOSIÇÃO)
    self.repository.create(lead)
    
    # 5. Feedback
    print("\n✅ Lead adicionado com sucesso!")
    print(f"   {lead.get_display_info()}")  # POLIMORFISMO
```

**Conceitos em ação:**
- **Criação de objeto**: `Lead(...)`
- **Composição**: `self.repository.create(lead)`
- **Polimorfismo**: `lead.get_display_info()` (funciona para Lead e Customer)

---

### `list_leads(self) -> None`
Lista todos os leads.

```python
def list_leads(self) -> None:
    # 1. Busca leads do repositório
    leads = self.repository.read_all()
    
    print("\n" + "-" * 60)
    print("LISTA DE LEADS")
    print("-" * 60)
    
    # 2. Verifica se há leads
    if not leads:
        print("Nenhum lead cadastrado ainda.")
        return
    
    # 3. Exibe cabeçalho da tabela
    print(f"\n{'#':<3} | {'Nome':<20} | {'Empresa':<17} | {'E-mail':<21} | Stage")
    print("-" * 95)
    
    # 4. Exibe cada lead
    for index, lead in enumerate(leads):
        print(f"{index:02d}  | {lead.get_display_info()}")  # POLIMORFISMO
    
    print(f"\nTotal: {len(leads)} lead(s)")
```

**Formatação:**
- `{index:02d}` → 2 dígitos: 01, 02, 03...
- `{'Nome':<20}` → Alinha à esquerda, largura 20

**Polimorfismo:**
- `lead.get_display_info()` funciona para Lead e Customer
- Cada um formata diferente
- Código não precisa saber o tipo!

---

### `search_leads(self) -> None`
Busca leads por termo.

```python
def search_leads(self) -> None:
    print("\n" + "-" * 60)
    print("BUSCAR LEADS")
    print("-" * 60)
    
    # 1. Captura termo
    query = input("Digite o termo de busca: ").strip()
    
    # 2. Valida
    if not query:
        print("\n❌ Consulta vazia!")
        return
    
    # 3. Busca usando repositório
    results = self.repository.search(query)
    
    # 4. Exibe resultados
    if not results:
        print(f"\n❌ Nenhum resultado encontrado para '{query}'")
        return
    
    # Exibe tabela de resultados
    print(f"\n{'#':<3} | {'Nome':<20} | {'Empresa':<17} | {'E-mail':<21} | Stage")
    print("-" * 95)
    
    for index, lead in results:  # results = [(índice, lead), ...]
        print(f"{index:02d}  | {lead.get_display_info()}")
    
    print(f"\nEncontrado(s): {len(results)} lead(s)")
```

**Tuplas:**
- `results = [(0, lead1), (5, lead2), ...]`
- `index` → Posição original na lista
- `lead` → Objeto Lead encontrado

---

### `export_csv(self) -> None`
Exporta leads para CSV.

```python
def export_csv(self) -> None:
    print("\n" + "-" * 60)
    print("EXPORTAR LEADS PARA CSV")
    print("-" * 60)
    
    # Delega ao repositório
    path = self.repository.export_to_csv()
    
    # Verifica resultado
    if path is None:
        print("\n❌ Erro ao exportar CSV!")
        print("   Verifique se o arquivo não está aberto em outro programa.")
    else:
        print(f"\n✅ Leads exportados com sucesso!")
        print(f"   Arquivo: {path}")
```

**Separação de responsabilidades:**
- CRMApp: Exibe mensagens
- LeadRepository: Faz a exportação
- Cada um cuida do seu!

---

### `show_statistics(self) -> None`
Exibe estatísticas do sistema.

```python
def show_statistics(self) -> None:
    leads = self.repository.read_all()
    
    print("\n" + "-" * 60)
    print("ESTATÍSTICAS DO SISTEMA")
    print("-" * 60)
    
    total = len(leads)
    print(f"\nTotal de leads: {total}")
    
    if total > 0:
        # Conta leads por estágio
        stages = {}
        for lead in leads:
            stages[lead.stage] = stages.get(lead.stage, 0) + 1
        
        # Exibe estatísticas
        print("\nLeads por estágio:")
        for stage, count in sorted(stages.items()):
            percentage = (count / total) * 100
            print(f"  • {stage.capitalize()}: {count} ({percentage:.1f}%)")
```

**Algoritmo de contagem:**
```python
stages = {}  # Dicionário vazio
for lead in leads:
    # Para cada lead, incrementa contador do estágio
    stages[lead.stage] = stages.get(lead.stage, 0) + 1
# Resultado: {"novo": 3, "contatado": 2, ...}
```

---

### `exit_app(self) -> None`
Encerra a aplicação.

```python
def exit_app(self) -> None:
    print("\n" + "=" * 60)
    print("Obrigado por usar o Mini-CRM!")
    print("Até logo! 👋")
    print("=" * 60)
    
    self.running = False  # Para o loop em run()
```

**Controle de estado:**
- `self.running = False` faz o `while self.running` parar
- Loop termina naturalmente
- Programa encerra

---

## 🎓 Conceitos OOP em Ação

### 1. **COMPOSIÇÃO** (has-a)

```python
class CRMApp:
    def __init__(self):
        self.repository = LeadRepository()  # "TEM UM" repositório
```

**Relação:**
- CRMApp **usa** LeadRepository
- CRMApp **não é** um LeadRepository
- Composição = "has-a"
- Herança = "is-a"

**Exemplo:**
- Lead "**é um**" Contact → HERANÇA
- CRMApp "**tem um**" Repository → COMPOSIÇÃO

---

### 2. **ENCAPSULAMENTO**

```
CRMApp
├── Métodos públicos:
│   ├── run()
│   ├── add_lead()
│   ├── list_leads()
│   └── ...
│
└── Atributos privados:
    ├── repository (usado internamente)
    └── running (controle interno)
```

---

### 3. **SEPARAÇÃO DE RESPONSABILIDADES**

| Classe | Responsabilidade |
|--------|-----------------|
| CRMApp | Interface (menus, inputs, outputs) |
| LeadRepository | Persistência (salvar/carregar) |
| Lead | Representar um lead |

**Cada classe cuida do seu!**

---

### 4. **POLIMORFISMO** (usado, não implementado)

```python
# CRMApp usa polimorfismo dos objetos Lead/Customer
print(lead.get_display_info())  # Funciona para Lead e Customer!
```

**Vantagem:**
- CRMApp não precisa saber se é Lead ou Customer
- Cada classe formata à sua maneira
- Código genérico, funciona para todos!

---

## 💡 Perguntas Frequentes

### Por que usar composição ao invés de herança?
**Resposta:** CRMApp **não é** um LeadRepository. CRMApp **usa** um repositório para salvar dados. Composição ("has-a") é mais apropriada que herança ("is-a").

### O que é Event Loop?
**Resposta:** Loop infinito que espera eventos (input do usuário), processa e repete. Comum em aplicações interativas e GUIs.

### Por que usar dicionário de comandos?
**Resposta:** Mais elegante e extensível que múltiplos `if/elif`. Fácil adicionar novas opções.

---

## 🚀 Próximo Passo

Leia: **`main_explicado.md`** para entender o ponto de entrada e fluxo completo!
