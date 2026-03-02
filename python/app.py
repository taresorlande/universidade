from PySide6.QtWidgets import QApplication

from screen.cadastrar import Cadastrar
from screen.listar import Listar

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # tela = Cadastrar(app)
    tela = Listar(app)
    tela.janela.show()

    sys.exit(tela.app.exec())