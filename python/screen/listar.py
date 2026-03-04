from modules.mysql import MySQL
from modules.aluno import Aluno

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QLabel
)

from PySide6.QtCore import Qt


class Listar:
    def __init__(self, app):
        self.app = app
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        self.banco = MySQL()

        self.configurar_janela()
        self.criar_componentes()
        self.aplicar_estilo()
        self.carregar_dados()

    def configurar_janela(self):
        self.janela.setWindowTitle("Sistema Universidade - Listagem de Alunos")

        screen = self.app.primaryScreen().geometry()
        largura = int(screen.width() * 0.7)
        altura = int(screen.height() * 0.75)

        self.janela.resize(largura, altura)
        self.janela.setMinimumSize(900, 500)
        self.janela.setLayout(self.layout)

    def criar_componentes(self):

        titulo = QLabel("LISTAGEM DE ALUNOS")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setObjectName("titulo")

        self.layout.addWidget(titulo)

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels(
            ["ID", "Nome", "Email", "CPF", "Telefone", "Matrícula"]
        )

        self.tabela.setAlternatingRowColors(True)
        self.tabela.setSelectionBehavior(QTableWidget.SelectRows)
        self.tabela.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.tabela.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)

        self.layout.addWidget(self.tabela)

        barra_botoes = QHBoxLayout()

        botao_atualizar = QPushButton("Atualizar")
        botao_atualizar.setObjectName("botaoPrimario")

        barra_botoes.addStretch()
        barra_botoes.addWidget(botao_atualizar)

        self.layout.addLayout(barra_botoes)

        botao_atualizar.clicked.connect(self.carregar_dados)

    def aplicar_estilo(self):

        self.janela.setStyleSheet("""

            QWidget {
                background-color: #f4f6f9;
                font-family: Segoe UI;
                font-size: 14px;
            }

            QLabel#titulo {
                font-size: 22px;
                font-weight: bold;
                color: #2c3e50;
                margin: 15px;
            }

            QTableWidget {
                background-color: white;
                border: 1px solid #dcdcdc;
                gridline-color: #eeeeee;
                color: #000000;
            }

            QHeaderView::section {
                background-color: #2c3e50;
                color: white;
                padding: 8px;
                border: none;
                font-weight: bold;
            }

            QTableWidget::item:selected {
                background-color: #3498db;
                color: white;
            }

            QPushButton {
                padding: 8px 18px;
                border-radius: 4px;
                font-weight: bold;
            }

            QPushButton#botaoPrimario {
                background-color: #2c3e50;
                color: white;
            }

            QPushButton#botaoPrimario:hover {
                background-color: #34495e;
            }
        """)

    def carregar_dados(self):

        self.banco.connect()
        alunos = Aluno.listar(self.banco)
        self.banco.disconnect()

        self.tabela.setRowCount(len(alunos))

        for linha, aluno in enumerate(alunos):
            self.tabela.setItem(linha, 0, QTableWidgetItem(str(aluno["id"])))
            self.tabela.setItem(linha, 1, QTableWidgetItem(aluno["nome"]))
            self.tabela.setItem(linha, 2, QTableWidgetItem(aluno["email"]))
            self.tabela.setItem(linha, 3, QTableWidgetItem(aluno["cpf"]))
            self.tabela.setItem(linha, 4, QTableWidgetItem(aluno["telefone"]))
            self.tabela.setItem(linha, 5, QTableWidgetItem("Ativo" if aluno["matricula"] else "Inativo"))