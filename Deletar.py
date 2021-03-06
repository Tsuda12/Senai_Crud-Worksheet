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
        self.janela.btn_deletar.clicked.connect(self.deletar_hospedagem)
        self.janela.show()


    #MÉTODOS
    def deletar_hospedagem(self):
        self.item_deletado = self.janela.spb_numero.text()

        self.planilha.drop(int(self.item_deletado), axis=0, inplace=True)

        self.planilha.to_excel("planilha/Hospedagem.xlsx", index=False)

    def mostrar_planilha(self):
        self.planilha.fillna('', inplace=True)

        self.janela.tbl_planilha.setRowCount(self.planilha.shape[0])
        self.janela.tbl_planilha.setColumnCount(self.planilha.shape[1])
        self.janela.tbl_planilha.setHorizontalHeaderLabels(self.planilha.columns)

        for linha in self.planilha.iterrows():
            valores = linha[1]
            for coluna, valor in enumerate(valores):
                if isinstance(valor, (float, int)):
                    valor = '{0:0,.0f}'.format(valor)
                item_tabela = QtWidgets.QTableWidgetItem(str(valor))
                self.janela.tbl_planilha.setItem(linha[0], coluna, item_tabela)