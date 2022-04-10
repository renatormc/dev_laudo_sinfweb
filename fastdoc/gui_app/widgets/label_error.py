from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt

class LabelError(QLabel):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        p = QPalette()
        # p.setColor(QPalette.Window, Qt.white)
        p.setColor(QPalette.WindowText, Qt.red)
        self.setAutoFillBackground(True)
        self.setPalette(p)
