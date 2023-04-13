import pyodbc
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#fnção para adicionar produtos e preços
@app.route('/adicionar_produto', methods=['POST'])
def adicionar_produto(): 
    produto = request.form['produto']
    preco = float (request.form['preco'])
    tipo = request.form['tipo']
    marca = request.form['marca']
    codigo_barras = request.form['codigo_barras']
    dados_conexao = ("Driver={SQL Server};"
                     "Server=DESKTOP-JRD01KQ;"
                     "Database=PROJETO_SOFTWARE;")

    cnx = pyodbc.connect(dados_conexao)
    cursor = cnx.cursor()
    
    inserir_produto = f"""INSERT INTO Produto(nome_produto, valor, tipo, marca, codigo_barras) VALUES('{produto}', {preco},'{tipo}','{marca}','{codigo_barras}')"""
    cursor.execute(inserir_produto)
    cnx.commit()
    cnx.close()

def atualizar_produto(): 
    produto = request.form['produto']
    preco = float (request.form['preco'])
    tipo = request.form['tipo']
    marca = request.form['marca']
    codigo_barras = request.form['codigo_barras']
    dados_conexao = ("Driver={SQL Server};"
                     "Server=DESKTOP-JRD01KQ;"
                     "Database=PROJETO_SOFTWARE;")

    cnx = pyodbc.connect(dados_conexao)
    cursor = cnx.cursor()
    
    inserir_produto = f"""UPDATE Produto SET nome_produto = '{produto}', valor = {preco} , tipo = '{tipo}', marca = '{marca}', codigo_barras = '{codigo_barras}') WHERE nome_produto = '{produto}'"""
    cursor.execute(inserir_produto)
    cnx.commit()
    cnx.close()


if __name__ == '__main__':
    app.run(debug=True)