# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fastdoc/gui_app/about_dialog/about_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(485, 287)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutDialog.sizePolicy().hasHeightForWidth())
        AboutDialog.setSizePolicy(sizePolicy)
        AboutDialog.setStyleSheet("background-color: rgb(61, 56, 70)")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AboutDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.lbl_icon = QtWidgets.QLabel(AboutDialog)
        self.lbl_icon.setText("")
        self.lbl_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_icon.setObjectName("lbl_icon")
        self.verticalLayout_2.addWidget(self.lbl_icon)
        self.label_2 = QtWidgets.QLabel(AboutDialog)
        self.label_2.setStyleSheet("font: 75 italic 10pt \"DejaVu Sans\";\n"
"font: 20pt \"DejaVu Sans\";\n"
"color: rgb(28, 113, 216);\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lbl_version = QtWidgets.QLabel(AboutDialog)
        self.lbl_version.setStyleSheet("color: yellow;")
        self.lbl_version.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_version.setObjectName("lbl_version")
        self.verticalLayout_2.addWidget(self.lbl_version)
        self.label_3 = QtWidgets.QLabel(AboutDialog)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(AboutDialog)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.setStretch(1, 1)

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "Fastdoc"))
        self.label_2.setText(_translate("AboutDialog", "Fastdoc"))
        self.lbl_version.setText(_translate("AboutDialog", "Version"))
        self.label_3.setText(_translate("AboutDialog", "Desenvolvedor: Renato Martins Costa"))
        self.label_4.setText(_translate("AboutDialog", "Página do projeto: https://github.com/renatormc/fastdoc"))