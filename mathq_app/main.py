from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QRadioButton, QButtonGroup
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import utils

app = QApplication([])
controller = utils.Controlador()
controller.menu.show()
app.exec_()