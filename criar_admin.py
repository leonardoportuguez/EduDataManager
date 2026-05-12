"""
Rode este script UMA VEZ após criar o banco de dados
para criar o usuário administrador com senha criptografada.

Uso:  python criar_admin.py
"""
from werkzeug.security import generate_password_hash
from database.db import executar, get_connection

ADMIN_EMAIL = "leoon1557@gmail.com"
ADMIN_SENHA = "usuario0987654"
ADMIN_NOME  = "Leonardo"

def criar_admin():
    conn = get_connection()
    if not conn:
        print("❌ Sem conexão com o banco. Verifique sua senha em database/db.py")
        return

    hash_senha = generate_password_hash(ADMIN_SENHA)

    executar("""
        INSERT INTO usuarios (nome, email, senha_hash, perfil)
        VALUES (%s, %s, %s, 'admin')
        ON DUPLICATE KEY UPDATE senha_hash = VALUES(senha_hash)
    """, (ADMIN_NOME, ADMIN_EMAIL, hash_senha))

    print(f"✅ Usuário admin criado!")
    print(f"   E-mail: {ADMIN_EMAIL}")
    print(f"   Senha:  {ADMIN_SENHA}")
    print(f"\nAcesse: http://localhost:5000/login")

if __name__ == "__main__":
    criar_admin()
