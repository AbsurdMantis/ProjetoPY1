import sqlite3


initbank = sqlite3.connect("yellowallertbank.db")
pointer = initbank.cursor()

pointer.execute("""CREATE TABLE IF NOT EXISTS Inventario (
       Ingrediente TEXT,
       Quantidade REAL)
               """)
pointer.execute("""CREATE TABLE IF NOT EXISTS Receitas (
       Prato TEXT,
       Ingrediente TEXT,
       Quantidade REAL)
       """)
pointer.execute("""CREATE TABLE IF NOT EXISTS Inventarioback (
       Ingrediente TEXT,
       Quantidade REAL)
               """)

inventario = []
recipe = []
platess = []
dailycomsumption = []
resultlist = []
inventarioback = []


def inventario0():
    inputingredient = str(input("Adicione o ingrediente, quando acabar digite 0:"))
    if inputingredient == "0":
        print(inventario)
    else:
        inputquanty = float(input("Insira a quantidade do mesmo ingrediente:"))
        invent1 = (inputingredient, inputquanty)
        inventario.append(tuple(invent1))
        inventarioback.append(tuple(invent1))
        inventario0()



def plateinterface():
    global inputplate
    inputplate = str(input("Insira aqui o nome do prato que deseja listar:"))
    platess.append(inputplate)
    recipe0()



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


def dailycomsu():
    for h in platess:
        print("Indique quantas vezes", h, "foi consumido hoje:")
        inputquantyconsumed = int(input("--"))
        for (x, y) in inventario:
            for (a, b, c) in recipe:
                if a == h:
                    if x == b:
                        global reference
                        global specific
                        global results
                        reference = y
                        specific = x
                        results = y - c * inputquantyconsumed
                        resultcalc = (specific, results)
                        resultlist.append(tuple(resultcalc))
                        pointer.execute("""
                        UPDATE Inventario SET Quantidade = '{}' WHERE Ingrediente = '{}'
                        """.format(results, specific))


def YellowAlert():
    for (a, b) in inventario:
        for (c, d) in resultlist:
            if c == a:
                f = d/b
                p = f*100
                if f >= 0.41:
                    print(c, "está em nível verde com", p, "% do inventário inicial")
                elif 0.21 <= f < 0.41:
                    print(c, "está em nível amarelo com", p, "% do inventário inicial")
                elif 0 <= f <= 0.20:
                    print(c, "está em nível vermelho com", p, "% do inventário inicial")

def IdleAlert():
    for (a, b) in inventario:
        for (c, d) in inventarioback:
            if c == a:
                f = d/b
                p = f*100
                if f >= 0.41:
                    print(c, "está em nível verde com", p, "% do inventário inicial")
                elif 0.21 <= f < 0.41:
                    print(c, "está em nível amarelo com", p, "% do inventário inicial")
                elif 0 <= f <= 0.20:
                    print(c, "está em nível vermelho com", p, "% do inventário inicial")

inputy = str(input("Deseja adicionar algo no inventário? 0 = Sim 1 = Não"))
if inputy == "0":
    inventario0()
    pointer.executemany("INSERT INTO Inventario VALUES(?, ?)", inventario)
    pointer.executemany("INSERT INTO Inventarioback VALUES(?, ?)", inventarioback)
    YellowAlert()
else:
    pointer.execute("""SELECT * FROM Inventario""")
    inventario = pointer.fetchall()
    inventarioback = pointer.fetchall()
    print("O inventário atual é:")
    for (a, b) in inventario:
        print("Ingrediente:", a, "-----", "Quantidade KG ou L:", b)
    IdleAlert()


inputp = str(input("Deseja adicionar algo no cardápio? 0 = Sim 1 = Não"))
if inputy == "0":
    plateinterface()
    pointer.executemany("INSERT INTO Receitas VALUES(?, ?, ?)", recipe)
else:
    pointer.execute("""SELECT * FROM Receitas""")
    recipe = pointer.fetchall()
    for (a, b, c) in recipe:
        platess.append(a)
    print("O cardápio atual é:")
    for t in recipe:
        print(t[0], "-", t[1], "-", t[2])

inputchecker = str(input("Houve consumo hoje? 0 = Sim 1 = Não"))
if inputchecker == "0":
    dailycomsu()
    YellowAlert()

initbank.commit()
