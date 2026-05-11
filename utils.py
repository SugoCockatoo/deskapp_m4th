from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QRadioButton, QButtonGroup, QListWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

# Menu 
class Menu(QWidget):
    def __init__(self):
        super().__init__()
        bigger_font = QFont("Arial", 36)

        self.resize(1920, 1080) 
        self.title = QLabel("M4THQ APP")
        self.title.setFont(bigger_font)
        self.button1 = QPushButton('Tests')
        self.button2 = QPushButton('Topics')
        self.button3 = QPushButton('Create')

        self.setWindowTitle("M4thQ App") 
        # Connect the signal to trigger when a button is clicked
        layoutV = QVBoxLayout()
        layoutH1 = QHBoxLayout()
        layoutH2 = QHBoxLayout()

        layoutH1.addWidget(self.button1, alignment = Qt.AlignCenter)
        layoutH1.addWidget(self.button2, alignment = Qt.AlignCenter)
        layoutH1.addWidget(self.button3, alignment = Qt.AlignCenter)
        layoutV.addWidget(self.title, alignment = Qt.AlignHCenter | Qt.AlignTop)

        layoutV.addLayout(layoutH1)
        layoutV.addLayout(layoutH2)
        self.setLayout(layoutV)

# test directory 
class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        bigger_font = QFont("Arial", 20)

        self.resize(720, 480) 
        self.title = QLabel("Dashboard")
        self.title.setFont(bigger_font)

        self.setWindowTitle("Dashboard/M4thQ App") 
        #Button Objects
        self.button_4 = QPushButton('Back')
        test_names = [
            'Limits_Basics_Test', 'Derivatives_Basics_Test', 'Integrals_Basics_Test',
            'Chain_Rule_Practice', 'Power_Rule_Review', 'Trig_Substitution_Lab',
            'Partial_Derivatives_Intro', 'Differential_Equations_101', 
            'Vector_Calculus_Basics', 'Infinite_Series_Convergence'
        ]

        # 2. Initialize the back button and the group
        self.button_4 = QPushButton('Back')
        self.button_group = QButtonGroup(self) # Setting 'self' manages memory better

        # 3. Use a list comprehension or loop to auto-create and group
        self.radio_buttons = []

        for i, name in enumerate(test_names, start=1):
            rb = QRadioButton(name)
            self.radio_buttons.append(rb)          # Keep a reference in a list
            self.button_group.addButton(rb, id=i)

        # Connect the signal to trigger when a button is clicked
        #button_group.idClicked.connect(on_button_clicked)
        layoutV = QVBoxLayout()
        layoutH1 = QHBoxLayout()
        layoutH2 = QHBoxLayout()

        layoutV.addWidget(self.title, alignment = Qt.AlignCenter | Qt.AlignTop)
        for rb in self.radio_buttons:
            layoutV.addWidget(rb, alignment=Qt.AlignCenter | Qt.AlignLeft)
        layoutH2.addWidget(self.button_4, alignment = Qt.AlignBottom | Qt.AlignLeft)
        
        selected_id = self.button_group.checkedId()
        button = self.button_group.button(selected_id)
        print(button)

        layoutV.addLayout(layoutH1)
        layoutV.addLayout(layoutH2)
        self.setLayout(layoutV)
        
# --- LA LÓGICA PARA CAMBIAR ---
class Controlador:
    def __init__(self):
        # Creamos las dos ventanas pero no las mostramos todavía
        self.menu = Menu()
        self.dash = Dashboard()

        # Conectamos los botones con las funciones de cambio
        self.menu.button1.clicked.connect(self.mostrar_dash)
        self.dash.button_4.clicked.connect(self.mostrar_menu)

    def mostrar_menu(self):
        self.dash.hide() # Escondemos el juego
        self.menu.show() # Mostramos el menú

    def mostrar_dash(self):
        self.menu.hide() # Escondemos el menú
        self.dash.show() # Mostramos el juego
