CREATE DATABASE IF NOT EXISTS loja_db;
USE loja_db;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    login VARCHAR(50) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL,
    nivel_acesso VARCHAR(50) NOT NULL
);

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    telefone VARCHAR(20)
);

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10,2),
    estoque INT
);

CREATE TABLE vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    usuario_id INT,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE itens_venda (
    id INT AUTO_INCREMENT PRIMARY KEY,
    venda_id INT,
    produto_id INT,
    quantidade INT,
    preco_unitario DECIMAL(10,2),
    FOREIGN KEY (venda_id) REFERENCES vendas(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

INSERT INTO usuarios (nome, login, senha_hash, nivel_acesso)
VALUES ('Admin', 'admin', '$2b$12$AbCdEfGhIjKlMnOpQrStUvWxYz1234567890abcdEFGHIJK', 'admin');
