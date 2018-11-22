'''
Created on Nov. 15, 2018

@author: tomil
'''
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import sys,os
from PyQt5.QtWidgets import QMainWindow, QApplication, qApp, QStyleFactory,QMessageBox as msg
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.Qt import Qt
import pandas as pd
import webbrowser
from time import sleep
from Movie_helper import imdb as db


 
class Ui_MainWindow(QtCore.QAbstractTableModel):
    def __init__(self,page,start,end,min_rating):
        
        QtCore.QAbstractTableModel.__init__(self, parent=None)
        
        self.data = db(page,start,end,min_rating)
        self.df = self.data.printdb()
#         print (self.df)

#         self.data = {'Name':['Tom', 'Jack', 'Steve', 'Rickyyyyyyyyyyyyyyyy'],'Age':[28,34,29,42]}
#         self.df = pd.DataFrame(self.data)
#        self.df.index.name = 'S/N'
#        print (self.df)

        self._data = self.df
        self.update()
        
    def update(self):
        self.file_path = 'Watched_movies.csv'
        if not os.path.isfile(self.file_path):
            self._data = self.df
            pass
        else:
            try:
                new_df = pd.read_csv(self.file_path)
                for item,row in self._data.iterrows():
                    for item1,row1 in new_df.iterrows():
                        if list(row) == list(row1):
                            self._data=self._data.drop (item)
            except pd.errors.EmptyDataError:
                pass


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
    
    def setupUi(self, MainWindow=None):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.update()
        
#        the two buttons
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 850, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)
        
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(250, 850, 93, 28))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(self.on_reset)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 850, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(qApp.quit)
        self.pushButton_2.setStatusTip('Exit application')
        
        self.pointListBox = QtWidgets.QTreeView(self.centralwidget)
        check=QtGui.QStandardItemModel()
        check.setHorizontalHeaderLabels(list(self.df))
        self.pointListBox.setModel(self)
#        print(type(self.pointListBox.setModel(self)))
        
        
        
#        self.pointListBox = QtWidgets.QTreeWidget(self.centralwidget)
        self.pointListBox.setGeometry(QtCore.QRect(100, 50, 800, 700))
        self.pointListBox.setSelectionMode(1)
#        self.setHorizontalHeaderLabels( "header0")
        
        
        header = self.pointListBox.header()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
#        header.setDefaultAlignment(Qt.AlignHCenter)
#        header.setStretchLastSection(False)
#        header.setSectionsMovable(True)
#
#        print(self.pointListBox.columnAt(1))#.setCheckState( Qt.Checked)
#        self.pointListBox.setHeader(self.header)
##        self.pointListBox.headerItem().setStretchLastSection(False)
#        self.barA = QtWidgets.QTreeWidgetItem(self.root, ["sample_count", "12141"])
#        self.bazA = QtWidgets.QTreeWidgetItem(self.root, ["ps_p_psla", "14.563151"])
#        
#        self.pointListBox.expandItem(self.root)
        
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
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.pushButton_1.setText(_translate("MainWindow", "Reset Default"))
        
    def on_click(self):
        
#        items = self.pointListBox.selectedItem()
#        crawler = index.model().itemFromIndex(index)
        if len(self.pointListBox.selectedIndexes())>0:
            index = self.pointListBox.selectedIndexes()
#            print(index[1].data())
            
            header = list(self._data)
            List=[]
            for i in index:
                List.append(i.data())
                
            new_df = pd.DataFrame.from_records([List] )
            new_df.columns=header
#            print(new_df)
            ret = msg.question(self.centralwidget,'', f"Are you sure select {index[0].data()}?", msg.Yes | msg.No)
            
            if ret == msg.Yes:
#                webbrowser.open(f"https://www.google.com.tr/search?q= {index[0].data()}  movie")#{index[1].data()}
                print('PyQt5 button click')
                
                if not os.path.isfile(self.file_path):
                    new_df.to_csv(self.file_path, columns = header, index=False)
                else:
                    try:
                        df = pd.read_csv(self.file_path)
                        frames = [df, new_df]
#                        print(set(df['Name']).intersection(set(new_df['Name'])))#if set is not empty check if year is the same
                        new_df=pd.concat(frames)
                        new_df=new_df.reset_index(drop=True)
                        new_df.to_csv(self.file_path, columns =header, index=False)
                        # read your files
                    except pd.errors.EmptyDataError:#incase file is already created and empty
                         new_df.to_csv(self.file_path, columns = header, index=False)
    
                print(new_df)
                self.update()
                self.centralwidget.update()
                
    #        else if ret == msg.No:
        else:
            msg.about(self.centralwidget, "Info", "You did not select any movie")
            print("hey")
            
    def on_reset(self):
        
            if not os.path.isfile(self.file_path):
                msg.about(self.centralwidget, "Info", "File ha already been deleted")
                pass
            else:
                ret = msg.question(self.centralwidget,'Warning', "Are you sure to reset all the values?", msg.Yes | msg.No)
                if ret == msg.Yes:
                    os.remove(self.file_path)
            self.update()
            self.centralwidget.update()
#            os.remove("movie_ratings.xlsx") remove all details from csv file
#        else if ret == msg.No:
    
    
        


class AppWindow(QMainWindow):
    def __init__(self,page,start,end,min_rating ):
        super().__init__()
        app = QtWidgets.QApplication(sys.argv)
        self.ui = Ui_MainWindow(page,start, end,min_rating)
        self.ui.setupUi(self)
        self.show()
#        sleep(100)
        sys.exit(app.exec_())


#if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    app.setStyle(QStyleFactory.create('Fusion'))
#    ex = AppWindow()
#    sys.exit(app.exec_())
    
# might allow user to see movies watched
#try to add if itas a movie or a series and try to eliminate series if possible
#
#
