import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from display import Display
from info import Info
from styles import setupTheme
from buttons import ButtonsGrid


if __name__ == "__main__":
    # cria applicação]
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Define o icono
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info("")
    window.addWidgetToVLayout(info)

    # Display 
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonGrid)

    # # Buttons
    # button1 = Button("Texto do botão")
    # buttonGrid.addWidget(button1, 0, 0)
    # button2 = Button("Texto do botão")
    # buttonGrid.addWidget(button2, 0, 1)


    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
