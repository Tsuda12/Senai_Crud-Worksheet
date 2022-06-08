#IMPORTS
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import janelaspy.AtualizarTela
import pandas as pd


#CLASSE
class Atualizar(janelaspy.AtualizarTela.Ui_Form):
    #CONSTRUTOR
    def __init__(self):
        self.janela = uic.loadUi("janelasui/atualizar.ui")
        self.planilha = pd.read_excel("planilha/Hospedagem.xlsx")
        self.mostrar_planilha()
        self.alimentar_combobox()
        self.janela.btn_atualizar.clicked.connect(self.atualizar_hospedagem)
        self.janela.show()


    #MÉTODOS
    def atualizar_hospedagem(self):
        numero_linha = self.janela.spb_numero.text()
        coluna = self.janela.cbx_coluna.currentText()

        self.planilha.loc[int(numero_linha), coluna] = self.janela.lineEdit.text()

        self.planilha.to_excel("planilha/Hospedagem.xlsx", index=False)

    def alimentar_combobox(self):
        lista_colunas = []

        for coluna in self.planilha.columns:
            lista_colunas.append(coluna)

        for coluna in lista_colunas:
            self.janela.cbx_coluna.addItem(coluna)

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
