'''
Created on Nov. 15, 2018

@author: tomil
'''
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, qApp, QStyleFactory
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.Qt import Qt
import pandas as pd
from Movie_helper import imdb as db

 
class Ui_MainWindow(QtCore.QAbstractTableModel):
    def __init__(self):
        QtCore.QAbstractTableModel.__init__(self, parent=None)
        
        self.data = db()
        self.df = self.data.printdb()
        print (self.df)
        self._data = self.df
        


      
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return list(self._data)[section]
#        return QAbstractTableModel.headerData(self, section, orientation, role)
   
    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return QtCore.QVariant(str(
                    self._data.values[index.row()][index.column()]))
        return QtCore.QVariant()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
#        the two buttons
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 300, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 300, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(qApp.quit)
        self.pushButton_2.setStatusTip('Exit application')
        
        self.pointListBox = QtWidgets.QTreeView(self.centralwidget)
        check=QtGui.QStandardItemModel()
        check.setHorizontalHeaderLabels(list(self.df))
        self.pointListBox.setModel(check)
        print(type(self.pointListBox.setModel(self)))
        
        
        
#        self.pointListBox = QtWidgets.QTreeWidget(self.centralwidget)
        self.pointListBox.setGeometry(QtCore.QRect(100, 110, 520, 155))
        self.pointListBox.setSelectionMode(3)
#        self.setHorizontalHeaderLabels( "header0")
        
        
#        self.header=QtWidgets.QHeaderView(check)
#        self.header.setSectionResizeMode(QHeaderView.ResizeToContents)
#        self.root = QtWidgets.QTreeWidgetItem(self.pointListBox, ["Sensor_data_net"])
#
#        self.root.setCheckState(0, Qt.Checked)
#        self.pointListBox.setHeader(self.header)
##        self.pointListBox.headerItem().setStretchLastSection(False)
#        self.barA = QtWidgets.QTreeWidgetItem(self.root, ["sample_count", "12141"])
#        self.bazA = QtWidgets.QTreeWidgetItem(self.root, ["ps_p_psla", "14.563151"])
#        
#        self.pointListBox.expandItem(self.root)
#
#
##         self.barA = QtWidgets.QTreeWidgetItem(self.A)
##         self.barA.setText(0,"bar")
##         self.barA.setText(1,"i")
##         self.barA.setText(2,"ii")
#        self.root_1 = QtWidgets.QTreeWidgetItem(self.pointListBox, ["root_1"])

        

        
        MainWindow.setCentralWidget(self.centralwidget)
#        MainWindow.setStyle(QStyleFactory.create('Fusion'))
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        
    def on_click(self):
        print('PyQt5 button click')
    
        


class AppWindow(QMainWindow):
    def __init__(self ):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
   



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    ex = AppWindow()

    sys.exit(app.exec_())
    
    