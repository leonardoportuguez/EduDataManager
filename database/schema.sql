-- ============================================
-- EduDataManager — Script de criação do banco
-- ============================================

CREATE DATABASE IF NOT EXISTS edudatamanager
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE edudatamanager;

-- Tabela de cursos
CREATE TABLE IF NOT EXISTS cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_curso VARCHAR(150) NOT NULL,
    carga_horaria INT NOT NULL,
    descricao TEXT,
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP,
    deletado TINYINT(1) DEFAULT 0
);

-- Tabela de disciplinas
CREATE TABLE IF NOT EXISTS disciplinas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_disciplina VARCHAR(150) NOT NULL,
    curso_id INT NOT NULL,
    carga_horaria INT,
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP,
    deletado TINYINT(1) DEFAULT 0,
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

-- Tabela de professores
CREATE TABLE IF NOT EXISTS professores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    disciplina VARCHAR(150),
    telefone VARCHAR(20),
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP,
    deletado TINYINT(1) DEFAULT 0
);

-- Tabela de alunos
CREATE TABLE IF NOT EXISTS alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    curso VARCHAR(150),
    status ENUM('ativo', 'inativo', 'formado', 'trancado') DEFAULT 'ativo',
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP,
    deletado TINYINT(1) DEFAULT 0
);

-- Tabela de notas
CREATE TABLE IF NOT EXISTS notas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT NOT NULL,
    disciplina_id INT NOT NULL,
    nota DECIMAL(4,2),
    data_lancamento DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id)
);

-- Tabela de frequência
CREATE TABLE IF NOT EXISTS frequencia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT NOT NULL,
    disciplina_id INT NOT NULL,
    data_aula DATE NOT NULL,
    presente TINYINT(1) DEFAULT 1,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id)
);

-- Tabela de usuários (login)
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    senha_hash VARCHAR(256) NOT NULL,
    perfil ENUM('admin', 'professor', 'secretaria') DEFAULT 'secretaria',
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de certificados
CREATE TABLE IF NOT EXISTS certificados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT NOT NULL,
    curso_id INT NOT NULL,
    data_emissao DATE NOT NULL,
    codigo_verificacao VARCHAR(50) UNIQUE,
    deletado TINYINT(1) DEFAULT 0,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

-- Dados de exemplo
INSERT INTO cursos (nome_curso, carga_horaria, descricao) VALUES
('Análise e Desenvolvimento de Sistemas', 2400, 'Curso superior de tecnologia em ADS'),
('Administração', 3000, 'Bacharelado em Administração de Empresas'),
('Enfermagem', 4000, 'Bacharelado em Enfermagem');

INSERT INTO disciplinas (nome_disciplina, curso_id, carga_horaria) VALUES
('Algoritmos e Programação', 1, 80),
('Banco de Dados', 1, 60),
('Engenharia de Software', 1, 60),
('Gestão de Pessoas', 2, 60),
('Marketing Digital', 2, 40);

INSERT INTO professores (nome, email, disciplina) VALUES
('Prof. Carlos Silva', 'carlos@edudatamanager.com', 'Banco de Dados'),
('Prof. Ana Souza', 'ana@edudatamanager.com', 'Algoritmos e Programação');

-- Usuário admin padrão (senha: admin123)
INSERT INTO usuarios (nome, email, senha_hash, perfil) VALUES
('Administrador', 'admin@edudatamanager.com',
 'pbkdf2:sha256:260000$placeholder', 'admin');
