'''
Created on Jul 22, 2019

@author: ftd

pip install PyQt5
pip install PyQt5-tools

'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,\
    QFrame, QComboBox,\
    QTableWidget, QTableWidgetItem, QTabWidget, QLabel
from PyQt5.QtGui import QIcon
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
import os
from PyQt5.QtCore import QRect
from PyQt5.Qt import QTreeWidgetItem, QTreeWidget, QHeaderView, QMessageBox
from src.main.pydev.com.ftd.generalutilities.database.api.IDatabase_driver import IDatabase_driver

class Database_maint_frame(QMainWindow):

    FROM, SUBJECT, DATE = range(3)
    
    def __init__(self, database_driver=None):
        
        # create application object
        app = QApplication(sys.argv)
        super().__init__()
        
        self.__title='Database maintain'
        self.__posx=200
        self.__posy=200
        self.__width=1080
        self.__height=720
        
        # Validation for database driver
        self.__database_driver = None
        if database_driver and isinstance(database_driver, IDatabase_driver):
            # set database driver
            self.__database_driver = database_driver
            
        # opened tables
        self.__opened_tables = []
        
        # set style sheet
        self.set_stylesheet()
        # initialize method
        self.initUI()
        
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
        self.__lefttop_square.setGeometry(10, 30, 230, 150)
        self.__leftbtm_square = QFrame(self)
        self.__leftbtm_square.setGeometry(10, 190, 230, 510)
        self.__right_square = QFrame(self)
        self.__right_square.setGeometry(250, 30, 820, 670)
        
        # add database combobox and add items
        self.__db_comboBox = QComboBox(self.__lefttop_square)
        self.__db_comboBox.setGeometry(QRect(15, 30, 200, 30))
        self.__db_comboBox.setObjectName(("comboBox"))
        # load data
        self.on_load_combolist(self.__db_comboBox)  # load event
        
        # add datatable treeview and add items
        self.__tb_treeview = QTreeWidget(self.__leftbtm_square)
        self.__tb_treeview.setGeometry(15, 30, 200, 440) 
        self.__tb_treeview_root = QTreeWidgetItem(self.__tb_treeview)
        self.__tb_treeview_root.setText(0, "Tables")
        self.__tb_treeview_root.setText(1, "root")
        self.__tb_treeview.addTopLevelItem(self.__tb_treeview_root) 
        self.__tb_treeview.expandAll()
        self.__tb_treeview.setHeaderHidden(True)
        
        # add tab
        self.__tab = QTabWidget(self.__right_square)
        self.__tab.setGeometry(10, 10, 800, 620)
        
        # add datagrid buttons
        self.__new_rec_btn = QPushButton('New',self)
        self.__new_rec_btn.setToolTip('Add a new record')
        self.__new_rec_btn.resize(60, 30)
        self.__new_rec_btn.move(400,665)
        self.__new_rec_btn.clicked.connect(self.click_new_rec_btn) # button click event
        
        self.__del_rec_btn = QPushButton('Delete',self)
        self.__del_rec_btn.setToolTip('Delete a new record')
        self.__del_rec_btn.resize(60, 30)
        self.__del_rec_btn.move(470,665)
        
        # event
        self.__del_rec_btn.clicked.connect(self.click_del_rec_btn) # button click event
        self.__db_comboBox.currentIndexChanged.connect(self.on_combox_selection_change) # selection change event
        self.__tb_treeview.doubleClicked.connect(self.on_treeview_doubleClick) # selection change event
        
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
        
    
    def closeEvent(self, event):
        '''
        window close event
        '''
        reply = QMessageBox.question(self, 'Message', 'Do you want to quit?', QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
    
    def click_new_rec_btn(self):
        '''
        new button click
        '''
        print('NEW BUTTON')
        
    
    def click_del_rec_btn(self):
        '''
        delete button click
        '''
        print('DELETE BUTTON')
    
    
    def on_load_combolist(self, parent):
        '''
        combobox load event
        '''
        self.load_databases(parent)
        
    
    def load_databases(self, parent):
        '''
        load the database name list and append into combolist
        '''
        if not self.__database_driver:
            QMessageBox.warning(self, 'Warning', "Invalid database driver, please check.", QMessageBox.Ok)
            return
            
        result, database_list, message = self.__database_driver.get_database_list()
        if not result:
            QMessageBox.critical(self, 'Error', message, QMessageBox.Ok)
        else:
            if len(database_list) > 0:
                parent.addItem("")
                for name in database_list:
                    parent.addItem(name)
            else:
                QMessageBox.warning(self, 'Warning', "Database is empty.", QMessageBox.Ok)
    
    
    def on_combox_selection_change(self):
        '''
        combobox selection change event
        '''
        if not self.__database_driver:
            return
        
        self.clear_treeview_nodes()
        
        if not self.__db_comboBox.currentText():
            return
        
        table_list = self.__database_driver.get_table_list(self.__db_comboBox.currentText())
        
        self.create_treeview_nodes(table_list)
    
    
    def clear_treeview_nodes(self):
        '''
        clear nodes from datatable treeview
        '''
        if self.__tb_treeview_root:
            while self.__tb_treeview_root.childCount() > 0:
                self.__tb_treeview_root.removeChild(self.__tb_treeview_root.takeChild(0))
        
    
    def create_treeview_nodes(self, nodelist=None):
        '''
        append nodes into datatable treeview
        '''
        if nodelist:
            for table in nodelist:
                child = QTreeWidgetItem(self.__tb_treeview_root) 
                child.setText(0,table)
                child.setText(1,'child')

    
    def on_treeview_doubleClick(self):
        '''
        treeview selection double click event
        '''
        if self.__tb_treeview.currentItem():
            hititem = self.__tb_treeview.currentItem()
            
            if hititem.text(1) == 'root':
                return
            
            if hititem.text(0) in self.__opened_tables:
                return
            
            columns = []
            column_types = []
            records = []
            try:
                # load the datatable record
                columns, column_types, records = self.__database_driver.get_records(self.__db_comboBox.currentText(), hititem.text(0))
            except Exception as e:
                QMessageBox.warning(self, 'Warning', "Table load failed, please retry.", QMessageBox.Ok)
                print('expect:', e)
                return
            
            # record the selected table
            self.__opened_tables.append(hititem.text(0))
            # render grid
            self.render_table_grid(hititem.text(0), columns, column_types, records)
            
            
    def render_table_grid(self, datatablename, columns, column_types, table_records):
        '''
        render the grid
        '''
        # Create table
        self.__datatable = QTableWidget()
        
        # render the columns
        self.__datatable.setRowCount(len(table_records))
        self.__datatable.setColumnCount(len(columns))
        self.__datatable.setHorizontalHeaderLabels(columns)
        
        # render the grid cells
        if table_records and len(table_records) > 0:
            rows_count = len(table_records)
            column_count = len(columns)
            for i in range(0, rows_count):  # Rows
                for j in range(0, column_count):  # Columns
                    self.__datatable.setItem(i , j, QTableWidgetItem(str(table_records[i][j])))
        
        # render grid style
        self.__datatable.setAlternatingRowColors(True)
        self.__datatable.horizontalHeader().setObjectName("dt_hheader")
        self.__datatable.verticalHeader().setObjectName("dt_vheader")
        self.__datatable.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        
        self.__datatable.doubleClicked.connect(self.on_gridcell_click) # double click event
  
        # Create tab
        self.__tab.addTab(self.__datatable, datatablename)
           
    
    def on_gridcell_click(self):
        for currentQTableWidgetItem in self.__datatable.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
