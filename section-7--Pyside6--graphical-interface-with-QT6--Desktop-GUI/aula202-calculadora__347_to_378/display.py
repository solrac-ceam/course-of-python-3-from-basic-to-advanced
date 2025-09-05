from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from utils import isEmpty, isNumOrDot
from variables import BIG_FONT_SIZE, MINIMUN_WIDTH, TEXT_MARGIN


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px;")
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUN_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])

    def keyPressEvent(self, event: QKeyEvent) -> None:
        # super().keyPressEvent(event)
        key = event.key()
        text = event.text()

        isEnter = key in [Qt.Key.Key_Enter, Qt.Key.Key_Return]
        isDelete = key in [Qt.Key.Key_Backspace, Qt.Key.Key_Delete]
        isEsc = key == Qt.Key.Key_Escape
        isOperator = key in [
            Qt.Key.Key_Plus,
            Qt.Key.Key_Minus,
            Qt.Key.Key_Slash,
            Qt.Key.Key_Asterisk,
        ]

        if isEnter:
            self.eqPressed.emit()
            return event.ignore()

        if isDelete:
            self.delPressed.emit()
            return event.ignore()

        if isEsc:
            self.clearPressed.emit()
            return event.ignore()

        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()

        if isOperator:
            self.operatorPressed.emit(text)
            return event.ignore()

    # def inputMethodEvent(self, event: QInputMethodEvent) -> None:
    #     print("event", event)
    #     return super().inputMethodEvent(event)
