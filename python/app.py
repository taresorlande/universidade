from screen.tela_cadastro import TelaCadastro
from screen.tela_listagem import TelaListagem

import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton
)

class App:
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.janela = QWidget()
        self.layout = QVBoxLayout()

        self.janela.setWindowTitle("Sistema Universidade")
        self.janela.resize(400, 200)
        self.janela.setLayout(self.layout)

        self.criar_botoes()

        self.janela.show()
        self.abrir_listagem()

    def criar_botoes(self):

        btn_listar = QPushButton("Listar Alunos")
        btn_cadastrar = QPushButton("Cadastrar Aluno")

        self.layout.addWidget(btn_listar)
        self.layout.addWidget(btn_cadastrar)

        btn_listar.clicked.connect(self.abrir_listagem)
        btn_cadastrar.clicked.connect(self.abrir_cadastro)

    def abrir_listagem(self):
        self.tela_listagem = TelaListagem(self.app)
        self.tela_listagem.janela.show()

    def abrir_cadastro(self):
        self.tela_cadastro = TelaCadastro(self.app)
        self.tela_cadastro.janela.show()

if __name__ == "__main__":
    sistema = App()
    sys.exit(sistema.app.exec())