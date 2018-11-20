
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.years=[]
        
        for yr in range(2000,date.today().year+1):
            self.years.append(yr)
            
        self.years=[str(i) for i in self.years]
        print (list(reversed(self.years)))
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(484, 288)
        Dialog.setModal(True)
        
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QtCore.QRect(40, 220, 391, 32))
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        
        
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QtCore.QRect(120, 80, 91, 31))
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(self.years)
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(30, 90, 81, 16))
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(270, 90, 47, 13))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setEnabled(True)
        self.comboBox_2.setGeometry(QtCore.QRect(340, 80, 91, 31))
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(reversed(self.years))
        
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setEnabled(True)
        self.comboBox_3.setGeometry(QtCore.QRect(220, 160, 91, 31))
        self.comboBox_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox_3.setAutoFillBackground(False)
        self.comboBox_3.setObjectName("comboBox_3")
        pages=[str(i) for i in range(1,11)]
        self.comboBox_3.addItems(pages)

        self.comboBox_3.setCurrentIndex(3)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(140, 170, 77, 13))
        self.label_3.setAutoFillBackground(False)
#        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
       
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 441, 16))
        self.label_4.setAutoFillBackground(False)
#        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(160, 30, 171, 16))
        self.label_5.setAutoFillBackground(False)
#        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        
        self.Dialog=Dialog
        self.retranslateUi(Dialog)
        self.buttonBox.button( QtWidgets.QDialogButtonBox.Ok).setText("Run")
        self.buttonBox.button( QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.okAction)
#        self.buttonBox.accepted.clicked.connect(self.okAction(Dialog))
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Year (Beginning)"))
        self.label_2.setText(_translate("Dialog", "Year(end)"))

        self.label_3.setText(_translate("Dialog", "Pages/year"))
        self.label_4.setText(_translate("Dialog", "Choose what year you want to begin and want to end and  how many pages per year "))
        self.label_5.setText(_translate("Dialog", "you want to search through"))
    
    def okAction(self):
        self.Dialog.accept()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

