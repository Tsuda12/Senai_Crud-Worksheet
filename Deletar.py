#IMPORTS
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import janelaspy.DeletarTela
import pandas as pd


#CLASSE
class Deletar(janelaspy.DeletarTela.Ui_Form):
    #CONSTRUTOR
    def __init__(self):
        self.janela = uic.loadUi("janelasui/deletar.ui")
        self.planilha = pd.read_excel("planilha/Hospedagem.xlsx")
        self.janela.btn_deletar.clicked.connect(self.deletar_hospedagem)
        self.janela.show()


    #MÉTODOS
    def deletar_hospedagem(self):
        print('Deletado')