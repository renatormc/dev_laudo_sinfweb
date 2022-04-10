import PyQt5.QtWidgets as qw
from typing import TYPE_CHECKING
from fastdoc.helpers import get_models_list, get_model_meta

if TYPE_CHECKING:
    from .gui_server import GuiServer

class GuiServerUi:

    def __init__(self, w: 'GuiServer') -> None:
        self.w = w
        

    def setup_ui(self):
        w = qw.QWidget()
        self.lay_main = qw.QVBoxLayout()
        w.setLayout(self.lay_main)
        self.w.setCentralWidget(w)
        self.create_choose_edit()
        self.create_model_combo()
        self.create_buttons()

        # self.w.setGeometry(0, 0, 600, 100)
        self.w.setFixedSize(600, 150)


    def create_buttons(self):
        lay = qw.QHBoxLayout()
        lay.addSpacerItem(qw.QSpacerItem(1,1, qw.QSizePolicy.Expanding, qw.QSizePolicy.Fixed))

        self.btn_init_dir = qw.QPushButton("Iniciar diretório")
        self.btn_init_dir.setMinimumSize(150, 50)
        self.btn_init_dir.clicked.connect(self.w.init_dir)
        lay.addWidget(self.btn_init_dir)

        self.btn_open = qw.QPushButton("Abrir formulário")
        self.btn_open.setMinimumSize(150, 50)
        self.btn_open.clicked.connect(self.w.run)
        lay.addWidget(self.btn_open)

        

        lay.addSpacerItem(qw.QSpacerItem(1,1, qw.QSizePolicy.Expanding, qw.QSizePolicy.Fixed))

        self.lay_main.addLayout(lay)

    def create_model_combo(self):
        self.cbx_models = qw.QComboBox()
        for m in get_models_list():
            try:
                full_name = get_model_meta(m)['full_name']
            except KeyError:
                full_name = m
            self.cbx_models.addItem(full_name, m)
        self.lay_main.addWidget(self.cbx_models)

    def create_choose_edit(self):
        lay = qw.QHBoxLayout()
        self.lay_main.addWidget(qw.QLabel("Diretório de trabalho"))

        self.led_workdir = qw.QLineEdit()
        self.led_workdir.textChanged.connect(self.w.check_dir_existence)
        lay.addWidget(self.led_workdir)

        self.btn_choose = qw.QToolButton()
        self.btn_choose.setText("...")
        self.btn_choose.clicked.connect(self.w.choose_dir)
        lay.addWidget(self.btn_choose)

        self.lay_main.addLayout(lay)
