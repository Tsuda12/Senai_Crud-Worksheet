#IMPORTS
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import janelaspy.CriarTela
import pandas as pd


#CLASSE
class Criar(janelaspy.CriarTela.Ui_Form):
    #CONSTRUTOR
    def __init__(self):
        self.janela = uic.loadUi("janelasui/criar.ui")
        self.planilha = pd.read_excel("planilha/Hospedagem.xlsx")
        self.janela.btn_enviar.clicked.connect(self.criar_hospedagem)
        self.janela.show()


    #MÉTODOS
    def criar_hospedagem(self):
        qtd_linha = len(self.planilha)

        for i in range(1, qtd_linha):
            self.planilha.loc[qtd_linha+1, 'Ano'] = int(self.janela.spb_ano.text())
            self.planilha.loc[qtd_linha+1, 'Proponente'] = self.janela.lne_propornente.text().upper()
            self.planilha.loc[qtd_linha+1, 'Proposto'] = self.janela.lne_proposto.text().upper()
            self.planilha.loc[qtd_linha+1, 'Tipo Proposto'] = self.janela.cbx_tipo_proposto.currentText().upper()
            self.planilha.loc[qtd_linha+1, 'Data Cadastro'] = self.janela.dt_data_cadastrada.text()
            self.planilha.loc[qtd_linha+1, 'Data Entrada'] = self.janela.dt_data_entrada.text()
            self.planilha.loc[qtd_linha+1, 'Data Saida'] = self.janela.dt_data_saida.text()
            self.planilha.loc[qtd_linha+1, 'Convenio'] = self.janela.cbx_convenio.currentText().upper()
            self.planilha.loc[qtd_linha+1, 'Id Unidade Requisitante'] = int(self.janela.spb_id_requisitante.text())
            self.planilha.loc[qtd_linha + 1, 'Nome Unidade Requisitante'] = self.janela.lne_nome_requisitante.text().upper()
            self.planilha.loc[qtd_linha + 1, 'Id Unidade Custo'] = int(self.janela.spb_id_custo.text())
            self.planilha.loc[qtd_linha + 1, 'Nome Unidade Custo'] = self.janela.lne_nome_custo.text().upper()
            self.planilha.loc[qtd_linha + 1, 'Valor'] = self.janela.spb_valor.text()
            self.planilha.loc[qtd_linha+1, 'Status'] = self.janela.cbx_status.currentText().upper()

        self.planilha.to_excel("planilha/Hospedagem.xlsx", index=False)