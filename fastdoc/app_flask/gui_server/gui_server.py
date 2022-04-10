import PyQt5.QtWidgets as qw
from PyQt5.QtCore import Qt
import sys
from fastdoc.app_flask.gui_server.gui_server_thread import ServerThread
from fastdoc.app_flask.helpers import get_available_port
from  fastdoc.app_flask.app import app as app_flask
from .webview_window import WebViewWindow
from .gui_server_ui import GuiServerUi
from pathlib import Path
from fastdoc import config
from fastdoc.helpers import init_dir

class GuiServer(qw.QMainWindow):
    def __init__(self, port):
        super(self.__class__, self).__init__()
        self.ui = GuiServerUi(self)
        self.ui.setup_ui()
        self.port = port
        self.ui.led_workdir.setText(str(config.workdir))
        # self.setWindowIcon(QtGui.QIcon(
        #     f"{script_dir}\\resources\\icon.png"))

    def choose_dir(self):
        dir_ = qw.QFileDialog.getExistingDirectory(self, "Escolher diretório", str(config.workdir))
        if dir_:
            self.ui.led_workdir.setText(dir_)
            

    def check_dir_existence(self):
        path = Path(self.ui.led_workdir.displayText())
        if path.exists() and path.is_dir():
            self.ui.btn_open.setEnabled(True)
            self.ui.btn_init_dir.setEnabled(True)
            config.workdir = path
        else:
            self.ui.btn_open.setEnabled(False)
            self.ui.btn_init_dir.setEnabled(False)

    def init_dir(self):
        model = self.ui.cbx_models.currentData(Qt.UserRole)
        ok = init_dir(model, config.workdir)
        if ok:
            qw.QMessageBox.about(self, "Mensagem", "Diretório iniciado com sucesso!")
        else:
            qw.QMessageBox.warning(self, "Mensagem", "Não há uma implementação de inicialização de diretório para este modelo!")

    def run(self):
        model = self.ui.cbx_models.currentData(Qt.UserRole)
        self.dialog = WebViewWindow(self.port, model)
        self.dialog.showMaximized()
        

def provide_GUI_for(application):
    qtapp = qw.QApplication(sys.argv)

    port = get_available_port()
    webapp = ServerThread(application, port)
    webapp.start()

    qtapp.aboutToQuit.connect(webapp.terminate)

    w = GuiServer(port)
    w.show()
    return qtapp.exec_()




def run_server():
    sys.exit(provide_GUI_for(app_flask))
  
