CREATE DATABASE PROJETO_SOFTWARE;
USE PROJETO_SOFTWARE;


CREATE TABLE Produto (
    id_produto INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    nome_produto VARCHAR(255) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    marca VARCHAR(100) NOT NULL,
    codigo_barras VARCHAR(50) NOT NULL
);

CREATE TABLE Login (
    id_login INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL,
    senha VARCHAR(50) NOT NULL
);

CREATE TABLE Estoque (
    id_estoque INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    quantidade_itens INT NOT NULL,
    data_entrada DATE NOT NULL,
    data_saida DATE,
    lote VARCHAR(50) NOT NULL,
    validade_produto DATE NOT NULL,
    id_produto INT,
    FOREIGN KEY (id_produto) REFERENCES Produto(id_produto)
);

CREATE TABLE Venda (
    id_venda INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    quantidade_venda INT NOT NULL,
    data_venda DATE NOT NULL,
    valor_total DECIMAL(10,2) NOT NULL,
    desconto DECIMAL(10,2),
    forma_pagamento VARCHAR(50) NOT NULL,
    id_produto INT,
    FOREIGN KEY (id_produto) REFERENCES Produto(id_produto),
    id_login INT,
    FOREIGN KEY (id_login) REFERENCES Login(id_login)
);

CREATE TABLE Compra (
    id_compra INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    quantidade_produtos INT NOT NULL,
    data_compra DATE NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    desconto DECIMAL(10,2),
    forma_pagamento VARCHAR(50) NOT NULL,
    id_produto INT,
    FOREIGN KEY (id_produto) REFERENCES Produto(id_produto)
);
 

