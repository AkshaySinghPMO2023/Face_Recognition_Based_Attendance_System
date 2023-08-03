# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddUser.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2

class Ui_Dialog(object):
    
    def on_click(self):
        textboxValue = self.textEdit.toPlainText()
        #QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        #self.textbox.setText("")
        print(textboxValue)
        key = cv2. waitKey(1)
        webcam = cv2.VideoCapture(0)
        while True:
            try:
                check, frame = webcam.read()
                print(check) #prints true as long as the webcam is running
                print(frame) #prints matrix values of each framecd 
                cv2.imshow("Capturing", frame)
                key = cv2.waitKey(1)
                if key == ord('s'): 
                    #ni=input('Enter a value:')
                    ni=textboxValue
                    n='TranningImages/'+ni+'.jpg'
                    print(n)
                    cv2.imwrite(filename=n, img=frame)
                    webcam.release()
                    img_new = cv2.imread(n, cv2.IMREAD_GRAYSCALE)
                    img_new = cv2.imshow("Captured Image", img_new)
                    cv2.waitKey(1650)
                    cv2.destroyAllWindows()
                    print("Processing image...")
                    img_ = cv2.imread(n, cv2.IMREAD_ANYCOLOR)
                    print("Converting RGB image to grayscale...")
                    gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                    print("Converted RGB image to grayscale...")
                    print("Resizing image to 650x480 scale...")
                    img_ = cv2.resize(gray,(650,480))
                    print("Resized...")
                    img_resized = cv2.imwrite(filename=n, img=img_)
                    print(n)
                    print("Image saved!")
                
                    break
                elif key == ord('q'):
                    print("Turning off camera.")
                    webcam.release()
                    print("Camera off.")
                    print("Program ended.")
                    cv2.destroyAllWindows()
                    break
                
            except(KeyboardInterrupt):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 40, 111, 19))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(100, 100, 191, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 160, 88, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Add User"))
        self.pushButton.setText(_translate("Dialog", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

