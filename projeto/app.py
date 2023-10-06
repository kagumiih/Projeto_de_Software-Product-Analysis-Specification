# app.py
import pyodbc
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__, template_folder='templates')
app.secret_key = 'senhasecreta'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('index.html', username=username)
    return render_template('login.html')

@app.route('/cadastro_produto')
def cadastro_produto():
    return render_template('cadastro_produto.html')

@app.route('/usuario')
def usuario():
    return render_template('cadastro_usuario.html')

@app.route('/estoque')
def estoque():
    return render_template('cadastro_estoque.html')
    #with pyodbc.connect(get_dados_conexao()) as cnx:
    #    cursor = cnx.cursor()

    #    sql = "SELECT id_produto, nome_produto FROM produto"
    #    cursor.execute(sql)
    #    produtos = cursor.fetchall()

    #    cursor.close()
    #    cnx.close()

    #return render_template('cadastro_estoque.html', produtos=produtos)#
@app.route('/venda')
def venda():
    return render_template('venda.html')

@app.route('/adicionar_produto', methods=['POST'])
def adicionar_produto():
    produto = request.form['produto']
    preco = float(request.form['preco'])
    tipo = request.form['tipo']
    marca = request.form['marca']
    codigo_barras = request.form['codigo_barras']
    inserir_produto(produto, preco, tipo, marca, codigo_barras)
    return jsonify({'status': 'OK'})

@app.route('/gerar_venda', methods=['POST'])
def gerar_venda():
    quantidade_venda = request.form['quantidade_venda']
    data = datetime.now()
    data_venda = data.strftime("%m/%d/%Y, %H:%M:%S")
    valor_total = float(request.form['valor_total'])
    desconto = float(request.form['desconto'])
    forma_pagamento = request.form['forma_pagamento']
    id_produto = int(request.form['id_produto'])
    inserir_venda(quantidade_venda, data_venda, valor_total, desconto, forma_pagamento, id_produto)
    return jsonify({'status': 'OK'})


@app.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    usuario = request.form['usuario']
    senha = request.form['senha']
    cadastrar_usuario_db(usuario, senha)
    return jsonify({'status': 'OK'})


@app.route('/cadastrar_estoque', methods=['POST'])
def cadastrar_estoque():
    quantidade = request.form['quantidade']
    data_entrada = request.form['data-entrada']
    data_saida = request.form['data-saida']
    lote = request.form['lote']
    validade = request.form['validade']
    id_produto = request.form['id_produto']
    cadastrar_estoque_db(quantidade, data_entrada, data_saida, lote, validade, id_produto)
    return jsonify({'status': 'OK'})

def inserir_produto(produto: str, preco: float, tipo: str, marca: str, codigo_barras: str):
    with pyodbc.connect(get_dados_conexao()) as cnx:
        cursor = cnx.cursor()
        inserir_produto_sql = f"""INSERT INTO Produto(nome_produto, valor, tipo, marca, codigo_barras) 
                                VALUES('{produto}', {preco},'{tipo}','{marca}','{codigo_barras}')"""
        cursor.execute(inserir_produto_sql)
        cnx.commit()

def inserir_venda(quantidade_venda: int, data_venda: str, valor_total: float, desconto: float, forma_pagamento: str, id_produto: int):
    with pyodbc.connect(get_dados_conexao()) as cnx:
        cursor = cnx.cursor()
        inserir_produto_sql = f"""INSERT INTO Venda(quantidade_venda, data_venda, valor_total, desconto, forma_pagamento, id_produto) 
                                VALUES({quantidade_venda}, '{data_venda}',{valor_total},{desconto},'{forma_pagamento}',{id_produto})"""
        cursor.execute(inserir_produto_sql)
        cnx.commit()

def atualizar_produto_db(produto: str, preco: float, tipo: str, marca: str, codigo_barras: str):
    with pyodbc.connect(get_dados_conexao()) as cnx:
        cursor = cnx.cursor()
        atualizar_produto_sql = f"""UPDATE Produto SET nome_produto = '{produto}', valor = {preco} , 
                                  tipo = '{tipo}', marca = '{marca}', codigo_barras = '{codigo_barras}'
                                  WHERE nome_produto = '{produto}'"""
        cursor.execute(atualizar_produto_sql)
        cnx.commit()

def cadastrar_usuario_db(usuario: str, senha: str):
    with pyodbc.connect(get_dados_conexao()) as cnx:
        cursor = cnx.cursor()
        cadastrar_usuario_sql = f"""INSERT INTO Login(usuario, senha) 
                                VALUES('{usuario}', '{senha}')"""
        cursor.execute(cadastrar_usuario_sql)
        cnx.commit()

def atualizar_usuario_db(usuario: str, senha: str):
    with pyodbc.connect(get_dados_conexao()) as cnx:
        cursor = cnx.cursor()
        atualizar_usuario_sql = f"""UPDATE Login SET usuario = '{usuario}', senha = '{senha}' 
                                WHERE usuario = '{usuario}' AND  senha = '{senha}'"""
        
        cursor.execute(atualizar_usuario_sql)
        cnx.commit()

@app.route('/login', methods=['POST'])
def login():
    user = get_user(request.form['username'], request.form['password'])
    if user != None:
        session['username'] = user[1]
        flash('Login bem-sucedido!', 'success')
        #return redirect(url_for('index'))
        return render_template('index.html', username=user[1])
    flash('Credenciais inválidas. Tente novamente.', 'danger')
    return render_template('login.html')

def get_user(usuario, senha):
    try:
        with pyodbc.connect(get_dados_conexao()) as cnx:
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM Login WHERE usuario=? and senha=?", (usuario,senha))
            user = cursor.fetchone()
        return user
    except pyodbc.Error as e:
        print("Erro ODBC:", e)
        return None

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('index'))

def cadastrar_estoque_db(quantidade: str, data_entrada: str, data_saida: str, lote: str, validade: str, id_produto: str):
    with pyodbc.connect(get_dados_conexao()) as cnx:
            cursor = cnx.cursor()
            cadastrar_estoque_sql = f"""INSERT INTO Estoque(quantidade_itens, 
                                                            data_entrada, 
                                                            data_saida,
                                                            lote,
                                                            validade_produto,
                                                            id_produto) 
                                    VALUES('{quantidade}', '{data_entrada}',
                                           '{data_saida}', '{lote}',
                                           '{validade}', '{id_produto}')"""
            cursor.execute(cadastrar_estoque_sql)
            cnx.commit()

def get_dados_conexao() -> str:
    return ("Driver={SQL Server};"
            "Server=DESKTOP-JRD01KQ;"
            "Database=PROJETO_SOFTWARE;")

@app.route('/produtos', methods=['POST', 'GET'])
def seleciona_produto():
    if request.method == 'POST':
        product_id = request.form['id_produto']
        product = get_product(product_id)
        return render_template('seleciona_produto.html',product=product)
        #return redirect(url_for('seleciona_produto', product=product))
    else:
        return redirect(url_for('seleciona_produto'))  

@app.route('/produto/<int:id_produto>')
def produto_selecionado(id_produto):
    product = get_product(id_produto)
    return redirect(url_for('seleciona_produto', product=product))

def get_product(id_produto):
    try:
        with pyodbc.connect(get_dados_conexao()) as cnx:
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM Produto WHERE id_produto=?", (id_produto,))
            product = cursor.fetchone()
        return product
    except pyodbc.Error as e:
        print("Erro ODBC:", e)
        return None
    
if __name__ == '__main__':
    app.run(debug=True)