'''
Created on Jun 27, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from tkinter.ttk import Combobox
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_selfdesign import Button_selfdesign
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.view.database.Popup_table_records import Popup_table_records

class Frame_mongodb_processor(FormatableFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, dtos=None, trans=None, **configs):
        '''
        Constructor
        '''
        self.__result = True
        self.__error = None
        
        FormatableFrame.__init__(self, parent.get_mainframe(), dtos, trans, **configs)
        
    
    #overwrite create_widges
    def create_widges(self):
        
        #frame
        self.__frame1 = FormatableFrame(self)
        self.__frame1.pack(side=TOP)
        #Title
        self.__label01 = Label(self.__frame1, text="Mongodb database functions", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        
        #---- panel 01 ----------
        canv1 = Canvas(self, height=100, width=550)
        #label
        label1 = Label(canv1, text='Please choose a database:')
        label1.place(height=20, width=200, x=10, y=10)
        #combox database name
        self.__comvalue = StringVar() 
        self.__comboxlist = Combobox(canv1,textvariable=self.__comvalue)
        self.__comboxlist.place(height=20, width=150, x=20, y=40)
        self.__comboxlist.bind("<<ComboboxSelected>>",self.load_collections)
        self.__comboxlist["state"] = "readonly"
        
        #---- panel 02 ----------
        canv2 = Canvas(self, height=200, width=550)
        #label
        label2 = Label(canv2, text='Please choose a table:')
        label2.place(height=20, width=200, x=10, y=10)
        #table list
        self.__listbox = Listbox(canv2, width=30)
        self.__scroll = Scrollbar(canv2)
        self.__listbox.config(yscrollcommand = self.__scroll.set)
        self.__scroll.place(height=150, width=20, x=220, y=40)
        self.__scroll.config(command = self.__listbox.yview)
        self.__listbox.place(height=150, width=200, x=20, y=40)
        for name in ['a','b','c','d','e','f','g','h','i','j','k','l']:
            self.__listbox.insert(0, name)
            
        #buttons
        self.__btn_view = Button_selfdesign(canv2, self.view_table, 'View', height=2)
        self.__btn_view.place(height=25, width=50, x=270, y=120)
        self.__btn_info = Button_selfdesign(canv2, self.show_table_info, 'Info', height=2)
        self.__btn_info.place(height=25, width=50, x=330, y=120)
        self.__btn_export = Button_selfdesign(canv2, self.export_table, 'Export', height=2)
        self.__btn_export.place(height=25, width=50, x=390, y=120)
        self.__btn_import = Button_selfdesign(canv2, self.import_table, 'Import', height=2)
        self.__btn_import.place(height=25, width=50, x=450, y=120)
        
        canv1.pack()
        canv2.pack()
     
    #overwrite create_widges   
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Next':{'process':self.get_nextframe(), 'before':self.before_next},
                   'Prev':None}
        self.__buttom = Frame_bottom(parent, ['Next','Prev'], exFuncs)
        self.__buttom.pack(fill=X, ipady=10,side=BOTTOM)
        
        
    def load_collections(self, db_name):
        '''
        load the collections(tables) from target database
        '''
        print('OPEN TABLES')
        
    
    def view_table(self):
        '''
        view records of the target table
        '''
        print('VIEW')
        popup = Popup_table_records(['a','b','c','d','e','f','g','h','i','j','k','l'])
        popup.grab_set()
        popup.focus_set()
        popup.wait_window()
        
        
    def show_table_info(self):
        '''
        show table info
        '''
        print('INFO')
        
        
    def export_table(self):
        '''
        export records to excel
        '''
        print('EXPORT')
        
        
    def import_table(self):
        '''
        import records from excel
        '''
        print('IMPORT')