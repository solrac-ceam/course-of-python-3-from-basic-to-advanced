# QSS - Estilos do QT for Python
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
import qdarkstyle
from PySide6.QtWidgets import QApplication
from variables import DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR, PRIMARY_COLOR

qss = f"""
    Button[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    Button[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    Button[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


def setupTheme(app: QApplication):
    # Aplicar o estilo escuro do qdarkstyle
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

    # Sobrepor com o QSS personalizado para estilização adicional
    app.setStyleSheet(app.styleSheet() + qss)
