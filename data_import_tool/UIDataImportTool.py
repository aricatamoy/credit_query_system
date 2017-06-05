# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataImportTool.ui'
#
# Created: Mon Jun 05 20:57:59 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DataImportTool(object):
    def setupUi(self, DataImportTool):
        DataImportTool.setObjectName("DataImportTool")
        DataImportTool.resize(465, 94)
        self.verticalLayout = QtWidgets.QVBoxLayout(DataImportTool)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.user_label = QtWidgets.QLabel(DataImportTool)
        self.user_label.setObjectName("user_label")
        self.horizontalLayout.addWidget(self.user_label)
        self.user_path_edit = QtWidgets.QLineEdit(DataImportTool)
        self.user_path_edit.setObjectName("user_path_edit")
        self.horizontalLayout.addWidget(self.user_path_edit)
        self.user_path_button = QtWidgets.QPushButton(DataImportTool)
        self.user_path_button.setObjectName("user_path_button")
        self.horizontalLayout.addWidget(self.user_path_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.import_button = QtWidgets.QPushButton(DataImportTool)
        self.import_button.setObjectName("import_button")
        self.horizontalLayout_3.addWidget(self.import_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(DataImportTool)
        QtCore.QMetaObject.connectSlotsByName(DataImportTool)

    def retranslateUi(self, DataImportTool):
        _translate = QtCore.QCoreApplication.translate
        DataImportTool.setWindowTitle(_translate("DataImportTool", "Excel数据导入工具"))
        self.user_label.setText(_translate("DataImportTool", "选择Excel文件："))
        self.user_path_button.setText(_translate("DataImportTool", "选择"))
        self.import_button.setText(_translate("DataImportTool", "导入到数据库"))

