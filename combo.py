from datetime import date
from time import sleep
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from Gui import AppWindow
from PyQt5.QtWidgets import QStyleFactory
from PyQt5.QtCore import QObject,QThread,pyqtSignal

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.years=[str(yr) for yr in range(2000,date.today().year+1)]
        
#        print (list(reversed(self.years)))
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(484, 288)
        Dialog.setModal(True)
        
#        QThread.currentThread().setObjectName('main') 
#        self.thread = QThread()
#        self.thread .start()
#        self.thread.connect_and_emit_trigger()
        
        
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
        self.comboBox.setCurrentIndex(len(self.years)-4)
        
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
        self.comboBox_3.setGeometry(QtCore.QRect(330, 160, 91, 31))
        self.comboBox_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox_3.setAutoFillBackground(False)
        self.comboBox_3.setObjectName("comboBox_3")
        self.pages=[str(i) for i in range(1,11)]
        self.comboBox_3.addItems(self.pages)
        self.comboBox_3.setCurrentIndex(3)
        
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(260, 170, 77, 13))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setEnabled(True)
        self.comboBox_4.setGeometry(QtCore.QRect(130, 160, 91, 31))
        self.comboBox_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox_4.setAutoFillBackground(False)
        self.comboBox_4.setObjectName("comboBox_4")
        self.pages=[str(x/10)  for x in range(50, 100,1)]
#        print(self.pages)
#        self.pages=[str(i) for i in self.pages]
        self.comboBox_4.addItems(self.pages)
        self.comboBox_4.setCurrentIndex(len(self.pages)-(len(self.pages)/2))
        
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(50, 170, 77, 13))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
       
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(30, 10, 441, 16))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(160, 30, 171, 16))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName("label_6")
        
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
        self.label_4.setText(_translate("Dialog", "Min Rating"))
        self.label_5.setText(_translate("Dialog", "Choose what year you want to begin and want to end and  how many pages per year "))
        self.label_6.setText(_translate("Dialog", "you want to search through"))
    
    def okAction(self):
        self.start=int(self.comboBox.currentText())
        self.end=int(self.comboBox_2.currentText())
        self.page=int(self.comboBox_3.currentText())
        self.min_rating=float(self.comboBox_4.currentText())
        print(self.start,self.end,self.page)
        if self.start<=self.end:
            self.Dialog.accept()
        else:
            QtWidgets.QMessageBox.about(self.Dialog, "Info", "The final year can not be greater than the initial year")
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    Dialog = QtWidgets.QDialog() 
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    result=ui.Dialog.exec_()
    if result==QtWidgets.QDialog.Accepted:
        c=AppWindow(ui.page,ui.start,ui.end,ui.min_rating)
    #    c.show()
    sys.exit(app.exec_())