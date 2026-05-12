from flask import Flask
from routes.routes import routes

app = Flask(__name__)
app.secret_key = "edudatamanager_chave_secreta_troque_em_producao"

# Registra as rotas
app.register_blueprint(routes)

if __name__ == "__main__":
    print("=" * 50)
    print("  EduDataManager — Iniciando servidor...")
    print("  Acesse: http://localhost:5000")
    print("  Login: admin@edudatamanager.com / admin123")
    print("=" * 50)
    app.run(debug=True)
