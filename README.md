# 🎓 EduDataManager — Sistema de Gestão Acadêmica

Sistema web completo para gestão acadêmica, construído com **Python + Flask + MySQL + Bootstrap**.

---

## ✅ Pré-requisitos

- Python 3.10+
- MySQL (XAMPP ou MySQL Workbench)
- PyCharm (ou qualquer editor)

---

## 🚀 Passo a passo para rodar o projeto

### PASSO 1 — Criar o banco de dados

Abra o **MySQL Workbench** e execute o arquivo `database/schema.sql`:

```sql
-- Clique em File > Open SQL Script > selecione database/schema.sql
-- Depois clique em ⚡ (Execute) ou Ctrl+Enter
```

### PASSO 2 — Configurar a senha do banco

Abra o arquivo `database/db.py` e troque a senha:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "SUA_SENHA",  # ← Coloque aqui sua senha do MySQL
    "database": "edudatamanager"
}
```

### PASSO 3 — Instalar as bibliotecas

No terminal do PyCharm:

```bash
pip install -r requirements.txt
```

### PASSO 4 — Criar o usuário administrador

```bash
python criar_admin.py
```

### PASSO 5 — Iniciar o servidor

```bash
python app.py
```

### PASSO 6 — Acessar o sistema

Abra no navegador:
```
http://localhost:5000
```

Login:
- **E-mail:** admin@edudatamanager.com
- **Senha:** admin123

---

## 📁 Estrutura do Projeto

```
EduDataManager/
│
├── app.py                  ← Entrada principal do servidor
├── criar_admin.py          ← Cria usuário admin no banco
├── requirements.txt        ← Bibliotecas necessárias
│
├── database/
│   ├── db.py               ← Conexão e funções de acesso ao banco
│   └── schema.sql          ← Script de criação das tabelas
│
├── models/
│   └── models.py           ← Funções de CRUD para cada entidade
│
├── routes/
│   └── routes.py           ← Rotas do Flask (URLs e lógica)
│
├── templates/              ← Páginas HTML (Jinja2 + Bootstrap)
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── alunos.html
│   ├── form_aluno.html
│   ├── professores.html
│   ├── form_professor.html
│   ├── cursos.html
│   ├── form_curso.html
│   ├── disciplinas.html
│   ├── form_disciplina.html
│   ├── notas.html
│   └── lixeira.html
│
├── static/
│   └── css/
│       └── style.css       ← Estilos customizados
│
└── backups/                ← Pasta para backups do banco
```

---

## 🔧 Funcionalidades

| Módulo | Funcionalidades |
|---|---|
| Alunos | Cadastrar, editar, remover, restaurar, buscar |
| Professores | Cadastrar, editar, remover |
| Cursos | Cadastrar, editar, remover |
| Disciplinas | Cadastrar, editar, remover, vincular ao curso |
| Notas | Lançar notas por aluno e disciplina |
| Lixeira | Restaurar alunos removidos |
| Login | Autenticação com senha criptografada |

---

## 📋 Próximas etapas (Etapas 2–5 do plano)

- [ ] Sistema de frequência
- [ ] Emissão de certificados
- [ ] Backup automático do banco
- [ ] Subir projeto no GitHub

---

## 💡 Dica

Para abrir o projeto no PyCharm:
1. `File → Open → selecione a pasta EduDataManager`
2. Configure o interpretador Python do ambiente virtual
3. Siga os passos acima

---

## 🛠 Tecnologias Utilizadas

- Python
- Flask
- MySQL
- Bootstrap 5
- HTML5
- CSS3
- Jinja2

---

## 🔐 Segurança

O sistema utiliza:

- Senhas criptografadas com Werkzeug Security
- Controle de login
- Estrutura modular Flask
- Soft delete em registros importantes

---

## 👨‍💻 Desenvolvido por

Leonardo Anderson Nascimento

Projeto desenvolvido para fins de estudo, portfólio e evolução prática em desenvolvimento Full Stack com Python.

---

## 📸 Screenshots

Em breve.

---

## ⭐ Como contribuir

1. Faça um fork do projeto
2. Crie uma branch:
```bash
git checkout -b minha-feature
```

3. Commit:
```bash
git commit -m "Minha nova feature"
```

4. Push:
```bash
git push origin minha-feature
```

5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob licença MIT.
