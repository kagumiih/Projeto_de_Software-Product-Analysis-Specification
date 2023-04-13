# app.py
import pyodbc
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar_produto', methods=['POST'])
def adicionar_produto():
    produto = request.form['produto']
    preco = float(request.form['preco'])
    tipo = request.form['tipo']
    marca = request.form['marca']
    codigo_barras = request.form['codigo_barras']
    inserir_produto(produto, preco, tipo, marca, codigo_barras)
    return jsonify({'status': 'OK'})

@app.route('/atualizar_produto', methods=['POST'])
def atualizar_produto():
    produto = request.form['produto']
    preco = float(request.form['preco'])
    tipo = request.form['tipo']
    marca = request.form['marca']
    codigo_barras = request.form['codigo_barras']
    atualizar_produto_db(produto, preco, tipo, marca, codigo_barras)
    return jsonify({'status': 'OK'})

def inserir_produto(produto: str, preco: float, tipo: str, marca: str, codigo_barras: str):
    with pyodbc.connect(get_dados_conexao()) as cnx:
        cursor = cnx.cursor()
        inserir_produto_sql = f"""INSERT INTO Produto(nome_produto, valor, tipo, marca, codigo_barras) 
                                VALUES('{produto}', {preco},'{tipo}','{marca}','{codigo_barras}')"""
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

def get_dados_conexao() -> str:
    return ("Driver={SQL Server};"
            "Server=DESKTOP-JRD01KQ;"
            "Database=PROJETO_SOFTWARE;")

if __name__ == '__main__':
    app.run(debug=True)
