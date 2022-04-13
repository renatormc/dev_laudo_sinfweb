from fastdoc import config
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QWidget


def get_icon(name):
    return QIcon(str(config.app_dir / "gui_app/assets/images" / name)) 


def ask_confirmation(parent: QWidget, title: str, message: str) -> bool:
    msg_box = QMessageBox(parent)
    msg_box.setIcon(QMessageBox.Question)
    msg_box.setWindowIcon(parent.windowIcon())
    msg_box.setText(message)
    msg_box.setWindowTitle(title)
    btn_yes = msg_box.addButton(QMessageBox.Yes)
    btn_no = msg_box.addButton(QMessageBox.No)
    msg_box.setDefaultButton(btn_no)
    btn_yes.setText("Sim")
    btn_no.setText("Não")
    msg_box.exec_()
    if msg_box.clickedButton() == btn_yes:
        return True
    return False

