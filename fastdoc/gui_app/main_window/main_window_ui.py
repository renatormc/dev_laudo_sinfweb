# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fastdoc/gui_app/main_window/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1193, 821)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.cbx_model = QtWidgets.QComboBox(self.centralwidget)
        self.cbx_model.setMinimumSize(QtCore.QSize(300, 0))
        self.cbx_model.setObjectName("cbx_model")
        self.horizontalLayout_2.addWidget(self.cbx_model)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.sca_form = QtWidgets.QScrollArea(self.centralwidget)
        self.sca_form.setWidgetResizable(True)
        self.sca_form.setObjectName("sca_form")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1173, 676))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.sca_form.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.sca_form)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_render = QtWidgets.QPushButton(self.centralwidget)
        self.btn_render.setMinimumSize(QtCore.QSize(180, 40))
        self.btn_render.setObjectName("btn_render")
        self.horizontalLayout.addWidget(self.btn_render)
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setMinimumSize(QtCore.QSize(180, 40))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setMinimumSize(QtCore.QSize(180, 40))
        self.btn_load.setObjectName("btn_load")
        self.horizontalLayout.addWidget(self.btn_load)
        self.btn_initial_data = QtWidgets.QPushButton(self.centralwidget)
        self.btn_initial_data.setMinimumSize(QtCore.QSize(180, 40))
        self.btn_initial_data.setObjectName("btn_initial_data")
        self.horizontalLayout.addWidget(self.btn_initial_data)
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setMinimumSize(QtCore.QSize(180, 40))
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout.addWidget(self.btn_clear)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1193, 22))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.act_add_token = QtWidgets.QAction(MainWindow)
        self.act_add_token.setObjectName("act_add_token")
        self.act_manage_models = QtWidgets.QAction(MainWindow)
        self.act_manage_models.setObjectName("act_manage_models")
        self.menuArquivo.addAction(self.act_add_token)
        self.menuArquivo.addAction(self.act_manage_models)
        self.menubar.addAction(self.menuArquivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Modelo"))
        self.btn_render.setText(_translate("MainWindow", "Gerar docx"))
        self.btn_save.setText(_translate("MainWindow", "Salvar preenchimento"))
        self.btn_load.setText(_translate("MainWindow", "Carregar preenchimento"))
        self.btn_initial_data.setText(_translate("MainWindow", "Carregar dados iniciais"))
        self.btn_clear.setText(_translate("MainWindow", "Limpar"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.act_add_token.setText(_translate("MainWindow", "Adicionar token"))
        self.act_manage_models.setText(_translate("MainWindow", "Gerenciar modelos"))
