import pyodbc

#fnção para adicionar produtos e preços
def adicionar_produto(): 
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    tipo = input("Tipo do produto: ")
    marca = input("Marca do produto: ")
    codigo_barras = (input("Código de barras: "))
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
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    tipo = input
    marca = input
    codigo_barras = (input("Código de barras: "))
    dados_conexao = ("Driver={SQL Server};"
                     "Server=DESKTOP-JRD01KQ;"
                     "Database=PROJETO_SOFTWARE;")

    cnx = pyodbc.connect(dados_conexao)
    cursor = cnx.cursor()
    
    inserir_produto = f"""UPDATE Produto SET nome_produto = '{produto}', valor = {preco} , tipo = '{tipo}', marca = '{marca}', codigo_barras = '{codigo_barras}') WHERE nome_produto = '{produto}'"""
    cursor.execute(inserir_produto)
    cnx.commit()
    cnx.close()


while True:
    print("Selecione uma opção:")
    print("1 - Adicionar produto")
    print("2 - Atualizar produto")
    opcao = input("Opção escolhida: ")
    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        atualizar_produto()