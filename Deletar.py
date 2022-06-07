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
        self.mostrar_planilha()
        #elf.janela.btn_deletar.clicked.connect(self.deletar_hospedagem)
        self.janela.show()


    #MÉTODOS
    def mostrar_planilha(self):
        #--Exibe linhas e colunas da planilha
        self.janela.tbl_planilha.setRowCount(self.planilha.shape[0])
        self.janela.tbl_planilha.setColumnCount(self.planilha.shape[1])

        #--Nomeia as colunas
        self.janela.tbl_planilha.setHorizontalHeaderLabels(self.planilha.columns)

        #--Itens nas linhas