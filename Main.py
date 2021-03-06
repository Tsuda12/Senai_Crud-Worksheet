#IMPORTS
from PyQt5 import QtCore, QtGui, QtWidgets
from Criar import Criar
from Ler import Ler
from Atualizar import Atualizar
from Deletar import Deletar
import janelaspy.MenuTela


#CLASSE
class Crud(janelaspy.MenuTela.Ui_MainWindow):
    #CONSTRUTOR
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)
        self.btn_criar.clicked.connect(self.abrir_criar)
        self.btn_ler.clicked.connect(self.abrir_ler)
        self.btn_atualizar.clicked.connect(self.abrir_atualizar)
        self.btn_deletar.clicked.connect(self.abrir_deletar)


    #MÉTODOS
    def abrir_criar(self):
        self.criar = Criar()

    def abrir_ler(self):
        self.ler = Ler()

    def abrir_atualizar(self):
        self.atualizar = Atualizar()

    def abrir_deletar(self):
        self.deletar = Deletar()


#MAIN
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    crud = Crud(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
