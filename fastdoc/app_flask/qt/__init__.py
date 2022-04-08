from PyQt5.QtCore import Qt, QAbstractListModel, QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QListView, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setup_ui()


    def setup_ui(self):
        self.main_layout = QVBoxLayout()
        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)       
        self.setCentralWidget(self.widget)

        # self.btn_click = QPushButton("Clicque-me")
        # self.btn_click.clicked.connect(self.populate)
        # self.main_layout.addWidget(self.btn_click)

        self.setGeometry(QRect(300, 300, 300, 300))

    def populate(self):
        self.model.todos.append("Teste 1")
        self.model.todos.append("Teste 2")
        self.model.layoutChanged.emit()


def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()