from database.db import executar, buscar

# ========== ALUNOS ==========

def listar_alunos():
    return buscar("SELECT * FROM alunos WHERE deletado = 0 ORDER BY nome")

def buscar_aluno(id):
    return buscar("SELECT * FROM alunos WHERE id = %s", (id,), um=True)

def inserir_aluno(nome, cpf, email, telefone, curso, status):
    return executar(
        "INSERT INTO alunos (nome, cpf, email, telefone, curso, status) VALUES (%s,%s,%s,%s,%s,%s)",
        (nome, cpf, email, telefone, curso, status)
    )

def editar_aluno(id, nome, cpf, email, telefone, curso, status):
    return executar(
        "UPDATE alunos SET nome=%s, cpf=%s, email=%s, telefone=%s, curso=%s, status=%s WHERE id=%s",
        (nome, cpf, email, telefone, curso, status, id)
    )

def remover_aluno(id):
    return executar("UPDATE alunos SET deletado=1 WHERE id=%s", (id,))

def restaurar_aluno(id):
    return executar("UPDATE alunos SET deletado=0 WHERE id=%s", (id,))

def lixeira_alunos():
    return buscar("SELECT * FROM alunos WHERE deletado = 1 ORDER BY nome")

def pesquisar_alunos(termo):
    return buscar(
        "SELECT * FROM alunos WHERE deletado=0 AND (nome LIKE %s OR cpf LIKE %s OR email LIKE %s)",
        (f"%{termo}%", f"%{termo}%", f"%{termo}%")
    )

# ========== PROFESSORES ==========

def listar_professores():
    return buscar("SELECT * FROM professores WHERE deletado = 0 ORDER BY nome")

def buscar_professor(id):
    return buscar("SELECT * FROM professores WHERE id = %s", (id,), um=True)

def inserir_professor(nome, email, disciplina, telefone):
    return executar(
        "INSERT INTO professores (nome, email, disciplina, telefone) VALUES (%s,%s,%s,%s)",
        (nome, email, disciplina, telefone)
    )

def editar_professor(id, nome, email, disciplina, telefone):
    return executar(
        "UPDATE professores SET nome=%s, email=%s, disciplina=%s, telefone=%s WHERE id=%s",
        (nome, email, disciplina, telefone, id)
    )

def remover_professor(id):
    return executar("UPDATE professores SET deletado=1 WHERE id=%s", (id,))

# ========== CURSOS ==========

def listar_cursos():
    return buscar("SELECT * FROM cursos WHERE deletado = 0 ORDER BY nome_curso")

def buscar_curso(id):
    return buscar("SELECT * FROM cursos WHERE id = %s", (id,), um=True)

def inserir_curso(nome_curso, carga_horaria, descricao):
    return executar(
        "INSERT INTO cursos (nome_curso, carga_horaria, descricao) VALUES (%s,%s,%s)",
        (nome_curso, carga_horaria, descricao)
    )

def editar_curso(id, nome_curso, carga_horaria, descricao):
    return executar(
        "UPDATE cursos SET nome_curso=%s, carga_horaria=%s, descricao=%s WHERE id=%s",
        (nome_curso, carga_horaria, descricao, id)
    )

def remover_curso(id):
    return executar("UPDATE cursos SET deletado=1 WHERE id=%s", (id,))

# ========== DISCIPLINAS ==========

def listar_disciplinas():
    return buscar("""
        SELECT d.*, c.nome_curso FROM disciplinas d
        LEFT JOIN cursos c ON d.curso_id = c.id
        WHERE d.deletado = 0 ORDER BY d.nome_disciplina
    """)

def buscar_disciplina(id):
    return buscar("SELECT * FROM disciplinas WHERE id = %s", (id,), um=True)

def inserir_disciplina(nome_disciplina, curso_id, carga_horaria):
    return executar(
        "INSERT INTO disciplinas (nome_disciplina, curso_id, carga_horaria) VALUES (%s,%s,%s)",
        (nome_disciplina, curso_id, carga_horaria)
    )

def editar_disciplina(id, nome_disciplina, curso_id, carga_horaria):
    return executar(
        "UPDATE disciplinas SET nome_disciplina=%s, curso_id=%s, carga_horaria=%s WHERE id=%s",
        (nome_disciplina, curso_id, carga_horaria, id)
    )

def remover_disciplina(id):
    return executar("UPDATE disciplinas SET deletado=1 WHERE id=%s", (id,))

# ========== NOTAS ==========

def listar_notas():
    return buscar("""
        SELECT n.*, a.nome AS aluno_nome, d.nome_disciplina
        FROM notas n
        JOIN alunos a ON n.aluno_id = a.id
        JOIN disciplinas d ON n.disciplina_id = d.id
        ORDER BY a.nome
    """)

def inserir_nota(aluno_id, disciplina_id, nota):
    return executar(
        "INSERT INTO notas (aluno_id, disciplina_id, nota) VALUES (%s,%s,%s)",
        (aluno_id, disciplina_id, nota)
    )

def atualizar_nota(id, nota):
    return executar("UPDATE notas SET nota=%s WHERE id=%s", (nota, id))

# ========== DASHBOARD ==========

def totais_dashboard():
    total_alunos = buscar("SELECT COUNT(*) AS total FROM alunos WHERE deletado=0", um=True)
    total_professores = buscar("SELECT COUNT(*) AS total FROM professores WHERE deletado=0", um=True)
    total_cursos = buscar("SELECT COUNT(*) AS total FROM cursos WHERE deletado=0", um=True)
    total_disciplinas = buscar("SELECT COUNT(*) AS total FROM disciplinas WHERE deletado=0", um=True)
    return {
        "alunos": total_alunos["total"] if total_alunos else 0,
        "professores": total_professores["total"] if total_professores else 0,
        "cursos": total_cursos["total"] if total_cursos else 0,
        "disciplinas": total_disciplinas["total"] if total_disciplinas else 0,
    }
