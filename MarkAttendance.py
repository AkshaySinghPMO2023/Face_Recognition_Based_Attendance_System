# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ma.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CDialog(object):
    def capt(self):
        import AttendenceSystem as at
        at.start_capturing()
    def setupUi(self, CDialog):
        CDialog.setObjectName("CDialog")
        CDialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(CDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(CDialog)
        self.label.setGeometry(QtCore.QRect(120, 30, 171, 19))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(CDialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 100, 88, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.capt)

        self.retranslateUi(CDialog)
        self.buttonBox.accepted.connect(CDialog.accept)
        self.buttonBox.rejected.connect(CDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CDialog)

    def retranslateUi(self, CDialog):
        _translate = QtCore.QCoreApplication.translate
        CDialog.setWindowTitle(_translate("CDialog", "Dialog"))
        self.label.setText(_translate("CDialog", " Click to Mark attendence"))
        self.pushButton.setText(_translate("CDialog", "Attendence"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CDialog = QtWidgets.QDialog()
    ui = Ui_CDialog()
    ui.setupUi(CDialog)
    CDialog.show()
    sys.exit(app.exec_())




