# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../form_recibo.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication


class ui_form(QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 768)
        Form.setMinimumSize(QtCore.QSize(1024, 768))
        Form.setMaximumSize(QtCore.QSize(1024, 768))
        Form.setWindowTitle("")
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frm_arriba = QtWidgets.QFrame(Form)
        self.frm_arriba.setEnabled(True)
        self.frm_arriba.setGeometry(QtCore.QRect(0, 0, 1024, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_arriba.sizePolicy().hasHeightForWidth())
        self.frm_arriba.setSizePolicy(sizePolicy)
        self.frm_arriba.setMinimumSize(QtCore.QSize(0, 80))
        self.frm_arriba.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frm_arriba.setStyleSheet("background-color: rgb(0, 183, 72);")
        self.frm_arriba.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_arriba.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_arriba.setObjectName("frm_arriba")
        self.pushButton_3 = QtWidgets.QPushButton(self.frm_arriba)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 3, 291, 85))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "background-color: #000000ff\n"
                                        "}")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/CFEmatico.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(140, 140))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frm_arriba)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 3, 291, 85))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/logo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 280, 1024, 161))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(450, 530, 121, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../images/recibo-2.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "Un momento por favor...\n"
                                      "estamos imprimiendo su comprobante"))
        Form.setWindowTitle(_translate("Form", "CFEmático"))

# import imagenes_rc

if __name__ == '__main__':
    app = QApplication(sys.argv)
    x = ui_form()
    sys.exit(app.exec_())
