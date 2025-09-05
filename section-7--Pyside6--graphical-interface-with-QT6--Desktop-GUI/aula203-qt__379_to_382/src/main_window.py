import sys
from typing import cast

from PySide6.QtCore import QEvent, QObject
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QApplication, QMainWindow
from window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.sendButton.clicked.connect(self.changeLabelResult)

        self.ui.nameLineEdit.installEventFilter(self)

    def changeLabelResult(self):
        name = self.ui.nameLineEdit.text()
        self.ui.labelResult.setText(f"Hello, {name}!")
        self.ui.nameLineEdit.clear()
        self.ui.nameLineEdit.setFocus()

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.KeyPress:
            # Tenho certeza que o evento e do tipo KeyPress
            event = cast(QKeyEvent, event)

            text = self.ui.nameLineEdit.text()
            self.ui.labelResult.setText(text + event.text())

        return super().eventFilter(watched, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
