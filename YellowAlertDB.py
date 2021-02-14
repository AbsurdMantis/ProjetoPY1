import sqlite3

inventario = []
inventariobackup = []
recipe = []
platess = []
#TODO: CRIAR FUNÇÃO PARA DISPLAY DE CARDÁPIO INTEGRANDO AO BANCO DE DADOS
dailycomsumption = []

#Adiciona ps items da tabela de inventário
def inventario0():
    inputingredient = str(input("Adicione o ingrediente, quando acabar digite 0:"))
    if inputingredient == "0":
        print(inventario)
        pass
    else:
        inputquanty = float(input("Insira a quantidade do mesmo ingrediente:"))
        invent1 = (inputingredient, inputquanty)
        inventario.append(tuple(invent1))
        inventariobackup.append(tuple(invent1))
        inventario0()

#Cria os pratos
def plateinterface():
    global inputplate
    inputplate = str(input("Insira aqui o nome do prato que deseja listar:"))
    platess.append(inputplate)
    recipe0()

#Adiciona os ingredientes desse mesmo prato
def recipe0():
    inputI = str(input("Insira o ingrediente do prato:"))
    inputQ = float(input("Insira a quantidade do ingrediente:"))
    invent = (inputplate, inputI, inputQ)
    recipe.append(tuple(invent))
    inputV = str(input("Deseja adicionar outro ingrediente?  0 = Sim 1 = Não"))
    if inputV == '0':
        recipe0()
    else:
        inputV = str(input("Deseja incluir outro prato?:  0 = Sim 1 = Não"))
        if inputV == '0':
            plateinterface()
        else:
            pass

#Avalia o consumo diário para subtrair do inventário
def dailycomsu():
    inputconsumed = str(input("Indique o prato consumido hoje:"))
    inputquantyconsumed = int(input("Indique quantas vezes o prato foi consumido:"))
    for (x, y) in inventario:
        for (a, b, c) in recipe:
            if a == inputconsumed:
                if x == b:
                    global reference
                    global specific
                    global results
                    reference = y
                    specific = x
                    results = y - c * inputquantyconsumed
                    print(results)
#TODO: TRANSFORMAR ISSO EM LOOP PARA OUTROS PRATOS

inventario0()
plateinterface()
dailycomsu()

#cria o banco e o adiciona a função pointer para executar o sqlite
initbank = sqlite3.connect("ftbankteste1577.db")
pointer = initbank.cursor()

#cria as tabelas necessárias das funções acima
pointer.execute("""CREATE TABLE Inventario (
       Ingrediente TEXT,
       Quantidade REAL)
               """)
pointer.execute("""CREATE TABLE Receitas (
       Prato TEXT,
       Ingrediente TEXT,
       Quantidade REAL)
       """)
#adiciona os items das funções às tabelas
pointer.executemany("INSERT INTO Inventario VALUES(?, ?)", inventario)
pointer.executemany("INSERT INTO Receitas VALUES(?, ?, ?)", recipe)

#dá update baseado no consumo diário
pointer.execute("""
                UPDATE Inventario SET Quantidade = '{}' WHERE Ingrediente = '{}'
                """.format(results, specific))
#fetch
testeitem = pointer.fetchall()

for x in testeitem:
    print(x)
#fecha o banco
#TODO:PARA FAZER O YELLOW ALERT COM UM FOR NECESSARIO ANTES FORMAR O LOOP DA FUNC DAILY COMSUMPTION
#def YellowAlert():
#    for (x,y) in results:
#        for (a,b) in inventariobackup:
#            c = y/b
#            if c >= 0.41:
#                print("Verde")
#            elif 0.21 <= c < 0.41:
#                print("Amarelo")
#           elif 0.20 <= c <= 0:
#                print("Vermelho")

#YellowAlert()

initbank.commit()
