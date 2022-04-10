from PyQt5.QtCore import QThread

class ServerThread(QThread):

    def __init__(self, app, port):
        QThread.__init__(self)
        self.app = app
        self.port = port

    def __del__(self):
        self.wait()
        
    def run(self):
        self.app.run(host='0.0.0.0', port=self.port, debug=False)
       