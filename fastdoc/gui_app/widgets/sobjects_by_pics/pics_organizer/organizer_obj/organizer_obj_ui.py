# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fastdoc\gui_app\widgets\sobjects_by_pics\pics_organizer\organizer_obj\organizer_obj.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OrganizerObj(object):
    def setupUi(self, OrganizerObj):
        OrganizerObj.setObjectName("OrganizerObj")
        OrganizerObj.resize(912, 202)
        self.verticalLayout = QtWidgets.QVBoxLayout(OrganizerObj)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(OrganizerObj)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.led_name = QtWidgets.QLineEdit(OrganizerObj)
        self.led_name.setObjectName("led_name")
        self.horizontalLayout.addWidget(self.led_name)
        self.btn_close = QtWidgets.QToolButton(OrganizerObj)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lsw_object = QtWidgets.QListWidget(OrganizerObj)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lsw_object.sizePolicy().hasHeightForWidth())
        self.lsw_object.setSizePolicy(sizePolicy)
        self.lsw_object.setMaximumSize(QtCore.QSize(16777215, 150))
        self.lsw_object.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.lsw_object.setDragEnabled(True)
        self.lsw_object.setDragDropOverwriteMode(True)
        self.lsw_object.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.lsw_object.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.lsw_object.setIconSize(QtCore.QSize(10000, 150))
        self.lsw_object.setMovement(QtWidgets.QListView.Free)
        self.lsw_object.setFlow(QtWidgets.QListView.LeftToRight)
        self.lsw_object.setViewMode(QtWidgets.QListView.ListMode)
        self.lsw_object.setObjectName("lsw_object")
        self.verticalLayout.addWidget(self.lsw_object)

        self.retranslateUi(OrganizerObj)
        QtCore.QMetaObject.connectSlotsByName(OrganizerObj)

    def retranslateUi(self, OrganizerObj):
        _translate = QtCore.QCoreApplication.translate
        OrganizerObj.setWindowTitle(_translate("OrganizerObj", "OrganizerObj"))
        self.label.setText(_translate("OrganizerObj", "Nome"))
        self.btn_close.setText(_translate("OrganizerObj", "X"))
