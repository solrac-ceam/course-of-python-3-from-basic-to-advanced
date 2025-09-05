from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, /, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Titulo da janela
        self.setWindowTitle("Calculadora")

        # Configurando o layout básico
        self.central_widget = QWidget()
        self.vLayout = QVBoxLayout()

        self.central_widget.setLayout(self.vLayout)
        self.setCentralWidget(self.central_widget)

    def adjustFixedSize(self):
        # Última coisa a sser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self) -> QMessageBox:
        return QMessageBox(self)
