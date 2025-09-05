import sys
from time import sleep

from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget
from workerui import Ui_MyWidget


class Worker(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def __init__(self):
        super().__init__()

    def doWork(self):
        self.started.emit("Starting...")
        for i in range(5):
            sleep(1)
            self.progressed.emit(str(i + 1))
        self.finished.emit("Finished!")


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MyWidget()
        self.ui.setupUi(self)

        self.ui.button1.clicked.connect(self.hardwork1)
        self.ui.button2.clicked.connect(self.hardwork2)

    def hardwork1(self):
        # Isso garante que o widget vai ter uma referência para worker e thread.
        self._worker1 = Worker()
        self._thread1 = QThread()

        # 1 - mover o worker para a thread.
        # Worker é movido para a thread. Todas as funções e métodos do
        # objeto de worker serão executados na thread criado pela QThread.
        self._worker1.moveToThread(self._thread1)

        # 2 - iniciar o trabalho.
        # Quando uma QThread é iniciada, emite o sinal started automaticamente.
        self._thread1.started.connect(self._worker1.doWork)

        # 3 - sair da thread quando o trabalho estiver concluído.
        # O sinal finished é emitido pelo objeto worker quando o trabalho que
        # ele está executando é concluído. Isso aciona o método quit da qthread
        # que interrompe o loop de eventos dela.
        self._worker1.finished.connect(self._thread1.quit)

        # 4 - limpar a memoria.
        # deleteLater solicita a exclusão do objeto worker do sistema de
        # gerenciamento de memória do Python. Quando o worker finaliza, ele
        # emite um sinal finished que vai executar o método deleteLater.
        # Isso garante que objetos sejam removidos da memória corretamente.
        self._thread1.finished.connect(self._thread1.deleteLater)
        self._worker1.finished.connect(self._worker1.deleteLater)

        # 5 - connectar os sinais do worker aos slots.
        # Aqui estão seus métodos e início, meio e fim;
        # execute o que quiser.
        self._worker1.started.connect(self.worker1Started)
        self._worker1.progressed.connect(self.worker1Progressed)
        self._worker1.finished.connect(self.worker1Finished)

        # 6 - iniciar a thread
        self._thread1.start()

    def worker1Started(self, text):
        self.ui.button1.setDisabled(True)
        self.ui.label1.setText(text)

    def worker1Progressed(self, text):
        self.ui.label1.setText(text)

    def worker1Finished(self, text):
        self.ui.label1.setText(text)
        self.ui.button1.setDisabled(False)

    def hardwork2(self):
        self._worker2 = Worker()
        self._thread2 = QThread()

        # 1 - mover o worker para a thread
        self._worker2.moveToThread(self._thread2)

        # 2 - iniciar o trabalho
        self._thread2.started.connect(self._worker2.doWork)

        # 3 - sair da thread quando o trabalho estiver concluído
        self._worker2.finished.connect(self._thread2.quit)

        # 4 - limpar a memoria
        self._thread2.finished.connect(self._thread2.deleteLater)
        self._worker2.finished.connect(self._worker2.deleteLater)

        # 5 - connectar os sinais do worker aos slots
        self._worker2.started.connect(self.worker2Started)
        self._worker2.progressed.connect(self.worker2Progressed)
        self._worker2.finished.connect(self.worker2Finished)

        # 6 - iniciar a thread
        self._thread2.start()

    def worker2Started(self, text):
        self.ui.button2.setDisabled(True)
        self.ui.label2.setText(text)

    def worker2Progressed(self, text):
        self.ui.label2.setText(text)

    def worker2Finished(self, text):
        self.ui.label2.setText(text)
        self.ui.button2.setDisabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    app.exec()
