import PyQt5.QtWidgets as qw
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import * 


class WebViewWindow(qw.QDialog):
    def __init__(self, port, model):
        super(self.__class__, self).__init__()
        self.port =port
        self.model = model
        self.setup_ui()
        self.webview.load(QUrl(f"http://localhost:{self.port}?model={model}"))


    def setup_ui(self):
        self.lay_main = qw.QVBoxLayout()
        self.setLayout(self.lay_main)
     
        self.webview = QWebEngineView()
        self.lay_main.addWidget(self.webview)
    

