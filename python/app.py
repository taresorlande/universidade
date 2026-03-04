from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QLabel
)

from PySide6.QtCore import Qt

from screen.cadastrar import Cadastrar
from screen.listar import Listar

import sys


class App:

    def __init__(self):
        self.app = QApplication(sys.argv)

        self.janela = QWidget()
        self.layout = QVBoxLayout()

        self.janela.setWindowTitle("Sistema Universidade")

        screen = self.app.primaryScreen().geometry()
        largura = int(screen.width() * 0.5)
        altura = int(screen.height() * 0.35)

        self.janela.resize(largura, altura)
        self.janela.setLayout(self.layout)

        self.tela_listagem = None
        self.tela_cadastro = None

        self.criar_componentes()
        self.aplicar_estilo()

        self.janela.show()

    def criar_componentes(self):

        # 🔹 Título
        self.titulo = QLabel("SISTEMA UNIVERSIDADE")
        self.titulo.setObjectName("titulo")
        self.titulo.setAlignment(Qt.AlignCenter)

        # 🔹 Subtítulo
        self.subtitulo = QLabel("Menu Principal")
        self.subtitulo.setObjectName("subtitulo")
        self.subtitulo.setAlignment(Qt.AlignCenter)

        self.layout.addStretch()
        self.layout.addWidget(self.titulo)
        self.layout.addWidget(self.subtitulo)
        self.layout.addSpacing(30)

        # 🔹 Botões
        self.botao_listar = QPushButton("Listar Alunos")
        self.botao_listar.setObjectName("botaoPrimario")
        self.botao_listar.clicked.connect(self.abrir_listagem)

        self.botao_cadastrar = QPushButton("Cadastrar Aluno")
        self.botao_cadastrar.setObjectName("botaoPrimario")
        self.botao_cadastrar.clicked.connect(self.abrir_cadastro)

        self.layout.addWidget(self.botao_listar)
        self.layout.addWidget(self.botao_cadastrar)
        self.layout.addStretch()

    def aplicar_estilo(self):

        self.janela.setStyleSheet("""

            QWidget {
                background-color: #fdf2f2;
                font-family: Segoe UI;
                font-size: 14px;
            }

            QLabel#titulo {
                font-size: 24px;
                font-weight: bold;
                color: #641e16;
            }

            QLabel#subtitulo {
                font-size: 16px;
                color: #922b21;
            }

            QPushButton {
                padding: 10px;
                border-radius: 6px;
                font-weight: bold;
            }

            QPushButton#botaoPrimario {
                background-color: #7b1e1e;
                color: white;
            }

            QPushButton#botaoPrimario:hover {
                background-color: #a93226;
            }
        """)

    def abrir_listagem(self):

        if self.tela_listagem is None:
            self.tela_listagem = Listar(self.app)

        self.tela_listagem.janela.show()

    def abrir_cadastro(self):

        if self.tela_cadastro is None:
            self.tela_cadastro = Cadastrar(self.app)

        self.tela_cadastro.janela.show()


if __name__ == "__main__":
    system = App()
    sys.exit(system.app.exec())