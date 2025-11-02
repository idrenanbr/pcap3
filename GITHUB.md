# Como Publicar no GitHub

## Passo a Passo para Entrega do Projeto

### 1. Criar um Repositório no GitHub

1. Acesse https://github.com
2. Faça login na sua conta
3. Clique em **"New"** (novo repositório)
4. Preencha as informações:
   - **Repository name:** `mini-crm-oop` (ou outro nome de sua preferência)
   - **Description:** "Mini-CRM com Orientação a Objetos - PCP 2SEM-CP3"
   - **Public** (para que o professor possa acessar)
   - **NÃO** marque "Initialize this repository with a README" (já temos um)
5. Clique em **"Create repository"**

### 2. Publicar o Código do Replit para o GitHub

#### Opção A: Usando o Terminal do Replit

```bash
# Inicializar repositório Git (se ainda não foi feito)
git init

# Adicionar todos os arquivos
git add .

# Fazer o primeiro commit
git commit -m "Initial commit - Mini-CRM com OOP"

# Adicionar o repositório remoto (substitua SEU_USUARIO pelo seu usuário do GitHub)
git remote add origin https://github.com/SEU_USUARIO/mini-crm-oop.git

# Enviar para o GitHub
git push -u origin main
```

#### Opção B: Usando a Interface do Replit

1. No Replit, vá para a aba **"Version Control"** (Git)
2. Clique em **"Connect to GitHub"**
3. Autorize o Replit a acessar sua conta GitHub
4. Selecione o repositório criado
5. Faça o commit e push das alterações

### 3. Verificar a Publicação

1. Acesse o repositório no GitHub
2. Verifique se todos os arquivos estão presentes:
   - ✅ `models.py`
   - ✅ `repository.py`
   - ✅ `crm_app.py`
   - ✅ `main.py`
   - ✅ `README.md`
   - ✅ `.gitignore`

### 4. Copiar o Link do Repositório

1. Na página do seu repositório no GitHub
2. Clique no botão verde **"Code"**
3. Copie a URL (exemplo: `https://github.com/SEU_USUARIO/mini-crm-oop`)
4. **Este é o link que você vai entregar no Canvas!**

### 5. Entregar no Canvas

1. Acesse o Canvas
2. Vá para a atividade **PCP - 2SEM-CP3 - Mini-CRM: Orientação a Objetos**
3. Cole o link do GitHub
4. Clique em **Enviar**

## ✅ Checklist Final

- [ ] Repositório criado no GitHub
- [ ] Código publicado (push realizado)
- [ ] README.md visível no repositório
- [ ] Link do repositório copiado
- [ ] Link entregue no Canvas

## 🎯 Importante

- **Só links do GitHub serão aceitos** - conforme instruções do professor
- Verifique se o repositório está **público** (não privado)
- Teste se o link funciona antes de entregar
- O professor precisa conseguir acessar e ver o código

## 📝 Exemplo de Link Correto

```
https://github.com/seu-usuario/mini-crm-oop
```

**NÃO** envie:
- ❌ Link do Replit
- ❌ Arquivo ZIP
- ❌ Código colado no Canvas
- ❌ Link de repositório privado

---

**Boa sorte! 🚀**
