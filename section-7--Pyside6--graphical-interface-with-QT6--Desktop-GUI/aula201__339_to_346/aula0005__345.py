# O básico sobre Signal e Slots (eventos e documentação)
import sys

from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QPushButton,
    QStatusBar,
    QWidget,
)

from PySide6.QtGui import QAction
from PySide6.QtCore import Slot


@Slot()
def slot_example(status_bar: QStatusBar):
    def inner():
        status_bar.showMessage("O meu slot foi executado")

    return inner


@Slot()
def outro_slot(checked):
    print("Está marcado?", checked)


@Slot()
def terceiro_slot(action: QAction):
    def inner():
        outro_slot(action.isChecked())

    return inner


app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle("Minha janela boniota")

botao1 = QPushButton("Texto do botão")
botao1.setStyleSheet("font-size: 80px;")

botao2 = QPushButton("Botão 2")
botao2.setStyleSheet("font-size: 40px;")

botao3 = QPushButton("Botão 3")
botao3.setStyleSheet("font-size: 40px;")

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

# StatusBar
status_bar = window.statusBar()
status_bar.showMessage("Mostrar mensagem na barra")

# MenuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu("Primeiro menu")
primeira_acao = primeiro_menu.addAction("Primeira ação")
primeira_acao.triggered.connect(slot_example(status_bar))

segunda_action = primeiro_menu.addAction("Segunda ação")
segunda_action.setCheckable(True)
segunda_action.toggled.connect(outro_slot)
segunda_action.hovered.connect(terceiro_slot(segunda_action))

botao1.clicked.connect(terceiro_slot(segunda_action))

window.show()
app.exec()  # Executa o loop da aplicação
