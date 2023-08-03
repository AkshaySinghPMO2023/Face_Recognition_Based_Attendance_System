# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'm2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog1(object):
    def setupUi(self, Dialog1):
        Dialog1.setObjectName("Dialog1")
        Dialog1.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog1)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog1)
        self.label.setGeometry(QtCore.QRect(140, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog1)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 51, 19))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog1)
        self.textEdit.setGeometry(QtCore.QRect(160, 100, 121, 21))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog1)
        self.pushButton.setGeometry(QtCore.QRect(160, 160, 101, 21))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog1)
        self.buttonBox.accepted.connect(Dialog1.accept)
        self.buttonBox.rejected.connect(Dialog1.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi(self, Dialog1):
        _translate = QtCore.QCoreApplication.translate
        Dialog1.setWindowTitle(_translate("Dialog1", "Add User"))
        self.label.setText(_translate("Dialog1", "Add Students"))
        self.label_2.setText(_translate("Dialog1", "Name:"))
        self.pushButton.setText(_translate("Dialog1", "Capture Pic"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog1 = QtWidgets.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(Dialog1)
    Dialog1.show()
    sys.exit(app.exec_())

