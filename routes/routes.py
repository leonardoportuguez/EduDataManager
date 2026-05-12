from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.models import *

routes = Blueprint("routes", __name__)

# ─── Autenticação ─────────────────────────────────────────────────────────────
def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if "usuario_id" not in session:
            return redirect(url_for("routes.login"))
        return f(*args, **kwargs)
    return decorated


@routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        from database.db import buscar
        from werkzeug.security import check_password_hash
        email = request.form["email"]
        senha = request.form["senha"]
        usuario = buscar("SELECT * FROM usuarios WHERE email=%s", (email,), um=True)
        if usuario and check_password_hash(usuario["senha_hash"], senha):
            session["usuario_id"] = usuario["id"]
            session["usuario_nome"] = usuario["nome"]
            return redirect(url_for("routes.dashboard"))
        flash("E-mail ou senha incorretos.", "danger")
    return render_template("login.html")


@routes.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("routes.login"))


# ─── Dashboard ────────────────────────────────────────────────────────────────
@routes.route("/")
@login_required
def dashboard():
    dados = totais_dashboard()
    return render_template("dashboard.html", dados=dados)


# ─── Alunos ───────────────────────────────────────────────────────────────────
@routes.route("/alunos")
@login_required
def alunos():
    termo = request.args.get("q", "")
    lista = pesquisar_alunos(termo) if termo else listar_alunos()
    return render_template("alunos.html", alunos=lista, termo=termo)


@routes.route("/alunos/novo", methods=["GET", "POST"])
@login_required
def novo_aluno():
    cursos = listar_cursos()
    if request.method == "POST":
        inserir_aluno(
            request.form["nome"], request.form["cpf"],
            request.form["email"], request.form["telefone"],
            request.form["curso"], request.form["status"]
        )
        flash("Aluno cadastrado com sucesso!", "success")
        return redirect(url_for("routes.alunos"))
    return render_template("form_aluno.html", aluno=None, cursos=cursos, acao="Novo")


@routes.route("/alunos/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_aluno_route(id):
    aluno = buscar_aluno(id)
    cursos = listar_cursos()
    if request.method == "POST":
        editar_aluno(
            id, request.form["nome"], request.form["cpf"],
            request.form["email"], request.form["telefone"],
            request.form["curso"], request.form["status"]
        )
        flash("Aluno atualizado!", "success")
        return redirect(url_for("routes.alunos"))
    return render_template("form_aluno.html", aluno=aluno, cursos=cursos, acao="Editar")


@routes.route("/alunos/remover/<int:id>")
@login_required
def remover_aluno_route(id):
    remover_aluno(id)
    flash("Aluno removido (pode ser restaurado).", "warning")
    return redirect(url_for("routes.alunos"))


@routes.route("/alunos/lixeira")
@login_required
def lixeira_alunos_route():
    lista = lixeira_alunos()
    return render_template("lixeira.html", alunos=lista)


@routes.route("/alunos/restaurar/<int:id>")
@login_required
def restaurar_aluno_route(id):
    restaurar_aluno(id)
    flash("Aluno restaurado com sucesso!", "success")
    return redirect(url_for("routes.lixeira_alunos_route"))


# ─── Professores ─────────────────────────────────────────────────────────────
@routes.route("/professores")
@login_required
def professores():
    lista = listar_professores()
    return render_template("professores.html", professores=lista)


@routes.route("/professores/novo", methods=["GET", "POST"])
@login_required
def novo_professor():
    if request.method == "POST":
        inserir_professor(
            request.form["nome"], request.form["email"],
            request.form["disciplina"], request.form["telefone"]
        )
        flash("Professor cadastrado!", "success")
        return redirect(url_for("routes.professores"))
    return render_template("form_professor.html", professor=None, acao="Novo")


@routes.route("/professores/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_professor_route(id):
    professor = buscar_professor(id)
    if request.method == "POST":
        editar_professor(
            id, request.form["nome"], request.form["email"],
            request.form["disciplina"], request.form["telefone"]
        )
        flash("Professor atualizado!", "success")
        return redirect(url_for("routes.professores"))
    return render_template("form_professor.html", professor=professor, acao="Editar")


@routes.route("/professores/remover/<int:id>")
@login_required
def remover_professor_route(id):
    remover_professor(id)
    flash("Professor removido.", "warning")
    return redirect(url_for("routes.professores"))


# ─── Cursos ──────────────────────────────────────────────────────────────────
@routes.route("/cursos")
@login_required
def cursos():
    lista = listar_cursos()
    return render_template("cursos.html", cursos=lista)


@routes.route("/cursos/novo", methods=["GET", "POST"])
@login_required
def novo_curso():
    if request.method == "POST":
        inserir_curso(
            request.form["nome_curso"],
            request.form["carga_horaria"],
            request.form["descricao"]
        )
        flash("Curso criado!", "success")
        return redirect(url_for("routes.cursos"))
    return render_template("form_curso.html", curso=None, acao="Novo")


@routes.route("/cursos/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_curso_route(id):
    curso = buscar_curso(id)
    if request.method == "POST":
        editar_curso(
            id, request.form["nome_curso"],
            request.form["carga_horaria"],
            request.form["descricao"]
        )
        flash("Curso atualizado!", "success")
        return redirect(url_for("routes.cursos"))
    return render_template("form_curso.html", curso=curso, acao="Editar")


@routes.route("/cursos/remover/<int:id>")
@login_required
def remover_curso_route(id):
    remover_curso(id)
    flash("Curso removido.", "warning")
    return redirect(url_for("routes.cursos"))


# ─── Disciplinas ─────────────────────────────────────────────────────────────
@routes.route("/disciplinas")
@login_required
def disciplinas():
    lista = listar_disciplinas()
    return render_template("disciplinas.html", disciplinas=lista)


@routes.route("/disciplinas/novo", methods=["GET", "POST"])
@login_required
def nova_disciplina():
    cursos_lista = listar_cursos()
    if request.method == "POST":
        inserir_disciplina(
            request.form["nome_disciplina"],
            request.form["curso_id"],
            request.form["carga_horaria"]
        )
        flash("Disciplina criada!", "success")
        return redirect(url_for("routes.disciplinas"))
    return render_template("form_disciplina.html", disciplina=None, cursos=cursos_lista, acao="Nova")


@routes.route("/disciplinas/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_disciplina_route(id):
    disciplina = buscar_disciplina(id)
    cursos_lista = listar_cursos()
    if request.method == "POST":
        editar_disciplina(
            id, request.form["nome_disciplina"],
            request.form["curso_id"], request.form["carga_horaria"]
        )
        flash("Disciplina atualizada!", "success")
        return redirect(url_for("routes.disciplinas"))
    return render_template("form_disciplina.html", disciplina=disciplina, cursos=cursos_lista, acao="Editar")


@routes.route("/disciplinas/remover/<int:id>")
@login_required
def remover_disciplina_route(id):
    remover_disciplina(id)
    flash("Disciplina removida.", "warning")
    return redirect(url_for("routes.disciplinas"))


# ─── Notas ───────────────────────────────────────────────────────────────────
@routes.route("/notas")
@login_required
def notas():
    lista = listar_notas()
    alunos_lista = listar_alunos()
    disciplinas_lista = listar_disciplinas()
    return render_template("notas.html", notas=lista,
                           alunos=alunos_lista, disciplinas=disciplinas_lista)


@routes.route("/notas/lancar", methods=["POST"])
@login_required
def lancar_nota():
    inserir_nota(
        request.form["aluno_id"],
        request.form["disciplina_id"],
        request.form["nota"]
    )
    flash("Nota lançada!", "success")
    return redirect(url_for("routes.notas"))
