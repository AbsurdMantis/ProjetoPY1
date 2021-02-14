import sys



from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5 import QtGui





class Janela(QMainWindow):
    def __init__(self):
        0
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 900
        self.altura = 600
        self.titulo = " Yellow Alert "


# labelingredientes1
        self.label_1 = QLabel(self)  # ecrever no programa
        self.label_1.setText("insira os ingredientes:")
        self.label_1.move(350, 5)
        self.label_1.setStyleSheet('QLabel {color:black ;font: bold; font-size:25px}')
        self.label_1.resize(300, 80)
#caixa de texto 1
        self.caixa_texto1 = QLineEdit(self)
        self.caixa_texto1.move(370,80)
        self.caixa_texto1.resize(190,30)
# botao 1
        botao1 = QPushButton("enter", self)  # botap deuy9 enter 1
        botao1.move(580, 80)
        botao1.resize(50, 30)
        botao1.setStyleSheet('QPushButton {background-color: #EFCE00; font-size:20px}')



# labelpratos2
        self.label_2 = QLabel(self)  # ecrever no programa
        self.label_2.setText("insira o nome do prato:")
        self.label_2.move(350, 100)
        self.label_2.setStyleSheet('QLabel {color:black ;font: bold; font-size:25px}')
        self.label_2.resize(340, 80)

#caixa de texto 2
        self.caixa_texto2 = QLineEdit(self)
        self.caixa_texto2.move(370, 170)
        self.caixa_texto2.resize(190, 30)
# botao 2
        botao2 = QPushButton("enter", self)  # botap de enter 1
        botao2.move(580, 170)
        botao2.resize(50, 30)
        botao2.setStyleSheet('QPushButton {background-color: #EFCE00; font-size:20px}')
        # botao2.clicked.connect(self.botao1_click)

# label3
        self.label_3 = QLabel(self)  # ecrever no programa
        self.label_3.setText("insira os ingredientes do prato:")
        self.label_3.move(350, 190)
        self.label_3.setStyleSheet('QLabel {color:black ;font: bold; font-size:25px}')
        self.label_3.resize(380, 80)
#caixa3
        self.caixa_texto3 = QLineEdit(self)
        self.caixa_texto3.move(370, 260)
        self.caixa_texto3.resize(190, 30)

        botao3 = QPushButton("enter", self)  # botap de enter 1
        botao3.move(580, 260)
        botao3.resize(50, 30)
        botao3.setStyleSheet('QPushButton {background-color: #EFCE00; font-size:20px}')

#label4
        self.label_4 = QLabel(self)  # ecrever no programa
        self.label_4.setText("insira os pratos consumidos:")
        self.label_4.move(350, 280)
        self.label_4.setStyleSheet('QLabel {color:black ;font: bold; font-size:25px}')
        self.label_4.resize(340, 80)

#caixa4
        self.caixa_texto3 = QLineEdit(self)
        self.caixa_texto3.move(370, 350)
        self.caixa_texto3.resize(190, 30)

        botao4 = QPushButton("enter", self)  # botap de enter 1
        botao4.move(580, 350)
        botao4.resize(50, 30)
        botao4.setStyleSheet('QPushButton {background-color: #EFCE00; font-size:20px}')



#botãosair
        botaoS = QPushButton("sair", self)  # botap de enter 1
        botaoS.move(430, 410)
        botaoS.resize(70, 35)
        botaoS.setStyleSheet('QPushButton {background-color: red; font-size:20px}')
        #botaoS.clicked.connect(self.botao1_click)




#logomarca
        self.alert = QLabel(self)
        self.alert.move (10,10)
        self.alert.setPixmap (QtGui.QPixmap('AlertLOgo40.jpeg'))
        self.alert.resize(300,150)


        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    #def botao1_click(self):
        #print ("botao 1 apertado")
        #self.label_1.setText("o teste funcionou")


aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec())