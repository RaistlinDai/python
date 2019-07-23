'''
Created on Jul 22, 2019

@author: ftd

pip install PyQt5
pip install PyQt5-tools

'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton,\
    QFrame
from PyQt5.QtGui import QIcon
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
import os

class Database_maint_frame(QMainWindow):

    def __init__(self):
        # create application object
        app = QApplication(sys.argv)
        super().__init__()
        
        self.__title='Database maintain'
        self.__posx=200
        self.__posy=200
        self.__width=1080
        self.__height=720
        
        # initialize method
        self.initUI()
        # set style sheet
        self.set_stylesheet()
        
        sys.exit(app.exec_()) 
        
        
    def initUI(self):
        '''
        UI initialize
        '''
        # set the window position(x,y) and size
        self.setGeometry(self.__posx, self.__posy, self.__width, self.__height)  
        # set the window title
        self.setWindowTitle(self.__title)
        
        # update window status
        self.update_status('Loading...')
        
        # add menu bar
        self.__mainMenu = self.menuBar()
        self.__fileMenu = self.__mainMenu.addMenu('File')
        self.__editMenu = self.__mainMenu.addMenu('Edit')
        self.__viewMenu = self.__mainMenu.addMenu('View')
        self.__searchMenu = self.__mainMenu.addMenu('Search')
        self.__toolsMenu = self.__mainMenu.addMenu('Tools')
        self.__helpMenu = self.__mainMenu.addMenu('Help')
        
        # add frame
        self.__lefttop_square = QFrame(self)
        self.__lefttop_square.setGeometry(10, 30, 230, 250)
        self.__leftbtm_square = QFrame(self)
        self.__leftbtm_square.setGeometry(10, 290, 230, 410)
        self.__right_square = QFrame(self)
        self.__right_square.setGeometry(250, 30, 820, 670)
        
        # add buttons
        self.__new_btn = QPushButton('New',self)
        self.__new_btn.setToolTip('Add a new record')
        self.__new_btn.resize(60, 30)
        self.__new_btn.move(400,660)
        self.__new_btn.clicked.connect(self.click_new_btn) # button click event
        
        self.__del_btn = QPushButton('Delete',self)
        self.__del_btn.setToolTip('Delete a new record')
        self.__del_btn.resize(60, 30)
        self.__del_btn.move(470,660)
        self.__del_btn.clicked.connect(self.click_del_btn) # button click event
        
        # show the window
        self.show()
    
    
    def set_stylesheet(self):
        '''
        set the style sheet from qss and icons
        '''
        # get the relative project path
        fileconstant = File_constant()
        root_path = os.path.dirname(os.path.abspath(__file__))
        proj_path = root_path[:root_path.index(fileconstant.MY_PROJECT_PACKAGE)]
        # set the qss
        qss_path = proj_path + "\\src\\main\\pydev\\com\\ftd\\resource\\style\\StyleSheet.qss"
        self.setStyleSheet(open(qss_path, "r").read())
        # set the window icon
        icon_path = proj_path + "\\src\\main\\pydev\\com\\ftd\\resource\\icons\\title_icon.jpg"
        self.setWindowIcon(QIcon(icon_path))
        
    
    def update_status(self, status):
        '''
        update the window status
        '''
        self.statusBar().showMessage(status)
        
    
    def click_new_btn(self):
        '''
        new button click
        '''
        print('NEW BUTTON')
        
    
    def click_del_btn(self):
        '''
        delete button click
        '''
        print('DELETE BUTTON')