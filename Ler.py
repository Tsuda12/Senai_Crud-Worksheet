#IMPORTS
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import janelaspy.LerTela
import pandas as pd


#CLASSE
class Ler(janelaspy.LerTela.Ui_Form):
    def __init__(self):
        self.janela = uic.loadUi("janelasui/ler.ui")
        self.planilha = pd.read_excel("planilha/Hospedagem.xlsx")
        self.alimentar_combobox()
        self.janela.lbl_numero_linhas.setText(f"{len(self.planilha)}")
        self.janela.btn_ler.clicked.connect(self.encontrar_hospedagem)
        self.janela.show()

    def alimentar_combobox(self):
        lista_colunas = []

        for coluna in self.planilha.columns:
            lista_colunas.append(coluna)

        for coluna in lista_colunas:
            self.janela.cbx_coluna.addItem(coluna)

    def encontrar_hospedagem(self):
        coluna_escolhida = self.janela.cbx_coluna.currentText()
        linha_escolhida = int(self.janela.spb_numero.text())

        resultado = self.planilha.loc[linha_escolhida, coluna_escolhida]

        self.janela.lbl_encontrado_2.setText(f"{resultado}")
