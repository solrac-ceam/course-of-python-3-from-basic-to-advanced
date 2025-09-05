import math
from typing import TYPE_CHECKING

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton
from utils import isEmpty, isNumOrDot, isValidnumber, stringToNumber
from variables import MEDIUM_FONT_SIZE

if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow


class Button(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        # self.setStyleSheet(f"font-size: {MEDIUM_FONT_SIZE}px;")
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(
        self,
        display: "Display",
        info: "Info",
        window: "MainWindow",
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.display = display
        self.info = info
        self.window = window

        self._gridMask = [
            ["C", "◀", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["N", "0", ".", "="],
        ]
        self._equation = ""
        self._leftNumber = None
        self._rightNumber = None
        self._operator = None

        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        self.display.eqPressed.connect(self._equalClicked)
        self.display.delPressed.connect(self.display.backspace)
        self.display.clearPressed.connect(self._reset)
        self.display.inputPressed.connect(self._insertTextToDisplay)
        self.display.operatorPressed.connect(self._operatorPressed)

        for i, rowData in enumerate(self._gridMask):
            for j, columnData in enumerate(rowData):
                button = Button(text=columnData)
                if not isNumOrDot(columnData) and not isEmpty(columnData):
                    button.setProperty("cssClass", "specialButton")
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)
                button.clicked.connect(
                    self._makeButtonSlot(self._insertTextToDisplay, button.text())
                )

    def _makeButtonSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)

        return realSlot

    @Slot()
    def _insertTextToDisplay(self, buttonText: str):
        newDisplayValue = self.display.text() + buttonText
        if not isValidnumber(newDisplayValue):
            return

        self.display.insert(buttonText)

    def _configSpecialButton(self, button: Button):
        text = button.text()

        if text == "C":
            button.clicked.connect(self._reset)

        if text in "+-*/^":
            button.clicked.connect(
                self._makeButtonSlot(self._operatorPressed, operator=text)
            )

        if text == "=":
            button.clicked.connect(self._equalClicked)

        if text == "◀":
            button.clicked.connect(self.display.backspace)

        if text == "N":
            button.clicked.connect(self._invertNumber)

    @Slot()
    def _reset(self):
        self._leftNumber = None
        self._rightNumber = None
        self._operator = None
        self.equation = ""
        self.display.clear()

    @Slot()
    def _operatorPressed(self, operator: str):
        displayText = self.display.text()
        if not isValidnumber(displayText) and self._leftNumber is None:
            self._showError("Vocẽ não digitou nada.")
            return

        if self._leftNumber is None:
            self._leftNumber = displayText

        self._operator = operator
        self.equation = f"{self._leftNumber} {self._operator}"
        self.display.clear()

    @Slot()
    def _equalClicked(self):
        displayText = self.display.text()
        if not isValidnumber(displayText) or self._leftNumber is None:
            self._showError("Equação imcompleta.")
            return

        self._rightNumber = displayText
        self.equation = f"{self.equation} {self._rightNumber}"

        try:
            if self._operator == "^" and self._leftNumber is not None:
                result = math.pow(float(self._leftNumber), float(self._rightNumber))
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            result = "NaN"
            self._showError("Divisão por zero.")
        except OverflowError:
            result = "Error"
            self._showError("Essa conta não pode ser realizada.")

        if result not in ["NaN", "Error"]:
            result = str(result)
            self.display.setText(result)
            self._leftNumber = None
            self._rightNumber = None
        else:
            self._reset()

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()
        if not isValidnumber(displayText):
            self._showError("No se puede invertir porque no es nm número.")
            return

        newNumber = -stringToNumber(displayText)
        self.display.setText(str(newNumber))

    def _showError(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
