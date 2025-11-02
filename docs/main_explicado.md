# 📘 Explicação Detalhada: main.py

## 🎯 Visão Geral

O arquivo `main.py` é o **ponto de entrada** da aplicação. É o arquivo executado para iniciar o sistema: `python main.py`.

---

## 📚 Conceitos Demonstrados

### ✅ 1. Ponto de entrada da aplicação
### ✅ 2. Instanciação de classes
### ✅ 3. Chamada de métodos
### ✅ 4. `__name__ == "__main__"`

---

## 📖 Estrutura do Arquivo

```python
"""Docstring do módulo"""

from crm_app import CRMApp  # Importação

def main():  # Função principal
    """Função principal"""
    app = CRMApp()
    app.run()

if __name__ == "__main__":  # Bloco de execução
    main()
```

---

## 🔧 Componentes

### 1. Docstring do Módulo

```python
"""
Mini-CRM com Orientação a Objetos
PCP - 2SEM-CP3
Autor: Alexandre Russi

Este sistema demonstra:
- Classes e Objetos
- Atributos e Métodos
- Herança (Contact -> Lead, Customer)
- Polimorfismo (métodos to_dict, get_display_info)
- Encapsulamento
"""
```

**O que é?**
- Documentação do módulo
- Acessível via `help(main)` ou IDEs
- Explica o que o sistema faz

---

### 2. Importação

```python
from crm_app import CRMApp
```

**O que faz?**
- Importa a classe `CRMApp` do módulo `crm_app`
- Agora podemos usar `CRMApp()` para criar objetos

---

### 3. Função `main()`

```python
def main():
    """Função principal - ponto de entrada da aplicação"""
    app = CRMApp()
    app.run()
```

#### Linha 1: Instanciação
```python
app = CRMApp()
```

**O que acontece?**
1. Python cria novo objeto da classe `CRMApp`
2. Chama `CRMApp.__init__()`
3. `__init__` inicializa:
   - `self.repository = LeadRepository()`
   - `self.running = True`
4. Retorna referência ao objeto
5. Armazena em `app`

**Conceito OOP:**
- `CRMApp` = **CLASSE** (molde)
- `app` = **OBJETO** (instância)

**Analogia:**
- Classe = Planta da casa
- Objeto = Casa construída

---

#### Linha 2: Chamada de Método
```python
app.run()
```

**O que acontece?**
1. Acessa o método `run()` do objeto `app`
2. Executa o código dentro de `run()`
3. `run()` inicia o event loop
4. Programa fica rodando até usuário sair

**Conceito:**
- `.` acessa membros do objeto
- `()` chama/executa o método

**Diferença:**
- `app.run` → Referência ao método (não executa)
- `app.run()` → Chamada do método (executa)

---

### 4. Bloco `if __name__ == "__main__"`

```python
if __name__ == "__main__":
    main()
```

**O que é?**
Garante que `main()` só seja executada quando o arquivo é rodado diretamente.

---

#### Como funciona `__name__`?

**Quando rodado diretamente:**
```bash
$ python main.py
```
→ `__name__` = `"__main__"` → Executa `main()`

**Quando importado:**
```python
import main  # Em outro arquivo
```
→ `__name__` = `"main"` → **NÃO** executa `main()`

---

#### Por que usar?

**Vantagens:**
1. **Reutilização**: Pode importar sem executar
2. **Testes**: Pode testar funções sem rodar o programa
3. **Modularidade**: Arquivo pode ser módulo ou script

**Exemplo:**
```python
# Em test.py
from main import main  # Importa sem executar
# Agora pode testar main() quando quiser
```

---

## 🔄 Fluxo Completo de Execução

### Passo a Passo:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Usuário executa: python main.py                         │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. Python lê e interpreta main.py                          │
│    - Define função main()                                   │
│    - Importa CRMApp                                         │
│    - __name__ = "__main__" (rodado diretamente)            │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. Executa: if __name__ == "__main__":                     │
│    - Condição é True                                        │
│    - Chama main()                                           │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. Dentro de main():                                        │
│    - app = CRMApp()                                         │
│      └─> Chama CRMApp.__init__()                           │
│          └─> self.repository = LeadRepository()            │
│              └─> Chama LeadRepository.__init__()           │
│                  └─> Cria diretório data/                  │
│          └─> self.running = True                           │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 5. Dentro de main():                                        │
│    - app.run()                                              │
│      └─> Chama CRMApp.run()                                │
│          └─> Exibe cabeçalho                               │
│          └─> Inicia loop: while self.running               │
│              └─> Mostra menu                               │
│              └─> Espera input                              │
│              └─> Processa opção                            │
│              └─> Repete...                                 │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 6. Usuário escolhe opção "0" (Sair)                        │
│    - exit_app() é chamado                                   │
│    - self.running = False                                   │
│    - Loop while para                                        │
│    - run() termina                                          │
│    - main() termina                                         │
│    - Programa encerra                                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎓 Conceitos OOP em Ação

### 1. **INSTANCIAÇÃO**

```python
app = CRMApp()
```

**Criando um objeto:**
- `CRMApp` é a classe (molde)
- `CRMApp()` chama o construtor
- `app` recebe o objeto criado

---

### 2. **CHAMADA DE MÉTODO**

```python
app.run()
```

**Executando método do objeto:**
- `app` é o objeto
- `.run()` chama o método run
- Código dentro de run() é executado

---

### 3. **COMPOSIÇÃO** (indireta)

```python
app = CRMApp()  # CRMApp cria LeadRepository internamente
```

**Hierarquia criada:**
```
app (CRMApp)
└── repository (LeadRepository)
```

---

## 🏗️ Hierarquia Completa das Classes

```
┌─────────────────────────────────────────────────────────┐
│                     CAMADA DE MODELO                    │
│                                                         │
│   Contact (base)                                        │
│   ├── Lead (herda de Contact)                          │
│   └── Customer (herda de Contact)                      │
│                                                         │
│   Conceitos: HERANÇA, POLIMORFISMO                      │
└─────────────────────────────────────────────────────────┘
                          ↑
                          │ usa
                          │
┌─────────────────────────────────────────────────────────┐
│                  CAMADA DE PERSISTÊNCIA                 │
│                                                         │
│   LeadRepository                                        │
│   ├── _load() (privado)                                │
│   ├── _save() (privado)                                │
│   └── create(), read_all(), search() (públicos)        │
│                                                         │
│   Conceitos: ENCAPSULAMENTO, REPOSITORY PATTERN         │
└─────────────────────────────────────────────────────────┘
                          ↑
                          │ usa (COMPOSIÇÃO)
                          │
┌─────────────────────────────────────────────────────────┐
│                   CAMADA DE INTERFACE                   │
│                                                         │
│   CRMApp                                                │
│   ├── repository (LeadRepository)                      │
│   ├── run() (event loop)                               │
│   └── add_lead(), list_leads(), etc                    │
│                                                         │
│   Conceitos: COMPOSIÇÃO, ENCAPSULAMENTO                 │
└─────────────────────────────────────────────────────────┘
                          ↑
                          │ instancia
                          │
┌─────────────────────────────────────────────────────────┐
│                    PONTO DE ENTRADA                     │
│                                                         │
│   main.py                                               │
│   ├── main()                                            │
│   └── if __name__ == "__main__"                        │
│                                                         │
│   Conceitos: INSTANCIAÇÃO, EXECUÇÃO                     │
└─────────────────────────────────────────────────────────┘
```

---

## 📊 Resumo dos Conceitos OOP no Projeto

### 1. **CLASSES E OBJETOS**
- Definimos: Contact, Lead, Customer, LeadRepository, CRMApp
- Criamos: `app = CRMApp()`

### 2. **HERANÇA**
- Lead herda de Contact
- Customer herda de Contact
- Usam `super()` para reutilizar código

### 3. **POLIMORFISMO**
- `to_dict()` sobrescrito em Lead e Customer
- `get_display_info()` sobrescrito em Lead e Customer
- Mesmo método, comportamentos diferentes

### 4. **ENCAPSULAMENTO**
- Métodos privados: `_load()`, `_save()`
- Métodos públicos: `create()`, `read_all()`
- Atributos agrupados em classes

### 5. **COMPOSIÇÃO**
- CRMApp "tem um" LeadRepository
- Relação "has-a" (não "is-a")

### 6. **ABSTRAÇÃO**
- Interface simples esconde complexidade
- Repository abstrai persistência
- Classes representam conceitos reais

---

## 💡 Perguntas Frequentes

### Por que usar uma função main()?
**Resposta:** Organização e boas práticas. Separa código de inicialização e permite testes/importação.

### O que é __name__?
**Resposta:** Variável especial que indica como o módulo está sendo usado (`"__main__"` se rodado diretamente, nome do módulo se importado).

### Por que não colocar tudo no main.py?
**Resposta:** SEPARAÇÃO DE RESPONSABILIDADES. Cada arquivo/classe tem uma responsabilidade específica. Facilita manutenção e entendimento.

---

## 🎉 Conclusão

O `main.py` é simples mas essencial:
1. **Importa** a classe principal
2. **Cria** um objeto da aplicação
3. **Inicia** o programa

Todo o resto (classes, herança, polimorfismo, etc) está nos outros arquivos!

---

## 🚀 Próximo Passo

Agora você entende todo o fluxo! 🎓

Revise os arquivos nesta ordem:
1. ✅ main.py (você está aqui!)
2. models.py → Herança e Polimorfismo
3. repository.py → Encapsulamento e Persistência
4. crm_app.py → Composição e Interface

**Bons estudos!** 📚
