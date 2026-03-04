from modules.mysql import MySQL
from modules.aluno import Aluno

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)

from PySide6.QtCore import Qt


class Cadastrar:
    def __init__(self, app):
        self.app = app
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        self.banco = MySQL()

        self.campos = {}

        self.configurar_janela()
        self.criar_componentes()
        self.aplicar_estilo()

    def configurar_janela(self):
        self.janela.setWindowTitle("Sistema Universidade - Cadastro de Aluno")

        screen = self.app.primaryScreen().geometry()
        largura = int(screen.width() * 0.5)
        altura = int(screen.height() * 0.7)

        self.janela.resize(largura, altura)
        self.janela.setMinimumSize(600, 500)
        self.janela.setLayout(self.layout)

    def criar_componentes(self):

        titulo = QLabel("CADASTRO DE ALUNO")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setObjectName("titulo")
        self.layout.addWidget(titulo)

        componentes = {
            "nome": "Nome",
            "email": "Email",
            "cpf": "CPF",
            "telefone": "Telefone",
            "endereco": "Endereço"
        }

        for chave, texto in componentes.items():
            label = QLabel(texto)
            campo = QLineEdit()
            campo.setPlaceholderText(f"Digite o {texto.lower()}")

            self.layout.addWidget(label)
            self.layout.addWidget(campo)

            self.campos[chave] = campo

        barra_botoes = QHBoxLayout()

        botao_cadastro = QPushButton("Cadastrar")
        botao_cadastro.setObjectName("botaoPrimario")

        barra_botoes.addStretch()
        barra_botoes.addWidget(botao_cadastro)

        self.layout.addLayout(barra_botoes)

        botao_cadastro.clicked.connect(self.cadastrar)

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
                color: #1e8449;
                margin: 15px;
            }

            QLabel {
                margin-top: 10px;
                font-weight: 600;
                color: #2c3e50;
            }

            QLineEdit {
                background-color: white;
                border: 1px solid #dcdcdc;
                padding: 8px;
                border-radius: 4px;
            }

            QLineEdit:focus {
                border: 2px solid #1e8449;
            }

            QPushButton {
                padding: 8px 20px;
                border-radius: 4px;
                font-weight: bold;
            }

            QPushButton#botaoPrimario {
                background-color: #1e8449;
                color: white;
            }

            QPushButton#botaoPrimario:hover {
                background-color: #239b56;
            }
        """)

    def validar_campos(self):
        dados = {chave: campo.text().strip() for chave, campo in self.campos.items()}

        for chave, valor in dados.items():
            if not valor:
                return False, f"O campo '{chave}' não pode estar vazio."

        if not dados["cpf"].isdigit() or len(dados["cpf"]) != 11:
            return False, "CPF deve conter exatamente 11 números."

        return True, dados

    def cadastrar(self):

        valido, resultado = self.validar_campos()

        if not valido:
            QMessageBox.warning(
                self.janela,
                "Validação",
                resultado
            )
            return

        aluno = Aluno(
            resultado["nome"],
            resultado["email"],
            resultado["cpf"],
            resultado["telefone"],
            resultado["endereco"],
        )

        try:
            self.banco.connect()
            aluno.cadastrar(self.banco)

            QMessageBox.information(
                self.janela,
                "Sucesso",
                "Aluno Cadastrado!"
            )
            self.limpar_campos()

        except Exception as e:
            QMessageBox.critical(
                self.janela,
                "Erro",
                f"Erro ao Cadastrar: {e}"
            )

        finally:
            self.banco.disconnect()

    def limpar_campos(self):
        for campo in self.campos.values():
            campo.clear()