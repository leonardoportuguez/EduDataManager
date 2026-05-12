import mysql.connector
from mysql.connector import Error

# =============================================
# Configurações de conexão com o banco MySQL
# =============================================
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "luasuperior3",   # ← Troque pela sua senha do MySQL
    "database": "edudatamanager",
    "charset": "utf8mb4"
}


def get_connection():
    """Retorna uma conexão ativa com o banco de dados."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"[ERRO] Não foi possível conectar ao banco: {e}")
        return None


def executar(query, params=None):
    """Executa INSERT, UPDATE ou DELETE e retorna lastrowid."""
    conn = get_connection()
    if not conn:
        return None
    try:
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"[ERRO] ao executar query: {e}")
        conn.rollback()
        return None
    finally:
        cursor.close()
        conn.close()


def buscar(query, params=None, um=False):
    """Executa SELECT e retorna lista de dicts (ou um dict se um=True)."""
    conn = get_connection()
    if not conn:
        return None
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params or ())
        resultado = cursor.fetchone() if um else cursor.fetchall()
        return resultado
    except Error as e:
        print(f"[ERRO] ao buscar dados: {e}")
        return None
    finally:
        cursor.close()
        conn.close()


# Teste rápido de conexão
if __name__ == "__main__":
    conn = get_connection()
    if conn:
        print("✅ Conectado com sucesso ao EduDataManager!")
        conn.close()
    else:
        print("❌ Falha na conexão. Verifique sua senha e se o MySQL está rodando.")
